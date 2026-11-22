"""Module d'Atlas : seulement ce qui est propre à Atlas. Le reste (énergie, survie, mods, Helminth) vient du moteur.

Relu par XeniX13 le 21-22/11/2026 (défense par le bouclier, Umbra, Nourish). Fiabilité indiquée ligne par ligne.
"""

FRAME = "Atlas"

# étiquettes relues : elles remplacent celles tirées automatiquement du wiki
CAPACITES = {
    "Landslide": {"apporte": ["degats", "zone", "mobilite", "invulnerabilite", "controle"],
                  "profite_de": ["puissance", "portee", "combo", "melee"], "fiabilite": "confirmé",
                  "note": "dégâts multipliés par le combo de capacité (jusqu'à 12x) ; invulnérable pendant la ruée"},
    "Petrify": {"apporte": ["controle", "vulnerabilite", "zone"], "valeurs": {"vulnerabilite": 0.5},
                "profite_de": ["duree", "portee"], "fiabilite": "confirmé",
                "note": "+50 % de dégâts subis sur les pétrifiés ; source principale de Rubble"},
    "Tectonics": {"apporte": ["degats", "zone", "controle"], "profite_de": ["puissance", "armure"], "fiabilite": "probable",
                  "note": "mur et rocher ; sert peu la boucle de Landslide"},
    "Rumblers": {"apporte": ["degats", "controle", "zone"], "profite_de": ["puissance", "duree", "sante", "armure"],
                 "fiabilite": "confirmé", "note": "l'invocation pétrifie autour d'Atlas"},
}

# passif : ce qu'il apporte au build (compte pour les besoins)
PASSIF = {"apporte": ["armure_bonus", "soin"], "fiabilite": "confirmé",
          "texte": "les ennemis pétrifiés lâchent du Rubble : soin, puis armure en plus (jusqu'à 1 500, compte pour Arcane Battery)"}

# augments : capacité visée et ce qu'ils apportent ; « cle » = indispensable à la boucle quand la capacité est centrale
AUGMENTS = {
    "Rubble Heap": {"pour": "Landslide", "apporte": ["energie", "bonus_degats"], "cle": True, "fiabilite": "confirmé",
                    "texte": "au-dessus de 1 400 Rubble, Landslide ne coûte rien et fait 2x dégâts"},
    "Path Of Statues": {"pour": "Landslide", "apporte": ["controle", "vulnerabilite"], "fiabilite": "confirmé",
                        "texte": "Landslide laisse une traînée qui pétrifie : plus de Rubble et de vulnérabilité"},
    "Rumbled": {"pour": "Rumblers", "apporte": ["overguard"], "cle": True, "fiabilite": "probable",
                "texte": "Atlas devient un Rumbler avec une Overguard (jusqu'à 300 % de sa santé max)"},
    "Ore Gaze": {"pour": "Petrify", "apporte": ["butin"], "cle": True, "fiabilite": "confirmé",
                 "texte": "ennemis pétrifiés : 25 % de chance de butin en plus"},
}

# capacité centrale imposée selon l'objectif (sinon le moteur choisit)
CENTRALE = {"degats": "Landslide", "boss": "Landslide", "tank": "Rumblers", "farm": "Petrify"}

# boucle de jeu par capacité centrale (sinon le moteur la décrit à partir des étiquettes)
BOUCLES = {
    "Landslide": ["Petrify (ou Path Of Statues) fige un groupe : +50 % de dégâts subis.",
                  "Landslide tue les pétrifiés : le Rubble fait monter l'armure jusqu'à 1 500.",
                  "Au-dessus de 1 400 Rubble, Rubble Heap rend Landslide gratuit et 2x plus fort.",
                  "Relancer Landslide toutes les 5 s fait monter le combo de capacité jusqu'à 12x (dégâts, Blood Rush, Weeping Wounds)."],
}

# capacités à garder même si le moteur ne les juge pas utiles (elles servent la boucle)
NE_PAS_REMPLACER = {"Landslide": ["Petrify"]}

# mods de l'arme exaltée quand la capacité centrale la donne
ARME_EXALTEE = {"Landslide": {"nom": "Landslide Fists", "mods": ["Blood Rush", "Weeping Wounds", "Primed Pressure Point", "Organ Shatter"]}}

# défense retenue par le joueur qui a relu le module
DEFENSE = "bouclier"

PIEGES = ["Fury et les mods d'attaque lourde ne servent à rien sur Landslide.",
          "Le Rubble soigne avant de donner de l'armure : blessé, l'armure ne monte pas.",
          "L'armure de Rubble baisse de 5/s : il faut un flux continu d'ennemis pétrifiés."]
