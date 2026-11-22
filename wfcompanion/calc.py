"""Moteur de calcul : les formules validées, en code, pour que l'agent ne calcule jamais « de tête ».

Chaque fonction cite sa source (page du wiki de la base ou mesure en jeu de XeniX13).
Les pourcentages sont passés en fractions : +90 % -> 0.9.
"""
import math, re

# ---------------------------------------------------------------- critiques
def crit_multiplier(base, relative=(), absolute=()):
    """Multiplicateur critique M = base x (1 + somme des bonus relatifs) + somme des bonus absolus.
    Source : page Critical Hit. Vérifié en jeu : Shattered Lash 3,2x -> 5,0x avec Organ Shatter (+0,9)."""
    return base * (1 + sum(relative)) + sum(absolute)


def crit_tier_multiplier(m, tier):
    """Multiplicateur d'un critique de niveau n (jaune = 1, orange = 2, rouge = 3) : 1 + n x (M - 1). Page Critical Hit."""
    return 1 + tier * (m - 1)


def crit_tiers(chance):
    """Probabilités des niveaux de critique pour une chance > 100 % (ex. 1.3 -> 70 % jaune, 30 % orange)."""
    low = math.floor(chance)
    frac = chance - low
    out = {}
    if 1 - frac > 0: out[low] = 1 - frac
    if frac > 0: out[low + 1] = frac
    return out


def average_crit_factor(chance, m):
    """Facteur moyen de dégâts dû aux critiques (espérance sur les niveaux)."""
    return sum(p * (crit_tier_multiplier(m, t) if t > 0 else 1.0) for t, p in crit_tiers(chance).items())


# ---------------------------------------------------------------- armure
def enemy_armor_dr(armor):
    """Réduction de dégâts d'un ennemi : 90 % x racine(armure / 2700) jusqu'à 2700, plafonnée à 90 %. Page Armor."""
    armor = max(0.0, armor)
    return 0.9 * math.sqrt(min(armor, 2700) / 2700)


def armor_strip_multiplier(armor, strip):
    """Gain de dégâts quand on retire une fraction strip de l'armure (0.5 = 50 %).
    À 2700 d'armure : 24 % -> x2,15 ; 50 % -> x3,64 ; 80 % -> x5,98 ; 100 % -> x10."""
    before = 1 - enemy_armor_dr(armor)
    after = 1 - enemy_armor_dr(armor * (1 - strip))
    return after / before


def player_armor_dr(armor):
    """Réduction de dégâts d'un joueur : armure / (armure + 300). Page Damage Reduction."""
    return armor / (armor + 300)


def effective_health(health, armor=0.0, shield=0.0, extra_dr=0.0):
    """PV effectifs : (santé / (1 - DR armure)) / (1 - autres DR) + bouclier. Les DR multiplicatives se combinent."""
    return health / (1 - player_armor_dr(armor)) / (1 - extra_dr) + shield


# ---------------------------------------------------------------- shield gating
def shield_gate_duration(shield, catalyzing=False):
    """Durée du shield gate (s) à bouclier plein. Page Shield.
    < 53 : S/180 + 1/3 ; 53 à 1150 : (S/350)^0,65 + 1/3 ; au-delà : 2,5 s. Catalyzing Shields : 1,33 s."""
    if catalyzing:
        return 1.33
    if shield < 53:
        return shield / 180 + 1 / 3
    if shield <= 1150:
        return (shield / 350) ** 0.65 + 1 / 3
    return 2.5


# ---------------------------------------------------------------- capacités
def ability_stat(bonuses=(), base=1.0):
    """Puissance, durée, portée ou efficacité totale : base + somme des bonus (additifs). 1.83 = 183 %."""
    return base + sum(bonuses)


def ability_cost(base_cost, efficiency):
    """Coût en énergie : coût de base x (2 - efficacité), au minimum 25 % du coût de base (efficacité 175 %).
    Source : pages Abilities et Energy, confirmé en jeu par XeniX13 (100 d'énergie -> 155 à 45 % d'efficacité).
    C'est un coût fixe propre à la capacité : il ne dépend pas de l'énergie max de la frame."""
    return base_cost * max(0.25, 2 - efficiency)


def energy_rank30(power_rank0):
    """ATTENTION : règle vérifiée sur une seule frame (Gara Prime : données 175 -> 225 en jeu, et 225 x 2,85 = 641
    affiché). Elle ne colle pas forcément aux autres frames : ne pas l'utiliser sans vérifier dans l'arsenal."""
    return power_rank0 + 50


def channel_drain(base_drain, efficiency=1.0, duration=1.0):
    """Drain par seconde d'une capacité canalisée : drain de base x (2 - efficacité) / durée.
    Page Abilities : le coût dans le temps est réduit par la durée et par l'efficacité. Le total (2 - eff) / durée
    ne descend pas sous 25 % du drain de base."""
    return base_drain * max(0.25, (2 - efficiency) / duration)


def channel_total_cost(initial, base_drain, seconds, efficiency=1.0, duration=1.0, growth=1.0):
    """Énergie totale pour lancer puis canaliser `seconds` secondes.
    growth > 1 : le drain est multiplié par ce facteur à chaque seconde (ex. Gaseous Quake : 1,2).
    Vérifié sur le wiki : Gaseous Quake sans mod, 10 s -> 100 + 16 x (1,2^0 + ... + 1,2^10) = environ 614."""
    d = channel_drain(base_drain, efficiency, duration)
    ticks = int(seconds) + 1
    total = d * ticks if growth == 1 else d * (growth ** ticks - 1) / (growth - 1)
    return ability_cost(initial, efficiency) + total


def max_energy(base, bonuses=()):
    """Énergie max = base x (1 + bonus). Ex. Gara Prime : 225 x 2,85 = 641,25."""
    return base * (1 + sum(bonuses))


def violet_shard_crit_bonus(tauforged, max_energy_value):
    """Fragment violet, dégâts critiques de mêlée : +25 % (+37,5 % tauforgé), doublé si l'énergie max dépasse 500."""
    b = 0.375 if tauforged else 0.25
    return b * 2 if max_energy_value > 500 else b


# ---------------------------------------------------------------- farm
def tries_for(probability_per_try, confidence=0.5):
    """Nombre de tirages pour avoir `confidence` de chances d'obtenir l'objet : ln(1 - conf) / ln(1 - p)."""
    p = probability_per_try
    if p >= 1: return 1
    return math.ceil(math.log(1 - confidence) / math.log(1 - p))


# ---------------------------------------------------------------- lecture des effets de mods
STAT_NAMES = {
    "ability strength": "strength", "ability duration": "duration", "ability range": "range",
    "ability efficiency": "efficiency", "critical damage": "crit_damage", "critical chance": "crit_chance",
    "status chance": "status_chance", "health": "health", "shield capacity": "shield", "armor": "armor",
    "energy max": "energy", "melee damage": "melee_damage", "damage": "damage", "multishot": "multishot",
    "fire rate": "fire_rate", "attack speed": "attack_speed", "range": "melee_range", "casting speed": "cast_speed",
    "toxin": "toxin", "heat": "heat", "cold": "cold", "electricity": "electricity", "slash": "slash",
    "puncture": "puncture", "impact": "impact", "status duration": "status_duration",
    "magazine capacity": "magazine", "reload speed": "reload_speed", "melee range": "melee_range",
}
_EFFECT = re.compile(r"^([+-]?\d+(?:\.\d+)?)(%?)\s+(.+?)\s*$")
_CONDITIONAL = re.compile(r"\b(on|while|when|for \d+s|per|stacks?|after|if|during)\b", re.I)


def parse_effect(text):
    """'+99% Ability Strength' -> ('strength', 0.99). Renvoie None pour un effet conditionnel ou inconnu
    (l'agent doit alors le traiter à part au lieu de l'additionner aveuglément)."""
    t = text.strip()
    if _CONDITIONAL.search(t):
        return None
    m = _EFFECT.match(t)
    if not m:
        return None
    val, pct, name = float(m.group(1)), m.group(2), m.group(3).lower().rstrip(".")
    name = re.sub(r"\s*\(.*\)$", "", name)
    key = STAT_NAMES.get(name)
    if not key:
        return None
    if not pct and key in ("health", "shield", "armor", "energy"):  # « +30 Shield Capacity » : valeur fixe, pas +3000 %
        return key + "_flat", val
    return key, (val / 100 if pct else val)


def parse_mod_effects(effects):
    """Liste de textes d'effets -> (stats additionnables, effets non interprétés)."""
    stats, rest = {}, []
    for e in effects:
        for part in re.split(r"\s*;\s*|\\n|\n", e):
            if not part.strip(): continue
            r = parse_effect(part)
            if r: stats[r[0]] = stats.get(r[0], 0) + r[1]
            else: rest.append(part.strip())
    return stats, rest
