"""Teste la boucle de l'agent avec un faux modèle (aucun Ollama requis)."""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from wfcompanion.agent import Agent


class FakeTools:
    def __init__(self): self.calls = []
    def call(self, name, args):
        self.calls.append((name, args)); return {"ok": True}


class Loop(unittest.TestCase):
    def test_tool_then_answer(self):
        script = iter([
            {"role": "assistant", "content": "", "tool_calls": [{"function": {"name": "ou_farmer", "arguments": {"objet": "X"}}}]},
            {"role": "assistant", "content": "", "tool_calls": [{"function": {"name": "calculer", "arguments": '{"operation": "tirages"}'}}]},
            {"role": "assistant", "content": "fini"}])
        tb = FakeTools()
        a = Agent(tb, lambda m, t: next(script))
        self.assertEqual(a.ask("?"), "fini")
        self.assertEqual(tb.calls, [("ou_farmer", {"objet": "X"}), ("calculer", {"operation": "tirages"})])
        self.assertEqual([m["role"] for m in a.messages], ["system", "user", "assistant", "tool", "assistant", "tool", "assistant"])

    def test_stops_after_max_rounds(self):
        tb = FakeTools()
        def chat(m, tools):
            if not tools: return {"role": "assistant", "content": "réponse forcée"}
            return {"role": "assistant", "content": "", "tool_calls": [{"function": {"name": "fiche_mod", "arguments": {}}}]}
        self.assertEqual(Agent(tb, chat).ask("?"), "réponse forcée")
        self.assertEqual(len(tb.calls), 1)  # les appels identiques ne sont pas rejoués

    def test_empty_answer_is_retried(self):
        script = iter([{"role": "assistant", "content": "", "thinking": "je réfléchis"},
                       {"role": "assistant", "content": "voilà"}])
        a = Agent(FakeTools(), lambda m, t: next(script))
        self.assertEqual(a.ask("?"), "voilà")

    def test_no_second_round_of_questions(self):
        seen = []
        def chat(m, tools):
            seen.append(m[-1]["content"]); return {"role": "assistant", "content": "Quel contenu vises-tu ?"}
        a = Agent(FakeTools(), chat)
        a.ask("un build banshee"); a.ask("steel path")
        self.assertNotIn("Rappel du système", seen[0]); self.assertIn("N'en pose plus", seen[1])


if __name__ == "__main__":
    unittest.main()
