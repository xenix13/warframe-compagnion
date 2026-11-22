"""Mode rapide et nettoyage des réponses (sans base ni modèle)."""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from wfcompanion import fastmode, optimizer
from wfcompanion.agent import _clean_answer


class Fast(unittest.TestCase):
    def test_build_requests(self):
        self.assertTrue(fastmode.wants_build("propose moi un build levelcap atlas", True))
        self.assertTrue(fastmode.wants_build("fais plutôt la variante persistence", True))
        self.assertFalse(fastmode.wants_build("pourquoi Rubble Heap ?", True))
        self.assertFalse(fastmode.wants_build("où farmer Rubble Heap ?", True))
        self.assertFalse(fastmode.wants_build("build level cap", False))  # pas de warframe connue

    def test_defense(self):
        self.assertEqual(fastmode.defense_of("avec arcane persistence"), "persistence")
        self.assertEqual(fastmode.defense_of("plutôt défense bouclier", "persistence"), "bouclier")
        self.assertEqual(fastmode.defense_of("build atlas", "persistence"), "persistence")

    def test_tidy(self):
        self.assertEqual(fastmode._tidy("VARIANTE BOUCLIER (jeu de XeniX13) : Brief Respite protège (XeniX13, 21/11/2026)"),
                         "Brief Respite protège")

    def test_pick_archetype(self):
        arch = {"archetypes": [{"id": "dps", "nom": "Nuke", "objectif": "dégâts level cap"},
                               {"id": "farm", "nom": "Farm", "objectif": "farm de ressources"}]}
        self.assertEqual(optimizer.pick_archetype(arch, "je veux farmer des ressources")["id"], "farm")
        self.assertEqual(optimizer.pick_archetype(arch, "un build quelconque")["id"], "dps")

    def test_clean_answer(self):
        t = "| A | B |\n\nStatut : complet et valide\nLe système a confirmé.\nPetrify assure le contrôle de foule."
        out = _clean_answer(t, False)
        self.assertNotIn("système", out); self.assertIn("contrôle de foule", out); self.assertIn("| A | B |", out)


if __name__ == "__main__":
    unittest.main()


class Levels(unittest.TestCase):
    def test_detect(self):
        from wfcompanion import niveaux
        self.assertEqual(niveaux.detect("je veux un build débutant"), "debutant")
        self.assertEqual(niveaux.detect("un build pour palier, début du steel path"), "intermediaire")
        self.assertEqual(niveaux.detect("build level cap"), "endgame")
        self.assertIsNone(niveaux.detect("build atlas"))

    def test_answers(self):
        from wfcompanion import niveaux
        self.assertEqual(niveaux.parse_answers("oui pour le reactor mais pas de corrompus", ["reacteur", "corrompus"]),
                         {"reacteur": True, "corrompus": False})
        self.assertEqual(niveaux.parse_answers("non", ["reacteur", "corrompus"]), {"reacteur": False, "corrompus": False})
        self.assertEqual(niveaux.parse_answers("j'ai le helminth mais pas d'arcanes", ["helminth", "arcanes", "syndicats"]),
                         {"helminth": True, "arcanes": False})

    def test_rules(self):
        from wfcompanion import niveaux
        r = niveaux.rules("debutant", {"reacteur": False})
        self.assertEqual(r["formas"], 0); self.assertFalse(r["helminth"]); self.assertNotIn("rare", r["access"])
        self.assertIn("rare", niveaux.rules("endgame", {})["access"])
