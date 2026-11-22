"""Pilote agent <-> robot : avec un faux modèle qui répond en JSON (ignoré si la base de test est absente)."""
import json, os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.environ.get("WF_TESTRUN", os.path.join(os.path.dirname(__file__), "..", "..", "testrun"))


class FakeApp:
    def __init__(self, tb, replies):
        self.tb, self.replies, self.base = tb, list(replies or []), tempfile.mkdtemp()
        self.chat_fn = (lambda m, t: {"content": self.replies.pop(0) if self.replies else '{"verdict": "ok"}'}) if replies is not None else None


@unittest.skipUnless(os.path.exists(os.path.join(ROOT, "companion-data", "warframe.sqlite")), "base de test absente")
class Pilote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from wfcompanion.tools import Toolbox
        d = os.path.join(ROOT, "companion-data")
        cls.tb = Toolbox(os.path.join(d, "warframe.sqlite"), os.path.join(d, "docs.sqlite"), os.path.join(ROOT, "base"))

    def test_sans_modele(self):
        from wfcompanion import pilote
        r = pilote.construire(FakeApp(self.tb, None), "Gara", "build tank avec splinter storm sans Nourish", None, "endgame", {}, [])
        self.assertEqual(r["demande"]["capacite_centrale"], "Splinter Storm")
        self.assertNotEqual(r["build"]["helminth"], "Nourish")

    def test_relecture_corrige(self):
        from wfcompanion import pilote
        replies = ['{"objectif": "tank", "capacite_centrale": "Splinter Storm", "imposes": [], "interdits": []}',
                   '```json\n{"verdict": "corriger", "corrections": [{"element": "helminth", "retirer": null, "mettre": "Gloom", "raison": "tank : soin"}]}\n```',
                   '{"verdict": "ok"}']
        app = FakeApp(self.tb, replies); trace = []
        r = pilote.construire(app, "Gara", "je veux tanker", None, "endgame", {}, trace)
        self.assertEqual(r["build"]["helminth"], "Gloom")
        self.assertTrue(os.path.exists(os.path.join(app.base, "04-retours-experience", "relectures.jsonl")))

    def test_noms_inventes_ignores(self):
        from wfcompanion import pilote
        replies = ['{"objectif": "tank"}', '{"verdict": "corriger", "corrections": [{"element": "helminth", "mettre": "Super Laser"}]}']
        r = pilote.construire(FakeApp(self.tb, replies), "Gara", "build tank", None, "endgame", {}, [])
        self.assertEqual(r["validation"]["statut"], "complet et valide")

    def test_retouche(self):
        from wfcompanion import pilote
        app = FakeApp(self.tb, None)
        last = pilote.construire(app, "Gara", "build nuke", None, "endgame", {}, [])
        r = pilote.retoucher(app, "Gara", "remplace Nourish par Roar", None, "endgame", {}, last, [])
        self.assertEqual(r["build"]["helminth"], "Roar")


if __name__ == "__main__":
    unittest.main()
