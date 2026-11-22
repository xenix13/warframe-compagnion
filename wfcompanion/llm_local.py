"""Modèle local intégré, sans Ollama : llama.cpp (llama-server) + un petit modèle GGUF, installés dans le dossier de l'outil.

- installer(root) télécharge une seule fois :
    * llama.cpp pour Windows (version Vulkan : marche sur les cartes AMD, NVIDIA et Intel ; sinon version CPU) depuis
      les « releases » GitHub de ggml-org/llama.cpp ;
    * le modèle Qwen3 1.7B en Q8_0 (environ 1,8 Go) depuis Hugging Face (Qwen/Qwen3-1.7B-GGUF, licence Apache 2.0).
- demarrer(root) lance llama-server en arrière-plan (port 8081) et renvoie l'adresse de son API compatible OpenAI ;
  l'interface lui parle comme à une IA en ligne (cloud.chat). Le serveur s'arrête avec l'interface.

Tout est rangé dans <root>/moteur-ia/ : llama/ (programme) et modeles/ (fichier .gguf).
"""
import atexit, glob, io, json, os, platform, re, shutil, subprocess, sys, time, urllib.request, zipfile

# la release « latest » (ex. v1.0.0) peut ne contenir que le code source : les programmes Windows sont dans les
# releases de build (bNNNNN) ; on prend la plus récente qui a une archive Windows
LLAMA_RELEASES = "https://api.github.com/repos/ggml-org/llama.cpp/releases?per_page=20"
# Qwen3 1.7B, version officielle de Qwen, en Q8_0 (1,8 Go) : architecture bien prise en charge par llama.cpp.
# (Qwen3.5 2B donnait un texte illisible avec llama.cpp 1.0 sur processeur : écarté.)
MODELE_REPO = "Qwen/Qwen3-1.7B-GGUF"
MODELE_QUANT = "Q8_0"            # sur un si petit modèle, Q8 garde nettement plus de qualité que Q4
MODELE_LEGER = ("Qwen/Qwen3-0.6B-GGUF", "Q8_0")
MODELES_ECARTES = ("Qwen3.5-",)  # fichiers à supprimer s'ils traînent dans modeles/
PORT = 8081
UA = {"User-Agent": "compagnon-warframe"}


def _dirs(root, gpu=False):
    """llama-cpu/ : version processeur (par défaut, la plus sûre) ; llama/ : version Vulkan (carte graphique, --gpu)."""
    base = os.path.join(root, "moteur-ia")
    return os.path.join(base, "llama" if gpu else "llama-cpu"), os.path.join(base, "modeles")


def _get(url, timeout=60):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def _download(url, dest, log=print):
    """Téléchargement avec avancement, dans un fichier .part renommé à la fin (reprise propre si coupure)."""
    tmp = dest + ".part"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r, open(tmp, "wb") as f:
        total, done, last = int(r.headers.get("Content-Length") or 0), 0, -1
        while True:
            chunk = r.read(1 << 20)
            if not chunk: break
            f.write(chunk); done += len(chunk)
            pct = 100 * done // total if total else -1
            if total and pct // 5 != last // 5: log(f"    {os.path.basename(dest)} : {pct} %"); last = pct
    os.replace(tmp, dest)


def server_exe(root, gpu=False):
    llama, _ = _dirs(root, gpu)
    hits = glob.glob(os.path.join(llama, "**", "llama-server.exe" if os.name == "nt" else "llama-server"), recursive=True)
    return hits[0] if hits else None


def model_file(root):
    """Le modèle conseillé s'il est là, sinon un autre .gguf (sauf les modèles écartés)."""
    _, models = _dirs(root)
    hits = [h for h in sorted(glob.glob(os.path.join(models, "*.gguf")))
            if not os.path.basename(h).startswith(MODELES_ECARTES)]
    want = MODELE_REPO.split("/")[1].replace("-GGUF", "")
    return next((h for h in hits if os.path.basename(h).startswith(want)), hits[0] if hits else None)


def installer_llama(root, log=print, gpu=False):
    """Télécharge llama.cpp pour Windows : version processeur par défaut, version Vulkan (carte graphique) avec gpu=True."""
    if server_exe(root, gpu): log("  llama.cpp : déjà installé"); return server_exe(root, gpu)
    if os.name != "nt":
        raise RuntimeError("installation automatique de llama.cpp prévue pour Windows ; ailleurs, installe llama.cpp "
                           "(https://github.com/ggml-org/llama.cpp) et mets llama-server dans moteur-ia/llama/")
    order = [r"bin-win-vulkan-x64\.zip$"] if gpu else [r"bin-win-cpu-x64\.zip$"]
    rel, pick, assets = None, None, {}
    for r_ in json.loads(_get(LLAMA_RELEASES)):
        if r_.get("draft"): continue
        assets = {a["name"]: a["browser_download_url"] for a in r_.get("assets", [])}
        pick = next((n for rx in order for n in assets if re.search(rx, n)), None)
        if pick: rel = r_; break
    if not pick: raise RuntimeError("aucune version Windows de llama.cpp trouvée dans les 20 dernières releases")
    llama, _ = _dirs(root, gpu); os.makedirs(llama, exist_ok=True)
    log(f"  llama.cpp {rel.get('tag_name')} : {pick}")
    z = os.path.join(llama, pick); _download(assets[pick], z, log)
    with zipfile.ZipFile(z) as zf: zf.extractall(llama)
    os.remove(z)
    exe = server_exe(root, gpu)
    if not exe: raise RuntimeError("llama-server introuvable dans l'archive téléchargée")
    return exe


def installer_modele(root, log=print, leger=False):
    """Télécharge le modèle GGUF (Qwen3 1.7B, ou 0.6B en version légère) depuis Hugging Face."""
    if model_file(root): log(f"  modèle : déjà installé ({os.path.basename(model_file(root))})"); return model_file(root)
    repo, quant = MODELE_LEGER if leger else (MODELE_REPO, MODELE_QUANT)
    info = json.loads(_get(f"https://huggingface.co/api/models/{repo}"))
    files = [s["rfilename"] for s in info.get("siblings", []) if s["rfilename"].endswith(".gguf")]
    pick = next((f for f in files if quant.lower() in f.lower() and "mmproj" not in f.lower()), None)
    if not pick: raise RuntimeError(f"fichier {quant} introuvable dans {repo} ({', '.join(files[:8])}…)")
    _, models = _dirs(root); os.makedirs(models, exist_ok=True)
    log(f"  modèle : {repo} / {pick}")
    dest = os.path.join(models, os.path.basename(pick))
    _download(f"https://huggingface.co/{repo}/resolve/main/{pick}", dest, log)
    for old in glob.glob(os.path.join(models, "*.gguf")):  # place libérée : anciens modèles écartés
        if os.path.basename(old).startswith(MODELES_ECARTES):
            try: os.remove(old); log(f"  ancien modèle supprimé : {os.path.basename(old)}")
            except OSError: pass
    return dest


def installer(root, log=print, leger=False, gpu=False):
    installer_llama(root, log, gpu)
    return installer_modele(root, log, leger)


def _alive(port):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as r: return r.status == 200
    except Exception: return False


def _ollama_charge():
    """Modèles qu'Ollama garde en mémoire en ce moment (ils prennent de la RAM ou de la mémoire vidéo)."""
    try:
        with urllib.request.urlopen("http://127.0.0.1:11434/api/ps", timeout=2) as r:
            return [m.get("name") for m in json.loads(r.read()).get("models", [])]
    except Exception: return []


def _sain(port, name):
    """Petit test au démarrage : le modèle doit répondre du texte lisible (pas une bouillie de langues mélangées)."""
    body = {"model": name, "messages": [{"role": "user", "content": "Réponds en un mot français : quelle est la couleur du ciel ?"}],
            "max_tokens": 30, "temperature": 0, "chat_template_kwargs": {"enable_thinking": False}}
    try:
        req = urllib.request.Request(f"http://127.0.0.1:{port}/v1/chat/completions", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            txt = json.loads(r.read())["choices"][0]["message"].get("content") or ""
    except Exception:
        return True  # test impossible : on ne bloque pas
    txt = re.sub(r"<think>.*?</think>", "", txt, flags=re.S)
    odd = sum(1 for c in txt if ord(c) > 0x2FF)  # écritures non latines (chinois, cyrillique, coréen…)
    return len(txt.strip()) > 0 and odd <= max(2, len(txt) // 10)


def demarrer(root, ctx=8192, port=PORT, log=print, gpu=False):
    """Lance llama-server (s'il ne tourne pas déjà) et renvoie (url de l'API, nom du modèle).
    Par défaut sur le processeur : un modèle de 2B y tourne bien, et on évite les pilotes graphiques.
    Avec gpu=True (version Vulkan) : si le démarrage précédent n'est pas allé au bout (plantage du PC pendant le
    chargement), on repasse tout seul sur le processeur."""
    base = os.path.join(root, "moteur-ia")
    lock = os.path.join(base, "demarrage-gpu.en-cours")
    if gpu and os.path.exists(lock):
        log("Le dernier démarrage sur la carte graphique ne s'est pas terminé (plantage ?) : démarrage sur le processeur.\n"
            f"  Pour réessayer la carte graphique : supprimer {lock} puis lancer avec --gpu.")
        gpu = False
    if gpu and not server_exe(root, True): installer_llama(root, log, True)
    if not gpu and not server_exe(root, False): installer_llama(root, log, False)
    exe, model = server_exe(root, gpu), model_file(root)
    if not exe or not model:
        raise RuntimeError("modèle local pas installé : lance installer.bat (ou python -m wfcompanion.installer)")
    name = os.path.splitext(os.path.basename(model))[0]
    if _alive(port): return f"http://127.0.0.1:{port}/v1", name
    busy = _ollama_charge()
    if busy: log(f"Attention : Ollama garde {', '.join(busy)} en mémoire ; fermer Ollama libère de la mémoire pour le compagnon.")
    cmd = [exe, "-m", model, "--port", str(port), "--host", "127.0.0.1", "-c", str(ctx), "-ngl", "99" if gpu else "0", "--jinja"]
    log_path = os.path.join(base, "llama-server.log")
    flags = 0x08000000 if os.name == "nt" else 0  # CREATE_NO_WINDOW : pas de fenêtre en plus
    if gpu: open(lock, "w").close()
    proc = subprocess.Popen(cmd, stdout=open(log_path, "w"), stderr=subprocess.STDOUT, creationflags=flags)
    atexit.register(lambda: proc.poll() is None and proc.terminate())
    log(f"Modèle local : démarrage de {name} sur {'la carte graphique' if gpu else 'le processeur'}…")
    for _ in range(180):  # chargement : quelques secondes, jusqu'à 1 à 2 min sur un vieux PC
        if proc.poll() is not None:
            if gpu and os.path.exists(lock): os.remove(lock)
            if gpu:
                log("  la carte graphique n'a pas pu charger le modèle : nouvel essai sur le processeur")
                return demarrer(root, ctx, port, log, gpu=False)
            raise RuntimeError(f"llama-server s'est arrêté : voir {log_path}")
        if _alive(port):
            if gpu and os.path.exists(lock): os.remove(lock)
            if not _sain(port, name):
                proc.terminate()
                raise RuntimeError(f"le modèle {name} répond un texte illisible avec cette version de llama.cpp "
                                   "(voir moteur-ia/llama-server.log) ; le robot marche sans lui")
            log(f"Modèle local prêt ({name})."); return f"http://127.0.0.1:{port}/v1", name
        time.sleep(1)
    raise RuntimeError(f"llama-server ne répond pas après 3 minutes : voir {log_path}")


# requêtes vers llama-server : réflexion coupée (petit modèle : bien plus rapide) ; JSON forcé pour le pilote
# max_tokens : une réponse ne peut pas partir en boucle jusqu'à remplir tout le contexte
NO_THINK = {"chat_template_kwargs": {"enable_thinking": False}, "max_tokens": 1000}
JSON_MODE = {**NO_THINK, "max_tokens": 400, "response_format": {"type": "json_object"}}
