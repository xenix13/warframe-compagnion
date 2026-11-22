"""Téléchargements avec cache ETag : on ne retélécharge que ce qui a changé.

On passe par curl (présent sur Windows 10+ et Linux) car le wiki refuse
parfois les requêtes urllib ; urllib sert de solution de repli.
"""
import json, os, shutil, subprocess, tempfile, urllib.request

UA = "Mozilla/5.0 (wf-companion)"


def _curl_available():
    return shutil.which("curl") is not None


def fetch_bytes(url, timeout=120):
    if _curl_available():
        r = subprocess.run(["curl", "-sS", "--fail", "-L", "-A", UA, "--max-time", str(timeout), url],
                           capture_output=True)
        if r.returncode == 0:
            return r.stdout
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_if_changed(url, dest, state, timeout=300):
    """Télécharge url vers dest si l'ETag a changé. Retourne True si le fichier a changé.

    state : dict persistant {url: etag}.
    """
    etag = state.get(url)
    if _curl_available():
        hdr = tempfile.NamedTemporaryFile(delete=False, suffix=".hdr"); hdr.close()
        tmp = dest + ".part"
        cmd = ["curl", "-sS", "-L", "-A", UA, "--max-time", str(timeout), "-D", hdr.name,
               "-o", tmp, "-w", "%{http_code}", url]
        if etag and os.path.exists(dest):
            cmd[1:1] = ["-H", f"If-None-Match: {etag}"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        code = (r.stdout or "").strip()[-3:]
        headers = open(hdr.name, encoding="latin-1").read(); os.unlink(hdr.name)
        if code == "304":
            if os.path.exists(tmp): os.unlink(tmp)
            return False
        if r.returncode != 0 or code != "200":
            if os.path.exists(tmp): os.unlink(tmp)
            raise RuntimeError(f"échec du téléchargement {url} (code {code}) : {r.stderr.strip()}")
        new = None
        for line in headers.splitlines():
            if line.lower().startswith("etag:"):
                new = line.split(":", 1)[1].strip()
        os.replace(tmp, dest)
        if new: state[url] = new
        return True
    # repli urllib
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if etag and os.path.exists(dest):
        req.add_header("If-None-Match", etag)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read(); new = resp.headers.get("ETag")
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return False
        raise
    with open(dest, "wb") as f:
        f.write(data)
    if new: state[url] = new
    return True


def load_state(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(path, state):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=1, ensure_ascii=False)
