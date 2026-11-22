"""Polarités et capacité (wiki, page Mods, « Drain & Polarity ») — commun aux warframes, armes et compagnons.

- Mod sur une polarité qui correspond : coût divisé par 2, arrondi au supérieur (Serration 14 -> 7).
- Mod sur une polarité qui ne correspond pas : coût + 25 %, arrondi mathématiquement (+1 pour 2-5, +2 pour 6-9, +3 pour 10-13…).
- Aura (et posture d'arme de mêlée) : elle DONNE de la capacité. Polarité qui correspond : apport x2 (7 -> 14) ;
  polarité qui ne correspond pas : apport - 25 %, arrondi mathématiquement (7 -> 5) ; emplacement sans polarité : apport normal.
- Polarité universelle (« any », Omni Forma) : correspond à tout, sauf Umbra.

Les warframes, armes et compagnons ont des polarités déjà posées. place() les utilise d'abord, et n'ajoute un forma que si
le build ne rentre pas, sur l'emplacement où il fait gagner le plus de capacité.
"""
import math


def _quarter(x):
    return math.floor(x / 4 + 0.5)  # 25 % arrondi mathématiquement (0,5 vers le haut)


def matches(slot, pol):
    if not slot or not pol: return False
    return slot == pol or (slot == "any" and pol != "umbra")


def mod_cost(cost, slot, pol):
    """Coût d'un mod de coût `cost` et de polarité `pol` sur un emplacement de polarité `slot`."""
    if not slot: return cost
    if matches(slot, pol): return math.ceil(cost / 2)
    return cost + _quarter(cost)


def aura_bonus(bonus, slot, pol):
    """Capacité apportée par une aura (ou une posture) d'apport `bonus` sur un emplacement de polarité `slot`."""
    if not slot: return bonus
    if matches(slot, pol): return bonus * 2
    return bonus - _quarter(bonus)


def place(mods, base_pols, capacity, n_slots=8):
    """mods : [(nom, coût, polarité)] ; base_pols : polarités déjà posées sur les emplacements.
    Renvoie {emplacements: [{polarite_origine, polarite, mod, cout, forma}], cout, formas}."""
    slots = [{"polarite_origine": p, "polarite": p, "mod": None, "cout": 0, "forma": False}
             for p in (list(base_pols or []) + [None] * n_slots)[:n_slots]]
    todo = sorted(mods, key=lambda m: -m[1])
    rest = []
    # 1. les mods les plus chers prennent d'abord les polarités qui leur correspondent
    for m in todo:
        s = next((s for s in slots if s["mod"] is None and matches(s["polarite"], m[2])), None)
        if s: s.update(mod=m[0], cout=mod_cost(m[1], s["polarite"], m[2]), _m=m)
        else: rest.append(m)
    # 2. puis les emplacements sans polarité (pas de pénalité), les plus chers d'abord
    rest2 = []
    for m in rest:
        s = next((s for s in slots if s["mod"] is None and not s["polarite"]), None)
        if s: s.update(mod=m[0], cout=m[1], _m=m)
        else: rest2.append(m)
    # 3. les mods qui restent vont sur les polarités qui ne correspondent pas (les moins chers y perdent le moins)
    for m in sorted(rest2, key=lambda m: m[1]):
        s = next((s for s in slots if s["mod"] is None), None)
        if s: s.update(mod=m[0], cout=mod_cost(m[1], s["polarite"], m[2]), _m=m)
    # 4. formas, seulement si ça ne rentre pas : là où le gain est le plus grand
    formas = 0
    while sum(s["cout"] for s in slots) > capacity:
        best, gain = None, 0
        for s in slots:
            m = s.get("_m")
            if not m or not m[2] or matches(s["polarite"], m[2]): continue
            g = s["cout"] - math.ceil(m[1] / 2)
            if g > gain: best, gain = s, g
        if not best: break
        m = best["_m"]
        best.update(polarite=m[2], cout=math.ceil(m[1] / 2), forma=True); formas += 1
    for s in slots: s.pop("_m", None)
    return {"emplacements": slots, "cout": sum(s["cout"] for s in slots), "formas": formas}
