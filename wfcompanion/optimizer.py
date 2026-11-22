"""Construit un build complet à partir du plan du robot scripté (moteur/robot.py), sans modèle de langage.

Le petit modèle du joueur ne sait pas construire un build fiable ; le code, si. On part de l'archétype choisi (noyau,
stats visées, choix proposés), on note chaque mod candidat selon ces stats et la variante de défense, on garde le meilleur
de chaque famille, puis on valide. Chaque choix garde l'option qui l'a emporté et celle qui la suivait : l'explication du
modèle (ou de l'interface) s'appuie dessus, comme le joueur le demande (« toujours comparer »).
"""
import json, re

from . import build as buildmod, niveaux
from .moteur import robot, regles

LEVEL = [("maximum", 5.0), ("peu importante", 0.2), ("tres haute", 4.0), ("très haute", 4.0), ("haute", 3.0), ("moyenne", 1.5), ("basse", 0.3)]
STAT = {"puissance": "strength", "duree": "duration", "durée": "duration", "portee": "range", "portée": "range",
        "efficacite": "efficiency", "efficacité": "efficiency", "sante": "health", "santé": "health", "armure": "armor",
        "bouclier": "shield", "energie": "energy", "énergie": "energy"}
FLAT_SCALE = {"health": 400, "shield": 400, "armor": 300, "energy": 200}
FAMILY = re.compile(r"^(Primed|Umbral|Archon|Amalgam|Galvanized|Flawed|Steel)\s+")
DEFENSES = ("bouclier", "persistence")
MELEE_FILL = ["Blood Rush", "Weeping Wounds", "Primed Pressure Point", "Organ Shatter", "Condition Overload",
              "Primed Fever Strike", "Primed Heated Charge", "Drifting Contact", "Body Count"]
FOCUS = "Zenurik"


def _level(txt):
    t = (txt or "").lower()
    for k, v in LEVEL:
        if k in t: return v
    return 1.0


def _root(name):
    return FAMILY.sub("", name)


def pick_archetype(arch, objectif):
    """Archétype dont l'objectif et le nom partagent le plus de mots avec la demande (le premier par défaut)."""
    lst = arch.get("archetypes") or []
    if not lst: return None
    words = {w for w in re.findall(r"\w{3,}", (objectif or "").lower())}
    syn = {"nuke": "dégâts", "dps": "dégâts", "tank": "survie", "farm": "farm", "boss": "mono", "archonte": "mono"}
    words |= {v for k, v in syn.items() if k in words}
    def score(a):
        text = (a.get("objectif", "") + " " + a.get("nom", "") + " " + a.get("id", "")).lower()
        return sum(1 for w in words if w in text)
    best = max(lst, key=score)
    return best if score(best) > 0 else lst[0]


def _names_in(tb, text, table):
    """Noms d'objets du jeu (mods ou arcanes) cités dans un texte libre, dans l'ordre où ils apparaissent."""
    found = []
    for r in tb.con.execute(f"SELECT DISTINCT name FROM {table}"):
        n = r["name"]
        if len(n) < 5: continue
        i = text.lower().find(n.lower())
        if i >= 0: found.append((i, -len(n), n))
    out = []
    for _, _, n in sorted(found):
        if not any(n.lower() in o.lower() for o in out): out.append(n)
    return out


def _weights(a, defense):
    w = {"strength": 1.0, "duration": 1.0, "range": 1.0, "efficiency": 1.0, "energy": 0.3,
         "health": 0.3, "shield": 0.2, "armor": 0.3,
         # valeurs fixes (« +30 Shield Capacity ») : ramenées à peu près à un pourcentage d'une frame moyenne
         "health_flat": 0.3 / 400, "shield_flat": 0.2 / 400, "armor_flat": 0.3 / 300, "energy_flat": 0.3 / 200}
    for k, v in (a.get("stats_cibles") or {}).items():
        if k.lower() in STAT:
            key = STAT[k.lower()]; w[key] = _level(v)
            if key in FLAT_SCALE: w[key + "_flat"] = w[key] / FLAT_SCALE[key]
    if defense == "persistence":
        w.update(health=1.2, armor=1.2, shield=-2.0, health_flat=1.2 / 400, armor_flat=1.2 / 300, shield_flat=-0.01)  # plus aucun bouclier
    return w


def _candidates(tb, frame_base):
    out = []
    for r in tb.con.execute("SELECT data FROM mods WHERE type = 'Warframe Mod' AND compat IN ('WARFRAME', ?) COLLATE NOCASE",
                            (frame_base,)):
        c = tb._mod_card(json.loads(r["data"]))
        av = c.get("avertissement", "")
        if "ATTENTION" in av or "affaiblie" in av or "n'existe pas" in av: continue
        if c.get("stats_additionnables"): out.append(c)
    seen, uniq = set(), []
    for c in out:
        if c["nom"] not in seen: seen.add(c["nom"]); uniq.append(c)
    return uniq


def _score(c, w):
    v = sum(w.get(k, 0) * x for k, x in c.get("stats_additionnables", {}).items())
    # mods de set (Carapace, Gladiator…) : leur vrai intérêt est le bonus de set, que le calcul ne compte pas ;
    # seuls les sets Augur et Umbra sont gardés à leur valeur
    if c.get("set") and not re.search(r"augur|umbra", c["set"], re.I): v *= 0.5
    return v


ARCHON_EL = {"toxin": "toxin", "electricity": "electric", "cold": "cold", "heat": "heat"}


def _archon_useless(c, elements):
    """Mod Archon dont l'effet en plus dépend d'un élément que le kit n'inflige pas : il vaut alors sa version normale
    (Primed…), souvent moins chère et plus facile à obtenir."""
    if not c["nom"].startswith("Archon ") or elements is None: return False
    extra = " ".join(c.get("effets_rang_max", [])[1:]).lower()
    need = [e for e, w in ARCHON_EL.items() if w in extra]
    return bool(need) and not any(e in elements for e in need)


def _how(acc):
    return {"corrompu": "mod corrompu, coffres du Déréliction", "syndicat": "vendu par un syndicat, plusieurs jours de réputation",
            "rare": "rare : Baro Ki'Teer, Nightwave, Archontes ou Simaris"}.get(acc, acc)


def later_keys(later):
    return [re.sub(r"\s*\(.*", "", x).replace("arcanes ", "").split(" et ")[0] for x in later]


def _kit_tags(a):
    """Étiquettes du build retenu par le robot (kit gardé + Helminth + passif), sinon du kit entier."""
    if a.get("tags_build"): return set(a["tags_build"])
    return {t for x in (a.get("kit") or {}).values() for t in x.get("apporte", [])}


def persistence_ok(r30, kit_tags):
    """Arcane Persistence (règle de XeniX13) : il faut une armure de base correcte. Avec peu d'armure, elle reste
    intéressante seulement si la frame a beaucoup de santé ET une capacité qui la rend insensible aux effets de statut."""
    armor, health = r30.get("armure") or 0, r30.get("sante") or 0
    if armor >= 300: return True, f"armure de base correcte ({armor})"
    if "armure_bonus" in kit_tags: return True, "le kit donne de l'armure en plus"
    if health >= 1000 and "immunite_statut" in kit_tags:
        return True, f"peu d'armure ({armor}) mais beaucoup de santé ({health}) et une immunité aux effets de statut"
    return False, (f"trop peu d'armure ({armor}) pour Persistence" + ("" if health >= 1000 else f", et pas assez de santé ({health})")
                   + ("" if "immunite_statut" in kit_tags else " ni d'immunité aux effets de statut"))


def choose_defense(tb, a, frame_row, R):
    """Le programme choisit la défense lui-même (le joueur peut toujours demander l'autre) :
    1. pas d'arcanes à ce niveau -> bouclier ; 2. frame sans bouclier -> Persistence ;
    3. défense retenue dans le module relu de la frame ; 4. Persistence exclue si la frame ne peut pas la tenir ;
    5. sinon le bouclier, qui marche sur presque toutes les frames."""
    r30 = tb.rank30(frame_row)
    if not R["arcanes"]: return "bouclier", "Arcane Persistence demande des arcanes, pas encore à ce niveau"
    if not r30["bouclier"]: return "persistence", "cette warframe n'a pas de bouclier : le shield gate ne marche pas"
    if a.get("defense_joueur") in DEFENSES: return a["defense_joueur"], "c'est la défense retenue par le joueur qui a relu le module de cette frame"
    if a.get("objectif_cle") == "eidolon": return "bouclier", "chasse aux Eidolons : il faut une régénération rapide (bouclier, Arcane Aegis)"
    if r30["armure"] >= 500 and "soin" in _kit_tags(a) and persistence_ok(r30, _kit_tags(a))[0]:
        return "persistence", f"armure de base {r30['armure']} et le kit soigne : Arcane Persistence tient, tout sur la santé et l'armure"
    if not persistence_ok(r30, _kit_tags(a))[0]: return "bouclier", "Arcane Persistence n'est pas jouable sur cette frame : " + persistence_ok(r30, _kit_tags(a))[1]
    return "bouclier", "le shield gate (Brief Respite) marche sans dépendre de l'armure"


def propose(tb, warframe, objectif="", defense=None, archetype_id=None, tier="endgame", profile=None, demande=None):
    """tier : debutant | intermediaire | endgame (voir niveaux.py) ; profile : réponses du joueur (corrompus, reactor…)."""
    f = tb.fiche_warframe(warframe)
    if "erreur" in f: return f
    name = f["nom"]; base = re.sub(r"\s+(Prime|Umbra)$", "", name)
    a = robot.plan(tb, name, objectif, tier, demande)  # le robot scripté décide ; plus besoin d'archétype écrit à la main
    if "erreur" in a: return a
    tier = tier if tier in niveaux.TIERS else "endgame"
    R = niveaux.rules(tier, profile)
    frow = json.loads(tb.con.execute("SELECT data FROM warframes WHERE name = ? COLLATE NOCASE", (name,)).fetchone()["data"])
    if defense in DEFENSES: why_def = "demandée par le joueur"
    else: defense, why_def = choose_defense(tb, a, frow, R)
    banned = set(a.get("interdits") or [])
    ok_mod = lambda n: niveaux.access(tb, n) in R["access"] and n.lower() not in banned
    text = json.dumps(a, ensure_ascii=False)
    why, hyp, later = [], [], []
    if defense == "persistence" and not R["arcanes"]:
        defense, why_def = "bouclier", "Arcane Persistence demande des arcanes, pas encore à ce niveau"
    why.insert(0, f"défense par {'le bouclier' if defense == 'bouclier' else 'Arcane Persistence (santé et armure)'} : {why_def}")
    pers_ok, pers_why = persistence_ok(tb.rank30(frow), _kit_tags(a))
    if defense == "persistence" and not pers_ok and tb.rank30(frow)["bouclier"]:
        hyp.insert(0, f"Arcane Persistence demandée, mais peu efficace ici : {pers_why} ; le bouclier tiendrait mieux")
    w = _weights(a, defense)
    no_energy = not R["focus"] and not R["arcanes"]  # ni Zenurik ni arcanes : l'efficacité est la seule source d'autonomie
    if no_energy: w["efficiency"] = max(w["efficiency"], 1.5); w["energy"] = max(w["energy"], 0.6)

    # --- 8 mods : le noyau d'abord, puis un augment cité par l'archétype, puis les meilleurs mods de stats
    core = [tb.fiche_mod(m)["mods"][-1]["nom"] for m in (a.get("noyau") or {}).get("mods", []) if "erreur" not in tb.fiche_mod(m)]
    for m in core:
        if not ok_mod(m): later.append(f"{m} ({_how(niveaux.access(tb, m))})")
    core = [m for m in core if ok_mod(m)]
    if defense == "persistence": core = [m for m in core if m != "Rolling Guard"]  # Persistence : la frame ne craint pas le coup unique
    mods = list(core)
    why += a.get("raisons") or []
    if mods: why.append(f"augments clés : {', '.join(mods)}")
    aug_text = json.dumps(a.get("choix") or [], ensure_ascii=False)
    for n in _names_in(tb, aug_text, "mods"):
        c = tb.fiche_mod(n)
        if "erreur" in c: continue
        c = c["mods"][-1]
        if c.get("augment_de") and c["nom"] not in mods and len(mods) < 3 and ok_mod(c["nom"]):
            mods.append(c["nom"]); why.append(f"augment {c['nom']} : proposé par le robot ({c['effets_rang_max'][0][:90]})")
            break
    elements = a.get("elements")
    useless = {c["nom"] for c in _candidates(tb, base) if _archon_useless(c, elements)}
    # Archon sans son élément : même valeur que la version normale, mais passe derrière (coût, difficulté d'obtention)
    sc = lambda c: _score(c, w) * (0.9 if c["nom"] in useless else 1)
    cands = sorted([c for c in _candidates(tb, base) if ok_mod(c["nom"])
                    and not (no_energy and c.get("stats_additionnables", {}).get("efficiency", 0) < 0)], key=lambda c: -sc(c))
    if useless & {c["nom"] for c in cands[:12]}:
        hyp.append("mods Archon dont l'effet en plus ne se déclenche pas avec ce kit (" + ", ".join(sorted(useless)) +
                   ") : leur version normale passe devant")
    if no_energy: hyp.append("pas de mod qui baisse l'efficacité (Blind Rage…) : sans focus ni arcanes, la frame doit rester autonome en énergie")
    families = {_root(m) for m in mods}
    skipped = []
    for c in cands:
        if len(mods) >= 8: skipped.append(c); continue
        if _root(c["nom"]) in families or c.get("augment_de") or c["nom"] in mods: continue
        if _score(c, w) <= 0: continue
        if c.get("exilus"): continue  # les mods Exilus vont dans l'emplacement Exilus
        mods.append(c["nom"]); families.add(_root(c["nom"]))
    # set Umbra : avec Umbral Intensify, la variante santé/armure prend aussi Umbral Fiber (et Vitality)
    if defense == "persistence" and "Umbral Intensify" in mods and ok_mod("Umbral Fiber"):
        for u in ("Umbral Fiber", "Umbral Vitality"):
            if u in mods: continue
            same = [m for m in mods if _root(m) == _root(u)]
            if same: mods[mods.index(same[0])] = u
            else:
                free = [m for m in mods if m not in core and not m.startswith("Umbral") and not
                        (tb.fiche_mod(m)["mods"][-1].get("augment_de"))]
                if len(mods) < 8: mods.append(u)
                elif free: mods[mods.index(min(free, key=lambda m: _score(tb.fiche_mod(m)["mods"][-1], w)))] = u
                else: continue
            families.add(_root(u))
            why.append(f"{u} : bonus du set Umbra avec Umbral Intensify")
    chosen_cards = {m: tb.fiche_mod(m)["mods"][-1] for m in mods}
    best_left = next((c for c in cands if c["nom"] not in mods and _root(c["nom"]) not in families and _score(c, w) > 0), None)
    if best_left:
        weakest = min((m for m in mods if m not in core), key=lambda m: _score(chosen_cards[m], w), default=None)
        if weakest: why.append(f"dernier mod retenu : {weakest} ; juste derrière : {best_left['nom']} ({', '.join(best_left['effets_rang_max'])})")

    # --- Exilus : meilleur mod Exilus selon les mêmes poids
    ex = [c for c in cands if c.get("exilus") and _root(c["nom"]) not in families and _score(c, w) > 0]
    exilus = ex[0]["nom"] if ex else ""
    if ex and exilus == ex[0]["nom"]: why.append(f"Exilus {exilus}" + (f" plutôt que {ex[1]['nom']}" if len(ex) > 1 else ""))

    # --- aura
    # Brief Respite convertit l'énergie dépensée en bouclier : inutile sur une frame sans énergie (Lavos, Hildryn)
    if a.get("sans_energie"): auras = ["Corrosive Projection", "Growing Power", "Steel Charge"]
    else: auras = (["Brief Respite", "Growing Power"] if defense == "bouclier" else ["Growing Power"]) + ["Corrosive Projection", "Steel Charge"]
    aura = next((x for x in auras if ok_mod(x)), "")
    if aura == "Brief Respite": why.append("aura Brief Respite : l'énergie dépensée devient du bouclier (défense par le bouclier)")
    elif aura == "Growing Power": why.append("aura Growing Power : plus de puissance" + ("" if defense == "bouclier" else " ; Brief Respite ne sert à rien sans bouclier (Arcane Persistence)"))
    elif aura == "Corrosive Projection": why.append("aura Corrosive Projection : retire de l'armure aux ennemis pour toute l'escouade"
                                                    + (" (Brief Respite ne sert pas : cette frame ne dépense pas d'énergie)" if a.get("sans_energie") else ""))
    elif aura: why.append(f"aura {aura} : la meilleure accessible à ce niveau")

    # --- arcanes : ceux que cite l'archétype, dans l'ordre, filtrés par la variante de défense
    arcs = [n for n in (a.get("arcanes") or []) if tb.con.execute(
        "SELECT 1 FROM arcanes WHERE name=? AND type='Warframe Arcane'", (n,)).fetchone()]
    if defense == "persistence":
        arcs = ["Arcane Persistence"] + [x for x in arcs if x != "Arcane Persistence"]
    else:
        arcs = [x for x in arcs if x != "Arcane Persistence"]
    arcs = list(dict.fromkeys(x for x in arcs + ["Molt Augmented", "Arcane Energize"] if x.lower() not in banned))[:2]
    if R["arcanes"]:
        why.append(f"arcanes {arcs[0]} et {arcs[1]} : choisis selon la capacité centrale" + (" ; Persistence imposée par la défense choisie" if defense == "persistence" else ""))
    else:
        later.append(f"arcanes {arcs[0]} et {arcs[1]}"); arcs = []

    # --- Helminth : capacité citée par l'archétype, de préférence sans [à vérifier]
    known = tb.helminth_abilities()
    helm, helm_note = a.get("helminth") or "", f"remplace {a.get('helminth_remplace')}"
    for c in ([] if helm else a.get("choix") or []):
        if "helminth" not in c.get("quoi", "").lower(): continue
        opts = sorted(c.get("options") or [], key=lambda o: "[à vérifier]" in o)
        for o in opts:
            hit = [k for k in known if k.lower() in o.lower() and known[k].lower() != base.lower()]
            if hit: helm, helm_note = hit[0], c.get("quoi", ""); break
    if not helm:
        helm = next((k for k in ("Nourish", "Roar", "Pillage") if k in known), ""); hyp.append(f"Helminth {helm} : choix par défaut")
    if not R["helminth"]:
        if helm: later.append(f"Helminth {helm}")
        helm = ""

    # --- arme exaltée : mods du noyau, complétés par ceux que cite l'archétype puis une base de mêlée
    armes = {}
    exn = (a.get("noyau") or {}).get("arme_exaltee")
    own = [x for x in tb.armes_exaltees(name) if not x["griffes_garuda"]]
    if exn and own:
        target = next((x for x in own if x["nom"].lower().startswith(exn["nom"].lower())), own[0])
        ok = {m["nom"].lower(): m["nom"] for m in tb.mods_arme(target["nom"])} if "erreur" not in tb.mods_arme(target["nom"]) else {}
        allowed = lambda m: m.lower() in ok and ok_mod(ok[m.lower()])
        base_of = lambda m: m if allowed(m) else (_root(m) if allowed(_root(m)) else None)  # Primed Pressure Point -> Pressure Point
        wm = [ok[x.lower()] for x in (base_of(m) for m in exn.get("mods", [])) if x]
        extra = [x for x in (base_of(m) for m in _names_in(tb, aug_text, "mods") + (MELEE_FILL if target["emplacement"] == "melee" else [])) if x]
        fam = {_root(m) for m in wm}
        for m in extra:
            if len(wm) >= 8: break
            k = m.lower()
            if k in ok and _root(ok[k]) not in fam: wm.append(ok[k]); fam.add(_root(ok[k]))
        warc = next((n for n in _names_in(tb, aug_text, "arcanes") if tb.con.execute(
            "SELECT 1 FROM arcanes WHERE name=? AND type='Melee Arcane'", (n,)).fetchone()), "") if target["emplacement"] == "melee" and R["arcanes"] else ""
        armes["exaltees"] = [{"nom": target["nom"], "mods": wm, "arcane": warc}]
        why.append(f"{target['nom']} : {', '.join(wm[:4])}… (combo de capacité)" )

    if not R["focus"]: later.append("focus Zenurik (après la quête The Second Dream)")
    energy = [e for e in (a.get("energie") or []) if not any(k.lower() in e.lower() for k in later_keys(later))]
    hors = ["armes", "compagnon"] + ([] if R["arcanes"] else ["arcanes"]) + ([] if R["helminth"] else ["helminth"]) \
        + ([] if R["focus"] else ["focus"]) + ([] if tier == "endgame" else ["mods", "exilus"])
    b = {"warframe": name, "role": a.get("nom"), "aura": aura, "exilus": exilus, "mods": mods[:8], "arcanes": arcs,
         "helminth": helm, "helminth_remplace": a.get("helminth_remplace") if helm else "", "focus": FOCUS if R["focus"] else "", "armes": armes, "hors_build": hors, "defense": defense,
         "niveau": tier, "reacteur": R["reacteur"],
         "source_energie": "; ".join(energy[:2]) or "orbes d'énergie, efficacité" + (", Zenurik" if R["focus"] else "")}
    if tier != "endgame" and "hors_archetype" not in b and later: b["hors_archetype"] = "pièces du noyau pas encore accessibles à ce niveau"
    v = tb.valider_build(b)
    # capacité : sans formas (débutant) ou avec peu (intermédiaire), on retire les mods les moins utiles jusqu'à ce que ça rentre
    removed = []
    while R["formas"] is not None and b["mods"]:
        need = (v.get("capacite") or {}).get("formas_necessaires_au_minimum", 0) or 0
        if need <= R["formas"] and not any("ne rentre pas" in e for e in v.get("erreurs") or []): break
        drop = min([m for m in b["mods"] if m not in core] or b["mods"], key=lambda m: _score(tb.fiche_mod(m)["mods"][-1], w))
        b["mods"].remove(drop); removed.append(drop); v = tb.valider_build(b)
    if removed:
        lim = "pas de forma" if not R["formas"] else "au plus %d formas" % R["formas"]
        hyp.append(f"emplacements laissés vides faute de capacité ({lim}{', sans Orokin Reactor' if not R['reacteur'] else ''}) : "
                   f"{', '.join(removed)} à ajouter plus tard, ou ces mods à un rang plus bas")
    return {"build": b, "archetype": {"id": a.get("id"), "nom": a.get("nom"), "objectif": a.get("objectif"),
                                     "boucle_de_jeu": a.get("boucle_de_jeu"), "survie": a.get("survie"),
                                     "energie": a.get("energie"), "pieges": a.get("pieges"),
                                     "helminth_remplace": a.get("helminth_remplace"), "raisons": a.get("raisons"),
                                     "choix": a.get("choix")},
            "autres_objectifs": [regles.LABEL[k] for k in regles.LABEL if k != a.get("objectif_cle")],
            "helminth_compare": a.get("helminth_options"), "variantes": a.get("variantes"), "demande": a.get("demande"), "fiabilite": a.get("fiabilite"),
            "choix_compares": why, "hypotheses": hyp + ["armes et compagnon : laissés au choix du joueur"],
            "niveau": tier, "a_viser_ensuite": later, "defense_raison": why_def,
            "validation": {k: v.get(k) for k in ("statut", "erreurs", "manquants", "totaux", "consequences_calculees", "capacite")},
            "archetype_relu": bool(a.get("module")), "persistence_possible": pers_ok}
