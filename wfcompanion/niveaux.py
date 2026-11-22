"""Niveau de progression du joueur : ce qu'un build a le droit d'utiliser.

Un débutant n'a ni Primed (Baro Ki'Teer), ni Umbral, ni Archon, ni Galvanized, ni les augments vendus par les syndicats
(plusieurs jours de réputation), ni Helminth, ni arcanes, ni focus. On le déduit des sources de chaque mod dans les tables
de drop, pas d'une liste écrite à la main. Ce qu'on ne peut pas deviner (mods corrompus, Orokin Reactor, Helminth…) se
demande au joueur, une fois : la réponse est gardée dans son profil.
"""
import json, os, re

TIERS = ("debutant", "intermediaire", "endgame")
LABEL = {"debutant": "débutant", "intermediaire": "intermédiaire (début du Steel Path)", "endgame": "endgame (level cap)"}

_DETECT = [
    ("debutant", r"d[ée]butant|novice|nouveau joueur|je (d[ée]bute|commence)|d[ée]but de (jeu|partie)|star ?chart|\bmr ?[1-7]\b|petit budget"),
    ("intermediaire", r"interm[ée]diaire|palier|milieu de (jeu|partie)|mid ?game|d[ée]but (du |de )?(steel path|sp)\b|"
                      r"(entrer|commencer|attaquer) (dans |le )?(le )?(steel path|sp)\b|\bmr ?(8|9|1[0-6])\b"),
    ("endgame", r"level ?cap|endgame|end game|fin de jeu|niveau max|archon(te)?s? hunt|chasse d'archonte"),
]

# ce qu'on demande au joueur selon le niveau visé (clé du profil, question)
QUESTIONS = {
    "debutant": [("reacteur", "Ta warframe a-t-elle un **Orokin Reactor** (capacité 60 au lieu de 30) ?"),
                 ("corrompus", "As-tu des **mods corrompus** (Blind Rage, Narrow Minded, Overextended… des coffres du Déréliction) ?")],
    "intermediaire": [("corrompus", "As-tu des **mods corrompus** (Blind Rage, Transient Fortitude, Narrow Minded…) ?"),
                      ("helminth", "As-tu le **Helminth** ?"),
                      ("arcanes", "As-tu des **arcanes de warframe** (Arcane Energize, Molt Augmented, Arcane Fury…) ?"),
                      ("syndicats", "Es-tu assez haut dans un **syndicat** pour acheter les augments de cette warframe ?")],
    "endgame": [],
}
KEYWORDS = {"reacteur": r"r[ée]act(eu|o)r|catalys|capacit[ée]", "corrompus": r"corromp|blind rage|coffre|vault|d[ée]r[ée]lict",
            "helminth": r"helminth", "arcanes": r"arcane", "syndicats": r"syndicat|augment|r[ée]putation"}
NEG = r"\b(pas|non|aucun|aucune|jamais|sans|n'ai|pas encore)\b"

SYNDICATES = ("Steel Meridian", "Arbiters of Hexis", "Cephalon Suda", "Perrin Sequence", "Red Veil", "New Loka",
              "Cephalon Simaris", "Conclave", "Nightwave", "Baro", "Ostron", "Solaris", "Entrati", "Necraloid", "Holdfasts",
              "Cavia", "Hex", "Vox Solaris", "Ventkids", "Quills", "Kahl")


def detect(message):
    t = message.lower()
    for tier, rx in _DETECT:
        if re.search(rx, t): return tier
    return None


def access(tb, name):
    """facile | corrompu | syndicat | rare : comment le joueur obtient ce mod (d'après les données du jeu)."""
    if re.match(r"^(Primed|Umbral|Archon|Galvanized|Amalgam)\s", name): return "rare"
    r = tb.con.execute("SELECT data FROM mods WHERE name = ? COLLATE NOCASE", (name,)).fetchone()
    if not r: return "rare"
    d = json.loads(r["data"])
    if d.get("rarity") == "Legendary": return "rare"
    locs = [x.get("location") or "" for x in d.get("drops") or []]
    locs += [p for (p,) in tb.con.execute("SELECT place FROM drops WHERE item = ? COLLATE NOCASE", (name,))]
    if any("Derelict Vault" in l for l in locs): return "corrompu"
    if not locs: return "rare"  # ni mission ni ennemi : Baro, Nightwave, Conclave…
    if all(any(s in l for s in SYNDICATES) for l in locs): return "syndicat"
    return "facile"


def rules(tier, profile):
    """Ce que le niveau et le profil autorisent."""
    p = profile or {}
    yes = lambda k, default: p.get(k) if p.get(k) is not None else default
    if tier == "debutant":
        return {"access": {"facile"} | ({"corrompu"} if yes("corrompus", False) else set()),
                "reacteur": yes("reacteur", False), "formas": 0, "helminth": False, "arcanes": False, "focus": False}
    if tier == "intermediaire":
        return {"access": {"facile"} | ({"corrompu"} if yes("corrompus", False) else set())
                          | ({"syndicat"} if yes("syndicats", True) else set()),
                "reacteur": True, "formas": 3, "helminth": yes("helminth", False), "arcanes": yes("arcanes", False), "focus": True}
    return {"access": {"facile", "corrompu", "syndicat", "rare"}, "reacteur": True, "formas": None,
            "helminth": True, "arcanes": True, "focus": True}


def parse_answers(message, keys):
    """« oui pour le reactor mais pas de corrompus » -> {"reacteur": True, "corrompus": False}. Un « oui » ou « non » seul
    vaut pour toutes les questions posées."""
    t = message.lower(); out = {}
    for k in keys:
        m = re.search(KEYWORDS[k], t)
        if not m: continue
        clause = re.split(r"[,.;!?]| mais | et ", t[max(0, m.start() - 40):m.end() + 40])
        around = next((c for c in clause if re.search(KEYWORDS[k], c)), t)
        out[k] = not re.search(NEG, around)
    rest = [k for k in keys if k not in out]
    if rest:
        if re.fullmatch(r"\W*(oui|yes|ouais|j'ai tout|tout)\W*.*", t) and not re.search(NEG, t): out.update({k: True for k in rest})
        elif re.fullmatch(r"\W*(non|no|rien|aucun|aucune)\b.*", t): out.update({k: False for k in rest})
    return out


def missing_questions(tier, profile):
    return [(k, q) for k, q in QUESTIONS.get(tier, []) if (profile or {}).get(k) is None]


def profile_path(base):
    return os.path.join(base, "04-retours-experience", "profil-joueur.json")


def load_profile(base):
    try:
        with open(profile_path(base), encoding="utf-8") as fh: return json.load(fh)
    except (OSError, json.JSONDecodeError): return {}


def save_profile(base, profile):
    os.makedirs(os.path.dirname(profile_path(base)), exist_ok=True)
    with open(profile_path(base), "w", encoding="utf-8") as fh:
        json.dump(profile, fh, ensure_ascii=False, indent=1)
