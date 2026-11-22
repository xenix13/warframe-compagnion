"""Build d'une arme : mods compatibles, capacité, et calcul des dégâts.

Règles de calcul (wiki : pages Damage, Elemental Damage, Critical Hit, Multishot) :
- dégât d'un type physique = base x (1 + bonus de dégâts) x (1 + bonus de ce type) ;
- dégât élémentaire d'un mod = dégât de base total x (1 + bonus de dégâts) x pourcentage du mod ;
- les éléments se combinent dans l'ordre des emplacements des mods ; l'élément propre de l'arme se combine en dernier ;
- critique = base x (1 + bonus) ; multiplicateur = base x (1 + bonus) ; statut, multitir, cadence : base x (1 + bonus).
Ne sont PAS comptés : bonus de faction (Bane), effets conditionnels (cumuls, combo, au kill), rivens, arcanes, Roar, buffs.
"""
import json, math, re

from . import calc, polarites

PRIMARY_ELEM = ("heat", "cold", "electricity", "toxin")
COMBOS = {frozenset(("heat", "cold")): "blast", frozenset(("electricity", "toxin")): "corrosive",
          frozenset(("heat", "toxin")): "gas", frozenset(("cold", "electricity")): "magnetic",
          frozenset(("cold", "toxin")): "viral", frozenset(("heat", "electricity")): "radiation"}
PHYS = ("impact", "puncture", "slash")
SLOT_CAT = {"principale": "Primary", "secondaire": "Secondary", "melee": "Melee"}
ARCANE_TYPES = {"principale": ("Primary Arcane", "Bow Arcane", "Shotgun Arcane"), "secondaire": ("Secondary Arcane",),
                "melee": ("Melee Arcane",)}


def compat_for(w):
    """Familles de mods (compatName) acceptées par une arme."""
    t, cat, name = (w.get("type") or ""), w.get("category"), w.get("name") or ""
    if t == "Exalted Weapon":  # le type réel se lit dans le nom (Artemis Bow = arc, Neutralizer = fusil de précision)
        t = "Bow" if "Bow" in name else "Sniper" if "Neutralizer" in name else "Rifle"
    base_name = re.sub(r"\s+(Prime|Wraith|Vandal|Prisma|Mk1-|Kuva |Tenet |Coda |Dex |Rakta |Sancti |Secura |Synoid |Telos |Vaykor )", "", name)
    out = {name.upper(), base_name.upper()}
    if cat == "Primary":
        out |= {"PRIMARY"}
        if t == "Shotgun": out |= {"SHOTGUN"}
        else: out |= {"RIFLE"}
        if t == "Sniper": out |= {"SNIPER"}
        if t == "Bow": out |= {"BOW"}
        if t == "Rifle" and (w.get("trigger") or "") in ("Auto", "Held", "Auto Burst"): out |= {"ASSAULT RIFLE"}
    elif cat == "Secondary":
        out |= {"PISTOL", "SECONDARY"}
        if t == "Throwing": out |= {"THROWN"}
    elif cat == "Melee":
        out |= {"MELEE"}
    return out


def _mod(tb, name):
    r = tb.fiche_mod(name)
    if "erreur" in r: return None, r
    return r["mods"][-1], None


def _effects(card):
    stats, rest = calc.parse_mod_effects(card["effets_rang_max"])
    return stats, rest


def compute(w, mods_stats):
    """mods_stats : liste ordonnée de dicts de stats (sortie de parse_mod_effects), un par emplacement."""
    base = {k: v for k, v in (w.get("damage") or {}).items() if k != "total" and isinstance(v, (int, float)) and v > 0}
    total_base = sum(base.values())
    dmg_bonus = sum(s.get("damage", 0) + s.get("melee_damage", 0) for s in mods_stats)
    phys_bonus = {p: sum(s.get(p, 0) for s in mods_stats) for p in PHYS}
    out = {}
    for p in PHYS:
        if base.get(p): out[p] = base[p] * (1 + dmg_bonus) * (1 + phys_bonus[p])
    # éléments des mods, dans l'ordre, puis éléments propres à l'arme
    seq = []
    for s in mods_stats:
        for e in PRIMARY_ELEM:
            if s.get(e): seq.append((e, total_base * (1 + dmg_bonus) * s[e]))
    for e in PRIMARY_ELEM:
        if base.get(e): seq.append((e, base[e] * (1 + dmg_bonus)))
    elems, pending = {}, None  # elems : type final -> valeur
    owner = {}  # élément primaire -> type final qui l'a absorbé
    for e, v in seq:
        if e in owner:
            elems[owner[e]] += v; continue
        if pending and pending[0] != e:
            combo = COMBOS[frozenset((pending[0], e))]
            elems[combo] = elems.get(combo, 0) + pending[1] + v
            owner[pending[0]] = owner[e] = combo
            pending = None
        elif pending:
            pending = (e, pending[1] + v)
        else:
            pending = (e, v)
    if pending:
        elems[pending[0]] = elems.get(pending[0], 0) + pending[1]
    for k, v in base.items():  # éléments combinés propres à l'arme (ex. Blast du Kuva Bramma)
        if k not in PHYS and k not in PRIMARY_ELEM: elems[k] = elems.get(k, 0) + v * (1 + dmg_bonus)
    out.update(elems)
    per_hit = sum(out.values())
    S = lambda k: sum(s.get(k, 0) for s in mods_stats)
    cc = (w.get("criticalChance") or 0) * (1 + S("crit_chance"))
    cm = (w.get("criticalMultiplier") or 0) * (1 + S("crit_damage"))
    st = (w.get("procChance") or 0) * (1 + S("status_chance"))
    ms = (w.get("multishot") or 1) * (1 + S("multishot"))
    speed_key = "attack_speed" if w.get("category") == "Melee" else "fire_rate"
    fr = (w.get("fireRate") or 0) * (1 + S(speed_key) + (S("fire_rate") if speed_key == "attack_speed" else 0))
    crit_factor = calc.average_crit_factor(cc, cm) if cm else 1
    avg_hit = per_hit * crit_factor * ms
    res = {"degats_par_type": {k: round(v, 1) for k, v in sorted(out.items(), key=lambda t: -t[1])},
           "degats_par_coup": round(per_hit, 1), "chance_critique": f"{round(cc * 100, 1)} %",
           "multiplicateur_critique": f"x{round(cm, 2)}", "chance_statut": f"{round(st * 100, 1)} %",
           "multitir": round(ms, 2), ("vitesse_attaque" if w.get("category") == "Melee" else "cadence"): round(fr, 2),
           "degats_moyens_par_coup": round(avg_hit), "dps_rafale": round(avg_hit * fr),
           "statuts_par_seconde": round(st * ms * fr, 2)}
    mag, rl = w.get("magazineSize"), w.get("reloadTime")
    if w.get("category") != "Melee" and mag and rl and fr:
        mag2 = mag * (1 + S("magazine")); rl2 = rl / (1 + S("reload_speed")) if S("reload_speed") > -1 else rl
        t_fire = mag2 / fr
        res["chargeur"] = round(mag2); res["rechargement_s"] = round(rl2, 2)
        res["dps_soutenu"] = round(avg_hit * fr * t_fire / (t_fire + rl2))
    if w.get("category") == "Melee":
        res["portee_m"] = round((w.get("range") or 0) + S("melee_range"), 2)
    return res


def _exalted_scaling(tb, w, frame, notes):
    """Applique la puissance / la portée de la warframe quand la règle de l'arme le dit (01-donnees/armes-exaltees.json)."""
    rule = tb.exalted_rule(w["name"])
    if not rule: return w
    w = dict(w)
    if not w.get("range") and rule.get("portee_base_m"): w["range"] = rule["portee_base_m"]
    st, rg = (frame or {}).get("strength"), (frame or {}).get("range")
    if rule.get("degats_x_puissance") and st:
        w["damage"] = {k: (v * st if isinstance(v, (int, float)) and k != "total" else v) for k, v in (w.get("damage") or {}).items()}
        notes.append(f"{w['name']} : dégâts de base x puissance de capacité ({round(st * 100)} %) [{rule.get('source', '')}]")
    elif rule.get("degats_x_puissance") is None:
        notes.append(f"{w['name']} : effet de la puissance de capacité sur les dégâts inconnu, non compté")
    if rule.get("portee_x_portee") and rg and w.get("range"):
        w["range"] = w["range"] * rg
        notes.append(f"{w['name']} : portée de base x portée de capacité ({round(rg * 100)} %)")
    if rule.get("combo_de_capacite"):
        notes.append(f"{w['name']} : dégâts multipliés par le compteur de combo de capacité (jusqu'à 12x), non compté dans le DPS")
    return w


COMBO_MAX = 12


def _combo_12x(tb, w, cards, stats_list, is_ex):
    """Mêlée : Blood Rush et Weeping Wounds ajoutent leur bonus x (multiplicateur de combo - 1), dans la même somme que les
    autres mods (wiki, page Blood Rush : 40 % à 2x, 440 % à 12x). Armes exaltées à compteur de combo de capacité (Ash, Atlas,
    Gara, Khora) : dégâts multipliés 1:1 par ce compteur (wiki, Update 38.5)."""
    if w.get("category") != "Melee": return None
    cc = st = 0.0
    for c in cards:
        txt = " ".join(c["effets_rang_max"])
        m = re.search(r"\+([\d.]+)% Critical Chance stacks with Combo", txt)
        if m: cc += float(m.group(1)) / 100
        m = re.search(r"\+([\d.]+)% Status Chance per Combo", txt)
        if m: st += float(m.group(1)) / 100
    ability_combo = is_ex and (tb.exalted_rule(w["name"]) or {}).get("combo_de_capacite")
    if not (cc or st or ability_combo): return None
    k = COMBO_MAX - 1
    s = compute(w, stats_list + [{"crit_chance": cc * k, "status_chance": st * k}])
    mult = COMBO_MAX if ability_combo else 1
    out = {"chance_critique": s["chance_critique"], "chance_statut": s["chance_statut"],
           "degats_moyens_par_coup": round(s["degats_moyens_par_coup"] * mult), "dps_rafale": round(s["dps_rafale"] * mult)}
    parts = [f"critique {s['chance_critique']}" + (" (Blood Rush)" if cc else ""), f"statut {s['chance_statut']}" + (" (Weeping Wounds)" if st else "")]
    if ability_combo: parts.append(f"dégâts x{COMBO_MAX} par le combo de capacité : {out['degats_moyens_par_coup']} par coup")
    out["detail"] = ", ".join(parts) + " (combo de capacité)" if ability_combo else ", ".join(parts) + " (combo de mêlée)"
    return out


def is_talons(w):
    """Griffes de Garuda : pas une arme exaltée en jeu, elles occupent l'emplacement de mêlée de Garuda."""
    return "Garuda" in (w.get("name") or "") and "Talons" in (w.get("name") or "")


def validate(tb, slot, spec, extra=None, exalted=False, frame=None):
    """spec : {nom, mods:[8], exilus, arcane}. Renvoie erreurs, manquants, lignes du tableau, stats calculées.
    exalted=True : arme exaltée d'une capacité (modée à part ; slot = emplacement dont elle prend les mods).
    frame : {"strength": puissance totale, "range": portée totale} de la warframe, pour les armes exaltées qui en dépendent."""
    name = (spec.get("nom") or "").strip()
    errors, missing, rows, notes = [], [], [], []
    r = tb.con.execute("SELECT data FROM weapons WHERE name = ? COLLATE NOCASE", (name,)).fetchone()
    if not r:
        f = tb.fiche_arme(name)
        if "erreur" in f: return {"erreurs": [f"arme {slot} « {name} » : inconnue"], "manquants": [], "lignes": [], "stats": None}
        r = tb.con.execute("SELECT data FROM weapons WHERE name = ? COLLATE NOCASE", (f["name"],)).fetchone()
    w = json.loads(r["data"])
    if w.get("category") != SLOT_CAT[slot]:
        return {"erreurs": [f"« {w['name']} » n'est pas une arme {slot} ({w.get('category')})"], "manquants": [], "lignes": [], "stats": None}
    is_ex = w.get("type") == "Exalted Weapon" and not is_talons(w)
    if is_ex and not exalted:
        return {"erreurs": [f"« {w['name']} » est une arme exaltée (donnée par une capacité) : elle va dans armes.exaltees, pas en {slot}"],
                "manquants": [], "lignes": [], "stats": None}
    if exalted and not is_ex:
        return {"erreurs": [f"« {w['name']} » n'est pas une arme exaltée"], "manquants": [], "lignes": [], "stats": None}
    ok = compat_for(w)
    names = [m for m in (spec.get("mods") or []) if m]
    if len(names) > 8: errors.append(f"{w['name']} : {len(names)} mods, 8 au maximum")
    if len(names) < 8: missing.append(f"{w['name']} : mods {len(names)} sur 8")
    cards, seen = [], set()
    for i, n in enumerate(names[:8], 1):
        c, err = _mod(tb, n)
        if not c: errors.append(f"{w['name']}, mod {i} « {n} » : {err['erreur']}"); continue
        if (c.get("pour") or "").upper() not in ok:
            errors.append(f"{w['name']} : « {c['nom']} » est un mod pour {c.get('pour')}, incompatible avec cette arme ({w.get('type')})"); continue
        root = re.sub(r"^(Primed|Umbral|Archon|Amalgam|Galvanized)\s+", "", c["nom"])
        if c["nom"].lower() in seen or root.lower() in seen:
            errors.append(f"{w['name']} : « {c['nom']} » en double ou de la même famille qu'un autre mod"); continue
        seen |= {c["nom"].lower(), root.lower()}
        cards.append(c)
    ex = (spec.get("exilus") or "").strip()
    excard = None
    if ex:
        excard, err = _mod(tb, ex)
        if not excard: errors.append(f"{w['name']}, exilus « {ex} » : {err['erreur']}")
        elif not excard.get("exilus") or (excard.get("pour") or "").upper() not in ok:
            errors.append(f"{w['name']} : « {excard['nom']} » ne va pas dans l'Exilus de cette arme"); excard = None
    arc = (spec.get("arcane") or "").strip()
    if is_ex or is_talons(w):
        w = _exalted_scaling(tb, w, frame, notes)
    if arc:
        hit = [a for a in tb.fiche_arcane(arc).get("arcanes", []) if a["type"] in ARCANE_TYPES[slot]]
        if not hit: errors.append(f"{w['name']} : arcane d'arme « {arc} » introuvable pour une arme {slot}")
        else: rows.append(("Arcane", hit[0]["nom"], "", hit[0]["effet_rang_max"][:1]))
    stats_list = []
    for c in cards + ([excard] if excard else []):
        st, rest = _effects(c)
        stats_list.append(st)
        rows.append(("Exilus" if c is excard else "Mod", c["nom"], f"coût {c['cout_rang_max']}", c["effets_rang_max"]))
        if rest: notes.append(f"{c['nom']} : effet non compté dans le calcul : {rest[0][:100]}")
    # capacité (60 au rang 30) : polarités déjà posées sur l'arme d'abord, formas seulement si ça ne rentre pas
    ex_pol = w.get("exilusPolarity")
    ex_cost = polarites.mod_cost(excard["cout_rang_max"], ex_pol, excard.get("polarite")) if excard else 0
    pl = polarites.place([(c["nom"], c["cout_rang_max"], c.get("polarite")) for c in cards], w.get("polarities"), 60 - ex_cost)
    formas = pl["formas"]
    used = pl["cout"] + ex_cost
    if used > 60: errors.append(f"{w['name']} : les mods ne rentrent pas (coût {used} pour 60)")
    if extra:
        stats_list.append(extra)
        notes.append("bonus des fragments d'Archonte inclus : " + ", ".join(f"{k} +{round(v * 100, 1):g} %" for k, v in extra.items()))
    stats = compute(w, stats_list)
    combo = _combo_12x(tb, w, cards, stats_list, is_ex)
    if combo:
        stats["a_combo_12x"] = combo
        notes.append(f"{w['name']} à combo 12x : " + combo["detail"])
    return {"arme": w["name"], "type": w.get("type"), "erreurs": errors, "manquants": missing, "remarques": notes,
            "lignes": rows, "stats": stats, "capacite": {"capacite": 60, "cout": used, "formas_necessaires_au_minimum": formas,
                                                 "emplacements": pl["emplacements"],
                                                 "polarites_de_base": {"mods": list(w.get("polarities") or []), "exilus": ex_pol,
                                                                       "posture": w.get("stancePolarity")}},
            "non_compte": "bonus de faction, cumuls conditionnels (combo, kills), rivens, arcanes et buffs ne sont pas dans le calcul"}
