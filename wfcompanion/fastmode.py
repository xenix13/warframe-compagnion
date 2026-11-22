"""Mode rapide : le code comprend la demande de build, le générateur construit, le modèle se contente d'expliquer.

Un petit modèle (3-4B) ne sait pas construire un build fiable, mais il sait reformuler une information juste. Ici :
1. la demande est reconnue par le code (warframe citée, mots de build, variante de défense) : aucun appel au modèle ;
2. optimizer.propose() construit et valide le build ;
3. un seul appel au modèle, sans outils, rédige l'explication ; s'il échoue, un texte écrit par le code la remplace.
Tout le reste (questions, farm, avis sur un build) passe par l'agent classique.
"""
import json, re

from . import niveaux, optimizer, pilote

BUILD_WORDS = re.compile(r"\b(d[ée]butant|palier|interm[ée]diaire|build|builds|propose|proposer|monte|monter|config|loadout|level ?cap|steel path|"
                         r"nuke|tank|dps|soutien|support|variante|persistence|bouclier)\b", re.I)
QUESTION_ONLY = re.compile(r"^\s*(pourquoi|comment|c'est quoi|qu'est-ce|explique|où|ou est|combien)\b", re.I)

EXPLAIN = ("Tu es le compagnon Warframe du joueur. Le programme a calculé et vérifié un build ; tu l'expliques, tu ne le "
           "modifies pas. Écris en français, court et concret, avec exactement ces titres : **Boucle de jeu**, **Survie**, "
           "**Énergie**, **À tester en jeu**. 2 à 4 puces par titre. Ne compare pas avec d'autres builds. Ne parle d'Arcane Persistence que si « persistence_possible » est vrai (sinon la frame n'a pas l'armure, ou la santé et l'immunité aux statuts, pour la jouer). Si « a_viser_ensuite » n'est pas vide, ajoute **À viser ensuite** : ce que le joueur pourra ajouter en progressant et pourquoi. Utilise seulement les noms et les chiffres fournis. "
           "Ne parle pas du programme, des outils, de validation ni de règles. Ne recopie pas le tableau du build.")


def wants_build(message, has_topic, tb=None):
    if QUESTION_ONLY.search(message) and not re.search(r"\bbuild\b", message, re.I): return False
    if re.search(r"\b(remplace|enl[eè]ve|retire|ajoute|mets|change|modifie|à la place|au lieu)\b", message, re.I):
        return False  # retouche du build affiché : l'agent s'en charge avec ses outils
    return bool(BUILD_WORDS.search(message)) and has_topic


def defense_of(message, previous=None):
    t = message.lower()
    if "persistence" in t or "persistance" in t: return "persistence"
    if "bouclier" in t or "shield" in t or "brief respite" in t: return "bouclier"
    return previous  # rien dit : le programme choisit (optimizer.choose_defense)


def frame_name(tb, base, message, previous=None):
    """Nom exact : la version Prime si le joueur dit « prime » (ou l'avait dit), sinon la version de base."""
    prime = bool(re.search(r"\bprime\b", message, re.I)) or bool(previous and previous.endswith("Prime"))
    for n in ([base + " Prime"] if prime else []) + [base]:
        if tb.con.execute("SELECT 1 FROM warframes WHERE name = ? COLLATE NOCASE", (n,)).fetchone(): return n
    return base


def table(b, r):
    rows = [("Aura", b["aura"]), ("Exilus", b["exilus"])] + [(f"Mod {i}", m) for i, m in enumerate(b["mods"], 1)]
    rows += [(f"Arcane {i}", x) for i, x in enumerate(b["arcanes"], 1)]
    rows += [("Helminth", b["helminth"]), ("Focus", b["focus"])]
    for e in (b.get("armes") or {}).get("exaltees", []):
        rows.append((e["nom"], ", ".join(e["mods"]) + (f" ; arcane {e['arcane']}" if e.get("arcane") else "")))
    t = "| Emplacement | Choix |\n|---|---|\n" + "\n".join(f"| {a} | {c} |" for a, c in rows if c)
    tot = (r["validation"] or {}).get("totaux") or {}
    if tot: t += "\n\n" + " · ".join(f"{k} **{v}**" for k, v in tot.items() if "Coût" not in k)
    return t


def _tidy(t):
    """Retire les mentions de provenance (« (XeniX13, 21/11/2026) », « VARIANTE BOUCLIER : ») pour l'affichage."""
    t = re.sub(r"\s*\((?:jeu de |avis de )?XeniX13[^)]*\)", "", t)
    t = re.sub(r"^VARIANTE [A-ZÉ]+\s*(\([^)]*\))?\s*:\s*", "", t)
    return t[:1].upper() + t[1:]


def fallback_text(r):
    a, b = r["archetype"], r["build"]
    other = "PERSISTENCE" if b["defense"] == "bouclier" else "BOUCLIER"
    surv = [s for s in a.get("survie") or [] if other not in s]
    tests = [p for p in (a.get("pieges") or [])] + [h for h in r.get("hypotheses", [])
                                                     if not re.match(r"(armes et compagnon|mods archon)", h, re.I)]
    if b["defense"] == "bouclier": tests = [t for t in tests if "Persistence retire" not in t]
    out = ["**Boucle de jeu**"] + [f"- {_tidy(x)}" for x in a.get("boucle_de_jeu") or []]
    out += ["", "**Survie**"] + [f"- {_tidy(x)}" for x in surv]
    out += ["", "**Énergie**"] + [f"- {_tidy(x)}" for x in a.get("energie") or []]
    if b.get("helminth"):
        out += ["", "**Helminth**", f"- {b['helminth']} à la place de {b.get('helminth_remplace') or a.get('helminth_remplace') or '?'}"]
    opts = [c for c in (a.get("choix") or []) if "helminth" not in c.get("quoi", "").lower()]
    if opts: out += ["", "**Autres options**"] + [f"- {c['quoi']} : {', '.join(c['options'])}" for c in opts]
    if tests: out += ["", "**À tester en jeu**"] + [f"- {_tidy(x)}" for x in tests[:5]]
    if r.get("a_viser_ensuite"):
        out += ["", "**À viser ensuite**"] + [f"- {x}" for x in r["a_viser_ensuite"]]
    return "\n".join(out)


def explain(app, r, message, trace):
    """Un seul appel au modèle, sans outils : il reformule le build calculé. None si pas de modèle ou échec."""
    if not app.chat_fn: return None
    payload = {k: r.get(k) for k in ("archetype", "hypotheses", "niveau", "a_viser_ensuite", "persistence_possible")}
    payload["build"] = {k: v for k, v in r["build"].items() if k not in ("hors_build",)}
    payload["consequences_calculees"] = (r["validation"] or {}).get("consequences_calculees")
    payload["totaux"] = (r["validation"] or {}).get("totaux")
    try:
        msg = app.chat_fn([{"role": "system", "content": EXPLAIN},
                           {"role": "user", "content": f"Demande du joueur : {message}\n\nDonnées :\n" + json.dumps(payload, ensure_ascii=False)}], None)
        text = (msg.get("content") or "").strip() or None
        trace.append("  [rapide] explication rédigée par le modèle")
        return text
    except Exception as e:  # le build reste juste : l'explication du code prend le relais
        trace.append(f"  [rapide] modèle indisponible ({str(e)[:80]}) : explication du programme")
        return None


def handle(app, message):
    """Renvoie la réponse du mode rapide, ou None pour laisser la main à l'agent classique."""
    tb = app.tb
    topic = getattr(app, "topic", None)
    prev = getattr(app, "fast_state", {}) or {}
    profile = niveaux.load_profile(app.base)
    pending = prev.get("pending"); assumed = []
    last = getattr(app, "last_gen", None)
    # retouche du build affiché (« remplace Nourish par Roar ») : traduite en corrections pour le robot
    if not pending and last and topic and prev.get("base") == topic and pilote.EDIT.search(message) \
            and not QUESTION_ONLY.search(message):
        trace0 = []
        name = prev.get("warframe") or topic
        r = pilote.retoucher(app, name, message, prev.get("defense_demandee"), prev.get("niveau") or "endgame", profile, last, trace0)
        if not r or "erreur" in r: return None
        tier, defense, objectif = prev.get("niveau") or "endgame", prev.get("defense_demandee"), prev.get("objectif", message)
        return _answer(app, r, message, name, topic, tier, defense, objectif, [], trace0)
    # précision sur le build affiché (« son kit tourne autour du 2 », « la portée compte ») : demande complétée, robot relancé
    if not pending and last and topic and prev.get("base") == topic and pilote.REFINE.search(message) \
            and not QUESTION_ONLY.search(message):
        trace0 = []
        name = prev.get("warframe") or topic
        r = pilote.affiner(app, name, message, prev.get("defense_demandee"), prev.get("niveau") or "endgame", profile, last, trace0)
        if r and "erreur" not in r:
            tier, defense, objectif = prev.get("niveau") or "endgame", prev.get("defense_demandee"), prev.get("objectif", message)
            return _answer(app, r, message, name, topic, tier, defense, objectif, [], trace0)
    if pending:  # réponse aux questions sur ce que le joueur possède
        got = niveaux.parse_answers(message, pending["keys"])
        if not got and wants_build(message, bool(topic)): pending = None  # nouvelle demande : on oublie les questions
        else:
            for k in pending["keys"]: profile[k] = got.get(k, False)  # sans réponse claire : on suppose que non
            assumed = [k for k in pending["keys"] if k not in got]
            niveaux.save_profile(app.base, profile)
            message, topic = pending["message"], pending["base"]
        prev["pending"] = None
    elif not wants_build(message, bool(topic)): return None
    same = prev.get("base") == topic
    tier = niveaux.detect(message) or (prev.get("niveau") if same else None) or "endgame"
    # ce que le joueur dit d'emblée (« je n'ai pas de mods corrompus ») compte tout de suite
    said = niveaux.parse_answers(message, [k for k, _ in niveaux.QUESTIONS.get(tier, [])])
    if said:
        profile.update(said); niveaux.save_profile(app.base, profile)
    ask = niveaux.missing_questions(tier, profile)
    if ask:
        app.fast_state = dict(prev, pending={"keys": [k for k, _ in ask], "message": message, "base": topic})
        q = (f"Pour un build **{niveaux.LABEL[tier]}**, j'évite ce qui est long ou difficile à obtenir. Deux ou trois questions "
             "d'abord (je garde tes réponses pour la suite) :\n" + "\n".join(f"- {x}" for _, x in ask)
             + "\n\nRéponds en une phrase, par exemple « oui pour le premier, non pour le reste ».")
        return {"reponse": q, "trace": [f"  [rapide] niveau {tier} : questions sur ce que le joueur possède"], "mode": "questions"}
    name = frame_name(tb, topic, message, prev.get("warframe") if same else None)
    defense = defense_of(message, prev.get("defense_demandee") if same else None)
    objectif = message if not same or BUILD_WORDS.search(message) and len(message) > 25 else prev.get("objectif", message)
    trace0 = []
    r = pilote.construire(app, name, objectif, defense, tier, profile, trace0, relire=getattr(app, "relecture", True))
    if "erreur" in r: return None
    return _answer(app, r, message, name, topic, tier, defense, objectif, assumed, trace0)


def _answer(app, r, message, name, topic, tier, defense_asked, objectif, assumed, trace0):
    app.last_gen = r
    app.fast_state = {"base": topic, "warframe": name, "defense": r["build"]["defense"], "defense_demandee": defense_asked,
                      "objectif": objectif, "niveau": tier}
    defense = r["build"]["defense"]
    trace = trace0 + [f"  [rapide] {name} ; niveau {tier} ; build « {r['archetype']['nom']} » ; défense {defense} ; contrôle : {r['validation']['statut']}"]
    text = explain(app, r, message, trace)
    goal = r["archetype"].get("objectif", "") if tier == "endgame" else f"niveau {niveaux.LABEL[tier]} : seulement des pièces faciles à obtenir"
    head = (f"### {name} — {r['archetype']['nom']}\n*{goal}* · défense par "
            f"{'le bouclier' if defense == 'bouclier' else 'Arcane Persistence (santé et armure)'}"
            + ("" if r.get("archetype_relu") else " · raisonnement automatique (fiabilité probable), à vérifier en jeu") + "\n\n"
            + "Le build est dans l'éditeur à droite.\n\n")
    status = "" if r["validation"]["statut"] == "complet et valide" else (
        "\n\n**À corriger** : " + "; ".join((r["validation"].get("erreurs") or []) + (r["validation"].get("manquants") or [])))
    alt = r.get("autres_objectifs") or []
    tail = ("\n\n**Je peux aussi te proposer** : un build " + ", ".join(alt)
            + (", ou la défense par " + ("Arcane Persistence" if defense == "bouclier" else "le bouclier")
               if defense != "bouclier" or r.get("persistence_possible") else "") + ". Dis-moi simplement ce que tu préfères.") if alt else ""
    nxt = ("\n\n**À viser ensuite** : " + " ; ".join(r["a_viser_ensuite"])) if r.get("a_viser_ensuite") and text and "viser" not in text.lower() else ""
    if assumed:
        names = {"reacteur": "Orokin Reactor", "corrompus": "mods corrompus", "helminth": "Helminth", "arcanes": "arcanes", "syndicats": "augments de syndicat"}
        nxt += "\n\n*Sans réponse claire, j'ai supposé que tu n'as pas : " + ", ".join(names[k] for k in assumed) + ". Dis-le-moi si c'est faux.*"
    tail = nxt + tail
    cons = [re.sub(r"\s*\(coût fixe[^)]*\)", "", c) for c in (r["validation"] or {}).get("consequences_calculees") or []]
    gives = ("\n\n**Ce que le build donne**\n" + "\n".join(f"- {c}" for c in cons)) if cons else ""
    answer = head + status.lstrip("\n") + ("\n\n" if status else "") + (text or fallback_text(r)) + gives + tail
    if app.agent:  # l'agent classique garde le fil : une question qui suit porte sur ce build
        app.agent.messages += [{"role": "user", "content": message},
                               {"role": "assistant", "content": answer + "\n\n(build calculé : " + json.dumps(r["build"], ensure_ascii=False) + ")"}]
        app.agent.building = True
    return {"reponse": answer, "trace": trace, "build_propose": r["build"], "mode": "rapide",
            "gen": {"warframe": name, "archetype": r["archetype"]["id"], "defense": app.fast_state.get("defense_demandee"), "niveau": tier,
                    "demande": r.get("demande"), "variantes": r.get("variantes")},
            "explication": text or fallback_text(r), "titre": f"{name} — {r['archetype']['nom']}", "tail": tail}
