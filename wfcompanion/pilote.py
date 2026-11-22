"""Le pilote : l'agent (petit modèle) et le robot scripté travaillent ensemble par messages JSON.

1. comprendre() : le modèle traduit la demande du joueur en une « demande » JSON (objectif, capacité centrale, imposés…) ;
   sans modèle, ou si sa réponse est illisible, le code la reconnaît lui-même (mots-clés).
2. Le robot (optimizer.propose -> moteur/robot.plan) compare des builds entiers et renvoie le meilleur et 2 variantes.
3. relire() : le modèle vérifie que le build correspond à la demande et répond {"verdict": "ok"} ou des corrections ;
   le robot les applique et reconstruit (2 tours au plus). Les contrôles durs (capacité, défense, mods) restent dans le code.
4. Chaque correction est notée dans 04-retours-experience/relectures.jsonl : c'est la matière pour améliorer le robot.

Le même format sert aux retouches du joueur (« remplace Nourish par Roar ») : elles deviennent des corrections.
"""
import datetime, json, os, re

from . import optimizer
from .moteur import regles as rg

MAX_TOURS = 2

DEMANDE_PROMPT = (
    "Tu traduis la demande d'un joueur de Warframe en JSON pour un programme qui construit les builds. Réponds UNIQUEMENT "
    "par un objet JSON, sans texte autour, avec ces clés :\n"
    '{"objectif": "degats|boss|tank|farm|soutien|armes", "capacite_centrale": "nom exact d\'une capacité ou null", '
    '"armes": true si le build doit servir les armes du loadout, "contenu": "ex. steel path, archonte, ou null", '
    '"imposes": [noms d\'objets que le joueur veut], "interdits": [noms d\'objets qu\'il ne veut pas], '
    '"stats_prioritaires": [parmi puissance, portee, duree, efficacite : celles que le joueur met en avant], '
    '"stats_basses": [celles dont il dit qu\'elles ne servent pas], "stats_max": [celles qu\'il veut au maximum, ou qui augmentent ce que rapporte le kit], '
    '"spam": true si le joueur veut relancer ses capacités sans arrêt}\n'
    "Règles : objectif « degats » par défaut. N'invente aucun nom : utilise seulement les noms cités par le joueur "
    "ou présents dans la liste des capacités fournie. Laisse capacite_centrale à null si le joueur n'en parle pas.")

RELIRE_PROMPT = (
    "Tu relis un build de Warframe calculé par un programme, pour un joueur. Le programme a déjà vérifié la capacité de mods, "
    "la défense et les règles du jeu. Toi, vérifie seulement que le build correspond à ce que le joueur a demandé "
    "(objectif, capacité qu'il veut jouer, objets qu'il veut ou refuse) et qu'il n'y a pas de choix absurde pour cet objectif. "
    "Réponds UNIQUEMENT par du JSON :\n"
    '{"verdict": "ok"} ou {"verdict": "corriger", "corrections": [{"element": "helminth|arcane|mod|capacite_centrale|objectif|variante", '
    '"retirer": "nom ou null", "mettre": "nom ou null", "raison": "phrase courte"}]}\n'
    "Pour passer à une variante proposée, utilise element « variante » et mettre = son numéro (1 ou 2). "
    "N'utilise que des noms présents dans les données. En cas de doute, réponds ok.")

RETOUCHE_PROMPT = (
    "Le joueur veut modifier le build affiché. Traduis sa demande en corrections JSON pour le programme. Réponds UNIQUEMENT "
    'par du JSON : {"corrections": [{"element": "helminth|arcane|mod|capacite_centrale|objectif|variante", '
    '"retirer": "nom ou null", "mettre": "nom ou null", "raison": "phrase courte"}]}. N\'invente aucun nom.')

# capacité désignée par son numéro (« son 2e pouvoir », « le 4 », « son deuxième sort »)
NUM = {"premier": 1, "premiere": 1, "première": 1, "second": 2, "seconde": 2, "deuxieme": 2, "deuxième": 2,
       "troisieme": 3, "troisième": 3, "quatrieme": 4, "quatrième": 4}
ABILITY_NUM = re.compile(r"\b(?:(?:son|sa|le|la|ton|ta|du|au)\s+)?(?:(\d)\s*(?:er|ère|e|ème|eme|nd|nde)?|(premi[eè]re?|second|seconde|deuxi[eè]me|"
                         r"troisi[eè]me|quatri[eè]me))\s+(?:pouvoir|capacit[ée]|comp[ée]tence|sort|skill|ability)\b|\b(?:son|ton|le)\s+(\d)\b(?!\s*%)", re.I)
# stats que le joueur met en avant (ou dont il dit qu'elles ne servent pas)
STATS = {"puissance": r"puissance|strength", "portee": r"port[ée]e|range", "duree": r"dur[ée]e|duration", "efficacite": r"efficacit[ée]|efficiency"}
NEG = r"(?:pas (?:besoin )?(?:de |d')|sans |inutile|peu importe|ne sert|pas important)"
# « plus il a de portée, plus il a d'armes » : la stat augmente ce que rapporte le kit -> au maximum
STAT_FR = {"puissance": r"puissance", "portee": r"port[ée]e", "duree": r"dur[ée]e", "efficacite": r"efficacit[ée]"}
STAT_MAX = [r"plus (?:il|elle|on|tu|la frame) (?:a|aura|met|monte)\s+(?:de |d'|la |sa )?({s})[^.]{{0,50}}plus",
            r"({s})\s+(?:augmente|donne|d[ée]termine|fait monter|monte)\s+(?:aussi\s+)?(?:le nombre|le max|plus d)",
            r"(?:max(?:imum)?|à fond)\s+(?:de |en )?({s})|({s})\s+(?:au\s+)?(?:max(?:imum)?|à fond)"]
SPAM = re.compile(r"\bspam|lancer en boucle|relancer sans arr[êe]t|en continu", re.I)
REFINE = re.compile(r"tourne autour|centr[ée]|ax[ée]|focus sur|repose sur|bas[ée] sur|scal|augmente avec|d[ée]pend de|"
                    r"en fonction de|monter la|prioris|plus de (?:puissance|port[ée]e|dur[ée]e)|" + ABILITY_NUM.pattern, re.I)

EDIT = re.compile(r"\b(remplace|remplacer|enl[eè]ve|enlever|retire|retirer|ajoute|ajouter|mets|mettre|change|changer|modifie|"
                  r"à la place|au lieu|sans|pas de|plutôt)\b", re.I)


def _json(text):
    """Premier objet JSON d'une réponse de modèle (il ajoute parfois du texte ou des ``` autour)."""
    if not text: return None
    t = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    m = re.search(r"\{.*\}", t, re.S)
    if not m: return None
    try: return json.loads(m.group(0))
    except json.JSONDecodeError:
        try: return json.loads(re.sub(r",\s*([}\]])", r"\1", m.group(0)))  # virgule en trop
        except json.JSONDecodeError: return None


def _ask(app, system, user, trace, label):
    if not app.chat_fn: return None
    try:
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        jf = getattr(app, "json_fn", None)  # Ollama : réponse JSON forcée (fiable même avec un modèle de 1 à 2 milliards de paramètres)
        msg = jf(msgs) if jf else app.chat_fn(msgs, None)
        out = _json(msg.get("content") or "")
        trace.append(f"  [pilote] {label} : " + ("JSON reçu" if out is not None else "réponse illisible, le code prend le relais"))
        return out
    except Exception as e:
        trace.append(f"  [pilote] {label} : modèle indisponible ({str(e)[:60]})")
        return None


def _known(tb, frame):
    """Noms que le robot connaît pour cette frame : capacités, Helminth, arcanes, mods."""
    f = tb.fiche_warframe(frame)
    caps = [c["nom"] for c in f.get("capacites", [])] if "erreur" not in f else []
    return {"capacites": caps, "helminth": list(tb.helminth_abilities()),
            "arcanes": [r["name"] for r in tb.con.execute("SELECT name FROM arcanes WHERE type = 'Warframe Arcane'")]}


def _match(tb, name, known):
    """Nom exact d'un objet du jeu (capacité, Helminth, arcane ou mod), ou None."""
    if not name or not isinstance(name, str): return None
    n = name.strip().lower()
    for lst in known.values():
        for x in lst:
            if x.lower() == n: return x
    r = tb.con.execute("SELECT name FROM mods WHERE name = ? COLLATE NOCASE", (name.strip(),)).fetchone()
    return r["name"] if r else None


def _names_in_text(tb, text, known):
    t = (text or "").lower()
    out = []
    for lst in known.values():
        out += [x for x in lst if len(x) >= 4 and re.search(r"\b" + re.escape(x.lower()) + r"\b", t)]
    return out


def demande_code(tb, frame, message):
    """Demande reconnue par le code seul (sans modèle)."""
    known = _known(tb, frame)
    d = {"objectif": rg.objectif_of(message), "armes": rg.armes_centrales(tb, message, frame)}
    t = message.lower()
    for c in known["capacites"]:
        if re.search(r"\b" + re.escape(c.lower()) + r"\b", t): d["capacite_centrale"] = c; break
    m = ABILITY_NUM.search(t)
    if m and "capacite_centrale" not in d:
        n = int(m.group(1) or m.group(3) or 0) or NUM.get((m.group(2) or "").lower(), 0)
        if 1 <= n <= len(known["capacites"]): d["capacite_centrale"] = known["capacites"][n - 1]
    for st, rx in STATS.items():
        if re.search(NEG + r"[^.,;]{0,20}(?:" + rx + ")", t): d.setdefault("stats_basses", []).append(st)
        elif re.search(rx, t): d.setdefault("stats_prioritaires", []).append(st)
    if SPAM.search(t): d["spam"] = True
    for st, rx in STAT_FR.items():
        if any(re.search(p.format(s=rx), t) for p in STAT_MAX):
            d.setdefault("stats_max", []).append(st)
            d["stats_prioritaires"] = [x for x in d.get("stats_prioritaires") or [] if x != st]
    neg = re.findall(r"\b(?:sans|pas de|pas d'|j'ai pas|je n'ai pas|interdit)\s+([^,.;]+)", t)
    d["interdits"] = [x for x in _names_in_text(tb, " ".join(neg), known)]
    d["imposes"] = [x for x in _names_in_text(tb, t, known) if x not in d["interdits"] and x != d.get("capacite_centrale")]
    return d


def comprendre(app, frame, message, trace):
    d = demande_code(app.tb, frame, message)
    known = _known(app.tb, frame)
    out = _ask(app, DEMANDE_PROMPT, f"Warframe : {frame}\nCapacités : {', '.join(known['capacites'])}\nDemande du joueur : {message}",
               trace, "demande")
    if isinstance(out, dict):
        if out.get("objectif") in rg.LABEL: d["objectif"] = out["objectif"]
        cap = _match(app.tb, out.get("capacite_centrale"), {"c": known["capacites"]})
        if cap: d["capacite_centrale"] = cap
        if isinstance(out.get("armes"), bool): d["armes"] = out["armes"] or d["armes"]
        if out.get("contenu"): d["contenu"] = str(out["contenu"])[:60]
        for key in ("stats_max", "stats_prioritaires", "stats_basses"):
            got = [x for x in out.get(key) or [] if x in STATS]
            if got: d[key] = list(dict.fromkeys((d.get(key) or []) + got))
        if out.get("spam") is True: d["spam"] = True
        for key in ("imposes", "interdits"):
            got = [_match(app.tb, x, known) for x in out.get(key) or [] if isinstance(x, str)]
            d[key] = list(dict.fromkeys((d.get(key) or []) + [x for x in got if x]))
    d["imposes"] = [x for x in d.get("imposes") or [] if x not in (d.get("interdits") or [])]
    return d


def appliquer(tb, frame, d, corrections, r=None):
    """Corrections (de l'agent ou du joueur) -> nouvelle demande. Les noms inconnus sont ignorés."""
    d = json.loads(json.dumps(d))
    known = _known(tb, frame)
    done = []
    for c in corrections or []:
        if not isinstance(c, dict): continue
        el = str(c.get("element") or "").lower()
        if el == "variante":
            try: d["variante"] = max(0, min(2, int(c.get("mettre"))))
            except (TypeError, ValueError): continue
            done.append(c); continue
        if el == "objectif" and c.get("mettre") in rg.LABEL:
            d["objectif"] = c["mettre"]; d.pop("variante", None); done.append(c); continue
        put, out = _match(tb, c.get("mettre"), known), _match(tb, c.get("retirer"), known)
        if el == "capacite_centrale" and put in known["capacites"]:
            d["capacite_centrale"] = put; d.pop("variante", None); done.append(c); continue
        if not put and not out: continue
        if out:
            d["interdits"] = list(dict.fromkeys((d.get("interdits") or []) + [out]))
            d["imposes"] = [x for x in d.get("imposes") or [] if x != out]
        if put:
            d["imposes"] = list(dict.fromkeys((d.get("imposes") or []) + [put]))
            d["interdits"] = [x for x in d.get("interdits") or [] if x != put]
            # remplacer un Helminth ou un arcane : l'ancien choix du robot laisse la place
            if r and el == "helminth" and r["build"].get("helminth") and r["build"]["helminth"] != put and not out:
                d["interdits"].append(r["build"]["helminth"])
        d.pop("variante", None); done.append(c)
    return d, done


def _resume(r):
    b = r["build"]
    return {"demande": r.get("demande"), "build": {"helminth": b.get("helminth"), "remplace": r["archetype"].get("helminth_remplace"),
            "arcanes": b.get("arcanes"), "aura": b.get("aura"), "mods": b.get("mods"), "exilus": b.get("exilus"), "defense": b.get("defense"),
            "capacite_centrale": (r.get("demande") or {}).get("capacite_centrale")},
            "variantes": [{"numero": i, **{k: v[k] for k in ("resume", "faiblesses")}} for i, v in enumerate(r.get("variantes") or [])],
            "boucle_de_jeu": r["archetype"].get("boucle_de_jeu"), "controle_du_programme": r["validation"].get("statut")}


def _log(app, kind, message, d, corrections):
    if not getattr(app, "base", None) or not corrections: return
    path = os.path.join(app.base, "04-retours-experience", "relectures.jsonl")
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"date": datetime.datetime.now().isoformat(timespec="seconds"), "type": kind,
                                 "message": message, "demande": d, "corrections": corrections}, ensure_ascii=False) + "\n")
    except OSError: pass


def construire(app, frame, message, defense, tier, profile, trace, d=None, relire=True):
    """Demande -> robot -> relecture -> corrections (2 tours au plus). Renvoie le résultat de optimizer.propose."""
    tb = app.tb
    d = d or comprendre(app, frame, message, trace)
    r = optimizer.propose(tb, frame, message, defense, None, tier, profile, d)
    if "erreur" in r: return r
    trace.append(f"  [robot] {r['archetype']['nom']} ; " + (r["variantes"][0]["resume"] if r.get("variantes") else ""))
    for tour in range(MAX_TOURS if relire else 0):
        v = _ask(app, RELIRE_PROMPT, f"Demande du joueur : {message}\n\nBuild proposé :\n" + json.dumps(_resume(r), ensure_ascii=False),
                 trace, f"relecture {tour + 1}")
        if not isinstance(v, dict) or v.get("verdict") != "corriger": break
        nd, done = appliquer(tb, frame, r.get("demande") or d, v.get("corrections"), r)
        if not done: trace.append("  [pilote] corrections inapplicables (noms inconnus) : build gardé"); break
        _log(app, "relecture", message, r.get("demande"), done)
        r2 = optimizer.propose(tb, frame, message, defense, None, tier, profile, nd)
        if "erreur" in r2 or r2["validation"].get("statut") != "complet et valide" and r["validation"].get("statut") == "complet et valide":
            trace.append("  [pilote] la correction casse le build : build précédent gardé"); break
        r, d = r2, nd
        r["corrections_relecture"] = (r.get("corrections_relecture") or []) + done
        trace.append("  [robot] corrigé : " + "; ".join(c.get("raison") or str(c.get("mettre")) for c in done))
    return r


def retouche_code(tb, frame, message, r):
    """Retouche reconnue par le code : « remplace X par Y », « enlève X », « mets Y »."""
    known = _known(tb, frame)
    t = message.lower()
    names = _names_in_text(tb, t, known)
    m = re.search(r"(?:remplace|change)\s+(.+?)\s+(?:par|contre|avec)\s+(.+)", t)
    if m:
        a, b = _names_in_text(tb, m.group(1), known), _names_in_text(tb, m.group(2), known)
        if a or b: return [{"element": "helminth" if (a or b)[0] in known["helminth"] else "mod", "retirer": (a or [None])[0],
                            "mettre": (b or [None])[0], "raison": "demandé par le joueur"}]
    if re.search(r"\b(enl[eè]ve|retire|sans|pas de)\b", t) and names:
        return [{"element": "mod", "retirer": n, "mettre": None, "raison": "demandé par le joueur"} for n in names]
    if re.search(r"\b(ajoute|mets|mettre|plutôt)\b", t) and names:
        return [{"element": "helminth" if n in known["helminth"] else "mod", "retirer": None, "mettre": n, "raison": "demandé par le joueur"}
                for n in names]
    return []


def retoucher(app, frame, message, defense, tier, profile, last, trace):
    """Retouche du build affiché, sans repasser par l'agent classique. None si rien n'a été compris."""
    corr = retouche_code(app.tb, frame, message, last)
    out = _ask(app, RETOUCHE_PROMPT, f"Build affiché :\n{json.dumps(_resume(last), ensure_ascii=False)}\n\nDemande du joueur : {message}",
               trace, "retouche")
    if isinstance(out, dict) and out.get("corrections"): corr = out["corrections"] + corr
    d, done = appliquer(app.tb, frame, last.get("demande") or {}, corr, last)
    if not done: return None
    _log(app, "retouche", message, last.get("demande"), done)
    trace.append("  [pilote] retouche : " + "; ".join(f"{c.get('retirer') or ''} -> {c.get('mettre') or ''}".strip() for c in done))
    return construire(app, frame, message, defense, tier, profile, trace, d=d, relire=False)


def affiner(app, frame, message, defense, tier, profile, last, trace):
    """Précision du joueur sur le build affiché (« son kit tourne autour du 2 », « la portée compte ») :
    la demande précédente est complétée, puis le robot reconstruit. None si rien de nouveau n'a été compris."""
    new = comprendre(app, frame, message, trace)
    old = dict(last.get("demande") or {})
    d = dict(old)
    changed = False
    if new.get("capacite_centrale") and new["capacite_centrale"] != old.get("capacite_centrale"):
        d["capacite_centrale"] = new["capacite_centrale"]; changed = True
    for key in ("stats_max", "stats_prioritaires", "stats_basses", "imposes", "interdits"):
        add = [x for x in new.get(key) or [] if x not in (old.get(key) or [])]
        if add: d[key] = list(dict.fromkeys((old.get(key) or []) + add)); changed = True
    if new.get("spam") and not old.get("spam"): d["spam"] = True; changed = True
    if not changed: return None
    d.pop("variante", None)
    trace.append("  [pilote] précision : " + json.dumps({k: d[k] for k in d if d.get(k) != old.get(k)}, ensure_ascii=False))
    return construire(app, frame, message, defense, tier, profile, trace, d=d, relire=False)
