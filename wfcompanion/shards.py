"""Fragments d'Archonte : 5 emplacements par warframe. Valeurs de la page « Archon Shard » du wiki (base, 13/11/2026).

Chaque bonus : (couleur, libellé, clé, valeur normale, valeur tauforgée, nature)
nature : "rel" = s'ajoute aux bonus des mods (puissance, durée...) ; "flat" = valeur fixe ajoutée après tous les bonus ;
"arme" = bonus d'arme ; "texte" = effet conditionnel ou utilitaire, affiché mais pas calculé.
"""

SHARDS = [
    ("Crimson", "puissance", "strength", 0.10, 0.15, "rel"),
    ("Crimson", "durée", "duration", 0.10, 0.15, "rel"),
    ("Crimson", "dégâts critiques de mêlée", "melee_crit_damage", 0.25, 0.375, "arme"),
    ("Crimson", "chance de statut principale", "primary_status", 0.25, 0.375, "arme"),
    ("Crimson", "chance critique secondaire", "secondary_crit", 0.25, 0.375, "arme"),
    ("Amber", "vitesse de lancement", "cast_speed", 0.25, 0.375, "texte"),
    ("Amber", "efficacité des orbes d'énergie", "energy_orbs", 0.50, 0.75, "texte"),
    ("Amber", "efficacité des orbes de santé", "health_orbs", 1.00, 1.50, "texte"),
    ("Amber", "énergie au départ", "energy_spawn", 0.30, 0.45, "texte"),
    ("Amber", "vitesse de parkour", "parkour", 0.15, 0.225, "texte"),
    ("Azure", "santé", "health_flat", 150, 225, "flat"),
    ("Azure", "bouclier", "shield_flat", 150, 225, "flat"),
    ("Azure", "énergie max", "energy_flat", 50, 75, "flat"),
    ("Azure", "armure", "armor_flat", 150, 225, "flat"),
    ("Azure", "régénération de santé", "health_regen", 5, 7.5, "texte"),
    ("Violet", "dégâts critiques de mêlée (doublés au-dessus de 500 d'énergie max)", "violet_melee_crit", 0.25, 0.375, "arme"),
    ("Violet", "électricité principale", "primary_electricity", 0.30, 0.45, "arme"),
    ("Violet", "dégâts des capacités sur cibles électrisées", "ability_dmg_electric", 0.10, 0.15, "texte"),
    ("Violet", "énergie par orbe de santé", "violet_equilibrium", 0.20, 0.30, "texte"),
    ("Emerald", "dégâts des statuts Toxine", "toxin_status", 0.30, 0.45, "texte"),
    ("Emerald", "soin par statut Toxine", "toxin_heal", 2, 3, "texte"),
    ("Emerald", "dégâts des capacités sur cibles corrodées", "ability_dmg_corrosive", 0.10, 0.15, "texte"),
    ("Emerald", "cumuls de Corrosion max", "corrosion_stacks", 2, 3, "texte"),
    ("Topaz", "santé max par kill Blast", "blast_health", 1, 2, "texte"),
    ("Topaz", "bouclier par kill Blast", "blast_shield", 5, 7.5, "texte"),
    ("Topaz", "chance critique secondaire par kill sous Chaleur", "heat_secondary_crit", 0.01, 0.015, "texte"),
    ("Topaz", "dégâts des capacités sur cibles irradiées", "ability_dmg_radiation", 0.10, 0.15, "texte"),
]
COLORS_FR = {"crimson": "rouge", "amber": "ambre", "azure": "azur", "violet": "violet", "emerald": "émeraude", "topaz": "topaze"}


def labels():
    out = []
    for color, lab, _, v, vt, _ in SHARDS:
        fr = COLORS_FR[color.lower()]
        out.append(f"{fr} : {lab}")
        out.append(f"{fr} tauforgé : {lab}")
    return out


def parse(text):
    """'rouge tauforgé : puissance' -> (clé, valeur, nature, libellé). None si inconnu."""
    t = (text or "").strip().lower()
    if not t: return None
    taufo = "tauforg" in t
    for color, lab, key, v, vt, kind in SHARDS:
        fr = COLORS_FR[color.lower()]
        if (fr in t or color.lower() in t) and lab.split(" (")[0].lower() in t:
            return key, (vt if taufo else v), kind, f"{fr}{' tauforgé' if taufo else ''} : {lab}"
    return None


def apply(shards):
    """Liste de textes -> (bonus par clé, erreurs, lignes lisibles)."""
    bonus, errors, rows = {}, [], []
    if len(shards) > 5: errors.append(f"{len(shards)} fragments : 5 au maximum")
    for s in shards[:5]:
        p = parse(s)
        if not p:
            errors.append(f"fragment « {s} » inconnu ; exemples : « rouge tauforgé : puissance », « azur : bouclier »"); continue
        key, val, kind, lab = p
        bonus[key] = bonus.get(key, 0) + val
        rows.append((lab, kind, val))
    return bonus, errors, rows
