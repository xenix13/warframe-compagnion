"""Tests du moteur de calcul sur des valeurs validées (wiki ou mesures en jeu de XeniX13).
Lancer : python -m unittest discover -s tests
"""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from wfcompanion import calc as c


class Crit(unittest.TestCase):
    def test_arsenal_gara_organ_shatter(self):
        # mesuré en jeu : 3,2x avant, 5,0x après Organ Shatter (+90 %)
        self.assertAlmostEqual(c.crit_multiplier(2, [0.6]), 3.2)
        self.assertAlmostEqual(c.crit_multiplier(2, [0.6, 0.9]), 5.0)

    def test_full_stack_estimate(self):
        # violet doublé 0,75 + Galvanized Steel 4 cumuls 1,20 + Organ Shatter 0,90
        self.assertAlmostEqual(c.crit_multiplier(2, [0.75, 1.2, 0.9]), 7.7)

    def test_tiers(self):
        self.assertAlmostEqual(c.crit_tier_multiplier(7.7, 2), 14.4)
        t = c.crit_tiers(1.3)
        self.assertAlmostEqual(t[1], 0.7); self.assertAlmostEqual(t[2], 0.3)

    def test_violet_shard(self):
        self.assertAlmostEqual(c.violet_shard_crit_bonus(True, 641), 0.75)
        self.assertAlmostEqual(c.violet_shard_crit_bonus(True, 500), 0.375)  # 500 ne suffit pas, il faut 501


class Armor(unittest.TestCase):
    def test_strip_multipliers_at_2700(self):
        for strip, expected in [(0.24, 2.15), (0.5, 3.64), (0.8, 5.98), (1.0, 10.0)]:
            self.assertAlmostEqual(c.armor_strip_multiplier(2700, strip), expected, places=2)

    def test_player_dr(self):
        self.assertAlmostEqual(c.player_armor_dr(300), 0.5)


class Shield(unittest.TestCase):
    def test_continuity(self):
        self.assertAlmostEqual(c.shield_gate_duration(52.999), c.shield_gate_duration(53), places=2)
        self.assertAlmostEqual(c.shield_gate_duration(1150), 2.5, places=2)
        self.assertEqual(c.shield_gate_duration(5000), 2.5)


class Abilities(unittest.TestCase):
    def test_gara_config_a(self):
        # Puissance 183 % = 100 + 44 (Umbral Intensify) + 99 (Blind Rage) - 60 (Overextended)
        self.assertAlmostEqual(c.ability_stat([0.44, 0.99, -0.60]), 1.83)
        # Portée 235 % = 100 + 45 (Stretch) + 90 (Overextended) ; portée de la Pique : 12 x 2,35 + 3 = 31,2 m
        r = c.ability_stat([0.45, 0.90])
        self.assertAlmostEqual(12 * r + 3, 31.2)
        self.assertAlmostEqual(c.max_energy(c.energy_rank30(175), [1.85]), 641.25)

    def test_cost_formula(self):
        self.assertAlmostEqual(c.ability_cost(50, 0.45), 77.5)
        self.assertAlmostEqual(c.ability_cost(100, 1.75), 25)
        self.assertAlmostEqual(c.ability_cost(100, 2.0), 25)  # plafond : 25 % du coût


class Channel(unittest.TestCase):
    def test_gaseous_quake_wiki(self):
        # wiki : 100 + environ 514 = 614 d'énergie pour 10 s, sans mod
        self.assertAlmostEqual(c.channel_total_cost(100, 16, 10, growth=1.2), 614.4, places=0)

    def test_duration_and_efficiency_reduce_drain(self):
        self.assertAlmostEqual(c.channel_drain(16, 1.0, 2.0), 8)
        self.assertAlmostEqual(c.channel_drain(16, 0.45, 1.0), 24.8)


class Farm(unittest.TestCase):
    def test_tries(self):
        self.assertEqual(c.tries_for(0.0759, 0.5), 9)


class Effects(unittest.TestCase):
    def test_parse(self):
        s, rest = c.parse_mod_effects(["+99% Ability Strength ; -60% Ability Efficiency"])
        self.assertAlmostEqual(s["strength"], 0.99); self.assertAlmostEqual(s["efficiency"], -0.60)
        self.assertEqual(rest, [])

    def test_conditional_left_aside(self):
        s, rest = c.parse_mod_effects(["+40% Critical Chance per Combo Multiplier"])
        self.assertEqual(s, {}); self.assertEqual(len(rest), 1)


if __name__ == "__main__":
    unittest.main()
