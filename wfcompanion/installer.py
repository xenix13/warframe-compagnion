"""Installation complète du compagnon (appelée par install.ps1 ou installer.bat) :
1. modèle local (llama.cpp + Qwen3 1.7B), sauf --sans-ia ;
2. données du jeu (base SQLite depuis WFCD, pages du wiki), via la mise à jour habituelle ;
3. raccourci « Compagnon Warframe » sur le bureau (Windows).

    python -m wfcompanion.installer [--leger] [--cpu] [--sans-ia] [--sans-raccourci]
"""
import argparse, os, subprocess, sys

from . import llm_local

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def base_dir(root=ROOT):
    """La base est dans le dossier de l'outil (installation GitHub) ou à côté (installation d'origine)."""
    for p in (os.path.join(root, "base-warframe"), os.path.join(os.path.dirname(root), "base-warframe")):
        if os.path.isdir(p): return p
    return os.path.join(root, "base-warframe")


def raccourci(root=ROOT, log=print):
    if os.name != "nt": return
    target = os.path.join(root, "lancer.bat")
    ps = ("$s=(New-Object -ComObject WScript.Shell).CreateShortcut([Environment]::GetFolderPath('Desktop')+'\\Compagnon Warframe.lnk');"
          f"$s.TargetPath='{target}';$s.WorkingDirectory='{root}';$s.WindowStyle=7;$s.Save()")
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=False)
    log("  raccourci « Compagnon Warframe » créé sur le bureau")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--leger", action="store_true", help="modèle plus petit (0.6B) pour un PC modeste")
    ap.add_argument("--gpu", action="store_true", help="installe aussi la version carte graphique (Vulkan) ; par défaut, processeur")
    ap.add_argument("--cpu", action="store_true", help=argparse.SUPPRESS)  # ancienne option : le processeur est le défaut
    ap.add_argument("--sans-ia", action="store_true", help="ne pas installer de modèle (le robot marche sans)")
    ap.add_argument("--sans-raccourci", action="store_true")
    a = ap.parse_args(argv)
    print("1/3  Modèle local")
    if a.sans_ia: print("  ignoré (--sans-ia)")
    else:
        try: llm_local.installer(ROOT, leger=a.leger, gpu=a.gpu)
        except Exception as e: print(f"  échec : {e}\n  L'outil marchera sans IA ; relance installer.bat plus tard.")
    print("2/3  Données du jeu (premier lancement : 1 à 3 minutes)")
    base = base_dir()
    os.makedirs(base, exist_ok=True)
    r = subprocess.run([sys.executable, "-m", "wfcompanion.update", "--base", base], cwd=ROOT)
    if r.returncode: print("  la mise à jour a échoué : relance mise-a-jour.bat quand la connexion est revenue")
    print("3/3  Raccourci")
    if not a.sans_raccourci: raccourci()
    print("\nInstallation terminée. Lance « Compagnon Warframe » depuis le bureau (ou lancer.bat).")


if __name__ == "__main__":
    sys.exit(main())
