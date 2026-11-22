"""Interface de build locale : http://localhost:8765

    python -m wfcompanion.web --base "E:\\IA\\warframe\\base-warframe" [--model gemma4:12b] [--api-url ... --model ...]

Le navigateur affiche le constructeur ; le serveur réutilise exactement les mêmes outils que l'agent
(base SQLite, moteur de calcul, contrôle des builds). La discussion passe par l'agent (Ollama ou IA en ligne).
"""
import traceback
import argparse, datetime, json, os, re, sys, threading, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from . import agent as ag, cloud, fastmode, loadouts, niveaux, optimizer

STATIC = os.path.join(os.path.dirname(__file__), "static")
LOCK = threading.Lock()  # un seul accès à la base et au modèle à la fois


class App:
    def __init__(self, base, data, chat_fn, ctx_box=None, ctx_tokens=16384):
        self.base, self.tb = base, ag.open_toolbox(base, data)
        self.chat_fn, self.ctx_box, self.ctx_tokens = chat_fn, ctx_box, ctx_tokens
        self.model_label, self.topic, self.fast_state, self.online = None, None, {}, False
        self.agent = self._new_agent() if chat_fn else None
        self.trace = []
        self.saves = os.path.join(base, "06-builds-joueur")

    def _log(self, t): self.trace.append(t)

    def _new_agent(self):
        a = ag.Agent(self.tb, self.chat_fn, log=self._log)
        a.ctx_box = self.ctx_box
        a.ctx_tokens = self.ctx_box["n"] if self.ctx_box else self.ctx_tokens
        return a

    # ---------- données pour les sélecteurs
    def warframes(self):
        return [r["name"] for r in self.tb.con.execute(
            "SELECT name FROM warframes WHERE type = 'Warframe' ORDER BY name")]

    def frame(self, name):
        f = self.tb.fiche_warframe(name)
        if "erreur" in f: return f
        r = self.tb.con.execute("SELECT data FROM warframes WHERE name = ? COLLATE NOCASE", (f["nom"],)).fetchone()
        w = json.loads(r["data"])
        f["image"] = w.get("imageName")
        f["exaltees_detail"] = self.tb.armes_exaltees(f["nom"])
        return f

    def polarities(self, kind, name):
        """Polarités déjà posées d'une arme ou d'un compagnon (pour l'éditeur)."""
        table = {"arme": "weapons", "compagnon": "companions"}.get(kind)
        if not table: return {"erreur": "type inconnu"}
        r = self.tb.con.execute(f"SELECT data FROM {table} WHERE name = ? COLLATE NOCASE", (re.sub(r" \(.*\)$", "", name),)).fetchone()
        if not r: return {"mods": [], "exilus": None, "posture": None}
        w = json.loads(r["data"])
        return {"mods": w.get("polarities") or [], "exilus": w.get("exilusPolarity"), "posture": w.get("stancePolarity"),
                "aura": w.get("aura")}

    def mods(self, slot, frame, q=""):
        base_name = re.sub(r"\s+(Prime|Umbra)$", "", frame or "")
        if slot == "aura": where, args = "compat = 'AURA'", []
        elif slot == "exilus": where, args = "compat = 'WARFRAME' AND is_exilus = 1", []
        else: where, args = "(compat = 'WARFRAME' OR compat = ? COLLATE NOCASE) AND compat != 'AURA'", [base_name]
        if q: where += " AND name LIKE ?"; args.append(f"%{q}%")
        out, seen = [], set()
        for r in self.tb.con.execute(f"SELECT data FROM mods WHERE type = 'Warframe Mod' AND {where} ORDER BY name", args):
            m = json.loads(r["data"]); c = self.tb._mod_card(m)
            av = c.get("avertissement", "")
            if "ATTENTION" in av or "affaiblie" in av or c["nom"] in seen: continue
            seen.add(c["nom"])
            out.append({"nom": c["nom"], "polarite": c.get("polarite"), "cout": c["cout_rang_max"], "rarete": c.get("rarete"),
                        "effets": c["effets_rang_max"], "augment": bool(c.get("augment_de")), "image": m.get("imageName"),
                        "set": c.get("set")})
        out.sort(key=lambda x: (not x["augment"], x["nom"]))
        return out

    def options(self, cat):
        return self.tb.options(cat)

    def weapons(self, cat, q=""):
        return self.tb.chercher_armes(cat, "critique", q or None, 400)

    def weapon_mods(self, arme, exilus):
        return self.tb.mods_arme(arme, exilus)

    def validate(self, build):
        return self.tb.valider_build(build)

    def chat(self, message, build):
        self.trace = []
        ctx = ""
        named = self._frame_named(message)
        if named: self.topic = named
        if not getattr(self, "topic", None) and build and build.get("warframe"): self.topic = _frame_base(build["warframe"])
        try:  # mode rapide (build calculé par le programme) : seulement pour un petit modèle local
            fast = fastmode.handle(self, message)  # builds : agent + robot (JSON), aussi en ligne
        except Exception as e:
            print(f"[mode rapide] erreur : {e}", file=sys.stderr); fast = None
        if fast:
            self.turns = getattr(self, "turns", []) + [{"role": "user", "content": message}, {"role": "assistant", "content": fast["reponse"]}]
            return fast
        if getattr(self, "small_model", False) and self.chat_fn:
            # petit modèle : pas d'agent à outils (prompt trop long pour lui) ; réponse courte tirée de la base
            return self._answer_from_docs(message)
        if not self.agent:
            return {"erreur": "aucun modèle configuré : lance l'interface avec --model (Ollama) ou --api-url (IA en ligne). "
                              "Sans modèle, seules les demandes de build (« build Atlas level cap ») fonctionnent."}
        shown = _frame_base((build or {}).get("warframe") or "")
        topic = getattr(self, "topic", None)
        if build and shown and (not topic or topic.lower() == shown.lower()):
            ctx = ("\n\n(Build affiché dans l'interface, à utiliser si la question le concerne : "
                   + json.dumps(build, ensure_ascii=False) + ")")
        # sinon le build de l'éditeur est celui d'une autre warframe : on ne le donne pas, même son nom égare un petit modèle
        try:
            answer = self.agent.ask(message + ctx)
        except Exception as e:
            print(f"[discussion] erreur : {e}", file=sys.stderr)
            return {"erreur": str(e), "trace": self.trace}
        self.turns = getattr(self, "turns", []) + [{"role": "user", "content": message}, {"role": "assistant", "content": answer}]
        return {"reponse": answer, "trace": self.trace, "build_propose": _last_build(_this_turn(self.agent.messages, message))}

    DOC_PROMPT = ("Tu es le compagnon Warframe du joueur. Réponds en français, en 3 à 8 phrases simples, uniquement à partir "
                  "des extraits de la base fournis. Si les extraits ne contiennent pas la réponse, dis-le en une phrase et "
                  "propose de demander un build. N'invente aucun chiffre.")

    def _answer_from_docs(self, message):
        """Question hors build avec un petit modèle : recherche dans la base, puis un seul appel court."""
        hits = self.tb.chercher_doc(message).get("resultats") or []
        ctx = "\n\n".join(f"[{h['titre']}] {h['extrait']}" for h in hits[:3])
        msgs = [{"role": "system", "content": self.DOC_PROMPT},
                {"role": "user", "content": f"Extraits de la base :\n{ctx or '(aucun extrait trouvé)'}\n\nQuestion : {message}"}]
        try:
            ans = (self.chat_fn(msgs, None).get("content") or "").strip()
        except Exception as e:
            return {"erreur": str(e)}
        ans = re.sub(r"<think>.*?</think>", "", ans, flags=re.S).strip()
        if hits: ans += "\n\n*Sources : " + ", ".join(dict.fromkeys(h["fichier"] for h in hits[:3])) + "*"
        self.turns = getattr(self, "turns", []) + [{"role": "user", "content": message}, {"role": "assistant", "content": ans}]
        return {"reponse": ans, "trace": [f"  [base] {len(hits)} extrait(s) ; réponse courte du petit modèle"]}

    def _frame_named(self, text):
        """Warframe citée dans le message du joueur (nom de base, sans Prime/Umbra), la plus longue s'il y en a plusieurs."""
        if not hasattr(self, "_frames"):
            self._frames = sorted({_frame_base(r[0]) for r in self.tb.con.execute("SELECT name FROM warframes")}, key=len, reverse=True)
        for n in self._frames:
            if re.search(r"\b" + re.escape(n) + r"\b", text, re.I): return n
        return None

    def generate(self, warframe, objectif="", defense=None, archetype=None, niveau="endgame"):
        """Bouton « Générer » de l'interface : le build vient du code, l'explication du modèle s'il y en a un."""
        self.topic = _frame_base(warframe)
        self.fast_state = {"base": self.topic, "warframe": warframe, "defense": defense, "objectif": objectif, "niveau": niveau}
        r = optimizer.propose(self.tb, warframe, objectif, defense, archetype, niveau, niveaux.load_profile(self.base))
        if "erreur" in r: return r
        self.fast_state["archetype"] = r["archetype"]["id"]; self.last_gen = r
        b = r["build"]
        names = [b["aura"], b["exilus"]] + b["mods"] + [m for e in (b.get("armes") or {}).get("exaltees", []) for m in e["mods"]]
        eff = {}
        for n in names:
            c = self.tb.fiche_mod(n) if n else {"erreur": 1}
            if "erreur" not in c: eff[n] = {"effets": c["mods"][-1]["effets_rang_max"], "image": None}
        for n in b["arcanes"]:
            hit = [x for x in self.tb.fiche_arcane(n).get("arcanes", []) if x["nom"].lower() == n.lower()]
            if hit:
                e = hit[0]["effet_rang_max"]; e = e if isinstance(e, list) else [e]
                eff[n] = {"effets": [x.replace(" +1 Arcane Revive", "") for x in e if x.strip() != "+1 Arcane Revive"]}
        f = self.frame(b["warframe"])
        if self.agent:  # une question qui suit dans la discussion porte sur ce build
            self.agent.messages += [{"role": "user", "content": f"Build généré pour {b['warframe']} ({r['archetype']['nom']})."},
                                    {"role": "assistant", "content": "(build calculé : " + json.dumps(b, ensure_ascii=False) + ")"}]
        return {"build": b, "archetype": r["archetype"], "autres": r.get("autres_objectifs", []),
                "choix": r["choix_compares"], "hypotheses": r["hypotheses"], "relu": r["archetype_relu"],
                "validation": r["validation"], "effets": eff, "image": f.get("image") if isinstance(f, dict) else None,
                "explication": fastmode.fallback_text(r), "modele": bool(self.chat_fn),
                "niveau": r.get("niveau"), "a_viser_ensuite": r.get("a_viser_ensuite"), "defense_raison": r.get("defense_raison")}

    def explain(self):
        r = getattr(self, "last_gen", None)
        if not r: return {"erreur": "génère d'abord un build"}
        trace = []
        t = fastmode.explain(self, r, f"build {r['build']['warframe']} : {r['archetype']['nom']}", trace)
        return {"explication": t, "trace": trace} if t else {"erreur": "le modèle n'a pas répondu", "trace": trace}

    def archetypes(self, warframe):
        a = self.tb.archetypes(warframe)
        if "erreur" in a: return {"archetypes": []}
        return {"archetypes": [{"id": x.get("id"), "nom": x.get("nom"), "objectif": x.get("objectif")} for x in a.get("archetypes", [])],
                "relu": bool(a.get("relu_par_le_joueur"))}

    def reset(self):
        self.topic = None; self.fast_state = {}
        if self.agent: self.agent = self._new_agent()
        return {"ok": True}

    # ---------- loadouts
    def loadout_list(self):
        return loadouts.list_all(self.base)

    def loadout_open(self, name):
        d = loadouts.load(self.base, name)
        if not d: return {"erreur": f"aucun loadout « {name} »"}
        v = d["versions"][-1]
        ch = loadouts.changes(self.tb, self.base, v["build"], v.get("instantane") or {})
        self.active = name
        if self.agent:  # l'agent repart avec le contexte du loadout et la fin de son ancienne conversation
            self.agent = self._new_agent()
            self.topic = _frame_base(d["versions"][-1]["build"].get("warframe") or "") or None
            self.agent.messages.append({"role": "user", "content": f"(Contexte, ne réponds pas : le joueur a ouvert son loadout « {name} », "
                                        f"version {v['version']} du {v['date'][:10]}. Build : {json.dumps(v['build'], ensure_ascii=False)}. "
                                        f"Synthèse : {v.get('synthese') or 'aucune'}. Changements depuis la sauvegarde : {json.dumps(ch, ensure_ascii=False)})"})
            self.agent.messages.append({"role": "assistant", "content": "Compris, j'ai le loadout en tête."})
            for m in (d.get("conversation") or [])[-8:]:
                self.agent.messages.append({"role": m["role"], "content": m["content"]})
        self.turns = []
        return {"loadout": d, "changements": ch}

    def loadout_save(self, name, build, synthese, raison):
        val = self.tb.valider_build(build)
        r = loadouts.save(self.tb, self.base, name, build, synthese, raison, getattr(self, "turns", []), val)
        self.turns = []; self.active = name
        return {**r, "statut_du_build": val.get("statut")}

    def loadout_synthese(self, build):
        if not self.agent: return {"erreur": "aucun modèle configuré : la synthèse est écrite par l'agent (lancer avec --model)"}
        self.trace = []
        msg = loadouts.SYNTH_PROMPT + "\n\nBuild : " + json.dumps(build, ensure_ascii=False)
        try: txt = self.agent.ask(msg)
        except Exception as e: return {"erreur": str(e)}
        return {"synthese": txt, "trace": self.trace}

    def loadout_update(self, name):
        if not self.agent: return {"erreur": "aucun modèle configuré : lancer avec --model"}
        d = loadouts.load(self.base, name)
        if not d: return {"erreur": f"aucun loadout « {name} »"}
        v = d["versions"][-1]
        ch = loadouts.changes(self.tb, self.base, v["build"], v.get("instantane") or {})
        self.trace = []
        try: ans = self.agent.ask(loadouts.update_prompt(name, d, ch))
        except Exception as e: return {"erreur": str(e)}
        return {"reponse": ans, "changements": ch, "trace": self.trace, "build_propose": _last_build(self.agent.messages)}

    def save(self, build, title):
        os.makedirs(self.saves, exist_ok=True)
        name = re.sub(r"[^\w\- ]", "", f"{build.get('warframe', 'build')} - {title or datetime.date.today().isoformat()}").strip()
        path = os.path.join(self.saves, name + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"titre": title, "date": datetime.date.today().isoformat(), "build": build}, f, ensure_ascii=False, indent=1)
        return {"ok": True, "fichier": os.path.relpath(path, self.base)}

    def saved(self):
        if not os.path.isdir(self.saves): return []
        out = []
        for f in sorted(os.listdir(self.saves)):
            if f.endswith(".json"):
                try:
                    with open(os.path.join(self.saves, f), encoding="utf-8") as fh: out.append({"fichier": f, **json.load(fh)})
                except (OSError, json.JSONDecodeError): pass
        return out


def _frame_base(name):
    return re.sub(r"\s+(Prime|Umbra)$", "", name.strip())


def _this_turn(messages, message):
    """Messages produits depuis la dernière question du joueur : un ancien build ne doit pas recharger l'éditeur."""
    for i in range(len(messages) - 1, -1, -1):
        m = messages[i]
        if m.get("role") == "user" and (m.get("content") or "").startswith(message[:200]): return messages[i:]
    return []


def _last_build(messages):
    """Dernier build passé à valider_build par l'agent : l'interface peut le charger d'un clic."""
    for m in reversed(messages):
        for c in m.get("tool_calls") or []:
            fn = c.get("function", {})
            if fn.get("name") == "valider_build":
                a = fn.get("arguments") or {}
                if isinstance(a, str):
                    try: a = json.loads(a)
                    except json.JSONDecodeError: continue
                b = a.get("build", a if "warframe" in a else None)  # un petit modèle oublie souvent l'enveloppe « build »
                if isinstance(b, str):
                    try: b = json.loads(b)
                    except json.JSONDecodeError: b = None
                if isinstance(b, dict) and b.get("warframe"): return b
    return None


def handler(app):
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a): pass

        def _send(self, obj, code=200, ctype="application/json; charset=utf-8"):
            body = obj if isinstance(obj, bytes) else json.dumps(obj, ensure_ascii=False).encode("utf-8")
            self.send_response(code); self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")  # l'interface à jour s'affiche sans vider le cache du navigateur
            self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)

        def do_GET(self):
            u = urlparse(self.path); q = {k: v[0] for k, v in parse_qs(u.query).items()}
            if u.path in ("/", "/index.html"):
                with open(os.path.join(STATIC, "index.html"), "rb") as f:
                    return self._send(f.read(), ctype="text/html; charset=utf-8")
            routes = {"/api/warframes": lambda: app.warframes(), "/api/frame": lambda: app.frame(q.get("nom", "")),
                      "/api/mods": lambda: app.mods(q.get("slot", "mod"), q.get("frame", ""), q.get("q", "")),
                      "/api/options": lambda: app.options(q.get("cat", "")),
                      "/api/weapons": lambda: app.weapons(q.get("cat", ""), q.get("q", "")),
                      "/api/weapon_mods": lambda: app.weapon_mods(q.get("arme", ""), q.get("exilus") == "1"),
                      "/api/pols": lambda: app.polarities(q.get("kind", ""), q.get("nom", "")),
                      "/api/saved": lambda: app.saved(),
                      "/api/loadouts": lambda: app.loadout_list(),
                      "/api/loadout": lambda: app.loadout_open(q.get("nom", "")),
                      "/api/archetypes": lambda: app.archetypes(q.get("frame", "")),
                      "/api/status": lambda: {"modele": app.model_label}}
            fn = routes.get(u.path)
            if not fn: return self._send({"erreur": "introuvable"}, 404)
            with LOCK:
                try: return self._send(fn())
                except Exception as e:
                    traceback.print_exc(); return self._send({"erreur": str(e)}, 500)

        def do_POST(self):
            n = int(self.headers.get("Content-Length") or 0)
            try: body = json.loads(self.rfile.read(n) or b"{}")
            except json.JSONDecodeError: return self._send({"erreur": "JSON invalide"}, 400)
            routes = {"/api/validate": lambda: app.validate(body.get("build") or {}),
                      "/api/chat": lambda: app.chat(body.get("message", ""), body.get("build")),
                      "/api/reset": lambda: app.reset(),
                      "/api/explain": lambda: app.explain(),
                      "/api/generate": lambda: app.generate(body.get("warframe", ""), body.get("objectif", ""),
                                                            body.get("defense"), body.get("archetype"),
                                                            body.get("niveau") or "endgame"),
                      "/api/save": lambda: app.save(body.get("build") or {}, body.get("titre", "")),
                      "/api/loadout/save": lambda: app.loadout_save(body.get("nom", ""), body.get("build") or {},
                                                                    body.get("synthese", ""), body.get("raison", "")),
                      "/api/loadout/synthese": lambda: app.loadout_synthese(body.get("build") or {}),
                      "/api/loadout/maj": lambda: app.loadout_update(body.get("nom", ""))}
            fn = routes.get(urlparse(self.path).path)
            if not fn: return self._send({"erreur": "introuvable"}, 404)
            with LOCK:
                try: return self._send(fn())
                except Exception as e:
                    traceback.print_exc(); return self._send({"erreur": str(e)}, 500)
    return H


def main(argv=None):
    ap = argparse.ArgumentParser(description="Interface de build locale du compagnon Warframe.")
    ap.add_argument("--base", required=True)
    ap.add_argument("--data", default=None)
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--model", default=None, help="modèle Ollama, ou « auto » : petit modèle conseillé, téléchargé si besoin")
    ap.add_argument("--host", default="http://localhost:11434")
    ap.add_argument("--api-url", default=None)
    ap.add_argument("--cloud", default=None, choices=sorted(cloud.PRESETS), help="IA en ligne gratuite prête à l'emploi")
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--ctx", type=int, default=16384)
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--gpu", action="store_true", help="modèle intégré sur la carte graphique (Vulkan) ; par défaut, le processeur")
    ap.add_argument("--local", action="store_true", help="modèle intégré (llama.cpp + petit modèle installés par installer.bat), sans Ollama")
    ap.add_argument("--think", default=None, help="réflexion du modèle : off (bien plus rapide), on, low, medium, high")
    a = ap.parse_args(argv)
    base = os.path.abspath(a.base)
    data = a.data or os.path.join(os.path.dirname(base), "companion-data")
    chat_fn, box = None, None
    online = None if a.local else cloud.resolve(a)
    json_fn = None
    if a.local:
        from . import llm_local, installer
        try:
            if not llm_local.model_file(installer.ROOT):
                print("Installation du modèle intégré (llama.cpp + Qwen3 1.7B, environ 1,8 Go, une seule fois)…")
                llm_local.installer(installer.ROOT, gpu=a.gpu)
            url, model = llm_local.demarrer(installer.ROOT, ctx=8192, gpu=a.gpu)
            a.model, a.api_url, a.ctx = model, None, 8192
            chat_fn = lambda m, t, url=url, model=model: cloud.chat(url, "local", model, m, t, extra=llm_local.NO_THINK)
            json_fn = lambda m, url=url, model=model: cloud.chat(url, "local", model, m, None, extra=llm_local.JSON_MODE)
        except Exception as e:
            print(f"Modèle local indisponible : {e}\nL'interface marche quand même : le robot construit et explique seul.")
            a.model = None
    elif online:
        url, key, model = online; a.api_url, a.model = url, model
        chat_fn = lambda m, t, url=url, key=key, model=model: cloud.chat(url, key, model, m, t)  # valeurs figées : « url » est réutilisé plus bas
    elif a.model:
        if True:
            try: a.model = ag.choose_model(a.host, a.model)
            except ag.ModelError as e: print(e); a.model = None
    if a.model and not online and not a.local:
        small = bool(re.search(r":(?:0\.\d+|1(?:\.\d+)?|2|3|e2|e4)b\b", a.model))
        if small and a.ctx == 16384: a.ctx = 8192  # petit modèle : le robot fait le travail, un contexte court suffit et va plus vite
        if small and a.think is None: a.think = "off"  # réfléchir ralentit beaucoup un petit modèle pour peu de gain ici
        box = {"n": a.ctx}
        chat_fn = lambda m, t: ag.ollama_chat(a.host, a.model, m, t, {"num_ctx": box["n"]}, a.think)
        json_fn = lambda m: ag.ollama_chat(a.host, a.model, m, None, {"num_ctx": box["n"]}, "off", fmt="json")
    app = App(base, data, chat_fn, box, a.ctx if not a.api_url else 65536)
    app.model_label = (f"{a.model} (en ligne)" if a.api_url else (f"{a.model} (intégré)" if a.local else a.model)) if chat_fn else None
    app.online = bool(a.api_url)
    app.json_fn = json_fn
    app.small_model = bool(a.local or (a.model and not online and re.search(r":(?:0\.\d+|1(?:\.\d+)?|2|3|e2|e4)b\b", a.model or "")))
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), handler(app))
    url = f"http://localhost:{a.port}"
    print(f"Interface : {url}   (modèle : {a.model or 'aucun, discussion désactivée'})   Ctrl+C pour arrêter.")
    if not a.no_browser:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try: srv.serve_forever()
    except KeyboardInterrupt: pass


if __name__ == "__main__":
    sys.exit(main())
