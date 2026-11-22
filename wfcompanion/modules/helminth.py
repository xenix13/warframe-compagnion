"""Capacités du Helminth les plus utilisées, avec des étiquettes relues (elles servent à toutes les frames).

Les pages du wiki décrivent chaque capacité avec beaucoup de détails (notes, astuces, interactions) : la lecture
automatique y trouve des étiquettes en trop. Pour les capacités les plus choisies, les étiquettes sont écrites ici.
Les autres sont lues dans la phrase de résumé de leur page (fiabilité « probable »).
Corriger une capacité du Helminth = corriger sa ligne ici. « frame » : frame d'origine, quand sa page n'est pas dans la base.
"""

CAPACITES = {
    # relu par XeniX13 : Roar augmente tous les dégâts (armes ET capacités) et touche les alliés, compagnon compris
    "Roar": {"apporte": ["bonus_degats", "bonus_armes", "soutien", "compagnon"], "profite_de": ["puissance", "duree"],
             "note": "bonus multiplicatif sur tous les dégâts (armes et capacités), aussi pour l'escouade et le compagnon"},
    "Xata's Whisper": {"apporte": ["bonus_armes"], "profite_de": ["puissance", "duree"],
                       "note": "dégâts Void en plus sur les armes seulement"},
    # relu par XeniX13 : Eclipse ne marche que sur les armes
    "Eclipse": {"apporte": ["bonus_armes", "reduction_degats"], "profite_de": ["puissance", "duree"],
                "note": "lumière : dégâts en plus sur les armes seulement ; ombre : réduction des dégâts subis"},
    "Pillage": {"apporte": ["retrait_armure", "bouclier", "soutien"], "profite_de": ["puissance", "portee"],
                "note": "retire bouclier et armure des ennemis proches, recharge ton bouclier, retire les statuts"},
    # relu par XeniX13 : le bonus Viral marche sur les capacités, mais seulement celles qui ont une chance de statut
    # (pas un statut garanti) ; il marche aussi sur les armes
    # relu par XeniX13 : le soin de Nourish ne marche que sur Grendel, pas en Helminth
    "Nourish": {"apporte": ["energie_x", "bonus_viral", "soutien", "compagnon"], "profite_de": ["puissance", "duree"],
                "note": "multiplie l'énergie reçue (orbe de 50 -> 100 à x2) ; bonus Viral sur les armes et sur les capacités "
                        "qui ont une chance de statut ; touche aussi les alliés et le compagnon ; ne crée pas d'énergie ; pas de soin en Helminth"},
    # relu par XeniX13 : le Helminth de Nokko est le choix principal de Banshee nuke pour l'énergie, avec Arcane Sculptor
    "Brightbonnet": {"frame": "Nokko", "apporte": ["energie", "bonus_puissance", "soutien", "cree_objet"],
                     "profite_de": ["puissance", "duree", "portee"],
                     "note": "champignon qui donne de l'énergie et de la puissance à toi et aux alliés ; c'est un objet créé, "
                             "donc il déclenche Arcane Sculptor"},
    "Gloom": {"apporte": ["controle", "soin", "zone"], "profite_de": ["puissance", "portee"],
              "note": "ralentit les ennemis autour, vol de vie sur les dégâts infligés ; canalisé"},
    "Thermal Sunder": {"apporte": ["degats", "zone", "controle", "statut"], "profite_de": ["puissance", "portee"]},
    "Fire Blast": {"apporte": ["degats", "zone", "retrait_armure_partiel", "feu", "statut"], "profite_de": ["puissance", "portee"],
                   "note": "le statut Feu retire 50 % de l'armure (pas un retrait complet)"},
    # relu par XeniX13 : Helminth de Sirius, statut Feu (-50 % d'armure, héritage de la chaleur), déclenche Arcane Hot Shot
    "Coronal Ejection": {"frame": "Sirius & Orion", "apporte": ["degats", "statut", "feu", "retrait_armure_partiel"],
                         "profite_de": ["puissance", "portee"], "note": "dégâts de Feu : statut Feu (-50 % d'armure), Arcane Hot Shot, Archon Vitality"},
    # relu par XeniX13 : Helminth de Caliban, contrôle et plus de dégâts sur les cibles prises
    "Sentient Wrath": {"frame": "Caliban", "apporte": ["controle", "zone", "vulnerabilite"], "profite_de": ["puissance", "duree", "portee"]},
    # relu par XeniX13 : Helminth d'Oberon ; son augment Smite Infusion ajoute de la Radiation aux armes (chasse aux Eidolons)
    "Smite": {"frame": "Oberon", "apporte": ["degats", "statut", "radiation"], "profite_de": ["puissance"]},
    "Terrify": {"apporte": ["controle", "retrait_armure", "zone"], "profite_de": ["puissance", "duree", "portee"]},
    "Breach Surge": {"apporte": ["controle", "degats", "zone"], "profite_de": ["puissance", "duree", "portee"]},
    "Dispensary": {"apporte": ["energie", "soin", "soutien"], "profite_de": ["duree"]},
    "Empower": {"apporte": ["bonus_degats"], "profite_de": [],
                "note": "la capacité suivante a +50 % de puissance (coûte de la santé et de l'énergie)"},
    "Silence": {"apporte": ["controle", "zone"], "profite_de": ["duree", "portee"]},
    "Larva": {"apporte": ["controle", "zone"], "profite_de": ["duree", "portee"]},
    "Ensnare": {"apporte": ["controle", "zone"], "profite_de": ["duree", "portee"]},
    "Spectral Scream": {"apporte": ["degats", "zone", "statut"], "profite_de": ["puissance", "portee"]},
    "Resonating Quake": {"apporte": ["degats", "zone", "controle"], "profite_de": ["puissance", "portee"]},
    "Shooting Gallery": {"apporte": ["controle", "bonus_degats", "soutien"], "profite_de": ["puissance", "duree"]},
    "Well Of Life": {"apporte": ["soin", "soutien"], "profite_de": ["puissance", "duree"]},
    "Hallowed Ground": {"apporte": ["degats", "zone", "soutien", "immunite_statut"], "profite_de": ["puissance", "duree", "portee"],
                        "note": "immunité aux statuts dans la zone"},
    "Marked For Death": {"apporte": ["degats", "zone"], "profite_de": ["puissance", "portee"]},
    "Infested Mobility": {"apporte": ["mobilite"], "profite_de": ["duree"]},
    "Elemental Ward": {"apporte": ["soutien"], "profite_de": ["puissance", "duree", "portee"],
                       "note": "effet selon l'élément de la frame"},
}
