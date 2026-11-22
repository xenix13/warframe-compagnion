"""Builds de référence (vrais builds du joueur, recopiés de ses captures) : comparaison avec ce que sort le robot.

Les fichiers sont dans <base>/04-retours-experience/builds-reference/<id>.json. Lancer :
    python -m wfcompanion.reference --base <base> --data <companion-data> [--id xaku]
Le rapport dit, pour chaque build, ce que le robot a en commun avec la référence et où il s'écarte.
"""
import argparse, glob, json, os, re

from . import optimizer

STATS = ("puissance", "duree", "portee", "efficacite")
TOT = {"puissance": "Puissance", "duree": "Durée", "portee": "Portée", "efficacite": "Efficacité"}


def load(base, only=None):
    out = []
    for p in sorted(glob.glob(os.path.join(base, "04-retours-experience", "builds-reference", "*.json"))):
        if os.path.basename(p).startswith("arme-"): continue
        r = json.load(open(p, encoding="utf-8"))
        if only and only.lower() not in r["id"].lower(): continue
        out.append(r)
    return out


def _pct(v):
    m = re.match(r"\s*(-?[\d.]+)", str(v or ""))
    return round(float(m.group(1))) if m else None


def compare(tb, ref):
    r = optimizer.propose(tb, ref["warframe"], ref["demande"])
    if "erreur" in r: return {"id": ref["id"], "erreur": r["erreur"]}
    b, rb = r["build"], ref["build"]
    mine = set(b["mods"]) | {b.get("aura"), b.get("exilus")} - {None, ""}
    theirs = set(rb["mods"]) | {rb.get("aura"), rb.get("exilus")} - {None, ""}
    tot = r["validation"].get("totaux") or {}
    stats = {s: {"reference": ref.get("stats_jeu", {}).get(s), "robot": _pct(tot.get(TOT[s]))} for s in STATS}
    return {"id": ref["id"], "usage": ref["usage"],
            "mods_communs": sorted(mine & theirs), "mods_manquants": sorted(theirs - mine), "mods_en_trop": sorted(mine - theirs),
            "score_mods": f"{len(mine & theirs)}/{len(theirs)}",
            "helminth": {"reference": rb.get("helminth"), "robot": b.get("helminth") or None,
                         "remplace_reference": rb.get("helminth_remplace"), "remplace_robot": b.get("helminth_remplace") or None},
            "arcanes": {"reference": rb.get("arcanes"), "robot": b.get("arcanes")},
            "capacite_centrale_robot": r["archetype"].get("nom"), "defense_robot": b.get("defense"),
            "stats": stats, "statut_robot": r["validation"].get("statut")}


def report(results):
    lines = []
    for c in results:
        if "erreur" in c: lines.append(f"## {c['id']} : ERREUR {c['erreur']}"); continue
        lines.append(f"## {c['id']} ({c['usage']}) — mods en commun {c['score_mods']}")
        lines.append(f"robot : {c['capacite_centrale_robot']} ; défense {c['defense_robot']} ; {c['statut_robot']}")
        lines.append(f"manquants : {', '.join(c['mods_manquants']) or '-'}")
        lines.append(f"en trop   : {', '.join(c['mods_en_trop']) or '-'}")
        h = c["helminth"]
        lines.append(f"Helminth  : réf. {h['reference']} (remplace {h['remplace_reference']}) / robot {h['robot']} (remplace {h['remplace_robot']})")
        lines.append(f"arcanes   : réf. {c['arcanes']['reference']} / robot {c['arcanes']['robot']}")
        lines.append("stats     : " + " ; ".join(f"{s} {v['reference']} / {v['robot']}" for s, v in c["stats"].items()))
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True); ap.add_argument("--data", required=True); ap.add_argument("--id")
    a = ap.parse_args()
    from .tools import Toolbox
    tb = Toolbox(os.path.join(a.data, "warframe.sqlite"), os.path.join(a.data, "docs.sqlite"), a.base)
    print(report([compare(tb, r) for r in load(a.base, a.id)]))


if __name__ == "__main__":
    main()
