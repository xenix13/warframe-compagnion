"""Mise à jour de la base (à lancer à la main, par le planificateur, ou à l'ouverture de l'app).

Exemple :
    python -m wfcompanion.update --base "E:\\IA\\warframe\\base-warframe"

Étapes :
  1. télécharge les sources qui ont changé (cache ETag : rien n'est retéléchargé si rien n'a bougé) ;
  2. si les données ont changé : reconstruit la base SQLite, les fichiers de farm et les fichiers de mods ;
  3. rafraîchit les pages du wiki dont la révision a changé ;
  4. écrit « 00 - Etat de la base.md » (dates des données) pour que l'agent sache de quand date ce qu'il lit.
"""
import argparse, datetime, glob, json, os, sys, time

from . import db, farm, mods_md, net, wiki
from .sources import SOURCES


def run(base, data_dir, do_wiki=True, force=False, log=print):
    raw = os.path.join(data_dir, "raw"); os.makedirs(raw, exist_ok=True)
    state_path = os.path.join(data_dir, "state.json")
    lock = os.path.join(data_dir, "update.lock")
    if os.path.exists(lock) and time.time() - os.path.getmtime(lock) < 3600:
        log("Une mise à jour est déjà en cours (update.lock) : abandon.")
        return {"skipped": True}
    open(lock, "w").close()
    try:
        state = net.load_state(state_path)
        changed = []
        for name, url in SOURCES.items():
            try:
                if net.fetch_if_changed(url, os.path.join(raw, name), state.setdefault("etags", {})) or force:
                    changed.append(name)
            except Exception as e:
                log(f"  source indisponible, ancienne copie gardée : {name} ({e})")
        missing = [n for n in SOURCES if not os.path.exists(os.path.join(raw, n))]
        if missing:
            raise RuntimeError(f"sources manquantes, impossible de construire la base : {missing}")
        log(f"Sources modifiées : {', '.join(changed) if changed else 'aucune'}")
        summary = {"sources": changed, "farm": [], "mods": [], "wiki": []}
        if changed or db.needs_rebuild(os.path.join(data_dir, "warframe.sqlite")):
            db.build(raw, os.path.join(data_dir, "warframe.sqlite")); log("Base SQLite reconstruite.")
            summary["farm"] = farm.build(raw, os.path.join(base, "01-donnees", "farm"))
            log(f"Fichiers de farm : {len(summary['farm'])}")
            summary["mods"] = mods_md.build(raw, os.path.join(base, "01-donnees", "mods"))
            log(f"Fichiers de mods : {len(summary['mods'])}")
        if do_wiki:
            try:
                summary["wiki"] = wiki.refresh(base, state, log=log)
                state["wiki_last_ok"] = datetime.date.today().isoformat()
                state.pop("wiki_error", None)
                log(f"Pages wiki mises à jour : {len(summary['wiki'])}")
            except Exception as e:
                state["wiki_error"] = str(e)[:300]
                log(f"  Wiki non rafraîchi, pages gardées telles quelles : {e}")
        state["last_run"] = datetime.datetime.now().isoformat(timespec="seconds")
        net.save_state(state_path, state)
        write_status(base, raw, state, summary)
        return summary
    finally:
        os.unlink(lock)


def write_status(base, raw, state, summary):
    with open(os.path.join(raw, "drops_info.json"), encoding="utf-8") as f:
        ts = json.load(f)["timestamp"]
    drops = datetime.datetime.fromtimestamp(ts / 1000, datetime.timezone.utc).date()
    notes = sorted(os.path.basename(p) for p in glob.glob(os.path.join(base, "03-patch-notes", "*.md")))
    last_note = notes[-1][:-3] if notes else "aucune"
    txt = f"""# État de la base (généré automatiquement)

- Dernière mise à jour automatique : {state['last_run']}
- Tables de drop : version du {drops:%d/%m/%Y}
- Données du jeu (mods, armes, warframes, arcanes) : WFCD warframe-items, téléchargées lors de la dernière mise à jour où elles avaient changé
- Pages du wiki : dernière actualisation automatique réussie : {state.get('wiki_last_ok', 'jamais depuis cette machine')}{' ; dernier essai refusé par le wiki (protection anti-robot), les pages sont celles du dernier import manuel' if state.get('wiki_error') else ''}
- Dernière note de patch présente dans la base : {last_note}
- Notes de patch : **pas encore mises à jour automatiquement** ; si une mise à jour du jeu est sortie après cette note, l'agent doit prévenir que la base peut ne pas la connaître.

Règle pour l'agent : avant de citer un taux de drop, une valeur de mod ou un build, comparer ces dates à la date du jour et le signaler si les données sont anciennes.
"""
    with open(os.path.join(base, "00 - Etat de la base.md"), "w", encoding="utf-8") as f:
        f.write(txt)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Met à jour la base Warframe du compagnon.")
    ap.add_argument("--base", required=True, help="dossier base-warframe")
    ap.add_argument("--data", default=None, help="dossier des données brutes et de la base SQLite (défaut : <base>/../companion-data)")
    ap.add_argument("--no-wiki", action="store_true", help="ne pas rafraîchir les pages du wiki")
    ap.add_argument("--force", action="store_true", help="reconstruire même si rien n'a changé")
    a = ap.parse_args(argv)
    data = a.data or os.path.join(os.path.dirname(os.path.abspath(a.base)), "companion-data")
    os.makedirs(data, exist_ok=True)
    s = run(os.path.abspath(a.base), data, do_wiki=not a.no_wiki, force=a.force)
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in s.items()}, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
