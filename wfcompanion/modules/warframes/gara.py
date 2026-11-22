"""Module de Gara : seulement ce qui a été relu. Le reste vient de la lecture automatique du wiki (fiabilité « probable »).

Relu par XeniX13 le 22/11/2026.
"""

FRAME = "Gara"

# étiquettes ajoutées à celles tirées automatiquement du wiki (sans les remplacer)
AJOUTS = {
    # la barrière de verre de Mass Vitrify compte comme un objet créé : elle déclenche Arcane Sculptor
    "Mass Vitrify": ["cree_objet"],
}

PIEGES = ["Arcane Sculptor marche grâce à la barrière de Mass Vitrify : valable si le build relance souvent son 4."]
