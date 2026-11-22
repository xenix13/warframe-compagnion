"""Régénère les fichiers « 01-donnees/mods/<Type> Mod.md » à partir de Mods.json.

Le fichier « Mod Set Mod.md » n'est jamais touché (il a été complété à la main).
Les étiquettes ATTENTION sur les mods qui n'existent pas en jeu sont conservées.
"""
import json, os, re

TYPES = ["Warframe Mod", "Primary Mod", "Secondary Mod", "Melee Mod", "Companion Mod", "Shotgun Mod", "Stance Mod",
         "Arch-Gun Mod", "Arch-Melee Mod", "Archwing Mod", "Necramech Mod", "Parazon Mod"]

# Mods confirmés inexistants en jeu par XeniX13 (retours de jeu, 13/11/2026)
CONFIRMED_FAKE = {
    "Primed Streamline": "[ATTENTION : n'existe pas en jeu (confirmé par XeniX13 le 13/11/2026) ; l'entrée vient des données du jeu mais n'a aucune date de sortie. Ne jamais l'utiliser dans un build]",
}
CONFIRMED_FAKE_EXPERT = {
    "Organ Shatter": "[ATTENTION : n'existe pas en jeu (confirmé par XeniX13 le 13/11/2026) : utiliser la version normale +90 %]",
}


def clean(s):
    s = s.replace("\\r", "").replace("\\n", " ")
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def line(x):
    ls = x.get("levelStats") or []
    stats = ls[-1]["stats"] if ls else []
    if not stats and x.get("description"): stats = [x["description"]]
    eff = " ; ".join(clean(t) for t in stats)
    cost = (x.get("baseDrain") or 0) + (x.get("fusionLimit") or 0)
    parts = [x.get("compatName") or "?", x.get("polarity") or "?", x.get("rarity") or "?", f"coût {cost} au rang max"]
    if x.get("isExilus") or x.get("isUtility"): parts.append("Exilus")
    if x.get("isAugment"): parts.append("Augment")
    s = f"- **{x['name']}** ({', '.join(parts)}) : {eff}"
    if x.get("modSet"):
        s += f" [fait partie d'un set : {x['modSet'].rsplit('/', 1)[-1]}]"
    return s.rstrip()


def weak_variant(u):
    """Versions affaiblies d'un mod (données « Beginner » ou « Intermediate ») : pas la version normale."""
    last = u.rsplit("/", 1)[-1]
    if "/Beginner/" in u or last.endswith("Beginner"): return "Beginner"
    if "/Intermediate/" in u or last.endswith("Intermediate"): return "Intermediate"
    return ""


def tags(x, std):
    u = x["uniqueName"]; r = x.get("fusionLimit"); t = []
    wk = weak_variant(u)
    if wk: t.append(f"[variante affaiblie du jeu : {wk}, rang max {r} ; ce n'est pas la version normale du mod]")
    if "/Expert/" in u:
        if not x["name"].startswith(("Primed", "Amalgam")) and (x["name"], x["type"]) in std:
            t.append(CONFIRMED_FAKE_EXPERT.get(x["name"],
                     f"[ATTENTION : variante Expert (rang max {r}) d'un mod qui existe en version normale ; très probablement "
                     "absente du jeu (même cas qu'Organ Shatter +165 %, confirmé inexistant par XeniX13) : utiliser la version normale]"))
        else:
            t.append(f"[variante du jeu : Expert, rang max {r}]")
    if not x.get("introduced"):
        t.append(CONFIRMED_FAKE.get(x["name"], "[ATTENTION : aucune date de sortie dans les données du jeu, ce mod n'est "
                                     "peut-être pas disponible en jeu : à vérifier avant de l'utiliser]"))
    return " ".join(t)


def build(raw, out_dir):
    with open(os.path.join(raw, "Mods.json"), encoding="utf-8") as f:
        D = [x for x in json.load(f) if x.get("name")]
    std = {(x["name"], x["type"]) for x in D if "/Expert/" not in x["uniqueName"] and not weak_variant(x["uniqueName"])}
    os.makedirs(out_dir, exist_ok=True)
    written = []
    for t in TYPES:
        ls = []
        for x in D:
            if x.get("type") != t: continue
            tg = tags(x, std)
            ls.append(line(x) + (" " + tg if tg else ""))
        ls.sort(key=lambda l: (re.search(r"\(([^,]+),", l).group(1).lower(), l.lower()))
        name = f"{t}.md"
        title = t.replace(" Mod", " Mods")
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write(f"# {title} (valeurs au rang maximum)\n\nGénéré automatiquement depuis les données du jeu "
                    "(WFCD warframe-items). Ne pas modifier à la main : les retours de jeu vont dans 04-retours-experience.\n\n"
                    + "\n".join(ls) + "\n")
        written.append(name)
    return written
