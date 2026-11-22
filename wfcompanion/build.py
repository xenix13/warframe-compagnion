"""Validation d'un build proposé par le modèle : c'est le code qui vérifie, complète et calcule.

Le modèle remplit une fiche (tous les emplacements d'un loadout). Ce module répond :
  - erreurs : mod inconnu ou inexistant en jeu, doublon, mod incompatible, aura qui n'en est pas une... ;
  - manquants : emplacements vides (un build n'est complet que quand cette liste est vide) ;
  - totaux exacts (puissance, durée, portée, efficacité, survie), capacité et formas nécessaires ;
  - un tableau prêt à recopier, avec les vrais effets des mods.
"""
import json, math, re

from . import calc, polarites, rules, shards as shardmod, weapon

FOCUS = {"madurai", "naramon", "unairu", "vazarin", "zenurik"}
SLOTS_HELP = ("{warframe, role, source_energie, polarites?, aura, exilus, mods[8], arcanes[2], helminth, focus, compagnon, "
              "armes:{principale, secondaire, melee, exaltees?}, fragments[5] (facultatif)}")
ABILITY = (("strength", "Puissance"), ("duration", "Durée"), ("range", "Portée"), ("efficiency", "Efficacité"))
UMBRA_SET = {"Umbral Intensify": {2: 1.25, 3: 1.75}, "Umbral Vitality": {2: 1.3, 3: 1.8}, "Umbral Fiber": {2: 1.3, 3: 1.8}}
SURVIE = (("health", "Santé"), ("shield", "Bouclier"), ("armor", "Armure"), ("energy", "Énergie max"))


def _list(v, n=None):
    if v is None: return []
    if isinstance(v, str): v = [x.strip() for x in re.split(r"[;,\n]", v) if x.strip()]
    return [str(x).strip() for x in v if str(x).strip()]


ALIASES = {"companion": "compagnon", "pet": "compagnon", "sentinel": "compagnon", "weapons": "armes", "arcane": "arcanes",
           "arcana": "arcanes", "shards": "fragments", "archon_shards": "fragments", "frame": "warframe", "rôle": "role",
           "energy_source": "source_energie", "source_d_energie": "source_energie", "energie": "source_energie"}
ARME_ALIASES = {"primary": "principale", "primaire": "principale", "secondary": "secondaire", "mêlée": "melee", "melée": "melee"}


EMPTY = {"none", "null", "aucun", "aucune", "-", "n/a", "na", "rien", "vide", "/"}


def _clean(v):
    """Un petit modèle écrit souvent « None » ou « aucun » pour un emplacement vide."""
    if isinstance(v, str): return "" if v.strip().lower() in EMPTY else v
    if isinstance(v, list): return [x for x in (_clean(x) for x in v) if x not in ("", None)]
    if isinstance(v, dict): return {k: _clean(x) for k, x in v.items()}
    return v


def _normalize(build):
    """Accepte les clés en anglais ou mal orthographiées : un petit modèle se trompe souvent de nom de champ."""
    build = _clean(build)
    out = {}
    for k, v in build.items():
        k2 = ALIASES.get(str(k).strip().lower(), str(k).strip().lower())
        out[k2] = v
    if isinstance(out.get("armes"), dict):
        out["armes"] = {ARME_ALIASES.get(str(k).lower(), str(k).lower()): v for k, v in out["armes"].items()}
    if isinstance(out.get("armes"), dict):  # arme exaltée : une seule (dict ou nom) ou une liste
        a = out["armes"]
        for k in [k for k in a if k.startswith("exalt") and k != "exaltees"]:
            v = a.pop(k); a.setdefault("exaltees", [])
            if not isinstance(a["exaltees"], list): a["exaltees"] = [a["exaltees"]]
            a["exaltees"] += v if isinstance(v, list) else [v]
        if "exaltees" in a and not isinstance(a["exaltees"], list): a["exaltees"] = [a["exaltees"]]
    for k in ("principale", "secondaire", "melee"):  # armes données à plat
        if k in out and isinstance(out[k], str):
            out.setdefault("armes", {}); out["armes"].setdefault(k, out.pop(k))
    return out


def validate(tb, build):
    """tb : Toolbox. build : dict rempli par le modèle."""
    if isinstance(build, str):
        try: build = json.loads(build)
        except json.JSONDecodeError: return {"erreur": "le build doit être un objet JSON", "format": SLOTS_HELP}
    build = _normalize(build)
    errors, missing, notes, rows = [], [], [], []
    hors = {str(x).lower() for x in _list(build.get("hors_build"))}  # parties laissées au choix du joueur (armes, compagnon)
    wf_name = (build.get("warframe") or "").strip()
    wf = tb.fiche_warframe(wf_name) if wf_name else {"erreur": "warframe manquante"}
    if "erreur" in wf:
        return {"erreur": wf["erreur"], "noms_proches": wf.get("noms_proches"), "format": SLOTS_HELP}
    base_name = re.sub(r"\s+(Prime|Umbra)$", "", wf["nom"])
    totals = {}
    cards = []

    def mod(name, role):
        r = tb.fiche_mod(name)
        if "erreur" in r:
            errors.append(f"{role} « {name} » : {r['erreur']}" + (f" ; noms proches : {', '.join(r['noms_proches'])}" if r.get("noms_proches") else ""))
            return None
        return r["mods"][-1]

    # --- aura
    pols = build.get("polarites") if isinstance(build.get("polarites"), dict) else None
    aura_info = {"polarite": wf.get("polarite_aura")}
    capacity = 30 if build.get("reacteur") is False else 60  # sans Orokin Reactor : 30
    aura = (build.get("aura") or "").strip()
    if not aura: missing.append("aura")
    else:
        c = mod(aura, "aura")
        if c:
            if (c.get("pour") or "").upper() != "AURA":
                errors.append(f"« {c['nom']} » n'est pas une aura (c'est un mod {c.get('pour')})")
            else:
                raw = tb.con.execute("SELECT base_drain, fusion_limit, polarity FROM mods WHERE name=? ORDER BY fusion_limit DESC", (c["nom"],)).fetchone()
                bonus = -(raw["base_drain"] or 0) + (raw["fusion_limit"] or 0)
                slot_pol = (pols or {}).get("aura") or wf.get("polarite_aura")
                got = polarites.aura_bonus(bonus, slot_pol, raw["polarity"])
                capacity += got
                aura_info = {"polarite": slot_pol, "apport": got, "apport_normal": bonus, "pol_mod": raw["polarity"], "forma": False}
                hint = "" if polarites.matches(slot_pol, raw["polarity"]) else (
                    f" (+{bonus * 2} avec un forma {raw['polarity']} sur l'aura" + (f" ; polarité {slot_pol} qui ne correspond pas : -25 %" if slot_pol else "") + ")")
                rows.append(("Aura", c["nom"], f"+{got} capacité" + hint, c["effets_rang_max"]))
                if "energy siphon" in c["nom"].lower():
                    notes.append("Energy Siphon : le joueur juge les auras d'énergie presque inutiles ; comparer avec une aura de dégâts ou de survie.")

    # --- exilus
    ex = (build.get("exilus") or "").strip()
    if not ex:
        if "exilus" not in hors: missing.append("exilus")
    else:
        c = mod(ex, "exilus")
        if c:
            if not c.get("exilus"): errors.append(f"« {c['nom']} » ne va pas dans l'emplacement Exilus")
            else: cards.append(("Exilus", c))

    # --- 8 mods
    names = _list(build.get("mods"))
    if len(names) > 8: errors.append(f"{len(names)} mods : 8 au maximum (hors aura et Exilus)")
    if len(names) < 8 and "mods" not in hors: missing.append(f"mods : {len(names)} sur 8")
    seen = set()
    for i, n in enumerate(names[:8], 1):
        c = mod(n, f"mod {i}")
        if not c: continue
        if c["nom"].lower() in seen: errors.append(f"« {c['nom']} » est en double"); continue
        seen.add(c["nom"].lower())
        pour = (c.get("pour") or "").upper()
        if pour == "AURA": errors.append(f"« {c['nom']} » est une aura : la mettre dans « aura »"); continue
        helm_aug = (build.get("helminth") or "").strip() and " ".join(c.get("effets_rang_max", [])).lower().startswith(
            (build.get("helminth") or "").strip().lower() + " augment:")
        if pour not in ("WARFRAME", base_name.upper()) and not helm_aug:  # augment d'une capacité du Helminth : autorisé
            errors.append(f"« {c['nom']} » est un mod pour {c.get('pour')}, pas pour {wf['nom']}"); continue
        cards.append((f"Mod {i}", c))
    fam = {}
    for _, c in cards:  # familles qui ne se cumulent pas (Intensify / Umbral / Archon / Primed d'un même mod)
        root = re.sub(r"^(Primed|Umbral|Archon|Amalgam|Galvanized|Steel)\s+", "", c["nom"])
        fam.setdefault(root, []).append(c["nom"])
    for root, lst in fam.items():
        if len(lst) > 1: errors.append(f"{' et '.join(lst)} sont de la même famille et ne se cumulent pas")

    drains = []
    # set Umbra (wiki, page Umbral Intensify) : 2 pièces = Intensify x1,25, Vitality et Fiber x1,30 ; 3 pièces = x1,75 et x1,80
    n_umbra = sum(1 for _, c in cards if c["nom"] in UMBRA_SET)
    for slot, c in cards:
        m = UMBRA_SET[c["nom"]][n_umbra] if c["nom"] in UMBRA_SET and n_umbra >= 2 else 1
        for k, v in c.get("stats_additionnables", {}).items(): totals[k] = totals.get(k, 0) + v * m
        if m != 1:
            notes.append(f"{c['nom']} : bonus du set Umbra ({n_umbra} pièces) compté, effet x{m}")
            c = dict(c, set=None, effets_rang_max=[f"{e} (x{m} avec le set Umbra : {n_umbra} pièces)" for e in c["effets_rang_max"]])
        rows.append((slot, c["nom"], f"coût {c['cout_rang_max']}", c["effets_rang_max"]))
        drains.append((slot, c["nom"], c["cout_rang_max"], c.get("polarite")))
        if c.get("effets_conditionnels_ou_speciaux") and not c.get("augment_de"):
            notes.append(f"{c['nom']} : effet non compté dans les totaux : {c['effets_conditionnels_ou_speciaux'][0][:110]}")
        if c.get("set") and c["nom"] not in UMBRA_SET: notes.append(f"{c['nom']} fait partie du set {c['set']} : le bonus de set n'est pas compté dans les totaux.")

    used = {c["nom"].lower() for _, c in cards}
    unused = [r["name"] for r in tb.con.execute("SELECT DISTINCT name FROM mods WHERE compat = ? COLLATE NOCASE", (base_name,))
              if r["name"].lower() not in used]
    if unused and len(unused) == len(list(tb.con.execute("SELECT DISTINCT name FROM mods WHERE compat = ? COLLATE NOCASE", (base_name,)))):
        notes.append(f"Aucun augment de {base_name} dans le build ({', '.join(unused)}). Un build centré sur une capacité a "
                     "souvent besoin de son augment : vérifier, et dire pourquoi s'il n'est pas pris.")

    # --- capacité et formas : polarités déjà posées sur la warframe d'abord, formas seulement si ça ne rentre pas
    base_pols = list(wf.get("polarites") or [])
    ex_pol = (pols or {}).get("exilus") or wf.get("polarite_exilus")
    ex_cost, ex_forma = 0, False
    for slot, n, cost, pol in drains:
        if slot == "Exilus": ex_cost = polarites.mod_cost(cost, ex_pol, pol); ex_card = (n, cost, pol)
    mods_d = [(n, cost, pol) for slot, n, cost, pol in drains if slot != "Exilus"]
    if pols and isinstance(pols.get("mods"), list) and any(pols["mods"]):
        # polarités posées par le joueur, emplacement par emplacement (dans l'ordre des mods)
        slot_pols = [(p or "").lower() or None for p in (pols.get("mods") + [None] * 8)[:8]]
        places = [{"polarite_origine": None, "polarite": p, "mod": m[0], "cout": polarites.mod_cost(m[1], p, m[2]), "forma": False}
                  for m, p in zip(mods_d, slot_pols)]
        left = list(base_pols); formas = 0
        for pl in places:
            p = pl["polarite"]
            if not p: continue
            if p in left: left.remove(p); pl["polarite_origine"] = p
            else: formas += 1; pl["forma"] = True
        total_drain = sum(pl["cout"] for pl in places) + ex_cost
        cap = {"capacite": capacity, "cout_des_8_mods": total_drain, "formas_posees": formas,
               "formas_necessaires_au_minimum": formas, "polarites": "posées par le joueur", "emplacements": places}
    else:
        pl = polarites.place(mods_d, base_pols, capacity - ex_cost)
        formas = pl["formas"]
        # forma sur l'emplacement d'aura : son apport double ; à prendre dès qu'on pose des formas (ou que ça ne rentre pas)
        ai = aura_info
        if ai.get("pol_mod") and not polarites.matches(ai.get("polarite"), ai["pol_mod"]) and (formas > 0 or pl["cout"] + ex_cost > capacity):
            cap2 = capacity - ai["apport"] + ai["apport_normal"] * 2
            pl2 = polarites.place(mods_d, base_pols, cap2 - ex_cost)
            if pl2["formas"] + 1 <= formas or (pl["cout"] + ex_cost > capacity and pl2["cout"] + ex_cost <= cap2):
                gain = ai["apport_normal"] * 2 - ai["apport"]
                capacity, pl, formas = cap2, pl2, pl2["formas"] + 1
                ai.update(polarite=ai["pol_mod"], apport=ai["apport_normal"] * 2, forma=True)
                rows[:] = [(a, b, f"+{ai['apport']} capacité (forma {ai['pol_mod']} sur l'aura)", d) if a == "Aura" else (a, b, c_, d)
                           for a, b, c_, d in rows]
                notes.append(f"forma {ai['pol_mod']} sur l'emplacement d'aura : +{gain} de capacité, moins de formas sur les mods")
        if pl["cout"] + ex_cost > capacity and ex_cost and drains and not polarites.matches(ex_pol, ex_card[2]) and ex_card[2]:
            ex_cost, ex_forma, ex_pol = math.ceil(ex_card[1] / 2), True, ex_card[2]; formas += 1
        total_drain = pl["cout"] + ex_cost
        cap = {"capacite": capacity, "cout_des_8_mods": total_drain, "formas_necessaires_au_minimum": formas,
               "emplacements": pl["emplacements"]}
    cap["aura"] = aura_info
    cap["exilus"] = {"polarite": ex_pol, "cout": ex_cost, "forma": ex_forma}
    cap["polarites_de_base"] = {"aura": wf.get("polarite_aura"), "exilus": wf.get("polarite_exilus"), "mods": base_pols}
    if total_drain > capacity: errors.append(f"le build ne rentre pas : coût {total_drain} pour {capacity} de capacité, même avec un forma sur chaque mod")

    # --- arcanes
    arcs = _list(build.get("arcanes"))
    if len(arcs) < 2 and "arcanes" not in hors: missing.append(f"arcanes : {len(arcs)} sur 2")
    for a in arcs[:2]:
        r = tb.fiche_arcane(a)
        hit = [x for x in r.get("arcanes", []) if x["type"] == "Warframe Arcane"]
        if not hit: errors.append(f"arcane de warframe « {a} » introuvable")
        else: rows.append(("Arcane", hit[0]["nom"], "", hit[0]["effet_rang_max"][:1]))

    # --- fragments d'Archonte
    frag = _list(build.get("fragments"))
    sh_bonus, sh_err, sh_rows = shardmod.apply(frag)
    errors += sh_err
    for k in ("strength", "duration"):
        if sh_bonus.get(k): totals[k] = totals.get(k, 0) + sh_bonus[k]
    for lab, kind, val in sh_rows:
        rows.append(("Fragment", lab, "", [("non calculé (effet conditionnel ou utilitaire)" if kind == "texte" else
                                           f"+{val:g}" if kind == "flat" else f"+{round(val * 100, 1):g} %")]))

    # --- armes
    armes = build.get("armes") or {}
    if isinstance(armes, dict):  # arme exaltée mise par erreur dans un emplacement normal : on la range à sa place
        own = {x["nom"].lower(): x["nom"] for x in tb.armes_exaltees(wf["nom"]) if not x["griffes_garuda"]}
        for slot in ("principale", "secondaire", "melee"):
            spec = armes.get(slot)
            n = (spec.get("nom") if isinstance(spec, dict) else spec) or ""
            if isinstance(n, str) and n.strip().lower() in own:
                armes.pop(slot)
                armes.setdefault("exaltees", []).append(spec)
                notes.append(f"« {own[n.strip().lower()]} » rangée dans les armes exaltées (elle était en {slot}) ; l'emplacement {slot} reste à remplir")
    detail = {}
    energy_for_violet = None
    for slot in ("principale", "secondaire", "melee"):
        spec = armes.get(slot) if isinstance(armes, dict) else None
        if isinstance(spec, dict):
            n = (spec.get("nom") or "").strip()
            if n and spec.get("mods"):
                extra = {}
                if slot == "melee":
                    if energy_for_violet is None:
                        rw = tb.con.execute("SELECT data FROM warframes WHERE name = ? COLLATE NOCASE", (wf["nom"],)).fetchone()
                        e30 = tb.rank30(json.loads(rw["data"]))["energie"]
                        energy_for_violet = e30 * (1 + totals.get("energy", 0)) + sh_bonus.get("energy_flat", 0)
                    v = sh_bonus.get("violet_melee_crit", 0) * (2 if energy_for_violet > 500 else 1)
                    extra["crit_damage"] = sh_bonus.get("melee_crit_damage", 0) + v
                elif slot == "principale":
                    extra["status_chance"] = sh_bonus.get("primary_status", 0)
                    if sh_bonus.get("primary_electricity"): extra["electricity"] = sh_bonus["primary_electricity"]
                elif slot == "secondaire":
                    extra["crit_chance"] = sh_bonus.get("secondary_crit", 0)
                res = weapon.validate(tb, slot, spec, {k: v for k, v in extra.items() if v},
                                      frame={"strength": 1 + totals.get("strength", 0), "range": 1 + totals.get("range", 0)})
                errors += res["erreurs"]; missing += res["manquants"]; notes += res.get("remarques", [])
                detail[slot] = {k: res.get(k) for k in ("arme", "type", "stats", "capacite", "non_compte")}
                detail[slot]["tableau"] = [(s_, n_, c_, e_) for s_, n_, c_, e_ in res["lignes"]]
                if res.get("stats"):
                    st = res["stats"]
                    rows.append((f"Arme {slot}", res["arme"], f"{res['capacite']['cout']}/60",
                                 [f"{st['degats_moyens_par_coup']} dégâts moyens par coup, DPS {st['dps_rafale']}, "
                                  f"critique {st['chance_critique']} {st['multiplicateur_critique']}, statut {st['chance_statut']}"]))
                continue
        else:
            n = (spec or "").strip() if isinstance(spec, str) else ""
        if not n:
            if "armes" not in hors: missing.append(f"arme {slot}")
            continue
        r = tb.fiche_arme(n)
        if "erreur" not in r and r.get("type") == "Exalted Weapon" and not weapon.is_talons({"name": r["name"]}):
            errors.append(f"« {r['name']} » est une arme exaltée (donnée par une capacité) : elle va dans armes.exaltees"); continue
        if "erreur" not in r and slot == "melee" and r.get("category") != "Melee":
            errors.append(f"« {r['name']} » n'est pas une arme de mêlée ({r.get('category')})"); continue
        if "erreur" not in r and slot in ("principale", "secondaire") and r.get("category") != {"principale": "Primary", "secondaire": "Secondary"}[slot]:
            errors.append(f"« {r['name']} » n'est pas une arme {slot} ({r.get('category')})"); continue
        if "erreur" in r: errors.append(f"arme {slot} « {n} » : inconnue" + (f" ; noms proches : {', '.join(r['noms_proches'])}" if r.get("noms_proches") else ""))
        else: rows.append((f"Arme {slot}", r["name"], "", [f"critique {round((r.get('criticalChance') or 0) * 100)} % x{r.get('criticalMultiplier')}, statut {round((r.get('procChance') or 0) * 100)} %"]))

    # --- griffes de Garuda (emplacement de mêlée imposé) et armes exaltées (modées à part)
    exalted = tb.armes_exaltees(wf["nom"])
    talons = [x["nom"] for x in exalted if x["griffes_garuda"]]
    mspec = armes.get("melee") if isinstance(armes, dict) else None
    mname = ((mspec.get("nom") if isinstance(mspec, dict) else mspec) or "").strip()
    if talons and mname and mname.lower() not in [t.lower() for t in talons] + ["garuda talons", "garuda prime talons"]:
        errors.append(f"{wf['nom']} ne peut pas équiper « {mname} » : ses griffes ({talons[0]}) occupent l'emplacement de mêlée")
    if not talons and "garuda" in mname.lower() and "talons" in mname.lower():
        errors.append(f"« {mname} » : seules Garuda et Garuda Prime ont ces griffes")
    ex_names = {x["nom"].lower(): x for x in exalted if not x["griffes_garuda"]}
    for spec in (armes.get("exaltees") or []) if isinstance(armes, dict) else []:
        if isinstance(spec, str): spec = {"nom": spec}
        if not isinstance(spec, dict): continue
        n = (spec.get("nom") or "").strip()
        x = ex_names.get(n.lower())
        if not x:
            errors.append(f"arme exaltée « {n} » : {wf['nom']} n'en a pas de ce nom" +
                          (f" (les siennes : {', '.join(v['nom'] for v in ex_names.values())})" if ex_names else " (aucune arme exaltée)"))
            continue
        if not spec.get("mods"):
            rows.append(("Arme exaltée", x["nom"], "", ["pas de mods indiqués"])); continue
        extra = {}
        if x["emplacement"] == "melee":
            if energy_for_violet is None:
                rw = tb.con.execute("SELECT data FROM warframes WHERE name = ? COLLATE NOCASE", (wf["nom"],)).fetchone()
                energy_for_violet = tb.rank30(json.loads(rw["data"]))["energie"] * (1 + totals.get("energy", 0)) + sh_bonus.get("energy_flat", 0)
            extra["crit_damage"] = sh_bonus.get("melee_crit_damage", 0) + sh_bonus.get("violet_melee_crit", 0) * (2 if energy_for_violet > 500 else 1)
        res = weapon.validate(tb, x["emplacement"], spec, {k: v for k, v in extra.items() if v}, exalted=True,
                              frame={"strength": 1 + totals.get("strength", 0), "range": 1 + totals.get("range", 0)})
        errors += res["erreurs"]; missing += res["manquants"]; notes += res.get("remarques", [])
        key = "exaltee " + x["nom"]
        detail[key] = {k: res.get(k) for k in ("arme", "type", "stats", "capacite", "non_compte")}
        detail[key]["tableau"] = [(s_, n_, c_, e_) for s_, n_, c_, e_ in res["lignes"]]
        if res.get("stats"):
            st = res["stats"]
            rows.append(("Arme exaltée", res["arme"], f"{res['capacite']['cout']}/60",
                         [f"{st['degats_moyens_par_coup']} dégâts moyens par coup, DPS {st['dps_rafale']}, "
                          f"critique {st['chance_critique']} {st['multiplicateur_critique']}, statut {st['chance_statut']}"]))
    if ex_names and not (armes.get("exaltees") if isinstance(armes, dict) else None):
        notes.append(f"{wf['nom']} a une arme exaltée ({', '.join(v['nom'] for v in ex_names.values())}) : "
                     "elle se mode à part, dans armes.exaltees, si le build l'utilise")

    # --- Arcane Persistence retire tout le bouclier : ce qui compte sur le bouclier ne sert plus
    arc_names = [str(x).lower() for x in _list(build.get("arcanes"))]
    if any("persistence" in x for x in arc_names):
        shieldy = [c["nom"] for _, c in cards if re.search(r"shield", " ".join(c.get("effets_rang_max", [])), re.I)]
        if aura.lower() == "brief respite": shieldy.insert(0, "Brief Respite")
        if shieldy:
            errors.append("Arcane Persistence retire tout le bouclier : " + ", ".join(shieldy) + " ne sert plus à rien. "
                          "Choisir la défense par le bouclier (shield gate) ou par l'armure, pas les deux.")

    # --- archétypes préparés : le build doit en suivre un, ou dire pourquoi il s'en écarte (champ hors_archetype)
    arch = tb.archetypes(wf["nom"]); arch_gap = ""
    if "erreur" not in arch:
        used_mods = {c["nom"].lower() for _, c in cards}
        followed = [a for a in arch.get("archetypes", [])
                    if all(m.lower() in used_mods for m in (a.get("noyau") or {}).get("mods", []))]
        if followed:
            notes.append("archétype suivi : " + ", ".join(f"« {a['nom']} »" for a in followed))
        elif not (build.get("hors_archetype") or "").strip():
            arch_gap = ("noyau d'un archétype : " + " ; ou ".join(
                f"{', '.join(a['noyau']['mods'])} pour « {a['nom']} »" for a in arch.get("archetypes", []) if (a.get("noyau") or {}).get("mods"))
                + " (ou champ hors_archetype avec la raison)")
            notes.append("aucun archétype préparé n'est suivi : " + arch_gap)

    # --- helminth : une capacité transférable d'une AUTRE warframe
    h = (build.get("helminth") or "").strip() if isinstance(build.get("helminth"), str) else ""
    h = re.sub(r"\s*\(.*?\)\s*$", "", h).strip()  # « Nourish (de Grendel) »
    known = tb.helminth_abilities()
    if not h:
        if "helminth" not in hors: missing.append("helminth")
    elif known:
        hit = [(a, f) for a, f in known.items() if a.lower() == h.lower()] or [(a, f) for a, f in known.items() if h.lower() in a.lower()]
        if not hit: errors.append(f"helminth « {h} » : ce n'est pas une capacité transférable ; voir options(helminth)")
        elif hit[0][1].lower() == base_name.lower():
            errors.append(f"helminth « {hit[0][0]} » est déjà une capacité de {base_name} : choisir la capacité d'une autre warframe")
        else:
            hn = tb.helminth_notes().get(hit[0][0])
            rep = str(build.get("helminth_remplace") or "").strip()
            caps = [c["nom"] for c in wf.get("capacites", [])]
            from .moteur.regles import exclusif
            clash = [c for c in caps if exclusif(hit[0][0], c) and c.lower() != rep.lower()]
            if clash: errors.append(f"helminth : {hit[0][0]} ne peut pas coexister avec {clash[0]} (même type de bonus) ; "
                                    f"remplacer {clash[0]} ou choisir un autre Helminth")
            if rep and rep.lower() not in [c.lower() for c in caps]:
                errors.append(f"helminth : « {rep} » n'est pas une capacité de {base_name} ({', '.join(caps)})"); rep = ""
            rows.append(("Helminth", f"{hit[0][0]} (de {hit[0][1]})" + (f" à la place de {rep}" if rep else ""), "",
                         [hn or ("" if rep else "remplace une capacité : dire laquelle et pourquoi")]))
            if hn: notes.append(f"Helminth {hit[0][0]} : {hn}")
    else: rows.append(("Helminth", h, "", ["non vérifié par la base"]))
    # --- compagnon
    cmp_ = (build.get("compagnon") or "").strip() if isinstance(build.get("compagnon"), str) else ""
    if not cmp_ and "compagnon" not in hors: missing.append("compagnon")
    else:
        allc = tb.companions()
        hit = [n for n, _ in allc if n.lower() == cmp_.lower()] or [n for n, _ in allc if cmp_.lower() in n.lower() or n.lower() in cmp_.lower()]
        if allc and not hit: errors.append(f"compagnon « {cmp_} » inconnu ; voir options(compagnon)")
        else: rows.append(("Compagnon", hit[0] if hit else cmp_, "", ["à justifier : ce qu'il apporte au build"]))
    foc = (build.get("focus") or "").strip()
    if not foc:
        if "focus" not in hors: missing.append("focus")
    elif foc.lower().split()[0] not in FOCUS: errors.append(f"focus « {foc} » inconnu : Madurai, Naramon, Unairu, Vazarin ou Zenurik")
    else: rows.append(("Focus", foc, "", []))
    frag = _list(build.get("fragments"))
    if frag: rows.append(("Fragments d'Archonte", " ; ".join(frag[:5]), "", ["non vérifié par la base"]))

    # --- rôle, source d'énergie, règles du joueur
    role = (build.get("role") or "").strip() if isinstance(build.get("role"), str) else ""
    if not role: missing.append("role (nuke, tank, soutien, contrôle...)")
    src = (build.get("source_energie") or "").strip() if isinstance(build.get("source_energie"), str) else ""
    cd = tb.costs_data(base_name) or {}
    special = cd.get("note_ressource")
    if not src and not (special and "énergie" not in cd.get("ressource", "")):
        missing.append("source_energie (d'où vient l'énergie : focus Zenurik, Helminth, arcane, orbes...)")
    elif not src: pass
    else: rows.append(("Source d'énergie", src, "", ["à justifier : elle doit REDONNER de l'énergie, pas seulement augmenter le maximum"]))
    if special: notes.append(f"Ressource propre à {base_name} : {special}")
    pr = rules.for_frame(tb.base, base_name)
    used_all = [c["nom"] for _, c in cards] + [r[1] for r in rows if r[0] in ("Aura", "Arcane")]
    advice = rules.check(pr, role, used_all, foc)
    notes += [f"note du joueur : {n}" for n in pr["notes"]]

    # --- conséquences chiffrées : ce que les choix donnent vraiment sur CETTE frame
    cons = []
    raw = tb.con.execute("SELECT data FROM warframes WHERE name = ? COLLATE NOCASE", (wf["nom"],)).fetchone()
    r30 = tb.rank30(json.loads(raw["data"]))
    armor = r30["armure"] * (1 + totals.get("armor", 0)) + sh_bonus.get("armor_flat", 0) + totals.get("armor_flat", 0)
    health = r30["sante"] * (1 + totals.get("health", 0)) + sh_bonus.get("health_flat", 0) + totals.get("health_flat", 0)
    shield = max(0, r30["bouclier"] * (1 + totals.get("shield", 0)) + ((sh_bonus.get("shield_flat", 0) + totals.get("shield_flat", 0)) if r30["bouclier"] else 0))
    energy = r30["energie"] * (1 + totals.get("energy", 0)) + sh_bonus.get("energy_flat", 0) + totals.get("energy_flat", 0)
    dr = calc.player_armor_dr(armor)
    cons.append(f"Survie avec ces mods : armure {round(armor)} (réduction {round(dr * 100)} %), santé {round(health)} "
                f"(environ {round(health / (1 - dr))} effectifs)" + (f", bouclier {round(shield)} (environ {round(shield * 2)} effectifs, "
                f"shield gate {calc.shield_gate_duration(shield):.2f} s)" if shield else ", pas de bouclier") + ".")
    for k, label, basev in (("armor", "d'armure", r30["armure"]), ("health", "de santé", r30["sante"]), ("shield", "de bouclier", r30["bouclier"])):
        if totals.get(k) and basev:
            cons.append(f"Les mods {label} ajoutent {round(basev * totals[k])} {label} (base {basev:g} au rang 30) : "
                        + ("gain faible, la base est petite." if basev < 300 else "gain réel, la base est correcte." if basev < 600 else "gain important, la base est grosse."))
    eff_now = calc.ability_stat([totals.get("efficiency", 0)])
    costs = tb.ability_costs(base_name)
    dur_now = calc.ability_stat([totals.get("duration", 0)])
    res_name = cd.get("ressource", "énergie")
    if costs and res_name.startswith("énergie"):
        cons.append(f"Coût de chaque capacité à {round(eff_now * 100)} % d'efficacité (coût fixe propre à la capacité = coût de base x "
                    f"(2 - efficacité), indépendant de l'énergie max) : "
                    + ", ".join(f"{n} {c:g} -> {calc.ability_cost(c, eff_now):g}" for n, (_, c) in sorted(costs.items(), key=lambda t: t[1][0]))
                    + f". Réserve d'énergie max du build : {round(energy)}"
                    + (f", soit environ {int(energy // calc.ability_cost(max(c for _, c in costs.values()), eff_now))} lancers de la capacité la plus chère."
                       if energy and max(c for _, c in costs.values()) else "."))
        for c in cd.get("capacites", []):
            per_s = [e for e in c.get("couts_supplementaires", []) if e["par"] == "s"]
            if not per_s or c.get("cout") is None: continue
            e = per_s[0]
            lo = calc.channel_drain(e["valeur"], eff_now, dur_now); hi = calc.channel_drain(e["valeur_max"], eff_now, dur_now)
            t10 = calc.ability_cost(c["cout"], eff_now) + hi * 10
            cons.append(f"{c['nom']} est canalisée ({c['cout_affiche_wiki']} sur le wiki) : avec ce build, le drain est de "
                        + (f"{lo:.1f} à {hi:.1f}" if hi != lo else f"{lo:.1f}") + f" d'énergie par seconde (réduit par la durée et l'efficacité) ; "
                        f"10 s coûtent jusqu'à {round(t10)} d'énergie pour une réserve de {round(energy)}"
                        + (", donc la réserve ne tient pas 10 s sans source d'énergie." if energy and t10 > energy else "."))
    elif special:
        cons.append(f"{base_name} n'utilise pas l'énergie comme les autres frames : {special}")
    dur_now = calc.ability_stat([totals.get("duration", 0)])
    for _, c in cards:
        ch = tb.channeled().get(c["nom"])
        if not ch: continue
        g = ch.get("croissance_du_drain_par_seconde", 1.0)
        line = (f"{c['nom']} rend {ch.get('capacite', 'la capacité')} canalisée : {ch['cout_initial']} d'énergie au lancement puis "
                f"{ch['drain_par_seconde']} par seconde" + (f", multiplié par {g:g} à chaque seconde" if g != 1 else "")
                + f". Avec ce build (efficacité {round(eff_now * 100)} %, durée {round(dur_now * 100)} %) : ")
        parts = []
        for sec in (5, 10):
            tot = calc.channel_total_cost(ch["cout_initial"], ch["drain_par_seconde"], sec, eff_now, dur_now, g)
            parts.append(f"{sec} s = {round(tot)} d'énergie" + (" (plus que la réserve)" if energy and tot > energy else ""))
        cons.append(line + " ; ".join(parts) + f" pour une réserve de {round(energy)}. " + ch.get("note", ""))
    arc_rows = [r for r in rows if r[0] == "Arcane"]
    for _, an, _, eff_txt in arc_rows:
        m = re.search(r"([\d.]+) maximum Energy per Armor point", " ".join(eff_txt))
        if m:
            gain = float(m.group(1)) * armor
            cons.append(f"{an} : {m.group(1)} d'énergie max par point d'armure x {round(armor)} d'armure = +{round(gain)} d'énergie max"
                        f" (soit +{round(gain / energy * 100) if energy else 0} %). Il ne redonne pas d'énergie."
                        + (" Très peu rentable ici : l'armure est trop faible." if gain < 100 else " Rentable ici." if gain >= 250 else ""))

    # --- totaux
    tot = {}
    for k, label in ABILITY:
        tot[label] = f"{round(calc.ability_stat([totals.get(k, 0)]) * 100)} %"
    eff = calc.ability_stat([totals.get("efficiency", 0)])
    tot["Coût d'une capacité de 100 d'énergie"] = round(calc.ability_cost(100, eff), 1)
    for k, label in SURVIE:
        if totals.get(k): tot[label + " (bonus des mods)"] = f"+{round(totals[k] * 100)} %"
        if totals.get(k + "_flat"): tot[label + " (valeur fixe des mods)"] = f"{totals[k + '_flat']:+g}"
    if eff < 0.75: notes.append(f"Efficacité {round(eff * 100)} % : les capacités coûtent cher. Le build doit avoir une source d'énergie "
                                "fiable (Zenurik, Helminth qui redonne de l'énergie, Arcane Energize, Equilibrium...).")
    if eff > 1.75: notes.append("Efficacité au-dessus de 175 % : le surplus ne réduit plus les coûts.")
    if len(names) >= 8 and not any(totals.get(k) for k in ("health", "shield", "armor")):
        notes.append("Pas de mod de santé, bouclier ou armure : c'est un choix possible, il faut seulement dire d'où vient la survie "
                     "(capacités, invisibilité, shield gate, arcanes).")
    elif any(totals.get(k) for k in ("health", "shield", "armor")):
        notes.append("Mod de santé, bouclier ou armure présent : il doit servir le build, par une synergie de survie (ex. Redirection "
                     "+ Arcane Aegis), une capacité qui en dépend, ou la ressource de la frame (Hildryn : plus de bouclier = plus de "
                     "capacités lancées). Expliquer lequel.")

    table = "| Emplacement | Choix | Coût | Effet |\n|---|---|---|---|\n" + "\n".join(
        f"| {s} | {n} | {c} | {' ; '.join(e)} |" for s, n, c, e in rows)
    done = not errors and not missing
    return {"statut": "complet et valide" if done else "à corriger",
            "erreurs": errors, "manquants": missing,
            "avis_du_joueur_non_suivis": advice,
            "archetype_non_suivi": arch_gap,
            "consequences_calculees": cons, "totaux": tot, "capacite": cap, "remarques": notes,
            "armes_detail": detail,
            "tableau_a_recopier_tel_quel": table,
            "suite": ("Recopie le tableau, puis explique : la boucle de jeu, la survie au level cap, et pour 3 choix importants "
                      "l'alternative comparée avec ses chiffres." + (" Pour chaque avis du joueur non suivi : soit tu modifies le build, soit tu "
                      "expliques dans ta réponse pourquoi ton build fait autrement." if advice else "") if done else
                      "Corrige les erreurs et remplis les manquants, puis rappelle valider_build avec le build complet.")}
