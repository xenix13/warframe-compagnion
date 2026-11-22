"""Loadouts enregistrés : un build, sa synthèse (rôle, boucle, mécaniques), sa conversation, et son historique de versions.

Dossier : <base>/06-builds-joueur/<nom>/
    loadout.json  : toutes les versions (build, synthèse, raison du changement, instantané des données du jeu)
    <nom>.md      : fiche lisible (et indexée pour la recherche de l'agent), régénérée à chaque sauvegarde

L'instantané garde, au moment de la sauvegarde, l'effet de chaque mod et arcane du build et les stats de base de la
warframe et des armes. En rouvrant le loadout, on compare à la base actuelle : tout ce qui a changé depuis (mod modifié,
supprimé, stats revues) est listé, ainsi que les notes de patch postérieures qui citent un élément du build.
"""
import datetime, glob, json, os, re, unicodedata

DIR = "06-builds-joueur"
SECTIONS = ("Objectif et rôle", "Boucle de jeu", "Mécaniques clés", "Survie", "Énergie", "Points faibles", "Alternatives", "À tester")


def slug(title):
    s = unicodedata.normalize("NFKD", title or "loadout").encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\- ]", "", s).strip()
    return re.sub(r"\s+", " ", s)[:80] or "loadout"


def _path(base, name):
    p = os.path.join(base, DIR, slug(name), "loadout.json")
    if not os.path.exists(p):  # nom tapé avec une autre casse
        for d in glob.glob(os.path.join(base, DIR, "*", "loadout.json")):
            if os.path.basename(os.path.dirname(d)).lower() == slug(name).lower(): return d
    return p


def _items(build):
    """Tous les éléments nommés du build, par nature."""
    mods = [build.get("aura"), build.get("exilus")] + list(build.get("mods") or [])
    arcanes = list(build.get("arcanes") or [])
    weapons = []
    for slot, spec in (build.get("armes") or {}).items():
        for spec in (spec if isinstance(spec, list) else [spec]):  # armes exaltées : une liste
            _weapon_items(spec, mods, arcanes, weapons)
    return [m for m in mods if m], [a for a in arcanes if a], weapons


def _weapon_items(spec, mods, arcanes, weapons):
    if isinstance(spec, dict):
        if spec.get("nom"): weapons.append(spec["nom"])
        mods += [spec.get("exilus")] + list(spec.get("mods") or [])
        if spec.get("arcane"): arcanes.append(spec["arcane"])
    elif isinstance(spec, str) and spec:
        weapons.append(spec)


def snapshot(tb, build):
    mods, arcanes, weapons = _items(build)
    snap = {"date": datetime.date.today().isoformat(), "mods": {}, "arcanes": {}, "armes": {}, "warframe": None}
    for m in mods:
        r = tb.fiche_mod(m)
        snap["mods"][m] = r["mods"][-1]["effets_rang_max"] if "erreur" not in r else None
    for a in arcanes:
        r = tb.fiche_arcane(a).get("arcanes", [])
        hit = [x for x in r if x["nom"].lower() == a.lower()] or r[:1]
        snap["arcanes"][a] = hit[0]["effet_rang_max"] if hit else None
    for w in weapons:
        f = tb.fiche_arme(w)
        snap["armes"][w] = None if "erreur" in f else {k: f.get(k) for k in ("totalDamage", "criticalChance", "criticalMultiplier", "procChance", "fireRate")}
    if build.get("warframe"):
        f = tb.fiche_warframe(build["warframe"])
        if "erreur" not in f:
            snap["warframe"] = {"rang_0": f["rang_0_donnees_du_jeu"], "couts": f.get("couts_des_capacites")}
    return snap


def changes(tb, base, build, snap):
    """Différences entre l'instantané sauvegardé et la base actuelle, et notes de patch postérieures."""
    now = snapshot(tb, build)
    out = []
    for kind, label in (("mods", "mod"), ("arcanes", "arcane"), ("armes", "arme")):
        for k, old in (snap.get(kind) or {}).items():
            new = now[kind].get(k)
            if old is not None and new is None: out.append(f"{label} « {k} » : n'existe plus dans les données actuelles")
            elif old != new and new is not None: out.append(f"{label} « {k} » a changé : avant {old} ; maintenant {new}")
    ow, nw = snap.get("warframe"), now.get("warframe")
    if ow and nw and ow != nw:
        if ow.get("rang_0") != nw.get("rang_0"): out.append(f"stats de base de {build.get('warframe')} changées : avant {ow['rang_0']} ; maintenant {nw['rang_0']}")
        if ow.get("couts") != nw.get("couts"): out.append(f"coûts des capacités de {build.get('warframe')} changés : avant {ow['couts']} ; maintenant {nw['couts']}")
    # notes de patch postérieures à la sauvegarde qui citent un élément du build
    since = snap.get("date") or "0000"
    mods, arcanes, weapons = _items(build)
    names = {n for n in mods + arcanes + weapons if n}
    if build.get("warframe"): names.add(re.sub(r"\s+(Prime|Umbra)$", "", build["warframe"]))
    notes = []
    for p in sorted(glob.glob(os.path.join(base, "03-patch-notes", "*.md"))):
        d = os.path.basename(p)[:10]
        if not re.match(r"\d{4}-\d{2}-\d{2}", d) or d <= since: continue
        with open(p, encoding="utf-8", errors="replace") as f:
            txt = f.read()
        hits = []
        for n in sorted(names):
            for line in txt.split("\n"):
                if re.search(r"\b" + re.escape(n) + r"\b", line, re.I):
                    hits.append(f"{n} : {line.strip()[:220]}"); break
        if hits: notes.append({"note": os.path.basename(p)[:-3], "mentions": hits[:12]})
    return {"changements_dans_les_donnees": out, "notes_de_patch_posterieures": notes,
            "sauvegarde_du": since, "a_jour": not out and not notes}


def load(base, name):
    p = _path(base, name)
    if not os.path.exists(p): return None
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def list_all(base):
    out = []
    for p in sorted(glob.glob(os.path.join(base, DIR, "*", "loadout.json"))):
        try:
            with open(p, encoding="utf-8") as f: d = json.load(f)
        except (OSError, json.JSONDecodeError): continue
        v = d["versions"][-1]
        out.append({"nom": d["nom"], "warframe": v["build"].get("warframe"), "versions": len(d["versions"]),
                    "derniere_modification": v["date"], "raison": v.get("raison", "")})
    return out


def save(tb, base, name, build, synthese="", raison="", conversation=None, validation=None):
    """Ajoute une version (l'ancienne est gardée dans l'historique)."""
    p = _path(base, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    d = load(base, name) or {"nom": name, "cree_le": datetime.date.today().isoformat(), "versions": [], "conversation": []}
    if not synthese and d["versions"]: synthese = d["versions"][-1].get("synthese", "")
    v = {"version": len(d["versions"]) + 1, "date": datetime.datetime.now().isoformat(timespec="minutes"),
         "raison": raison or ("création" if not d["versions"] else "modification"), "build": build, "synthese": synthese,
         "instantane": snapshot(tb, build), "jeu": _game_version(base)}
    d["versions"].append(v)
    if conversation is not None:
        d["conversation"] = (d.get("conversation") or []) + conversation
        d["conversation"] = d["conversation"][-40:]
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    _write_md(base, d, validation or tb.valider_build(build))
    return {"ok": True, "nom": name, "version": v["version"], "dossier": os.path.relpath(os.path.dirname(p), base)}


def _game_version(base):
    notes = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(base, "03-patch-notes", "*.md")))
    return notes[-1] if notes else "inconnue"


def _write_md(base, d, val):
    v = d["versions"][-1]; b = v["build"]
    lines = [f"# Loadout : {d['nom']}", "",
             f"**Statut : loadout du joueur, version {v['version']} du {v['date'][:10]}** (jeu : dernière note de patch en base « {v['jeu']} »). "
             "C'est un build daté : avant de le reproposer, vérifier les changements depuis cette date (outil ouvrir_loadout).", "",
             f"- Warframe : {b.get('warframe')} ; rôle : {b.get('role') or 'non précisé'} ; source d'énergie : {b.get('source_energie') or 'non précisée'}",
             f"- Statut du contrôle : {val.get('statut')}", ""]
    if val.get("tableau_a_recopier_tel_quel"): lines += ["## Build", "", val["tableau_a_recopier_tel_quel"], ""]
    if val.get("totaux"): lines += ["## Totaux [calcul]", "", "; ".join(f"{k} {x}" for k, x in val["totaux"].items()), ""]
    if val.get("consequences_calculees"): lines += ["## Ce que le build donne [calcul]", ""] + [f"- {c}" for c in val["consequences_calculees"]] + [""]
    if v.get("synthese"): lines += ["## Synthèse (explication du build)", "", v["synthese"].strip(), ""]
    lines += ["## Historique des versions", ""] + [f"- v{x['version']} ({x['date'][:10]}) : {x.get('raison', '')}" for x in d["versions"]]
    with open(os.path.join(base, DIR, slug(d["nom"]), f"{slug(d['nom'])}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


SYNTH_PROMPT = ("Écris la SYNTHÈSE de ce build pour la garder dans la fiche du loadout. Utilise exactement ces titres de section, "
                "en Markdown (### Titre), avec des phrases courtes et les chiffres des outils : " + ", ".join(SECTIONS) + ". "
                "Explique les mécaniques du jeu qui font marcher le build (capacités, augments, interactions, coûts canalisés, "
                "fragments, Helminth), pas seulement la liste des mods. N'invente rien : appelle valider_build sur le build si besoin. "
                "Réponds uniquement avec la synthèse.")


def update_prompt(name, d, ch):
    v = d["versions"][-1]
    return (f"Le loadout « {name} » a été sauvegardé le {v['date'][:10]} (version {v['version']}). Voici le build : "
            f"{json.dumps(v['build'], ensure_ascii=False)}\nSa synthèse :\n{v.get('synthese') or '(aucune)'}\n\n"
            f"Changements détectés depuis : {json.dumps(ch, ensure_ascii=False)}\n\n"
            "Mets ce build à jour : garde son intention (rôle, boucle de jeu), revérifie chaque élément touché par un changement "
            "avec les outils, remplace ce qui ne marche plus, puis valide le build complet avec valider_build. "
            "Explique en quelques lignes ce que tu as changé et pourquoi. S'il n'y a rien à changer, dis-le.")
