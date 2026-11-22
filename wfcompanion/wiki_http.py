"""Appels à l'API du wiki, avec plusieurs méthodes essayées dans l'ordre (le wiki refuse certaines signatures).

La première méthode qui marche est retenue pour la suite de l'exécution. En cas d'échec complet,
l'erreur liste le code HTTP de chaque méthode, pour le diagnostic.
"""
import json, re, shutil, subprocess, urllib.error, urllib.parse, urllib.request

from .sources import WIKI_API

UA_BROWSER = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/126.0.0.0 Safari/537.36")
HEADERS = {"User-Agent": UA_BROWSER, "Accept": "application/json,text/html;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.9"}
_working = []


class WikiBlocked(RuntimeError):
    """Le wiki refuse les clients automatiques depuis cette connexion (page « Please wait »)."""


def _curl(params, post, ua):
    exe = shutil.which("curl")
    if not exe:
        raise RuntimeError("curl absent")
    cmd = [exe, "-sS", "-L", "--compressed", "--max-time", "120", "-A", ua,
           "-H", "Accept: " + HEADERS["Accept"], "-H", "Accept-Language: " + HEADERS["Accept-Language"],
           "-w", "\n%{http_code}"]
    q = urllib.parse.urlencode(params)
    cmd += ["--data", q, WIKI_API] if post else [WIKI_API + "?" + q]
    r = subprocess.run(cmd, capture_output=True)
    body, _, code = r.stdout.rpartition(b"\n")
    code = code.decode("ascii", "replace").strip()
    if r.returncode != 0 or code != "200":
        raise RuntimeError(f"HTTP {code or '?'} (curl code {r.returncode}) {r.stderr.decode('utf-8', 'replace').strip()[:120]}")
    return body


def _urllib(params, post, ua):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(WIKI_API if post else WIKI_API + "?" + q,
                                 data=q.encode() if post else None, headers={**HEADERS, "User-Agent": ua})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}")


def _powershell(params, post, ua):
    exe = shutil.which("powershell") or shutil.which("pwsh")
    if not exe:
        raise RuntimeError("PowerShell absent")
    q = urllib.parse.urlencode(params)
    script = ("$ProgressPreference='SilentlyContinue';[Console]::OutputEncoding=[Text.Encoding]::UTF8;"
              f"$r=Invoke-WebRequest -UseBasicParsing -Method Post -Uri '{WIKI_API}' -Body '{q}' "
              f"-UserAgent '{ua}' -ContentType 'application/x-www-form-urlencoded';"
              "[Console]::Out.Write($r.Content)")
    r = subprocess.run([exe, "-NoProfile", "-NonInteractive", "-Command", script], capture_output=True)
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError("PowerShell : " + r.stderr.decode("utf-8", "replace").strip()[:160])
    return r.stdout


METHODS = [
    ("curl POST navigateur", lambda p: _curl(p, True, UA_BROWSER)),
    ("curl GET Mozilla/5.0", lambda p: _curl(p, False, "Mozilla/5.0")),
    ("urllib POST navigateur", lambda p: _urllib(p, True, UA_BROWSER)),
    ("PowerShell POST", lambda p: _powershell(p, True, UA_BROWSER)),
]


def api(params):
    """Appelle l'API du wiki et renvoie le JSON décodé."""
    params = {**params, "format": "json", "formatversion": 2}
    order = _working + [m for m in METHODS if m not in _working]
    errors = []
    for m in order:
        name, fn = m
        try:
            raw = fn(params)
            d = json.loads(raw.decode("utf-8-sig", "replace").strip())
        except Exception as e:  # on essaie la méthode suivante
            errors.append(f"{name} : {e}")
            continue
        if not _working:
            _working.append(m)
        return d
    short = [re.sub(r"\s+", " ", e)[:70] for e in errors]
    if any("403" in e for e in errors):
        raise WikiBlocked("le wiki demande une vérification anti-robot (HTTP 403) depuis cette connexion ; "
                          "les pages wiki ne peuvent pas être rafraîchies d'ici. Détail : " + " | ".join(short))
    raise RuntimeError("wiki inaccessible -> " + " | ".join(short))
