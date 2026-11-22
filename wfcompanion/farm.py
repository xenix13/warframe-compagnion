"""Génère les fichiers Markdown « Farm - … » (pour le RAG) à partir des tables de drop."""
import collections, datetime, glob, json, os, re

KEEP = {"Farm - Principes et limites.md"}  # écrit à la main : jamais supprimé ni réécrit

LABELS = (
    ("ennemi", 8, "Ennemis et activités (taux par ennemi tué ou par coffre/récompense d'activité ; pour un ennemi, déjà multiplié par son taux de drop)"),
    ("mission", 10, "Missions et récompenses (taux par tirage de la rotation indiquée)"),
    ("relique", 8, "Reliques du Vide (Intact)"),
)
PLAN_RE = re.compile(r"Blueprint|Prime|Neuroptics|Chassis|Systems|Barrel|Receiver|Stock|Blade|Handle|Hilt|Link|String|Limb|Grip|"
                     r"Gauntlet|Ornament|Pouch|Head|Boot|Guard|Stars|Disc|Lens|Carapace|Cerebrum|Band|Buckle|Strap|Chain|Core|"
                     r"Harness|Heatsink|Kubrow|Kavat|Specter|Mk\s?I|Sigil|Glyph|Scene|Captura|Skin|Syandana|Armor|Helmet")


def _j(raw, n):
    with open(os.path.join(raw, n), encoding="utf-8") as f:
        return json.load(f)


def _clean(s):
    return re.sub(r"<[^>]+>", "", s).strip()


def _norm_item(i):
    i = i.strip()
    m = re.match(r"^([\d,]+)X (.+)$", i)
    return (m.group(2), m.group(1)) if m else (i, None)


def build(raw, out_dir, today=None):
    today = today or datetime.date.today()
    D = _j(raw, "drops_all.slim.json")
    mods = _j(raw, "Mods.json"); arc = _j(raw, "Arcanes.json"); res = _j(raw, "Resources.json")
    rba = _j(raw, "drops_resourceByAvatar.json")["resourceByAvatar"]
    info = _j(raw, "drops_info.json")
    tables_date = datetime.datetime.fromtimestamp(info["timestamp"] / 1000, datetime.timezone.utc).date()

    modn = {m["name"] for m in mods if m.get("name")}
    arcn = {a["name"] for a in arc} | {"Arcane " + a["name"] for a in arc}
    resn = {r["name"] for r in res} | {i["item"] for a in rba for i in a["items"]
                                        if not re.search(r"Region Resource|Blueprint", i["item"])}
    desc = {m["name"]: m.get("description", "") for m in _j(raw, "Misc.json")}
    desc.update({r["name"]: r.get("description", "") for r in res})

    idx = collections.defaultdict(list)
    for x in D:
        it, q = _norm_item(x["item"]); p = _clean(x["place"])
        try: ch = float(x["chance"])
        except (TypeError, ValueError): continue
        if p.endswith(" Relic"): cat = "relique"
        elif ("Rotation" in p or ("/" in p and "(" in p) or "Bounty" in p or p in ("Sorties", "Arbitrations")
              or p.startswith("Sortie")): cat = "mission"
        else: cat = "ennemi"
        extra = ""
        if "stage" in x: extra = f", étape {x['stage']}" + (f" à {x['maxStage']}" if x.get("maxStage") else "")
        idx[it].append((cat, p + extra, x["rarity"], ch, q))
    have = {(_clean(x["place"]).split(" (")[0], _norm_item(x["item"])[0]) for x in D}
    for a in rba:
        for i in a["items"]:
            if (a["source"], i["item"]) in have or i.get("chance") is None: continue
            idx[i["item"]].append(("ennemi", a["source"], i["rarity"], float(i["chance"]), None))

    def sec(rows, cat, n, label):
        r = sorted([(p, ra, ch, q) for c, p, ra, ch, q in rows if c == cat], key=lambda t: -t[2])
        seen, out = set(), []
        for p, ra, ch, q in r:
            if (p, ch) in seen: continue
            seen.add((p, ch)); out.append((p, ra, ch, q))
        if not out: return None
        s = "; ".join(f"{p} ({ra}, {ch:g} %{', x' + q if q else ''})" for p, ra, ch, q in out[:n])
        tot = len(out)
        return (f"  - {label} ({tot} source{'s' if tot > 1 else ''}, meilleures d'abord) : {s}"
                + (f" ; … (+{tot - n} autres)" if tot > n else ""))

    def entry(it):
        out = [f"### {it}"]
        if it in resn:
            loc = re.search(r"Location:\s*(.+)", desc.get(it, ""))
            if loc: out.append("  - Lieux d'après la description en jeu : " + loc.group(1).strip())
        for cat, n, label in LABELS:
            s = sec(idx[it], cat, n, label)
            if s: out.append(s)
        return "\n".join(out)

    def kind(it):
        if it in modn: return "mods"
        if it in arcn: return "arcanes"
        if it in resn: return "ressources"
        if PLAN_RE.search(it): return "plans"
        return "autres"

    groups = collections.defaultdict(list)
    for it in sorted(idx, key=str.lower):
        groups[kind(it)].append(it)

    head = (f"Source : tables de drop officielles de Warframe (WFCD warframe-drop-data, version du {tables_date:%d/%m/%Y}), "
            f"générées automatiquement le {today:%d/%m/%Y}. Les taux changent à chaque mise à jour du jeu. "
            "Pour un ennemi, le taux est celui d'un tirage sur un ennemi tué, déjà multiplié par le taux de drop de l'ennemi ; "
            "la même rubrique contient aussi des coffres et des récompenses d'activités (Archimedea, Netracells, etc.). "
            "Pour une mission, le taux est celui de la récompense dans la rotation indiquée. Le taux ne dit rien de la vitesse "
            "du farm : voir « Farm - Principes et limites ».\n")

    os.makedirs(out_dir, exist_ok=True)
    for old in glob.glob(os.path.join(out_dir, "Farm - *.md")):
        if os.path.basename(old) not in KEEP:
            os.unlink(old)
    written = []

    def split(kn, title, d, maxb=180000):
        chunks, cur, sz = [], [], 0
        for i in groups[kn]:
            e = len(entry(i)) + 3
            if sz + e > maxb and cur: chunks.append(cur); cur, sz = [], 0
            cur.append(i); sz += e
        if cur: chunks.append(cur)
        for n, c in enumerate(chunks, 1):
            name = f"Farm - {kn} (partie {n} sur {len(chunks)})" if len(chunks) > 1 else f"Farm - {kn}"
            t = f"# {title} : {c[0]} à {c[-1]}\n\n{d}\n\n{head}\n" + "\n\n".join(entry(i) for i in c) + "\n"
            with open(os.path.join(out_dir, name + ".md"), "w", encoding="utf-8") as f:
                f.write(t)
            written.append(name + ".md")

    split("mods", "Où farmer les mods", "Pour chaque mod : ennemis qui le lâchent, missions et récompenses, reliques.")
    split("arcanes", "Où farmer les arcanes", "Pour chaque arcane : ennemis et activités, missions et récompenses, reliques.")
    split("ressources", "Où farmer les ressources", "Pour chaque ressource : lieux, ennemis, missions et récompenses.")
    split("plans", "Où farmer les plans, pièces et accessoires", "Plans de warframes et d'armes, pièces Prime, cosmétiques.")
    split("autres", "Où farmer les autres objets", "Objets divers (Endo, crédits, essences, sculptures, etc.).")
    written.append(_no_drop_mods(mods, set(idx), out_dir, tables_date))
    return written


FAMILY_NOTES = {
    "Primed": "D'après le wiki (« Primed Mods ») : la plupart sont vendus par Baro Ki'Teer contre des Ducats et des crédits, selon son inventaire du moment ; Primed Fury, Primed Vigor, Primed Shred et Primed Sure Footed ne viennent que des récompenses de connexion quotidienne (jours 200, 400, 600, 900), non échangeables.",
    "Galvanized": "D'après le wiki (« Galvanized Mods ») : achetés au rang 0 chez le vendeur des Arbitrations (salle des Arbiters of Hexis, dans n'importe quel relais) pour 20 Vitus Essence chacun.",
    "Amalgam": "D'après le wiki (« Amalgam Mods ») : récompenses des Thermia Fractures et autres sources listées sur la page.",
    "Archon": "D'après le wiki (« Archon Mods ») : vendus par Chipper de Kahl's Garrison pour 40 Stock (rang 3, Fort).",
    "Autre": "Pas de table de drop officielle : vendeurs de syndicats, quêtes, événements, Nightwave, Archimedea, boutique, etc. La source n'est pas dans la base : ne pas l'inventer, chercher la page du mod sur le wiki.",
}


def _no_drop_mods(mods, dropped, out_dir, tables_date):
    by = {}
    for m in mods:
        n = m.get("name")
        if n and n not in dropped: by.setdefault(n, m)

    def fam(n):
        for p in ("Primed", "Galvanized", "Amalgam"):
            if n.startswith(p): return p
        return "Archon" if n.startswith("Archon ") else "Autre"
    g = collections.defaultdict(list)
    for n, m in by.items(): g[fam(n)].append((n, m))
    out = [f"# Où trouver les mods sans table de drop\n\nMods des données du jeu absents des tables de drop officielles "
           f"(version du {tables_date:%d/%m/%Y}). Ils ne tombent ni sur les ennemis ni en récompense de mission.\n"]
    for f in ("Primed", "Galvanized", "Amalgam", "Archon", "Autre"):
        out.append(f"## Famille : {f} ({len(g[f])} mods)\n\n{FAMILY_NOTES[f]}\n")
        for n, m in sorted(g[f], key=lambda t: t[0].lower()):
            out.append(f"- **{n}** ({m.get('compatName', '?')}, {m.get('rarity', '?')}, "
                       f"{'échangeable' if m.get('tradable') else 'non échangeable'})")
        out.append("")
    name = "Farm - mods sans table de drop.md"
    with open(os.path.join(out_dir, name), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    return name
