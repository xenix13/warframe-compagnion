"""Prépare le dépôt GitHub à partir de l'installation actuelle (outil + base), sans rien de personnel ni de secret.

    python -m wfcompanion.depot --sortie E:\\IA\\warframe\\depot-github [--publier xenix13/warframe-compagnion] [--public]

Copie l'outil et la base dans <sortie>, en laissant de côté : clés d'API (cle-*.txt), données générées (companion-data),
modèle (moteur-ia), loadouts et profil du joueur, journaux, captures. Puis git init + commit, et, avec --publier,
crée le dépôt avec l'outil « gh » (privé par défaut) et l'envoie.
"""
import argparse, fnmatch, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXCLUS = ["__pycache__", "*.pyc", "cle-*.txt", "cle-api.txt", "*.key", ".env", "companion-data", "moteur-ia", "*.log",
          "rapport-references.txt", "m[0-9].png", "*.part", ".git", "depot-github",
          "06-builds-joueur", "profil-joueur.json", "relectures.jsonl", "etat-maj.json"]

GITIGNORE = """# secrets : ne jamais publier
cle-*.txt
cle-api.txt
.env
# généré ou téléchargé à l'installation
companion-data/
moteur-ia/
__pycache__/
*.pyc
*.log
*.part
rapport-references.txt
# personnel
base-warframe/06-builds-joueur/
base-warframe/04-retours-experience/profil-joueur.json
base-warframe/04-retours-experience/relectures.jsonl
"""

NOTICE = """# Sources et licences

- Code de l'outil : © XeniX13.
- Données du jeu (mods, armes, warframes, tables de drop) : téléchargées à l'installation depuis WFCD
  (https://github.com/WFCD), sous licence MIT.
- Pages du wiki dans `base-warframe/02-wiki` : copies converties du wiki officiel de Warframe
  (https://wiki.warframe.com), sous licence CC BY-SA ; chaque page indique sa source en deuxième ligne.
- Modèle intégré : Qwen3 1.7B (Qwen, licence Apache 2.0), version GGUF officielle, téléchargé à l'installation.
- Moteur du modèle : llama.cpp (ggml-org, licence MIT), téléchargé à l'installation.
- Warframe est une marque de Digital Extremes ; cet outil n'est ni affilié ni approuvé.
"""


def _skip(name):
    return any(fnmatch.fnmatch(name, p) for p in EXCLUS)


def copier(src, dst):
    for cur, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if not _skip(d)]
        rel = os.path.relpath(cur, src)
        os.makedirs(os.path.join(dst, rel), exist_ok=True)
        for f in files:
            if not _skip(f): shutil.copy2(os.path.join(cur, f), os.path.join(dst, rel, f))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--publier", help="owner/nom du dépôt à créer avec gh (ex. xenix13/warframe-compagnion)")
    ap.add_argument("--public", action="store_true", help="dépôt public (privé par défaut)")
    a = ap.parse_args(argv)
    out = os.path.abspath(a.sortie)
    if os.path.exists(out) and os.listdir(out) and not os.path.isdir(os.path.join(out, ".git")):
        sys.exit(f"{out} existe et n'est pas un dépôt : choisis un dossier vide")
    os.makedirs(out, exist_ok=True)
    print(f"Copie de l'outil : {ROOT}")
    copier(ROOT, out)
    base = next((p for p in (os.path.join(ROOT, "base-warframe"), os.path.join(os.path.dirname(ROOT), "base-warframe"))
                 if os.path.isdir(p)), None)
    if base and os.path.abspath(base) != os.path.join(out, "base-warframe"):
        print(f"Copie de la base : {base}")
        copier(base, os.path.join(out, "base-warframe"))
    open(os.path.join(out, ".gitignore"), "w", encoding="utf-8").write(GITIGNORE)
    open(os.path.join(out, "SOURCES.md"), "w", encoding="utf-8").write(NOTICE)
    leaks = [os.path.join(c, f) for c, _, fs in os.walk(out) for f in fs if fnmatch.fnmatch(f, "cle-*.txt")]
    if leaks: sys.exit(f"ARRÊT : un fichier de clé a été copié ({leaks[0]}) ; rien n'est publié")
    if not shutil.which("git"):
        print("git introuvable : dossier prêt, mais pas de commit (installe Git for Windows)"); return
    run = lambda *c: subprocess.run(c, cwd=out, check=True)
    if not os.path.isdir(os.path.join(out, ".git")): run("git", "init", "-b", "main")
    run("git", "add", "-A")
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=out).returncode:
        run("git", "commit", "-m", "Compagnon Warframe : outil, robot de build et base")
    print(f"Dépôt prêt : {out}")
    if a.publier:
        if not shutil.which("gh"): sys.exit("gh introuvable : installe GitHub CLI (https://cli.github.com) puis « gh auth login »")
        has_remote = subprocess.run(["git", "remote", "get-url", "origin"], cwd=out, capture_output=True).returncode == 0
        if has_remote: run("git", "push", "-u", "origin", "main")
        else: run("gh", "repo", "create", a.publier, "--public" if a.public else "--private", "--source", ".", "--push")
        print(f"Publié : https://github.com/{a.publier}")


if __name__ == "__main__":
    sys.exit(main())
