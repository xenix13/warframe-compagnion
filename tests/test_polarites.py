"""Polarités : règles du wiki (page Mods) et exemples donnés par XeniX13."""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from wfcompanion import polarites as P


class Polarites(unittest.TestCase):
    def test_aura(self):
        self.assertEqual(P.aura_bonus(7, "madurai", "madurai"), 14)   # polarité qui correspond : x2
        self.assertEqual(P.aura_bonus(7, "vazarin", "madurai"), 5)    # qui ne correspond pas : -25 % arrondi
        self.assertEqual(P.aura_bonus(7, None, "madurai"), 7)         # emplacement sans polarité

    def test_mod(self):
        self.assertEqual(P.mod_cost(14, "madurai", "madurai"), 7)
        self.assertEqual(P.mod_cost(5, "vazarin", "madurai"), 6)      # 2-5 : +1
        self.assertEqual(P.mod_cost(9, "vazarin", "madurai"), 11)     # 6-9 : +2
        self.assertEqual(P.mod_cost(10, "vazarin", "madurai"), 13)    # 10-13 : +3
        self.assertEqual(P.mod_cost(14, "vazarin", "madurai"), 18)    # 14-16 : +4
        self.assertEqual(P.mod_cost(10, "any", "naramon"), 5)

    def test_place_uses_existing_polarities_first(self):
        mods = [("A", 14, "madurai"), ("B", 10, "vazarin"), ("C", 6, "naramon")]
        r = P.place(mods, ["madurai", "vazarin"], 60)
        self.assertEqual(r["formas"], 0); self.assertEqual(r["cout"], 7 + 5 + 6)

    def test_forma_only_when_needed(self):
        mods = [(str(i), 14, "madurai") for i in range(8)]
        r = P.place(mods, [], 60)
        self.assertEqual(r["cout"] <= 60, True); self.assertGreater(r["formas"], 0)
        self.assertTrue(all(s["forma"] == (s["polarite"] != s["polarite_origine"]) for s in r["emplacements"]))


if __name__ == "__main__":
    unittest.main()


class StatsCles(unittest.TestCase):
    def test_range_counts(self):
        from wfcompanion.moteur import etiquettes as et
        self.assertEqual(et.stats_cles("Range:15 m (grab radius) 3 / 4 / 5 / 6 (max weapons)\n\nMisc: x", ""), ["portee"])
        self.assertEqual(et.stats_cles("", "the maximum number of weapons is affected by ability range."), ["portee"])
        self.assertEqual(et.stats_cles("Range:10 / 11 / 12 / 14 m (cone length)\n\nMisc: x", ""), [])

    def test_player_says_range_max(self):
        from wfcompanion import pilote
        self.assertTrue(any(__import__("re").search(p.format(s=pilote.STAT_FR["portee"]), "plus il a de portée plus il a d'armes")
                            for p in pilote.STAT_MAX))
