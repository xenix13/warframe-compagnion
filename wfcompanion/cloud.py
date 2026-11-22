"""Connexion à une IA en ligne par le protocole « compatible OpenAI » (la plupart des offres gratuites le parlent).

Le reste de l'agent ne change pas : mêmes outils, même contrôle des builds. Seul le modèle est ailleurs.
La clé reste sur la machine du joueur (variable d'environnement WF_API_KEY ou fichier cle-api.txt, jamais dans le code).
"""
import json, time, urllib.error, urllib.request


class CloudError(RuntimeError):
    pass


# Offres gratuites compatibles OpenAI (vérifié en novembre 2026 ; les plafonds changent souvent, voir le site du fournisseur).
# La clé se met dans cle-<fournisseur>.txt (ou cle-api.txt), à côté des .bat : elle ne quitte jamais la machine du joueur.
# « prefer » : motifs pour choisir le modèle parmi ceux que le fournisseur liste au lancement (les noms changent souvent).
PRESETS = {
    "gemini": {"url": "https://generativelanguage.googleapis.com/v1beta/openai", "model": "gemini-2.5-flash",
               "site": "https://aistudio.google.com/apikey",
               "prefer": [r"gemini-(\d+(\.\d+)?)-flash$", r"gemini-(\d+(\.\d+)?)-flash-latest$", r"gemini-flash-latest$"]},
    "groq": {"url": "https://api.groq.com/openai/v1", "model": "llama-3.3-70b-versatile",
             "site": "https://console.groq.com/keys",
             "prefer": [r"openai/gpt-oss-120b$", r"llama-3\.3-70b-versatile$", r"llama-4-maverick"]},
    "openrouter": {"url": "https://openrouter.ai/api/v1", "model": "meta-llama/llama-3.3-70b-instruct:free",
                   "site": "https://openrouter.ai/keys", "prefer": [r":free$"]},
}


def resolve(a):
    """--cloud <fournisseur> : remplit l'adresse, le modèle par défaut et la clé. Renvoie (url, clé, modèle) ou None."""
    import os
    preset = PRESETS.get((getattr(a, "cloud", None) or "").lower())
    url = a.api_url or (preset or {}).get("url")
    if not url: return None
    model = a.model or (preset or {}).get("model")
    key = a.api_key or os.environ.get("WF_API_KEY")
    for f in ([f"cle-{a.cloud.lower()}.txt"] if preset else []) + ["cle-api.txt"]:
        if not key and os.path.exists(f):
            with open(f, encoding="utf-8") as fh: key = fh.read().strip()
    if not key:
        where = f"cle-{a.cloud.lower()}.txt" if preset else "cle-api.txt"
        raise SystemExit(f"Clé manquante : crée le fichier {where} dans le dossier du compagnon et colle ta clé dedans"
                         + (f" (clé gratuite : {preset['site']})." if preset else "."))
    if preset and not a.model:
        model = discover(url, key, preset) or model
    return url, key, model


def discover(url, key, preset):
    """Choisit le modèle le plus récent qui correspond aux motifs du fournisseur ; None si la liste n'est pas lisible."""
    import re
    try:
        req = urllib.request.Request(url.rstrip("/") + "/models", headers={"Authorization": f"Bearer {key}"})
        with urllib.request.urlopen(req, timeout=15) as r:
            ids = [m.get("id", "") for m in json.loads(r.read()).get("data", [])]
    except Exception:
        return None
    ids = [i.split("/", 1)[1] if i.startswith("models/") else i for i in ids]
    for pat in preset.get("prefer", []):
        hits = [i for i in ids if re.search(pat, i)]
        if hits:
            ver = lambda i: [float(x) for x in re.findall(r"\d+(?:\.\d+)?", i)[:2]] or [0]
            return sorted(hits, key=ver)[-1]
    return None


def to_openai(messages):
    """Convertit l'historique interne (format Ollama) au format OpenAI : identifiants d'appels et arguments en texte."""
    out, pending, n = [], [], 0
    for m in messages:
        role = m["role"]
        if role == "assistant" and m.get("tool_calls"):
            calls = []
            for c in m["tool_calls"]:
                n += 1; cid = f"call_{n}"; pending.append(cid)
                fn = c.get("function", {})
                args = fn.get("arguments") or {}
                calls.append({"id": cid, "type": "function", "function": {
                    "name": fn.get("name"), "arguments": args if isinstance(args, str) else json.dumps(args, ensure_ascii=False)}})
            out.append({"role": "assistant", "content": m.get("content") or None, "tool_calls": calls})
        elif role == "tool":
            cid = pending.pop(0) if pending else f"call_{n}"
            out.append({"role": "tool", "tool_call_id": cid, "content": m.get("content") or ""})
        else:
            out.append({"role": role, "content": m.get("content") or ""})
    return out


def from_openai(msg):
    """Réponse OpenAI -> format interne."""
    out = {"role": "assistant", "content": msg.get("content") or ""}
    calls = []
    for c in msg.get("tool_calls") or []:
        fn = c.get("function", {})
        args = fn.get("arguments") or "{}"
        if isinstance(args, str):
            try: args = json.loads(args)
            except json.JSONDecodeError: args = {}
        calls.append({"function": {"name": fn.get("name"), "arguments": args}})
    if calls: out["tool_calls"] = calls
    return out


def chat(base_url, key, model, messages, tools, debug=False, max_wait=90, extra=None):
    body = {"model": model, "messages": to_openai(messages), "temperature": 0.2, **(extra or {})}
    if tools: body["tools"] = tools
    url = base_url.rstrip("/") + "/chat/completions"
    data = json.dumps(body).encode()
    for attempt in range(4):
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json",
                                                               "Authorization": f"Bearer {key}"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                full = json.loads(r.read())
            if debug:
                u = full.get("usage", {})
                print(f"  [debug] jetons_entree={u.get('prompt_tokens')} jetons_sortie={u.get('completion_tokens')} "
                      f"fin={full['choices'][0].get('finish_reason')}")
            return from_openai(full["choices"][0]["message"])
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:300]
            if e.code == 429 and attempt < 3:  # plafond de l'offre gratuite : on attend puis on réessaie
                wait = min(max_wait, int(e.headers.get("Retry-After") or 0) or 15 * (attempt + 1))
                print(f"  [cloud] plafond de requêtes atteint, attente de {wait} s...")
                time.sleep(wait); continue
            if e.code in (401, 403):
                raise CloudError(f"clé refusée par le fournisseur (HTTP {e.code}) : vérifie la clé. {detail}")
            raise CloudError(f"le fournisseur a répondu HTTP {e.code} : {detail}")
        except urllib.error.URLError as e:
            raise CloudError(f"fournisseur injoignable ({e.reason}) : vérifie l'adresse --api-url et la connexion")
    raise CloudError("plafond de requêtes de l'offre gratuite atteint : réessaie plus tard")
