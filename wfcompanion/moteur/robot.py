"""Le robot scripté : il raisonne avec les étiquettes et les règles, sans modèle de langage.

plan() décide, pour une warframe et un objectif : la capacité centrale, la boucle de jeu, ce qui couvre la survie et
l'énergie, les augments clés, le Helminth (et la capacité qu'il remplace), les arcanes et les stats à viser.
optimizer.propose() s'en sert ensuite pour choisir les mods, vérifier la capacité et valider le build.
Chaque décision garde sa raison, écrite à partir de la règle qui l'a déclenchée.
"""
import json, re

from . import etiquettes as et, regles as rg
from .. import modules


def _tags_text(text):
    """Étiquettes d'un texte court (effet d'augment, passif) avec les mêmes motifs que les pages de capacités."""
    t = " ".join(x for x in re.split(r"(?<=[.!?])\s+|\n", (text or "").lower())
                 if not re.search(r"\b(not|cannot|can't|unaffected|ignores?|except)\b", x))
    return [tag for tag, rx in et._RULES if re.search(rx, t)]


def kit(tb, f, M):
    """Capacités de la frame avec leurs étiquettes : celles du module (confirmées) ou tirées du wiki (probables)."""
    base = re.sub(r"\s+(Prime|Umbra)$", "", f["nom"])
    out = {}
    for c in f.get("capacites", []):
        name = c["nom"]
        if M and name in getattr(M, "CAPACITES", {}):
            out[name] = dict(M.CAPACITES[name]); out[name].setdefault("fiabilite", "confirmé")
            continue
        e = et.extract(et.ability_page(tb.base or "", base, name))
        if not e:  # pas de page : la description du jeu suffit pour un premier jet
            e = {"apporte": _tags_text(c.get("description")), "profite_de": ["puissance", "duree", "portee"], "fiabilite": "à vérifier",
                 "stats_cles": et.stats_cles("", (c.get("description") or "").lower()),
                 "canalisee": bool(re.search(r"\bchannel", c.get("description") or "", re.I))}
        from ..modules import helminth as H
        if name in H.CAPACITES:  # capacité relue côté Helminth : c'est la même, ses étiquettes valent aussi dans le kit
            e = dict(e, apporte=list(dict.fromkeys(H.CAPACITES[name]["apporte"] + [t for t in e["apporte"] if t != "degats"])))
        if M and name in getattr(M, "AJOUTS", {}):
            e = dict(e, apporte=list(dict.fromkeys(e["apporte"] + M.AJOUTS[name])))
        out[name] = e
    return out


def _augments(tb, base, M):
    out = {}
    exw = [x["nom"].split()[0].lower() for x in (tb.armes_exaltees(base) or []) if not x.get("griffes_garuda")]
    for r in tb.con.execute("SELECT name, data FROM mods WHERE compat = ? COLLATE NOCASE AND variant = ''", (base,)):
        card = tb._mod_card(json.loads(r["data"]))
        txt = " ".join(card["effets_rang_max"])
        if M and r["name"] in getattr(M, "AUGMENTS", {}):
            out[r["name"]] = dict(M.AUGMENTS[r["name"]]); continue
        m = re.match(r"\s*(.+?) Augment:", txt)
        tags = _tags_text(txt)
        if any(re.search(r"\b" + re.escape(w) + r"\b", txt.lower()) for w in exw) and "bonus_armes" not in tags:
            tags.append("bonus_armes")  # l'augment change l'arme exaltée (nouveau tir, dégâts) : il sert l'arme
        out[r["name"]] = {"pour": m.group(1) if m and m.group(1) != "Passive" else None, "apporte": tags,
                          "texte": txt[:200], "fiabilite": "probable"}
    return out


def helminth_tags(tb, hab, hframe):
    """Étiquettes d'une capacité du Helminth : relues (modules/helminth.py) ou lues dans le résumé de sa page."""
    from ..modules import helminth as H
    if hab in H.CAPACITES: return {**H.CAPACITES[hab], "fiabilite": "confirmé"}
    e = et.extract(et.ability_page(tb.base or "", hframe, hab))
    if not e: return None
    return {"apporte": _tags_text(e["resume"]), "profite_de": e["profite_de"], "fiabilite": "probable", "note": e["resume"]}


def _central(kit_, obj, M):
    if M and getattr(M, "CENTRALE", {}).get(obj) in kit_: return M.CENTRALE[obj], "capacité centrale choisie par le module de la frame"
    want = rg.CENTRALE[obj]
    def score(name):
        t = kit_[name]["apporte"]
        s = sum((len(want) - i) * 2 for i, w in enumerate(want) if w in t)
        if obj in ("degats", "boss") and "puissance" in kit_[name].get("profite_de", []): s += 1
        if obj == "degats" and "zone" in t: s += 1
        if obj == "boss" and "vulnerabilite" in t: s += 1
        return s
    best = max(kit_, key=score)
    return best, f"c'est la capacité qui apporte le plus ce que demande l'objectif ({', '.join(rg.APPORTS_LABEL(want))})"


# --- arcanes qui peuvent entrer dans une variante (le choix final se fait en comparant des builds entiers)
ARC_CANDIDATS = ["Molt Augmented", "Arcane Fury", "Arcane Energize", "Arcane Sculptor", "Arcane Battery", "Arcane Aegis", "Molt Efficiency",
                 "Arcane Expertise", "Arcane Bellicose", "Arcane Hot Shot", "Arcane Avenger"]
EQUI = "Equilibrium"


def _names(lst):
    return {str(x).strip().lower() for x in (lst or []) if str(x).strip()}


def plan(tb, warframe, message="", niveau="endgame", demande=None):
    """demande (facultatif, rempli par l'agent) : {objectif, capacite_centrale, armes, imposes[], interdits[], variante}.
    Le robot compare des builds entiers (Helminth x capacité remplacée x arcanes x source d'énergie) et renvoie le meilleur,
    avec les variantes suivantes pour comparer."""
    d = demande or {}
    f = tb.fiche_warframe(warframe)
    if "erreur" in f: return f
    name = f["nom"]; base = re.sub(r"\s+(Prime|Umbra)$", "", name)
    M = modules.warframe(base)
    obj = d.get("objectif") if d.get("objectif") in rg.LABEL else rg.objectif_of(message)
    weapons = bool(d["armes"]) if "armes" in d else rg.armes_centrales(tb, message, name)
    if weapons and obj == "degats": obj = "armes"  # « build Mirage pour mon Kuva Bramma » : la frame sert les armes
    if obj == "eidolon": weapons = True  # on tue les Eidolons avec les armes (Rubico…), la frame les renforce
    imposes, interdits = _names(d.get("imposes")), _names(d.get("interdits"))
    k = kit(tb, f, M)
    if not k: return {"erreur": f"capacités de {name} introuvables"}
    asked = next((n for n in k if n.lower() == str(d.get("capacite_centrale") or "").strip().lower()), None)
    if asked: central, why_central = asked, "demandée par le joueur"
    # boss avec une arme : la capacité centrale doit servir l'arme (Sonar plutôt que Sound Quake)
    else: central, why_central = _central(k, "armes" if weapons and obj == "boss" else obj, M)
    ctags = set(k[central]["apporte"]) | set(k[central].get("profite_de", []))
    if (M and getattr(M, "ARME_EXALTEE", {}).get(central)) or any(
            x["nom"].lower().startswith(central.lower().split()[0]) and not x["griffes_garuda"] for x in tb.armes_exaltees(f["nom"])):
        ctags.add("arme")  # la capacité centrale donne une arme exaltée : les bonus d'armes la servent
    if weapons: ctags.add("arme")  # build centré sur les armes du loadout : idem
    # capacité qui donne une arme exaltée (Balefire, Shattered Lash…) : le joueur la joue, on la garde et ses bonus d'armes comptent
    exalted_abil = {n for n in k for x in tb.armes_exaltees(f["nom"])
                    if not x["griffes_garuda"] and x["nom"].lower().split()[0] == n.lower().split()[0]}
    if exalted_abil and obj in ("degats", "tank", "armes", "boss"): ctags.add("arme")
    raisons = [f"objectif : {rg.LABEL[obj]}" + (" ; build centré sur les armes du loadout" if weapons else ""),
               f"capacité centrale {central} : {why_central}"]
    prof_c = set(k[central].get("profite_de", []))
    canal = bool(k[central].get("canalisee")) or central in tb.channeled()
    r30 = f.get("rang_30_sans_mod") or {}
    # frame sans énergie (Lavos : temps de recharge ; Hildryn : capacités payées en bouclier) : pas d'exigence d'énergie
    no_energy_frame = (r30.get("energie") is not None and r30.get("energie") == 0)
    shield_frame = no_energy_frame and (r30.get("bouclier") or 0) >= 1000
    melee = "melee" in prof_c or any(x["nom"].lower().startswith(central.lower().split()[0]) and x["emplacement"] == "melee"
                                     and not x["griffes_garuda"] for x in tb.armes_exaltees(name))

    # --- passif et augments
    passif = (dict(M.PASSIF) if M and getattr(M, "PASSIF", None) else
              {"apporte": _tags_text(str(f.get("passif") or "")), "texte": str(f.get("passif") or "")[:200], "fiabilite": "probable"})
    augs = _augments(tb, base, M)
    key_augs = [n for n, a in augs.items() if (a.get("pour") == central and a.get("cle")) or n.lower() in imposes]
    key_augs += [n for n, a in augs.items() if a.get("pour") == central and n not in key_augs and n.lower() not in interdits
                 and rg.synergy(a["apporte"], ctags, central)[0] > 0][:max(0, 2 - len(key_augs))]
    key_augs = [n for n in key_augs if n.lower() not in interdits or n.lower() in imposes]
    for n in key_augs: raisons.append(f"augment {n} : renforce {central}" + (f" ({augs[n]['texte']})" if augs[n].get("texte") else ""))
    energy_aug = any("energie" in augs[n]["apporte"] for n in key_augs)

    def coverage(without=None):
        tags = set(passif["apporte"])
        for n, a in k.items():
            if n != without: tags |= set(a["apporte"])
        for n in key_augs: tags |= set(augs[n]["apporte"])
        return tags
    needs = [x for x in rg.BESOINS_OBJECTIF[obj] if not (x == "energie" and no_energy_frame)]
    if no_energy_frame: raisons.append("pas d'énergie sur cette frame : " + ("ses capacités se paient en bouclier" if shield_frame
                                                                              else "ses capacités marchent sur des temps de recharge"))

    # --- candidats : capacités remplaçables, capacités du Helminth, arcanes
    keep = set(getattr(M, "NE_PAS_REMPLACER", {}).get(central, [])) if M else set()
    keep |= {n for n in k if n.lower() in imposes}
    if obj in ("degats", "tank", "armes", "boss"): keep |= exalted_abil
    replaceable = [n for n in k if n != central and n not in keep] or [n for n in k if n != central]
    pool = {h: fr for h, fr in tb.helminth_abilities().items() if fr.lower() != base.lower() and h not in k and h.lower() not in interdits}
    forced_h = [h for h in pool if h.lower() in imposes]
    if forced_h: pool = {h: pool[h] for h in forced_h}
    htags = {h: e for h, fr in pool.items() if (e := helminth_tags(tb, h, fr))}
    arc_ok = [a for a in ARC_CANDIDATS if a.lower() not in interdits]
    forced_a = [r["name"] for r in tb.con.execute("SELECT name FROM arcanes WHERE type = 'Warframe Arcane'") if r["name"].lower() in imposes]
    equi_ok = EQUI.lower() not in interdits

    def arc_value(a, tags, objets):
        """Valeur d'un arcane hors énergie (l'énergie est comptée à part, une seule fois)."""
        if a == "Molt Augmented": return (1.0 if "puissance" in prof_c else 0.2) + (0.6 if obj in ("degats", "boss", "armes") else 0)
        if a == "Arcane Expertise": return 1.6 if shield_frame else -5
        if a == "Arcane Bellicose": return 1.3 if (r30.get("sante") or 0) >= 600 and "puissance" in prof_c and obj != "eidolon" else 0
        if a == "Arcane Hot Shot": return 1.4 if "feu" in tags and "arme" in ctags and obj != "eidolon" else -5
        if a == "Arcane Avenger": return 1.4 if obj == "eidolon" else (0.3 if "arme" in ctags else 0)
        if a == "Arcane Fury": return 1.6 if melee else 0
        if a == "Arcane Battery": return 0.8 if "armure_bonus" in tags else 0
        if a == "Arcane Aegis": return 1.4 if obj == "eidolon" else (0.6 if obj == "tank" or shield_frame else 0.1)
        if a == "Molt Efficiency": return (0.6 if "duree" in prof_c else 0.2) if not no_energy_frame else 0
        if a == "Arcane Sculptor":  # sans objet créé, il ne se déclenche jamais ; sinon vaut ce que vaut l'efficacité au build
            return (0.3 + (0.8 if canal else 0.4 if (k[central].get("cout") or 50) >= 75 else 0)) if objets else -5
        if a == "Arcane Energize": return 0.0 if not no_energy_frame else -5  # vaut par l'énergie qu'il rend (comptée à part)
        return 0

    def energy(tags, h, e, arcs, objets, use_equi, equi_alone=False):
        """Sources d'énergie de la variante, qui s'additionnent (rendements décroissants) : (facteur 0..1, [phrases]).
        Zenurik et l'efficacité sont toujours là mais comptent peu (règle de XeniX13 : source secondaire)."""
        if no_energy_frame: return 1.0, ["pas besoin d'énergie sur cette frame"]
        src = [(0.3, "Zenurik (focus) et efficacité")]
        if energy_aug: src.append((1.0, "augment : " + ", ".join(n for n in key_augs if "energie" in augs[n]["apporte"])))
        if "energie" in (tags - set(e["apporte"] if e else [])): src.append((0.9, "le kit rend lui-même de l'énergie"))
        if e and "energie" in e["apporte"]: src.append((0.6, f"{h} (Helminth) rend de l'énergie"))
        if use_equi: src.append((0.7 * (0.8 if canal else 1.0), f"{h} + {EQUI} : les orbes de santé donnent de l'énergie, que {h} multiplie"))
        if equi_alone: src.append((0.5 * (0.8 if canal else 1.0), f"{EQUI} : les orbes de santé donnent de l'énergie"))
        if "Molt Efficiency" in arcs: src.append((0.35, "Molt Efficiency : efficacité qui monte avec les kills"))
        if "Arcane Energize" in arcs: src.append((0.65 * (0.8 if canal else 1.0), "Arcane Energize : rend de l'énergie en ramassant des orbes"))
        if "Arcane Sculptor" in arcs and objets:
            src.append(((0.65 if canal else 0.5), f"Arcane Sculptor : lancer {objets[0]} donne 175 % d'efficacité pendant 12 s"))
        left_ = 1.0
        for f_, _ in src: left_ *= (1 - f_)
        return round(1 - left_, 3), [p for _, p in sorted(src[1:], key=lambda x: -x[0])] + [src[0][1]]

    # augments des capacités du Helminth (ex. Smite Infusion) : ils comptent dans la valeur du Helminth
    haug = {}
    for h, fr in pool.items():
        best_v = 0
        for n, a in _augments(tb, re.sub(r"\s+(Prime|Umbra)$", "", fr.split(" & ")[0]), None).items():
            if (a.get("pour") or "").lower() == h.lower(): best_v = max(best_v, rg.synergy(a["apporte"], ctags, central)[0])
        haug[h] = best_v
        if obj == "eidolon" and any((a.get("pour") or "").lower() == h.lower() and "radiation" in a["apporte"]
                                    for a in _augments(tb, re.sub(r"\s+(Prime|Umbra)$", "", fr.split(" & ")[0]), None).values()):
            haug[h] += 1.5  # Eidolons : la Radiation dans les armes compte beaucoup
    # capacité seule à apporter une protection du kit : la remplacer retire une couche de survie
    def unique_survival(n):
        mine = set(k[n]["apporte"]) & set(rg.SURVIE)
        others = set().union(*[set(a["apporte"]) for m, a in k.items() if m != n]) | set(passif["apporte"])
        return bool(mine - others)
    variants = []
    for rep in replaceable + [None]:  # None : pas de Helminth, le kit reste entier
        left = coverage(without=rep)
        loss = rg.synergy(k[rep]["apporte"], ctags, central)[0] * rg.FIABILITE.get(k[rep].get("fiabilite"), 0.8) if rep else 0
        if rep and k[rep].get("fiabilite") == "à vérifier": loss = max(loss, 1.0)  # on ne sacrifie pas une capacité mal connue
        if rep and k[rep].get("stats_cles"): loss += 1.5  # une capacité qui monte fort avec une stat porte souvent le kit
        # capacité qui fait le rôle : l'énergie de toute l'escouade, ou ce que le soutien apporte aux alliés
        if rep and {"energie", "soutien"} <= set(k[rep]["apporte"]): loss += 1.5
        elif rep and obj == "soutien" and "soutien" in k[rep]["apporte"]: loss += 0.6
        if rep and unique_survival(rep): loss += 0.8
        # frame à Persistence probable (armure de base >= 500) : le soin du kit est ce qui la fait tenir
        if rep and (r30.get("armure") or 0) >= 500 and "soin" in k[rep]["apporte"] and obj != "eidolon": loss += 2.0
        obj_kit = [n for n, a in k.items() if n != rep and "cree_objet" in a["apporte"]]
        kept_now = [n for n in k if n != rep]
        for h, e in ((list(htags.items()) or [(None, None)]) if rep else [(None, None)]):
            if h and any(rg.exclusif(h, n) for n in kept_now): continue  # ne coexiste pas avec une capacité gardée du kit
            hs, hwhy = rg.synergy(e["apporte"], ctags | ({"efficacite_arcane"} if not obj_kit else set()), central) if e else (0, [])
            if e and obj == "tank" and "bonus_puissance" in e["apporte"]: hs -= 0.75  # buff temporaire : peu utile pour tenir
            if e and "puissance" in e.get("profite_de", []) and "puissance" in prof_c: hs += 0.4
            if e and haug.get(h): hs += 0.8 * haug[h]; hwhy = hwhy + ["son augment se met aussi dans le build"]
            if e and canal and "energie" in e["apporte"]:  # capacité centrale canalisée : il faut une source d'énergie continue
                hs += 1.2; hwhy = hwhy + [f"{central} est canalisée : il faut une vraie source d'énergie continue"]
            if e and obj == "eidolon" and "radiation" in e["apporte"]: hs += 1.0; hwhy = hwhy + ["Radiation : efficace contre les Eidolons"]
            hs *= rg.FIABILITE_HELMINTH.get(e["fiabilite"], 0.6) if e else 1
            tags = left | (set(e["apporte"]) if e else set())
            objets = obj_kit + ([h] if e and "cree_objet" in e["apporte"] else [])
            use_equi = bool(e and "energie_x" in e["apporte"] and equi_ok and not rg.covered(left, "energie") and not energy_aug
                            and not no_energy_frame)
            pairs = [p for p in __import__("itertools").combinations(dict.fromkeys(forced_a + arc_ok), 2)
                     if all(x in p for x in forced_a[:2])]
            alone_opts = [False] + ([True] if equi_ok and not use_equi and not no_energy_frame and not energy_aug else [])
            for arcs, equi_alone in ((a_, q_) for a_ in pairs for q_ in alone_opts):
                ef, esrc = energy(tags, h, e, arcs, objets, use_equi, equi_alone)
                sc = hs - loss + sum(arc_value(a, tags, objets) for a in arcs)
                ex = {}
                for x in needs:
                    if x == "energie": sc += ef * rg.BESOINS[x][1]; ex[x] = ef >= 0.75
                    elif x == "passer_armure" and not rg.covered(tags, x) and "retrait_armure_partiel" in tags:
                        ex[x] = True; sc += 0.6 * rg.BESOINS[x][1]  # statut Feu : -50 % seulement
                    else:
                        ok = rg.covered(tags, x); ex[x] = ok; sc += rg.BESOINS[x][1] if ok else 0
                # exigence non remplie (les quatre règles de base) : pénalité nette, pour qu'un build complet passe devant
                sc -= 1.5 * sum(1 for ok in ex.values() if not ok)
                layers = len(set(tags) & set(rg.SURVIE))
                sc += min(max(layers - 1, 0), 3) * (0.5 if obj == "tank" else 0.15)
                if use_equi: sc += 0.5 - 0.3  # règle de XeniX13 : Nourish + Equilibrium est la source habituelle ; coûte un emplacement
                if equi_alone: sc -= 0.3  # coûte un emplacement de mod
                variants.append({"score": round(sc, 2), "energie_facteur": ef, "helminth": h or "", "helminth_de": pool.get(h, ""), "remplace": rep or "",
                                 "arcanes": list(arcs), "mods_en_plus": [EQUI] if use_equi or equi_alone else [], "energie": " + ".join(esrc[:-1]) or esrc[-1], "energie_sources": esrc,
                                 "exigences": ex, "objets": objets, "pourquoi_helminth": list(dict.fromkeys(hwhy))[:3],
                                 "couches_de_survie": layers, "tags": tags})
    variants.sort(key=lambda v: -v["score"])
    # 3 variantes vraiment différentes : une par Helminth
    top, seen = [], set()
    for v in variants:
        if v["helminth"] in seen: continue
        seen.add(v["helminth"]); top.append(v)
        if len(top) == 3: break
    if not top: return {"erreur": "aucune variante possible avec ces contraintes"}
    lab = {"survie": "survie", "energie": "énergie", "passer_armure": "passer l'armure"}
    if forced_h: top = [v for v in top if v["helminth"]] or top
    for v in top:
        v["faiblesses"] = [rg.BESOINS[x][2] for x, ok in v["exigences"].items() if not ok]
        v["resume"] = ((f"{v['helminth']} à la place de {v['remplace']}" if v["helminth"] else "pas de Helminth : le kit sert déjà le build")
                       + f" ; arcanes {' + '.join(v['arcanes'])}"
                       + (f" ; {', '.join(v['mods_en_plus'])}" if v["mods_en_plus"] else "") + f" ; énergie : {v['energie']}")
    pick = min(max(int(d.get("variante") or 0), 0), len(top) - 1)
    best = top[pick]
    helm, replace, arcs, extra_mods = best["helminth"], best["remplace"], best["arcanes"], best["mods_en_plus"]
    have_final, objets = set(best["tags"]), best["objets"]
    left = coverage(without=replace or None)
    if not helm: raisons.append("pas de Helminth : aucune capacité transférable ne vaut ce qu'elle ferait perdre au kit")
    if helm:
        raisons.append(f"Helminth {helm} (de {best['helminth_de']}) à la place de {replace} : " + "; ".join(best["pourquoi_helminth"] or ["meilleur build complet"]))
        raisons.append(f"{replace} remplacée : c'est la capacité qui sert le moins la boucle de {central}")
    if extra_mods: raisons.append(f"{EQUI} : avec {helm}, les orbes de santé deviennent de l'énergie multipliée" if helm and "energie_x" in htags[helm]["apporte"]
                                  else f"{EQUI} : les orbes de santé deviennent de l'énergie")
    if "Arcane Sculptor" in arcs: raisons.append(f"Arcane Sculptor : {', '.join(objets)} crée un objet, donc l'efficacité monte à 175 %")
    raisons.append("arcanes " + " et ".join(f"{a} ({rg.ARCANES[a]['phrase']})" for a in arcs if a in rg.ARCANES))
    if len(top) > 1: raisons.append("comparé à : " + " | ".join(f"{v['resume']} (score {v['score']})" for v in top if v is not best))

    # --- stats visées : ce qui fait monter la capacité centrale et ses partenaires
    partners = [n for n in k if n != central and n != (replace or None) and rg.synergy(k[n]["apporte"], ctags, central)[0] > 0]
    prof = set(prof_c)
    for n in partners: prof |= {p for p in k[n].get("profite_de", []) if p in ("duree", "portee")}
    # efficacité : une source d'énergie moins importante que les autres (règle de XeniX13). Elle ne monte que si le joueur
    # veut relancer sans arrêt (spam), le demande, ou si les vraies sources d'énergie du build ne suffisent pas.
    ef = best.get("energie_facteur", 0.4)
    prio, low = set(d.get("stats_prioritaires") or []), set(d.get("stats_basses") or [])
    if no_energy_frame and not shield_frame: eff = "peu importante"
    elif d.get("spam") or "efficacite" in prio: eff = "haute"
    elif energy_aug or "Arcane Sculptor" in arcs: eff = "peu importante"
    elif ef >= 0.88: eff = "moyenne" if canal else "basse"
    elif ef >= 0.75: eff = "moyenne"
    else: eff = "haute"
    kept = [n for n in k if n != replace]
    dur_any = "duree" in prof or any("duree" in k[n].get("profite_de", []) for n in kept)
    stats = {"puissance": "haute" if "puissance" in prof else "basse",
             "duree": ("haute" if obj == "tank" else "moyenne") if dur_any else "basse",
             "portee": "moyenne" if "portee" in prof else "basse", "efficacite": eff}
    # portée : essentielle quand la capacité centrale agit en zone, ou quand presque tout le kit gardé en dépend
    kept = [n for n in k if n != replace]
    if "portee" in prof_c and ("zone" in k[central]["apporte"] or sum("portee" in k[n].get("profite_de", []) for n in kept) >= 3):
        stats["portee"] = "haute"
    # builds offensifs ou tank à zone : la portée est souvent poussée (235 à 280 % sur les builds du joueur)
    if obj in ("degats", "armes", "tank", "farm") and any("portee" in k[n].get("profite_de", []) and "zone" in k[n]["apporte"] for n in kept):
        stats["portee"] = "haute" if stats["portee"] != "maximum" else "maximum"
    if obj == "soutien" and stats["portee"] == "haute": stats["portee"] = "moyenne"  # soutien : peu de portée suffit
    # augments au-delà de la capacité centrale (retrait d'armure, bonus pour les armes, critique…) et augment du Helminth
    pool_aug = {n: a for n, a in augs.items() if n not in key_augs and (a.get("pour") in kept or a.get("pour") is None)}
    if helm:
        for n, a in _augments(tb, re.sub(r"\s+(Prime|Umbra)$", "", best["helminth_de"].split(" & ")[0]), None).items():
            if (a.get("pour") or "").lower() == helm.lower(): pool_aug[n] = dict(a, helminth=True)
    extra_augs = []
    for n, a in sorted(pool_aug.items(), key=lambda x: -rg.synergy(x[1]["apporte"], ctags, central)[0]):
        if n.lower() in interdits or len(key_augs) + len(extra_augs) >= 3: continue
        v, why_a = rg.synergy(a["apporte"], ctags, central)
        if v >= 1.2:
            extra_augs.append(n)
            raisons.append(f"augment {n}" + (" (capacité du Helminth)" if a.get("helminth") else "") + f" : {why_a[0]}")
    # stat clé d'une capacité gardée (ex. la portée augmente le nombre d'armes) : au maximum
    for n in kept:
        for st in k[n].get("stats_cles") or []:
            if st not in low and stats.get(st) != "maximum":
                stats[st] = "maximum"
                raisons.append(f"{st} au maximum : sur {n}, elle augmente ce que la capacité rapporte, pas seulement sa zone ou sa durée")
    for st in prio: stats[st] = "haute" if stats.get(st) != "maximum" else "maximum"
    for st in d.get("stats_max") or []:
        if st in stats and stats[st] != "maximum":
            stats[st] = "maximum"; raisons.append(f"{st} au maximum : le joueur explique qu'elle augmente ce que rapporte le kit")
    for st in low: stats[st] = "peu importante"
    if obj == "eidolon" and "portee" not in prio:  # chasse aux Eidolons : la portée ne sert pas, durée et puissance hautes
        stats.update(portee="peu importante", duree="haute", puissance="haute")
    if prio or low or d.get("spam"):
        raisons.append("stats : " + ", ".join(f"{k} {v}" for k, v in stats.items())
                       + (" (le joueur veut relancer ses capacités sans arrêt)" if d.get("spam") else " (selon la demande du joueur)"))
    elif eff in ("basse", "peu importante"):
        raisons.append("efficacité peu poussée : le build a déjà une vraie source d'énergie, les emplacements servent mieux ailleurs")
    if shield_frame: stats["bouclier"] = "haute"  # le bouclier est à la fois la survie et l'« énergie » de la frame
    if obj == "tank" and "sante" in prof: stats["sante"] = "haute"
    if obj == "tank" and "armure" in prof: stats["armure"] = "moyenne"

    # --- arme exaltée donnée par la capacité centrale
    exalted = None
    if M and getattr(M, "ARME_EXALTEE", {}).get(central): exalted = M.ARME_EXALTEE[central]
    else:
        own = [x for x in tb.armes_exaltees(name) if not x["griffes_garuda"] and x["nom"].lower().startswith(central.lower().split()[0])]
        if own and own[0]["emplacement"] == "melee":
            exalted = {"nom": own[0]["nom"], "mods": ["Blood Rush", "Weeping Wounds", "Primed Pressure Point", "Organ Shatter"]}

    # --- boucle de jeu, survie, énergie : écrites à partir des règles
    if M and getattr(M, "BOUCLES", {}).get(central): loop = list(M.BOUCLES[central])
    else:
        loop = [f"{n} : {rg.synergy(k[n]['apporte'], ctags, central)[1][0]}." for n in partners[:2]]
        if helm and best["pourquoi_helminth"]: loop.append(f"{helm} (Helminth) : {best['pourquoi_helminth'][0]}.")
        fr = {"puissance": "la puissance", "duree": "la durée", "portee": "la portée", "sante": "la santé", "armure": "l'armure",
              "combo": "le combo", "melee": "les mods de mêlée"}
        loop.append(f"{central} : capacité principale, qui profite de " + ", ".join(fr.get(p, p) for p in sorted(prof)) + ".")
    surv = [f"{n} : {', '.join(rg.APPORTS_LABEL([t for t in a['apporte'] if t in rg.SURVIE]))}"
            for n, a in k.items() if n != replace and set(a["apporte"]) & set(rg.SURVIE)]
    if helm and set(htags[helm]["apporte"]) & set(rg.SURVIE):
        surv.append(f"{helm} (Helminth) : {', '.join(rg.APPORTS_LABEL([t for t in htags[helm]['apporte'] if t in rg.SURVIE]))}")
    ps = [t for t in passif["apporte"] if t in rg.SURVIE]
    if ps: surv.append("passif : " + (passif["texte"] if M and getattr(M, "PASSIF", None) else ", ".join(rg.APPORTS_LABEL(ps))))
    energie = [f"{n} : {augs[n].get('texte', '')}" for n in key_augs if "energie" in augs[n]["apporte"]]
    for src in best["energie_sources"]:
        if not src.startswith("augment") and src not in energie: energie.append(src)
    pieges = list(getattr(M, "PIEGES", []) if M else []) + [f"à surveiller : {m}" for m in best["faiblesses"]]
    choix = [{"quoi": f"Helminth (remplace {replace})", "options": [v["helminth"] for v in top if v["helminth"]]}]
    if objets and "Arcane Sculptor" not in arcs:
        choix.append({"quoi": "arcane d'efficacité", "options": [f"Arcane Sculptor ({', '.join(objets)} crée un objet)"]})

    # éléments infligés par le kit gardé et le Helminth : les mods Archon n'apportent leur effet en plus qu'avec cet élément
    txt = " ".join(c.get("description") or "" for c in f.get("capacites", []) if c["nom"] != replace)
    txt += " " + " ".join(et.ability_page(tb.base or "", base, n)[:3000] for n in kept)
    if helm: txt += " " + str(htags[helm].get("note") or "") + " " + et.ability_page(tb.base or "", best["helminth_de"], helm)[:3000]
    elements = sorted({e for e, rx in {"toxin": r"toxin", "electricity": r"electric", "cold": r"\bcold|freez", "heat": r"\bheat|fire\b|burn"}.items()
                       if re.search(rx, txt, re.I)})
    # Exilus : une frame qui n'a pas de survie « dure » (seulement de l'esquive, du contrôle…) ou peu de santé prend
    # une fenêtre d'invulnérabilité en plus : elle n'esquivera pas tout
    hard = set(rg.SURVIE_DURE) & (set(have_final) | set(passif["apporte"]))
    # règle de XeniX13 : Rolling Guard seulement si la frame peut se faire tuer d'un coup (pas de vraie protection,
    # pas de gros bouclier ni de grosse santé) ; elle sert aussi à se débarrasser d'un statut dangereux (Feu, Poison)
    if (r30.get("bouclier") or 0) >= 1000: hard.add("gros bouclier")
    if (r30.get("sante") or 0) >= 1000: hard.add("grosse santé")
    survie_mod = None
    if not hard and obj != "eidolon":
        survie_mod = "Rolling Guard"
        raisons.append("Rolling Guard : pas de vraie protection dans le kit, risque d'être tué d'un coup ; une roulade donne 3 s "
                       "d'invulnérabilité et retire les statuts (Feu, Poison)")
        if "Rolling Guard".lower() in interdits: survie_mod = None
        else: surv.append("Rolling Guard : 3 s d'invulnérabilité après une roulade (7 s de recharge)")
    rel = "confirmé" if all(a.get("fiabilite") == "confirmé" for a in k.values()) else "probable"
    public = [{x: v[x] for x in ("score", "helminth", "helminth_de", "remplace", "arcanes", "mods_en_plus", "energie",
                                 "exigences", "faiblesses", "resume")} for v in top]
    return {"id": f"{central.lower().replace(' ', '-')}-{obj}", "nom": f"{central}, {rg.LABEL[obj]}",
            "objectif": f"{rg.LABEL[obj]} ; capacité centrale {central}", "capacite_centrale": central,
            "boucle_de_jeu": loop, "survie": surv or ["à trouver : aucune capacité de survie repérée"], "energie": energie,
            "noyau": {"mods": key_augs + extra_augs + extra_mods + ([survie_mod] if survie_mod else []) + [m for m in d.get("imposes") or [] if tb.con.execute(
                          "SELECT 1 FROM mods WHERE name = ? COLLATE NOCASE", (m,)).fetchone() and m not in key_augs + extra_mods],
                      **({"arme_exaltee": exalted} if exalted else {})},
            "interdits": sorted(interdits), "choix": choix,
            "helminth": helm, "helminth_remplace": replace, "helminth_options": [(v["helminth"], v["score"]) for v in top],
            "variantes": public, "variante_choisie": pick, "demande": {"objectif": obj, "capacite_centrale": central, "armes": weapons,
                **{x: d[x] for x in ("imposes", "interdits", "contenu", "stats_max", "stats_prioritaires", "stats_basses", "spam") if x in d}},
            "arcanes": arcs, "stats_cibles": stats, "elements": elements, "sans_energie": no_energy_frame,
            "rolling_guard": bool(survie_mod),
            "tags_build": sorted(set(have_final) | set(passif["apporte"])), "pieges": pieges, "raisons": raisons,
            "defense_joueur": getattr(M, "DEFENSE", None) if M else None, "module": bool(M), "fiabilite": rel,
            "objectif_cle": obj, "kit": {n: {"apporte": a["apporte"], "fiabilite": a.get("fiabilite")} for n, a in k.items()}}
