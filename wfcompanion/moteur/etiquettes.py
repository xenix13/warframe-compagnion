"""Étiquettes : ce qu'un élément du jeu APPORTE et ce dont il PROFITE.

Le robot ne lit pas le wiki comme un humain : il ramène chaque capacité à quelques étiquettes. Une synergie devient alors
une correspondance entre ce qu'un élément apporte et ce dont un autre profite (voir regles.py).

Les étiquettes d'une frame sans module sont tirées automatiquement de sa page de capacité (fiabilité « probable ») ;
un module (modules/warframes/<frame>.py) les remplace par des étiquettes relues (« confirmé »).
"""
import glob, os, re

# ce qu'une capacité peut apporter (vocabulaire commun à tout le moteur)
APPORTS = {
    "degats": "dégâts",
    "zone": "effet de zone",
    "controle": "contrôle des ennemis",
    "vulnerabilite": "ennemis qui subissent plus de dégâts",
    "retrait_armure": "retrait d'armure",
    "bonus_degats": "bonus de dégâts (armes et capacités)",
    "bonus_armes": "bonus pour les armes (dégâts, élément, critique)",
    "retrait_armure_partiel": "retrait d'armure partiel (statut Feu : -50 %)",
    "feu": "inflige le statut Feu",
    "radiation": "Radiation (utile contre les Eidolons)",
    "bonus_viral": "bonus Viral (armes, et capacités qui ont une chance de statut)",
    "bonus_puissance": "puissance de capacité en plus",
    "cree_objet": "crée un objet (déclenche Arcane Sculptor)",
    "compagnon": "touche aussi le compagnon",
    "reduction_degats": "réduction des dégâts subis",
    "invulnerabilite": "invulnérabilité",
    "invisibilite": "invisibilité",
    "esquive": "esquive (les attaques peuvent passer à travers)",
    "overguard": "Overguard",
    "immunite_statut": "insensible aux effets de statut",
    "soin": "soin",
    "bouclier": "rend du bouclier",
    "armure_bonus": "armure en plus",
    "energie": "énergie",
    "energie_x": "multiplie l'énergie reçue (sans en créer)",
    "mobilite": "déplacement",
    "statut": "effets de statut",
    "butin": "butin en plus",
    "soutien": "aide l'escouade",
}
# ce qui fait monter une capacité
PROFITE = {"puissance": "Strength", "duree": "Duration", "portee": "Range"}

# mots du wiki (anglais) -> étiquette ; volontairement prudent : une étiquette ratée vaut mieux qu'une fausse
_RULES = [
    ("degats", r"\b(deal|deals|dealing|inflict|inflicts|inflicting)\b[^.]{0,90}\bdamage\b|\bdamage per (second|tick)\b|\bexplod"),
    ("zone", r"\bwithin (a )?\d|\bradius\b|\ball enemies\b|\benemies in\b|\bnearby enemies\b|\bin a cone\b"),
    ("controle", r"\b(stun\w*|knockdowns?|knocks? \w*\s?down|ragdoll\w*|petrif\w*|freez\w*|frozen|immobiliz\w*|blind\w*|"
                 r"sleep\w*|lift\w*|pulls?|pulled|disarm\w*|confus\w*|suspend\w*|entangl\w*|trap\w*|slow\w*|crystalliz\w*)\b"),
    ("vulnerabilite", r"\btake(s)? (\d+% )?(more|increased|additional|bonus) damage|\bdamage vulnerability|\bvulnerab|"
                      r"\bweak ?points?\b|\bmarked\b"),
    ("retrait_armure", r"\b(strip|strips|stripping|remove|removes|reduce|reduces)\b[^.]{0,60}\barmor\b|\barmor (strip|reduction)|\barmor of (nearby |all |affected )?enemies"),
    ("bonus_armes", r"bonus to (?:your |their )?weapons|to their attacks|(?:primary|secondary|weapon)[^.]{0,25}critical chance|"
                    r"weapon critical|critical chance for"),
    ("radiation", r"\bradiation"),
    ("feu", r"\bheat (?:damage|status)|<dt_fire|\bset ablaze|\bburn"),
    ("bonus_degats", r"\b(increase|increases|increased|bonus|boost|boosts)\b[^.]{0,25}\bdamage\b(?! taken)(?! reduction)"),
    ("immunite_statut", r"\bimmun\w* to (?:all )?status|\bstatus (?:effect )?immun|\bstatus immunity|\bimmune to status"),
    ("esquive", r"\bdodge|\bevasion\b|\bevade|phase through|harmlessly pass"),
    ("reduction_degats", r"(?<!area )(?<!aoe )\bdamage reduction\b(?![^.]{0,15}against)|\breduc\w* (the )?damage taken\b|\breduces? incoming damage"),
    ("invulnerabilite", r"\binvulnerab|\bimmune to (all )?damage"),
    ("invisibilite", r"\binvisib|\bcloak"),
    ("overguard", r"\b(grant|grants|gain|gains|give|gives|receive|receives)\b[^.]{0,40}\boverguard\b"),
    ("soin", r"\b(heals?|healing)\b(?! (rumblers?|enemies|the ring))|\brestores? (\d+ )?health|\bhealth regen"),
    ("bouclier", r"\brestores? (\d+ )?shields?|\bshield (regen|recharge)|\brebuild"),
    ("armure_bonus", r"\b(bonus|additional|increased?) armor\b|\bgains? (\d+ )?armor"),
    ("energie", r"\b(restores?|regenerat\w+|grants?|gives?|returns?|generat\w+)\b[^.]{0,30}\benergy\b|\benergy (orb|regen|multiplier)"),
    ("mobilite", r"\b(dash|dashes|teleport|teleports|leap|leaps|charge forward|speed boost|sprint speed)\b"),
    ("statut", r"\bstatus (effect|chance|proc)|\bprocs?\b"),
    ("butin", r"\bloot\b|\bdrop chance\b|\bextra (drops|loot)"),
    ("soutien", r"\ballies\b|\bsquad\b|\bteammates\b"),
    ("bonus_puissance", r"\b(increase|increases|buff|buffs|boost|boosts|bonus)\b[^.]{0,30}\bability strength\b"),
    ("cree_objet", r"\b(throw|throws|spawn|spawns|summon|summons|place|places|deploy|deploys|release|releases|create|creates|plant|plants)\b"
                   r"[^.]{0,40}\b(mushroom|turret|totem|pillar|wall|barrier|clone|ward|beacon|mine|tower|pylon|bubble|globe|rift|portal|decoy)"),
]


# « stat clé » : la stat ne change pas seulement la taille de la zone ou le temps, elle augmente ce que la capacité
# rapporte (nombre d'armes ou de cibles, multiplicateur…). Le robot la monte alors au maximum.
_GEOM = r"radius|length|width|range|distance|cone|area|aoe|height|reach|diameter|spread|m\b"
_COUNT = r"\bnumber of|\bmax(?:imum)? (?:number|weapons|targets|count|enemies)|\bcount\b|\bclones\b|\bcharges\b|\bstacks\b|\bmirrors\b|\bweapons\b(?! and)"
# la puissance est déjà visée haute quand elle compte : on ne cherche la « stat clé » que pour la portée et la durée
_STAT_EN = {"duree": "duration", "portee": "range"}
_KEY_SENT = [r"(?:number|amount|maximum|count|max)[^.]{0,60}(?:affected by|scales? with|increases? with|based on|depends? on|"
             r"determined by)\s+(?:ability\s+|power\s+)?(%s)",
             r"(?:ability\s+|power\s+)?(%s)\s+(?:also\s+)?(?:affects|increases|determines|scales|raises)\s+(?:the\s+)?"
             r"(?:number|maximum|amount|count|max)"]


def stats_cles(head, body):
    """Stats qui augmentent ce que la capacité rapporte, au-delà de la zone ou du temps."""
    out = []
    for st, en in _STAT_EN.items():
        m = re.search(en.capitalize() + r":\s*(.*?)(?=\n\s*\n|Strength:|Duration:|Range:|Misc:|Subsumable|$)", head, re.S)
        if m and m.group(1).strip() != "N/A":
            labels = re.findall(r"\(([^)]*)\)", m.group(1))
            if any(re.search(_COUNT, l, re.I) and not re.search(_GEOM, l, re.I) for l in labels):
                out.append(st); continue
        if any(re.search(rx % en, body, re.I) for rx in _KEY_SENT): out.append(st)
    return out


def ability_page(base, frame, ability):
    """Texte de la page du wiki d'une capacité (dossier de la frame, ou du Helminth pour ses capacités propres)."""
    for folder in (frame, "Helminth", "*"):
        hits = glob.glob(os.path.join(base, "02-wiki", "warframes", folder, f"Capacité - {glob.escape(ability)}.md"))
        if hits:
            with open(hits[0], encoding="utf-8", errors="replace") as fh: return fh.read()
    return ""


def _summary(text):
    """L'en-tête de la page : coût, description d'une phrase et lignes de stats (Strength / Duration / Range)."""
    head = text.split("\nInfo\n", 1)[0]
    info = text.split("\nInfo\n", 1)[1].split("\nAugment", 1)[0] if "\nInfo\n" in text else ""
    info = info.split("\nHelminth\n", 1)[0]
    return head, info


def extract(text):
    """Étiquettes déduites d'une page de capacité. Renvoie {apporte, profite_de, cout, helminth, resume}."""
    if not text: return None
    head, info = _summary(text)
    # la description et les premiers points de « Info » décrivent la mécanique ; la suite (notes, astuces) ajoute du bruit
    bullets = [l for l in info.split("\n") if l.strip().startswith("-")][:6]
    body = (head + "\n" + "\n".join(bullets)).lower()
    # les phrases négatives (« does not affect enemies with Overguard ») ne doivent pas donner d'étiquette
    body = " ".join(x for x in re.split(r"(?<=[.!?])\s+|\n", body)
                    if not re.search(r"\b(not|cannot|can't|unaffected|ignores?|except)\b", x))
    apporte = [tag for tag, rx in _RULES if re.search(rx, body)]
    profite = [k for k, lab in PROFITE.items() if re.search(lab + r":\s*(?!N/A)\S", head)]
    m = re.search(r"\|\s*(?:\d+|N/A)\s+(\d+)", head)
    desc = re.search(r"\|\s*(?:\d+|N/A)\s+\d+[^|]*\|\s*(.+?)(Introduced in|\|)", head, re.S)
    # capacité canalisée : elle consomme de l'énergie tant qu'elle est maintenue (il faut une vraie source d'énergie)
    canal = bool(desc and re.search(r"\bchannel", desc.group(1), re.I))
    return {"apporte": apporte, "profite_de": profite, "cout": int(m.group(1)) if m else None, "canalisee": canal,
            "stats_cles": stats_cles(head, body),
            "helminth": "Subsumable to Helminth" in head, "fiabilite": "probable",
            "resume": re.sub(r"\s+", " ", desc.group(1)).strip()[:240] if desc else ""}
