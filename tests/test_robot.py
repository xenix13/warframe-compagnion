"""Robot scripté : tests sur la base de test (ignorés si elle n'est pas là)."""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.environ.get("WF_TESTRUN", os.path.join(os.path.dirname(__file__), "..", "..", "testrun"))


@unittest.skipUnless(os.path.exists(os.path.join(ROOT, "companion-data", "warframe.sqlite")), "base de test absente")
class Robot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from wfcompanion.tools import Toolbox
        d = os.path.join(ROOT, "companion-data")
        cls.tb = Toolbox(os.path.join(d, "warframe.sqlite"), os.path.join(d, "docs.sqlite"), os.path.join(ROOT, "base"))

    def test_atlas_level_cap(self):
        from wfcompanion import optimizer
        r = optimizer.propose(self.tb, "Atlas Prime", "build level cap")
        b = r["build"]
        self.assertIn("Rubble Heap", b["mods"]); self.assertIn("Umbral Intensify", b["mods"])
        self.assertEqual(b["aura"], "Brief Respite"); self.assertEqual(b["defense"], "bouclier")
        w = b["armes"]["exaltees"][0]["mods"]
        self.assertIn("Blood Rush", w); self.assertIn("Weeping Wounds", w)
        self.assertNotEqual(b["helminth"], ""); self.assertNotIn("Petrify", r["archetype"]["helminth_remplace"] or "")

    def test_nourish_is_not_an_energy_source(self):
        from wfcompanion.moteur import robot
        self.assertNotIn("energie", robot.helminth_tags(self.tb, "Nourish", "Helminth")["apporte"])

    def test_generic_frame(self):
        from wfcompanion.moteur import robot
        p = robot.plan(self.tb, "Banshee", "build dégâts")
        self.assertEqual(p["fiabilite"], "probable"); self.assertTrue(p["boucle_de_jeu"])
        self.assertNotEqual(p["helminth_remplace"], p["capacite_centrale"])

    def test_weapon_only_buffs(self):
        from wfcompanion.moteur import robot
        # Eclipse ne boost que les armes : inutile pour Sound Quake, utile si le build joue les armes du loadout
        nuke = dict(robot.plan(self.tb, "Banshee", "build dégâts")["helminth_options"])
        guns = dict(robot.plan(self.tb, "Banshee", "build pour jouer mes armes")["helminth_options"])
        self.assertLess(nuke.get("Eclipse", 0), guns.get("Eclipse", 0))
        boss = robot.plan(self.tb, "Banshee", "build boss avec mon fusil")
        self.assertEqual(boss["capacite_centrale"], "Sonar")

    def test_banshee_nuke_nokko_sculptor(self):
        from wfcompanion import optimizer
        r = optimizer.propose(self.tb, "Banshee", "build nuke")
        self.assertEqual(r["build"]["helminth"], "Brightbonnet")
        self.assertIn("Arcane Sculptor", r["build"]["arcanes"])
        self.assertEqual(r["validation"]["statut"], "complet et valide")

    def test_gara_nourish_equilibrium(self):
        from wfcompanion.moteur import robot
        p = robot.plan(self.tb, "Gara", "build nuke")
        self.assertEqual(p["helminth"], "Nourish"); self.assertIn("Equilibrium", p["noyau"]["mods"])
        # Arcane Sculptor reste proposé en option grâce à la barrière de Mass Vitrify
        self.assertTrue(any("Arcane Sculptor" in o for c in p["choix"] for o in c["options"]))

    def test_exclusive_buffs(self):
        from wfcompanion.moteur import robot
        for msg in ("build xaku prime plateforme d'armes", "build xaku prime nuke"):
            p = robot.plan(self.tb, "Xaku Prime", msg)
            if p["helminth_remplace"] != "Xata's Whisper":
                self.assertNotIn(p["helminth"], ("Roar", "Eclipse"))
        v = self.tb.valider_build({"warframe": "Xaku Prime", "helminth": "Eclipse", "helminth_remplace": "The Lost"})
        self.assertTrue(any("coexister" in e for e in v["erreurs"]))


if __name__ == "__main__":
    unittest.main()
