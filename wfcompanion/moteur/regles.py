"""Règles du moteur, communes à toutes les frames : objectifs, besoins, synergies.

C'est ici qu'est écrite la « réflexion » : ce qu'un objectif demande, et quelles étiquettes se renforcent entre elles.
Une règle a une fiabilité (confirmé / probable) et une phrase d'explication, réutilisée telle quelle pour le joueur.
Corriger une mécanique du jeu = corriger une règle ici, une seule fois.
"""
import re

from .etiquettes import APPORTS

# --- objectifs : reconnus dans la demande du joueur, dans cet ordre
OBJECTIFS = [
    ("eidolon", r"eidolon|teralyst|gantulyst|hydrolyst|tridolon|plaines? d'eidolon"),
    ("boss", r"\bboss|archon(te)?s?\b|chasse|mono[- ]?cible|eidolon|profit[- ]?taker"),
    ("farm", r"\bfarm|ressources?|butin|loot|survie longue"),
    ("soutien", r"\bsoutien|support|buff|heal|soign"),
    ("tank", r"\btank|survie|survivre|défense|defense|increvable|tenir"),
    ("degats", r"\bnuke|dps|dégâts|degats|tuer|level ?cap|steel path|clear"),
]
# build centré sur les armes du loadout (principale, secondaire, mêlée) : reconnu par ces mots ou par un nom d'arme
ARMES = r"\barmes?\b|\bprimaire|\bprincipale|\bsecondaire|\bm[êe]l[ée]e\b|\bmelee\b|\bfusil|\bpistolet|\bplate-?forme d'armes?|\bweapon"
LABEL = {"eidolon": "chasse aux Eidolons", "armes": "plateforme d'armes", "degats": "dégâts", "tank": "tank", "farm": "farm et contrôle", "soutien": "soutien", "boss": "boss et mono-cible"}

# ce que la capacité centrale doit apporter selon l'objectif (par ordre de préférence)
CENTRALE = {"eidolon": ["bonus_armes", "bonus_degats", "vulnerabilite"], "armes": ["bonus_armes", "bonus_degats", "vulnerabilite", "retrait_armure", "controle"], "degats": ["degats"], "boss": ["degats"], "tank": ["reduction_degats", "invulnerabilite", "overguard", "armure_bonus"],
            "farm": ["controle", "butin"], "soutien": ["soutien", "energie", "reduction_degats", "soin", "bonus_degats"]}

# besoins d'un build complet (les quatre exigences du joueur) : nom -> (étiquettes qui le remplissent, poids, phrase)
SURVIE = ["reduction_degats", "invulnerabilite", "invisibilite", "esquive", "overguard", "armure_bonus", "controle", "soin"]
# survie « dure » : ce qui protège vraiment ; une frame qui n'a que de l'esquive ou du contrôle prend une fenêtre
# d'invulnérabilité en plus (Rolling Guard en Exilus) : elle n'esquivera pas tout
SURVIE_DURE = ["reduction_degats", "invulnerabilite", "overguard", "armure_bonus"]
BESOINS = {
    "survie": (SURVIE, 3.0, "la frame doit survivre seule"),
    "energie": (["energie"], 2.0, "la frame doit être autonome en énergie"),
    "passer_armure": (["retrait_armure", "vulnerabilite", "bonus_degats"], 2.0, "à haut niveau, les dégâts doivent passer l'armure"),
}
BESOINS_OBJECTIF = {"eidolon": ["survie"], "armes": ["survie", "energie", "passer_armure"], "degats": ["survie", "energie", "passer_armure"], "boss": ["survie", "energie", "passer_armure"],
                    "tank": ["survie", "energie"], "farm": ["survie", "energie"], "soutien": ["survie", "energie"]}

# un candidat lu automatiquement (« probable ») compte un peu moins qu'un candidat relu (« confirmé »)
FIABILITE = {"confirmé": 1.0, "probable": 0.8, "à vérifier": 0.6}
# Helminth lu automatiquement : ses étiquettes sont souvent bruitées (notes du wiki) ; un Helminth relu passe devant
FIABILITE_HELMINTH = {"confirmé": 1.0, "probable": 0.6, "à vérifier": 0.5}

# le manque comblé compte en plus de la synergie (retrait d'armure : 1.2 + 2.0 quand rien ne passe l'armure)
# capacités qui ne peuvent pas coexister sur une même frame (relu par XeniX13 ; liste à compléter) :
# si le kit garde l'une, le Helminth ne peut pas en être une autre du même groupe
EXCLUSIFS = [{"Roar", "Eclipse", "Xata's Whisper"}]


def exclusif(a, b):
    """Vrai si les capacités a et b ne peuvent pas coexister."""
    return a != b and any(a in g and b in g for g in EXCLUSIFS)


# --- synergies : (étiquette apportée par le candidat, étiquette de la capacité centrale, bonus, phrase)
SYNERGIES = [
    ("vulnerabilite", "degats", 2.0, "rend les ennemis plus vulnérables aux dégâts de {c}"),
    # statut Feu : -50 % d'armure seulement ; un vrai retrait (Terrify, Pillage, Abating Link…) vaut mieux à haut niveau
    ("feu", "arme", 1.0, "le statut Feu des capacités alimente Arcane Hot Shot et l'héritage de chaleur des armes"),
    ("retrait_armure_partiel", "degats", 0.6, "le statut Feu retire 50 % de l'armure : aide {c}, sans valoir un vrai retrait"),
    ("retrait_armure_partiel", "arme", 0.6, "le statut Feu retire 50 % de l'armure : aide les armes, sans valoir un vrai retrait"),
    ("retrait_armure", "degats", 1.2, "retire l'armure, donc les dégâts de {c} passent mieux à haut niveau"),
    ("bonus_degats", "degats", 1.8, "augmente les dégâts de {c}"),
    # bonus réservé aux armes : ne sert que si le build frappe avec des armes (étiquette « arme ») :
    # arme exaltée donnée par la capacité centrale, ou armes du loadout (principale, secondaire, mêlée) au centre du build
    ("bonus_armes", "arme", 1.8, "augmente les dégâts des armes que le build utilise"),
    ("bonus_degats", "arme", 0.0, ""),  # déjà compté sur « degats » ; listé pour mémoire : Roar sert aussi les armes
    ("vulnerabilite", "arme", 1.5, "rend les ennemis plus vulnérables aux armes"),
    ("retrait_armure", "arme", 1.2, "retire l'armure, donc les armes passent mieux à haut niveau"),
    ("controle", "arme", 0.5, "immobilise les ennemis pour les armes"),
    ("reduction_degats", "arme", 0.6, "protège pendant que les armes font le travail"),
    ("overguard", "arme", 0.6, "protège pendant que les armes font le travail"),
    ("invisibilite", "arme", 0.6, "rend invisible pendant que les armes font le travail (bonus furtif)"),
    ("compagnon", "arme", 0.2, "le bonus profite aussi au compagnon"),
    ("compagnon", "degats", 0.2, "le bonus profite aussi au compagnon"),
    ("controle", "degats", 0.7, "immobilise les ennemis pendant que {c} les tue"),
    ("controle", "zone", 0.3, "regroupe ou fige les ennemis dans la zone de {c}"),
    # Nourish : le Viral ne passe sur une capacité que si elle a une chance de statut (pas garanti)
    ("bonus_viral", "statut", 1.6, "ajoute du Viral à {c}, qui peut infliger des statuts (chance, pas garanti)"),
    ("bonus_viral", "arme", 1.6, "ajoute du Viral aux armes que le build utilise"),
    ("bonus_puissance", "puissance", 0.8, "augmente un peu la puissance (buff temporaire), donc {c}"),
    ("cree_objet", "efficacite_arcane", 0.6, "crée un objet : déclenche Arcane Sculptor (efficacité)"),
    ("energie_x", "degats", 0.8, "multiplie l'énergie des orbes pour relancer {c} (ne crée pas d'énergie)"),
    ("energie", "degats", 0.5, "redonne de l'énergie pour relancer {c}"),
    ("reduction_degats", "degats", 0.6, "protège pendant que {c} fait le travail"),
    ("overguard", "degats", 0.6, "protège pendant que {c} fait le travail"),
    ("invisibilite", "degats", 0.4, "rend invisible pendant que {c} fait le travail"),
    ("armure_bonus", "armure", 1.0, "donne de l'armure, qui renforce {c}"),
    # tank : une couche de survie différente complète la capacité centrale (réduction + soin, etc.)
    ("soin", "reduction_degats", 0.8, "soigne pendant que {c} réduit les dégâts : les deux se complètent"),
    ("controle", "reduction_degats", 0.4, "immobilise les ennemis : {c} encaisse moins"),
    ("overguard", "reduction_degats", 0.6, "ajoute une Overguard par-dessus la réduction de {c}"),
]

# arcanes de warframe : étiquettes, niveau d'accès minimal (voir niveaux.py), défense requise
ARCANES = {
    "Molt Augmented": {"apporte": ["bonus_degats"], "profite": "puissance", "phrase": "puissance de capacité qui monte avec les kills"},
    "Arcane Energize": {"apporte": ["energie"], "phrase": "redonne de l'énergie à toi et à l'escouade"},
    "Arcane Persistence": {"apporte": ["reduction_degats"], "defense": "persistence", "phrase": "dégâts subis plafonnés, mais retire tout le bouclier : à jouer avec une armure correcte"},
    "Arcane Aegis": {"apporte": ["bouclier"], "defense": "bouclier", "phrase": "rend du bouclier quand il est touché"},
    "Arcane Fury": {"apporte": ["bonus_degats"], "melee": True, "phrase": "dégâts de mêlée en plus sur critique"},
    "Arcane Battery": {"apporte": ["energie"], "armure": True, "phrase": "énergie maximale selon l'armure (ne régénère pas)"},
    "Arcane Sculptor": {"apporte": ["energie"], "phrase": "175 % d'efficacité pendant 12 s après avoir créé un objet avec une capacité"},
    "Arcane Expertise": {"apporte": ["bouclier"], "phrase": "la puissance s'applique aussi au bouclier max (frame qui vit de son bouclier)"},
    "Arcane Bellicose": {"apporte": ["bonus_degats"], "phrase": "puissance en plus selon la santé max (frame à beaucoup de santé)"},
    "Arcane Hot Shot": {"apporte": ["bonus_armes"], "phrase": "chances de critique des armes quand les capacités infligent le statut Feu"},
    "Arcane Avenger": {"apporte": ["bonus_armes"], "phrase": "chances de critique en plus quand on est touché"},
    "Molt Efficiency": {"apporte": ["energie"], "profite": "duree", "phrase": "durée et efficacité qui montent avec les kills"},
}


def objectif_of(message):
    t = (message or "").lower()
    for key, rx in OBJECTIFS:
        if re.search(rx, t): return key
    return "degats"


def armes_centrales(tb, message, frame=""):
    """Le build est-il centré sur les armes du loadout ? (mots de la demande, ou nom d'une arme cité)"""
    t = (message or "").lower()
    if re.search(ARMES, t): return True
    for r in tb.con.execute("SELECT name FROM weapons WHERE type != 'Exalted Weapon'"):
        n = r["name"].lower()
        if len(n) >= 4 and n not in frame.lower() and re.search(r"\b" + re.escape(n) + r"\b", t): return True
    return False


def covered(tags, need):
    return any(t in tags for t in BESOINS[need][0])


def synergy(cand_tags, central_tags, central_name):
    """Bonus et phrases des règles qui relient un candidat à la capacité centrale.
    Une étiquette du candidat ne compte qu'une fois (la règle la plus forte) : un build qui frappe à la fois avec une
    capacité et avec une arme exaltée ne compte pas deux fois la même vulnérabilité."""
    best = {}
    for a, b, bonus, phrase in SYNERGIES:
        if a in cand_tags and b in central_tags and bonus and bonus > best.get(a, (0, ""))[0]:
            best[a] = (bonus, phrase.format(c=central_name))
    ranked = sorted(best.values(), key=lambda x: -x[0])
    return sum(b for b, _ in ranked), [p for _, p in ranked]


def APPORTS_LABEL(tags):
    """Étiquettes en français, pour les phrases montrées au joueur."""
    return [APPORTS.get(t, t) for t in tags]
