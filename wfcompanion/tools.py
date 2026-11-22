"""Outils que l'agent peut appeler. Peu nombreux et simples, pour qu'un petit modèle s'en serve bien.

Chaque outil renvoie un petit dictionnaire (ou un message d'erreur clair) : le modèle ne calcule rien
et ne cite aucune valeur de mémoire.
"""
import glob, json, os, re

from . import calc, db, docs, rules
from .mods_md import clean, tags, weak_variant


class Toolbox:
    def __init__(self, sqlite_path, docs_path, base=None):
        self.con = db.connect(sqlite_path)
        self.docs_path = docs_path
        self.base = base
        rows = [json.loads(r["data"]) for r in self.con.execute("SELECT data FROM mods")]
        self._std = {(x["name"], x["type"]) for x in rows
                     if "/Expert/" not in x["uniqueName"] and not weak_variant(x["uniqueName"])}

    # ------------------------------------------------------------------ mods
    def _mod_card(self, m):
        ls = m.get("levelStats") or []
        effects = [clean(t) for t in (ls[-1]["stats"] if ls else [m.get("description", "")])]
        stats, other = calc.parse_mod_effects(effects)
        card = {"nom": m["name"], "pour": m.get("compatName"), "polarite": m.get("polarity"), "rarete": m.get("rarity"),
                "cout_rang_max": (m.get("baseDrain") or 0) + (m.get("fusionLimit") or 0),
                "rang_max": m.get("fusionLimit"), "effets_rang_max": effects}
        if stats: card["stats_additionnables"] = stats
        if other: card["effets_conditionnels_ou_speciaux"] = other
        if m.get("isExilus") or m.get("isUtility"): card["exilus"] = True
        if m.get("isAugment") and (m.get("compatName") or "").upper() not in ("WARFRAME", "AURA", "ANY", ""):
            card["augment_de"] = m.get("compatName")
        if m.get("modSet"): card["set"] = m["modSet"].rsplit("/", 1)[-1]
        t = tags(m, self._std)
        if t: card["avertissement"] = t
        return card

    def fiche_mod(self, nom):
        rows = [json.loads(r["data"]) for r in self.con.execute("SELECT data FROM mods WHERE name = ? COLLATE NOCASE", (nom,))]
        if not rows:
            close = [r["name"] for r in self.con.execute(
                "SELECT DISTINCT name FROM mods WHERE name LIKE ? LIMIT 8", (f"%{nom}%",))]
            return {"erreur": f"aucun mod nommé « {nom} »", "noms_proches": close,
                    "conseil": "si c'est un effet et pas un nom de mod, utilise chercher_mods ; effets valides : " + EFFECTS_HINT}
        fake = lambda c: "n'existe pas" in c.get("avertissement", "") or "probablement absente" in c.get("avertissement", "")
        cards = [self._mod_card(m) for m in rows]
        real = [c for c in cards if not fake(c)]
        if not real:
            return {"erreur": f"« {nom} » figure dans les données mais n'existe pas en jeu : ne pas l'utiliser",
                    "detail": cards[0].get("avertissement")}
        normal = [c for c in real if "variante affaiblie" not in c.get("avertissement", "")] or real
        for c in normal:
            if "variante du jeu" in c.get("avertissement", ""):
                c["variante"] = c.pop("avertissement")
        return {"mods": normal}

    def chercher_mods(self, effet, pour=None, limite=12):
        effet = SYNONYMS.get(effet.strip().lower(), effet.strip())
        if pour and pour.strip().lower() in ("warframe", "frame"): pour = "WARFRAME"
        q = "SELECT data FROM mods WHERE variant IN ('', 'Expert') AND data LIKE ?"
        args = [f"%{effet}%"]
        if pour:
            q += " AND (compat LIKE ? OR type LIKE ?)"; args += [f"%{pour}%", f"%{pour}%"]
        res = []
        for r in self.con.execute(q, args):
            m = json.loads(r["data"]); c = self._mod_card(m)
            if any(effet.lower() in e.lower() for e in c["effets_rang_max"]) and not any(
                    w in c.get("avertissement", "") for w in ("ATTENTION", "affaiblie")):
                res.append({"nom": c["nom"], "pour": c["pour"], "cout": c["cout_rang_max"], "effets": c["effets_rang_max"]})
        res.sort(key=lambda c: c["nom"])
        if not res:
            return {"erreur": f"aucun mod avec l'effet « {effet} »" + (f" pour « {pour} »" if pour else ""),
                    "conseil": "effets valides (en anglais) : " + EFFECTS_HINT}
        return {"effet": effet, "total": len(res), "mods": res[:limite]}

    # ------------------------------------------------------------------ fiches
    def fiche_warframe(self, nom):
        r = self.con.execute("SELECT data FROM warframes WHERE name = ? COLLATE NOCASE", (nom,)).fetchone()
        if not r:
            close = [x["name"] for x in self.con.execute("SELECT name FROM warframes WHERE name LIKE ? LIMIT 8", (f"%{nom}%",))]
            return {"erreur": f"aucune warframe nommée « {nom} »", "noms_proches": close}
        w = json.loads(r["data"])
        base_name = re.sub(r"\s+(Prime|Umbra)$", "", w["name"])
        r30 = self.rank30(w)
        return {"nom": w["name"],
                "rang_0_donnees_du_jeu": {"sante": w.get("health"), "bouclier": w.get("shield"), "armure": w.get("armor"), "energie": w.get("power")},
                "rang_30_sans_mod": r30,
                "profil_de_survie": self.survival_profile(r30),
                "vitesse_sprint": w.get("sprintSpeed"), "polarite_aura": w.get("aura"), "polarite_exilus": w.get("exilusPolarity"), "polarites": w.get("polarities"),
                "passif": self.passive_detail(base_name) or re.sub(r"<[^>]+>", "", w.get("passiveDescription") or ""),
                "ressource": (self.costs_data(base_name) or {}).get("note_ressource") or "énergie",
                "couts_des_capacites": ({f"{c['numero']} {c['nom']}": (c["cout_affiche_wiki"] or "pas de coût en énergie")
                                         for c in self.costs_data(base_name)["capacites"]} if self.costs_data(base_name)
                                        else {k: v[1] for k, v in self.ability_costs(base_name).items()}),
                "lecture_des_couts": "« +X/s » = capacité canalisée, X par seconde tant qu'elle est maintenue ; « +X/shot », "
                                     "« /enemy » = coût par action. Voir calculer(cout_canalise).",
                "capacites": [{"nom": a["name"], "description": a.get("description")} for a in w.get("abilities", [])],
                **self._exalted_info(w),
                "note": "le passif compte dans le build ; les chiffres détaillés des capacités sont dans dossier_build"}

    def armes_exaltees(self, warframe):
        """Armes données par une capacité de la warframe (exaltées), et griffes de Garuda (emplacement de mêlée)."""
        r = self.con.execute("SELECT data FROM warframes WHERE name = ? COLLATE NOCASE", (warframe,)).fetchone()
        if not r: return []
        w = json.loads(r["data"])
        parts = (w.get("uniqueName") or "").split("/")
        if len(parts) < 4: return []
        rows = [json.loads(x["data"]) for x in self.con.execute(
            "SELECT data FROM weapons WHERE type = 'Exalted Weapon' AND unique_name LIKE ?", ("/Lotus/Powersuits/" + parts[3] + "/%",))]
        variant = "Umbra" if "Umbra" in w["name"] else "Prime" if "Prime" in w["name"] else None
        pick = lambda v: [x for x in rows if (v in x["name"] if v else not re.search(r"\b(Prime|Umbra)\b", x["name"]))]
        chosen = pick(variant) or pick(None)
        return [{"nom": x["name"], "emplacement": {"Melee": "melee", "Primary": "principale", "Secondary": "secondaire"}[x["category"]],
                 "griffes_garuda": "Garuda" in x["name"] and "Talons" in x["name"]} for x in sorted(chosen, key=lambda x: x["name"])]

    def exalted_rule(self, name):
        """Règle de l'arme exaltée (puissance, portée, combo) dans 01-donnees/armes-exaltees.json, modifiable à la main."""
        path = os.path.join(self.base or "", "01-donnees", "armes-exaltees.json")
        try:
            with open(path, encoding="utf-8") as f: d = json.load(f)
        except (OSError, json.JSONDecodeError): return None
        return d.get(re.sub(r"\s+Prime\b", "", name)) or d.get(name.replace("Prime ", ""))

    def _exalted_info(self, w):
        ex = self.armes_exaltees(w["name"])
        if not ex: return {}
        out = {}
        talons = [x["nom"] for x in ex if x["griffes_garuda"]]
        others = [f"{x['nom']} ({x['emplacement']})" for x in ex if not x["griffes_garuda"]]
        if talons:
            out["arme_de_melee_imposee"] = (f"{talons[0]} : ce n'est pas une arme exaltée, elles occupent l'emplacement de mêlée "
                                            "de Garuda (pas d'autre arme de mêlée possible). À moder comme une arme de mêlée, dans armes.melee.")
        if others:
            out["armes_exaltees"] = others
            out["note_armes_exaltees"] = ("arme donnée par une capacité, modée à part (8 mods, Exilus, arcane de son type depuis l'Update 38.5) : "
                                          "à mettre dans armes.exaltees du build ; ses mods ne touchent pas les armes normales")
        return out

    def fiche_arme(self, nom):
        r = self.con.execute("SELECT data FROM weapons WHERE name = ? COLLATE NOCASE", (nom,)).fetchone()
        if not r:  # un seul résultat proche : on le prend (ex. « nikana prime » mal orthographié)
            near = self.con.execute("SELECT data FROM weapons WHERE name LIKE ? AND type NOT LIKE '%Component%'", (f"%{nom}%",)).fetchall()
            if len(near) == 1: r = near[0]
        if not r:
            close = [x["name"] for x in self.con.execute("SELECT name FROM weapons WHERE name LIKE ? LIMIT 8", (f"%{nom}%",))]
            return {"erreur": f"aucune arme nommée « {nom} »", "noms_proches": close,
                    "conseil": "pour trouver une arme, utilise chercher_armes(categorie=principale|secondaire|melee, tri=critique|statut|degats)"}
        w = json.loads(r["data"])
        keep = ("name", "category", "type", "totalDamage", "criticalChance", "criticalMultiplier", "procChance", "fireRate",
                "range", "magazineSize", "reloadTime", "multishot", "disposition", "masteryReq", "polarities", "stancePolarity",
                "heavyAttackDamage", "slamAttack", "slamRadius", "followThrough", "comboDuration", "noise", "trigger", "damage")
        out = {k: (round(v, 3) if isinstance(v, float) else v) for k, v in w.items() if k in keep}
        out["attaques"] = [{k: a.get(k) for k in ("name", "crit_chance", "crit_mult", "status_chance", "speed", "damage")}
                           for a in (w.get("attacks") or [])[:3]]
        return out

    CAT = {"principale": "Primary", "primaire": "Primary", "primary": "Primary", "fusil": "Primary",
           "secondaire": "Secondary", "secondary": "Secondary", "pistolet": "Secondary",
           "melee": "Melee", "mêlée": "Melee", "melée": "Melee", "corps a corps": "Melee", "corps à corps": "Melee"}
    TRI = {"critique": "criticalChance", "crit": "criticalChance", "multiplicateur": "criticalMultiplier",
           "statut": "procChance", "status": "procChance", "degats": "totalDamage", "dégâts": "totalDamage",
           "disposition": "disposition", "cadence": "fireRate", "vitesse": "fireRate", "portee": "range", "portée": "range"}

    def _weapon_summary(self, w):
        dmg = {k: round(v, 1) for k, v in (w.get("damage") or {}).items() if k not in ("total",) and isinstance(v, (int, float)) and v > 0}
        main = max(dmg, key=dmg.get) if dmg else None
        out = {"nom": w["name"], "type": w.get("type"), "maitrise": w.get("masteryReq"),
               "critique": f"{round((w.get('criticalChance') or 0) * 100)} % x{round(w.get('criticalMultiplier') or 0, 2)}",
               "statut": f"{round((w.get('procChance') or 0) * 100)} %", "degats": round(w.get("totalDamage") or 0, 1),
               "degat_principal": main, "disposition_riven": w.get("disposition")}
        if w.get("category") == "Melee": out["portee_m"] = w.get("range")
        else: out["cadence"] = round(w.get("fireRate") or 0, 2)
        if "Incarnon" in json.dumps(w.get("tags") or []) or "Incarnon" in (w.get("name") or ""): out["incarnon"] = True
        return out

    def chercher_armes(self, categorie, tri="critique", nom=None, limite=12):
        """Liste des armes d'une catégorie, triées par une stat (critique, statut, dégâts, disposition, cadence, portée)."""
        cat = self.CAT.get((categorie or "").strip().lower())
        if not cat:
            return {"erreur": f"catégorie inconnue : {categorie}", "categories": ["principale", "secondaire", "melee"]}
        key = self.TRI.get((tri or "critique").strip().lower(), "criticalChance")
        q = "SELECT data FROM weapons WHERE category = ? AND type NOT LIKE '%Component%' AND type != 'Exalted Weapon'"
        args = [cat]
        if nom: q += " AND name LIKE ?"; args.append(f"%{nom}%")
        rows = [json.loads(r["data"]) for r in self.con.execute(q, args)]
        rows = [w for w in rows if w.get("masterable", True) and (w.get("totalDamage") or 0) > 0]
        rows.sort(key=lambda w: -(w.get(key) or 0))
        return {"categorie": categorie, "tri": tri, "total": len(rows), "armes": [self._weapon_summary(w) for w in rows[:limite]],
                "note": "stats de base (sans mod) ; choisir l'arme selon son rôle dans le build, pas seulement sa stat la plus haute"}

    def fiche_arcane(self, nom):
        rows = [json.loads(r["data"]) for r in self.con.execute(
            "SELECT data FROM arcanes WHERE name LIKE ? LIMIT 5", (f"%{nom}%",))]
        if not rows: return {"erreur": f"aucun arcane contenant « {nom} »"}
        return {"arcanes": [{"nom": a["name"], "type": a.get("type"), "rarete": a.get("rarity"),
                             "effet_rang_max": [clean(s) for s in (a.get("levelStats") or [{}])[-1].get("stats", [])]}
                            for a in rows]}

    def archetypes(self, warframe):
        """Archétypes de build préparés pour la warframe (01-donnees/archetypes/<warframe>.json) : boucle de jeu, survie,
        énergie, pièces du noyau, choix à faire, pièges. Écrits hors ligne, relus par le joueur."""
        base_name = re.sub(r"\s+(Prime|Umbra)$", "", (warframe or "").strip())
        path = os.path.join(self.base or "", "01-donnees", "archetypes", base_name + ".json")
        if not os.path.exists(path):
            for p in glob.glob(os.path.join(self.base or "", "01-donnees", "archetypes", "*.json")):
                if os.path.basename(p)[:-5].lower() == base_name.lower(): path = p
        try:
            with open(path, encoding="utf-8") as fh: d = json.load(fh)
        except (OSError, json.JSONDecodeError):
            return {"erreur": f"pas d'archétype préparé pour {base_name} : raisonne à partir du dossier"}
        d["consigne"] = ("Choisis l'archétype dont l'objectif correspond à la demande, garde son noyau, fais les choix proposés "
                         "en comparant les options, respecte les pièges, puis valide. Les éléments [à vérifier] doivent être "
                         "présentés comme tels au joueur.")
        return d

    def proposer_build(self, warframe, objectif="", defense="bouclier", niveau="endgame"):
        """Build complet calculé par le programme à partir de l'archétype qui correspond à l'objectif (déjà validé).
        niveau : debutant | intermediaire | endgame ; tient compte du profil du joueur (ce qu'il possède)."""
        from . import optimizer, niveaux
        return optimizer.propose(self, warframe, objectif, defense, None, niveau, niveaux.load_profile(self.base))

    def dossier_build(self, warframe):
        """Tout ce qu'il faut pour réfléchir un build, en un seul appel."""
        f = self.fiche_warframe(warframe)
        if "erreur" in f: return f
        name = f["nom"]; base_name = re.sub(r"\s+(Prime|Umbra)$", "", name)
        out = {"warframe": {k: v for k, v in f.items() if k not in ("capacites", "note")}}
        arch = self.archetypes(name)
        if "erreur" not in arch:  # savoir déjà structuré : il passe avant les extraits du wiki
            out["archetypes"] = arch
        caps = []
        if self.base:
            for p in sorted(glob.glob(os.path.join(self.base, "02-wiki", "warframes", base_name, "Capacit*.md"))):
                with open(p, encoding="utf-8", errors="replace") as fh:
                    txt = fh.read()
                body = txt.split("\n", 2)[-1].strip()
                caps.append({"capacite": os.path.basename(p)[len("Capacité - "):-3],
                             "chiffres_et_fonctionnement": body[:400 if "archetypes" in out else 900]})
        out["capacites"] = caps or f["capacites"]
        out["augments"] = []
        for r in self.con.execute("SELECT data FROM mods WHERE compat = ? COLLATE NOCASE AND variant = ''", (base_name,)):
            c = self._mod_card(json.loads(r["data"]))
            a = {"nom": c["nom"], "cout": c["cout_rang_max"], "effet": c["effets_rang_max"]}
            n = self.augment_notes(c["nom"])
            if n and "archetypes" not in out: a["fonctionnement"] = n  # l'archétype explique déjà les augments
            ch = self.channeled().get(c["nom"])
            if ch: a["cout_en_energie"] = ch
            out["augments"].append(a)
        fb = docs.search(self.docs_path, base_name, limit=3, max_chars=500, file_like=f"04-retours-experience/%{base_name}%")
        fb += [x for x in docs.search(self.docs_path, base_name, limit=3, max_chars=500,
                                      file_like="04-retours-experience/Retours du joueur%") if base_name.lower() in (x["titre"] + x["extrait"]).lower()]
        out["retours_du_joueur_sur_cette_frame"] = fb or "aucun : pas de build de référence, raisonner depuis les capacités"
        pr = rules.for_frame(self.base, base_name)
        if any(pr[k] for k in ("obligatoires", "interdits", "notes")) or pr["focus"]:
            out["avis_du_joueur_sur_cette_frame"] = {**pr, "lecture": "avis avec leur raison, pas des règles absolues : comprends la raison, applique-la si elle vaut pour ton build, sinon explique"}
        out["mods_de_warframe_par_stat"] = self._mods_by_stat()
        if "archetypes" in out:  # garder le dossier court pour les petits modèles : 3 mods par stat suffisent
            out["mods_de_warframe_par_stat"] = {k: v[:3] for k, v in out["mods_de_warframe_par_stat"].items()}
        out["a_faire_ensuite"] = ("1) choisir le rôle et la boucle de jeu ; 2) fixer 2 stats prioritaires ; 3) choisir les mods "
                                  "(fiche_mod pour vérifier chaque mod retenu) ; 4) défense au level cap ; 5) calculer les totaux avec "
                                  "calculer(stat_capacite) ; 6) comparer au moins deux options par choix important.")
        return out

    def _mods_by_stat(self):
        if getattr(self, "_by_stat", None): return self._by_stat
        keys = {"strength": "puissance", "duration": "duree", "range": "portee", "efficiency": "efficacite",
                "energy": "energie_max", "health": "sante", "shield": "bouclier", "armor": "armure"}
        acc = {v: [] for v in keys.values()}
        for r in self.con.execute("SELECT data FROM mods WHERE type = 'Warframe Mod' AND compat = 'WARFRAME'"):
            m = json.loads(r["data"])
            if weak_variant(m["uniqueName"]): continue
            c = self._mod_card(m)
            if "ATTENTION" in c.get("avertissement", ""): continue
            for k, v in c.get("stats_additionnables", {}).items():
                if k in keys and v > 0:
                    acc[keys[k]].append((v, c["nom"], c["cout_rang_max"], c["effets_rang_max"]))
        self._by_stat = {k: [{"nom": n, "cout": co, "effets": e} for _, n, co, e in sorted(v, key=lambda t: -t[0])[:7]]
                         for k, v in acc.items()}
        return self._by_stat

    def options(self, categorie):
        """Listes de choix pour les emplacements autres que les 8 mods."""
        cat = categorie.strip().lower()
        if cat in ("aura", "auras"):
            return {"auras": [{"nom": c["nom"], "polarite": c["polarite"], "effet": c["effets_rang_max"]} for c in
                              (self._mod_card(json.loads(r["data"])) for r in self.con.execute(
                                  "SELECT data FROM mods WHERE compat='AURA' AND variant='' ORDER BY name"))]}
        if cat in ("exilus",):
            return {"exilus": [{"nom": c["nom"], "cout": c["cout_rang_max"], "effet": [e[:90] for e in c["effets_rang_max"]]} for c in
                               (self._mod_card(json.loads(r["data"])) for r in self.con.execute(
                                   "SELECT data FROM mods WHERE compat='WARFRAME' AND is_exilus=1 AND variant IN ('', 'Expert') ORDER BY name"))
                               if "ATTENTION" not in c.get("avertissement", "")]}
        types = {"arcanes": ("Warframe Arcane",), "arcane": ("Warframe Arcane",), "arcanes_melee": ("Melee Arcane",),
                 "arcanes_principale": ("Primary Arcane", "Bow Arcane", "Shotgun Arcane"), "arcanes_secondaire": ("Secondary Arcane",)}
        if cat in types:
            return {cat: [{"nom": a["name"], "effet": clean((a.get("levelStats") or [{}])[-1].get("stats", [""])[0]).replace(" +1 Arcane Revive", "")[:100]}
                          for a in (json.loads(r["data"]) for r in self.con.execute(
                              f"SELECT data FROM arcanes WHERE type IN ({','.join('?' * len(types[cat]))}) ORDER BY name", types[cat]))]}
        if cat in ("fragments", "fragment", "shards", "archon"):
            from . import shards
            return {"fragments": shards.labels(), "note": "5 au maximum ; écrire le libellé tel quel dans le build (champ fragments)"}
        if cat in ("helminth",):
            h = self.helminth_abilities()
            return {"helminth": [f"{a} ({f})" for a, f in sorted(h.items())],
                    "notes_du_joueur": {k: v for k, v in self.helminth_notes().items() if not k.startswith("_")},
                    "note": "une capacité par warframe ; les chiffres sont dans chercher_doc"} if h else {"erreur": "liste indisponible"}
        if cat in ("compagnon", "compagnons"):
            return {"compagnons": [f"{n} ({t})" for n, t in self.companions()]}
        return {"erreur": f"catégorie inconnue : {categorie}", "categories": ["aura", "exilus", "arcanes", "fragments", "arcanes_melee",
                                                                              "arcanes_principale", "arcanes_secondaire",
                                                                              "helminth", "compagnon"]}

    # ------------------------------------------------------------------ stats au rang 30, passif, coûts
    ARMOR_RANK_EXCEPTIONS = ("Nidus", "Lavos", "Kullervo")

    def _energy_table(self):
        """Énergie au rang 0 et au rang 30 par warframe, lue dans la page Energy du wiki de la base."""
        if getattr(self, "_energy", None) is not None: return self._energy
        out = {}
        p = os.path.join(self.base or "", "02-wiki", "systemes", "Energy.md")
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="replace") as f:
                for line in f:
                    m = re.match(r"^([A-Z][\w' &-]+?) \| \d+ \| (\d+) \| (\d+)\s*$", line)
                    if m: out[m.group(1).lower()] = (int(m.group(2)), int(m.group(3)))
        self._energy = out
        return out

    def rank30(self, w):
        """Stats au rang 30 sans mod. Les données du jeu (et le codex) donnent le rang 0."""
        name = w["name"]; base_name = re.sub(r"\s+(Prime|Umbra)$", "", name)
        e = self._energy_table().get(name.lower())
        energy = e[1] if e else (w.get("power") or 0) + 50
        health = (w.get("health") or 0) + 100
        shield = (w.get("shield") or 0) + (100 if (w.get("shield") or 0) > 0 else 0)
        notes = ["énergie : " + ("table du wiki (page Energy)" if e else "règle habituelle +50, non vérifiée pour cette frame"),
                 "santé et bouclier : bonus de rang habituel +100 (page Health : « normalement +100, avec des exceptions »), à confirmer dans l'arsenal"]
        if base_name in self.ARMOR_RANK_EXCEPTIONS:
            notes.append("armure : cette frame gagne de l'armure avec le rang (page Armor) : la valeur au rang 30 est plus haute, voir l'arsenal")
        return {"sante": health, "bouclier": shield, "armure": w.get("armor") or 0, "energie": energy, "fiabilite": notes}

    def costs_data(self, base_name):
        """Coûts, canalisation, ressource et passif d'une warframe (01-donnees/couts-capacites.json, relevé du wiki)."""
        if getattr(self, "_costs", None) is None:
            try:
                with open(os.path.join(self.base or "", "01-donnees", "couts-capacites.json"), encoding="utf-8") as f:
                    self._costs = json.load(f)
            except (OSError, json.JSONDecodeError):
                self._costs = {}
        return self._costs.get(base_name)

    def passive_detail(self, base_name):
        d = self.costs_data(base_name)
        if d and d.get("passif"): return d["passif"][:700]
        p = os.path.join(self.base or "", "02-wiki", "warframes", base_name, f"{base_name} - capacités.md")
        if not os.path.exists(p): return None
        with open(p, encoding="utf-8", errors="replace") as f: txt = f.read(6000)
        m = re.search(r"## Passive\s*\n(.*?)(?=\n## )", txt, re.S)
        return re.sub(r"\n{2,}", " ", m.group(1)).strip()[:700] if m else None

    def ability_costs(self, base_name):
        """Coût de base de chaque capacité : {nom: (numéro, coût)}."""
        d = self.costs_data(base_name)
        if d:
            return {c["nom"]: (c["numero"], c["cout"]) for c in d["capacites"] if c.get("cout") is not None}
        out = {}
        for p in sorted(glob.glob(os.path.join(self.base or "", "02-wiki", "warframes", base_name, "Capacit*.md"))):
            with open(p, encoding="utf-8", errors="replace") as f: txt = f.read(600)
            m = re.search(r"\|\s*(\d)\s+(\d+)\s*\|", txt)
            if m: out[os.path.basename(p)[len("Capacité - "):-3]] = (int(m.group(1)), int(m.group(2)))
        return out

    def survival_profile(self, r30):
        a = r30["armure"]; dr = calc.player_armor_dr(a)
        level = "faible" if a < 300 else ("moyenne" if a < 600 else "élevée")
        txt = (f"armure {level} ({a:g}) : réduction de dégâts {round(dr * 100)} % ; santé effective environ "
               f"{round(r30['sante'] / (1 - dr))} sans mod")
        if r30["bouclier"]:
            txt += (f" ; bouclier {r30['bouclier']:g} avec 50 % de réduction (environ {round(r30['bouclier'] * 2)} effectifs) "
                    f"et un shield gate de {calc.shield_gate_duration(r30['bouclier']):.2f} s à bouclier plein")
        else:
            txt += " ; pas de bouclier, donc pas de shield gate"
        if a < 300: txt += ". Les mods et arcanes qui dépendent de l'armure rapportent peu sur cette frame."
        elif a >= 600: txt += ". Les effets qui dépendent de l'armure sont rentables sur cette frame."
        return txt

    def channeled(self):
        """Capacités canalisées connues (fichier 01-donnees/capacites-canalisees.json de la base)."""
        if getattr(self, "_chan", None) is None:
            try:
                with open(os.path.join(self.base or "", "01-donnees", "capacites-canalisees.json"), encoding="utf-8") as f:
                    self._chan = {k: v for k, v in json.load(f).items() if not k.startswith("_")}
            except (OSError, json.JSONDecodeError):
                self._chan = {}
        return self._chan

    def augment_notes(self, name, max_chars=900):
        """Notes de fonctionnement d'un augment (fichier 01-donnees/augments-notes.json, extrait du wiki).
        Les lignes qui parlent d'énergie, de canalisation ou de durée passent en premier : ce sont elles qui changent un build."""
        if getattr(self, "_aug", None) is None:
            try:
                with open(os.path.join(self.base or "", "01-donnees", "augments-notes.json"), encoding="utf-8") as f:
                    self._aug = json.load(f)
            except (OSError, json.JSONDecodeError):
                self._aug = {}
        txt = self._aug.get(name)
        if not txt: return None
        lines = [l for l in txt.split("\n") if l.strip()]
        key = [l for l in lines if re.search(r"energy|drain|channel|cost|per second|duration|cap of|maximum", l, re.I)]
        rest = [l for l in lines if l not in key]
        out, size = [], 0
        for l in key + rest:
            if size + len(l) > max_chars: break
            out.append(l.strip()); size += len(l)
        return "\n".join(out)

    def helminth_abilities(self):
        """Capacités transférables via le Helminth, lues dans les pages de capacités du wiki de la base."""
        if getattr(self, "_helminth", None) is not None: return self._helminth
        out = {}
        if self.base:
            for p in glob.glob(os.path.join(self.base, "02-wiki", "warframes", "*", "Capacit*.md")):
                try:
                    with open(p, encoding="utf-8", errors="replace") as fh: txt = fh.read(4000)
                except OSError: continue
                if "Subsumable to Helminth" in txt:
                    out[os.path.basename(p)[len("Capacité - "):-3]] = os.path.basename(os.path.dirname(p))
        # capacités relues dans modules/helminth.py dont la page manque dans la base (frame récente)
        from .modules import helminth as H
        for n, v in H.CAPACITES.items():
            if v.get("frame") and n not in out: out[n] = v["frame"]
        self._helminth = out
        return out

    def helminth_notes(self):
        try:
            with open(os.path.join(self.base or "", "01-donnees", "helminth-notes.json"), encoding="utf-8") as fh: return json.load(fh)
        except (OSError, json.JSONDecodeError): return {}

    def companions(self):
        return [(r["name"], r["type"]) for r in self.con.execute("SELECT name, type FROM companions WHERE type IN ('Pets', 'Sentinel') ORDER BY name")]

    def noter_retour(self, sujet, remarque):
        """Enregistre une remarque du joueur (correction, fait de jeu, préférence) pour les prochaines conversations."""
        import datetime
        if not self.base: return {"erreur": "base introuvable"}
        if len(remarque.strip()) < 15: return {"erreur": "remarque trop courte : recopie ce que le joueur a dit, en une ou deux phrases"}
        path = os.path.join(self.base, "04-retours-experience", "Retours du joueur notés par l'agent.md")
        new = not os.path.exists(path)
        with open(path, "a", encoding="utf-8") as f:
            if new:
                f.write("# Retours du joueur notés par l'agent\n\nRemarques dites par le joueur pendant les conversations, notées "
                        "telles quelles par l'agent. Statut : [dit par le joueur, non vérifié]. Les notes rédigées à la main dans "
                        "ce dossier priment sur celles-ci.\n")
            f.write(f"\n## {sujet.strip()}\n- {datetime.date.today():%d/%m/%Y} [dit par le joueur] : {remarque.strip()}\n")
        return {"ok": True, "note": "remarque enregistrée ; elle sera retrouvée par chercher_doc et dossier_build"}

    def noter_regle(self, warframe, type, nom="", raison="", si_role=None):
        """Enregistre une règle du joueur que valider_build imposera ensuite."""
        if not self.base: return {"erreur": "base introuvable"}
        f = self.fiche_warframe(warframe)
        frame = "*" if warframe.strip() in ("*", "toutes") else re.sub(r"\s+(Prime|Umbra)$", "", f.get("nom", "")) if "erreur" not in f else None
        if not frame: return {"erreur": f"warframe inconnue : {warframe}"}
        kind = type.strip().lower()
        if kind in ("obligatoire", "interdit") and "erreur" in self.fiche_mod(nom) and "erreur" in self.fiche_arcane(nom):
            return {"erreur": f"« {nom} » n'est ni un mod ni un arcane connu : vérifie le nom anglais"}
        if not rules.add(self.base, frame, kind, nom, raison, si_role):
            return {"erreur": "type inconnu : obligatoire, interdit, focus ou note"}
        return {"ok": True, "note": f"avis enregistré pour {frame} ; valider_build le rappellera"}

    def mods_arme(self, arme, exilus=False):
        """Mods compatibles avec une arme (pour l'interface et l'agent)."""
        from . import weapon
        r = self.con.execute("SELECT data FROM weapons WHERE name = ? COLLATE NOCASE", (arme,)).fetchone()
        if not r: return {"erreur": f"arme inconnue : {arme}"}
        w = json.loads(r["data"]); ok = weapon.compat_for(w)
        out, seen = [], set()
        for row in self.con.execute("SELECT data FROM mods WHERE type IN ('Primary Mod','Shotgun Mod','Secondary Mod','Melee Mod') ORDER BY name"):
            m = json.loads(row["data"])
            if (m.get("compatName") or "").upper() not in ok: continue
            c = self._mod_card(m)
            av = c.get("avertissement", "")
            if "ATTENTION" in av or "affaiblie" in av or c["nom"] in seen: continue
            if exilus and not c.get("exilus"): continue
            seen.add(c["nom"])
            out.append({"nom": c["nom"], "polarite": c.get("polarite"), "cout": c["cout_rang_max"], "rarete": c.get("rarete"),
                        "effets": c["effets_rang_max"], "augment": (m.get("compatName") or "").upper() == w["name"].upper(),
                        "image": m.get("imageName"), "set": c.get("set"), "exilus": bool(c.get("exilus"))})
        return out

    # ------------------------------------------------------------------ loadouts du joueur
    def lister_loadouts(self):
        from . import loadouts
        return {"loadouts": loadouts.list_all(self.base)} if self.base else {"erreur": "base introuvable"}

    def ouvrir_loadout(self, nom):
        from . import loadouts
        d = loadouts.load(self.base, nom)
        if not d:
            return {"erreur": f"aucun loadout « {nom} »", "loadouts": [x["nom"] for x in loadouts.list_all(self.base)]}
        v = d["versions"][-1]
        return {"nom": d["nom"], "version": v["version"], "date": v["date"], "build": v["build"], "synthese": v.get("synthese"),
                "historique": [{"version": x["version"], "date": x["date"][:10], "raison": x.get("raison")} for x in d["versions"]],
                "changements_depuis_la_sauvegarde": loadouts.changes(self, self.base, v["build"], v.get("instantane") or {})}

    def enregistrer_loadout(self, nom, build, synthese="", raison=""):
        """Enregistre une NOUVELLE version d'un loadout (les anciennes restent dans l'historique)."""
        from . import loadouts
        val = self.valider_build(build)
        if val.get("erreurs"):
            return {"erreur": "le build a des erreurs : corrige-les avant d'enregistrer", "erreurs": val["erreurs"]}
        return loadouts.save(self, self.base, nom, build, synthese, raison, validation=val)

    def valider_build(self, build):
        from . import build as b
        return b.validate(self, build)

    # ------------------------------------------------------------------ farm et doc
    def ou_farmer(self, objet):
        src = db.best_sources(self.con, objet, 5)
        if not src:
            close = [r["item"] for r in self.con.execute("SELECT DISTINCT item FROM drops WHERE item LIKE ? LIMIT 8", (f"%{objet}%",))]
            return {"erreur": f"« {objet} » n'est pas dans les tables de drop", "noms_proches": close,
                    "conseil": "mod Primed -> Baro Ki'Teer ; Galvanized -> vendeur des Arbitrations (20 Vitus Essence) ; sinon chercher_doc"}
        for kind, rows in src.items():
            for r in rows:
                r["tirages_pour_50pct"] = calc.tries_for(r["chance"] / 100, 0.5)
        ts = self.con.execute("SELECT value FROM meta WHERE key='drops_timestamp'").fetchone()
        return {"objet": objet, "sources": src, "taux": "en % par tirage",
                "note": "la rubrique ennemi_ou_activite contient aussi des coffres et des récompenses d'activités ; "
                        "le taux ne dit rien de la vitesse du farm", "tables_drop_timestamp_ms": ts["value"] if ts else None}

    def lister_documents(self, dossier=""):
        """Fichiers de la base sous un dossier (ex. « 02-wiki/warframes/Atlas »)."""
        root = os.path.realpath(self.base or "")
        d = os.path.realpath(os.path.join(root, dossier or ""))
        if not (d == root or d.startswith(root + os.sep)) or not os.path.isdir(d): return {"erreur": f"dossier inconnu : {dossier}"}
        out = []
        for n in sorted(os.listdir(d)):
            p = os.path.join(d, n)
            out.append(n + ("/" if os.path.isdir(p) else f" ({os.path.getsize(p) // 1024 + 1} Ko)"))
        return {"dossier": os.path.relpath(d, root).replace("\\", "/"), "contenu": out[:300]}

    def lire_document(self, chemin, debut=0):
        """Texte complet d'un document de la base, par tranches de 15 000 caractères."""
        root = os.path.realpath(self.base or "")
        p = os.path.realpath(os.path.join(root, chemin or ""))
        if not p.startswith(root + os.sep) or not os.path.isfile(p): return {"erreur": f"document inconnu : {chemin} (voir lister_documents ou chercher_doc)"}
        with open(p, encoding="utf-8", errors="replace") as fh: txt = fh.read()
        debut = max(0, int(debut or 0)); part = txt[debut:debut + 15000]
        out = {"document": os.path.relpath(p, root).replace("\\", "/"), "texte": part, "taille": len(txt)}
        if debut + 15000 < len(txt): out["suite"] = f"lire_document avec debut={debut + 15000}"
        return out

    def chercher_doc(self, question):
        res = docs.search(self.docs_path, question)
        return {"resultats": res} if res else {"erreur": "rien trouvé dans la doc ; dire que la base ne contient pas l'information"}

    # ------------------------------------------------------------------ calculs
    def calculer(self, operation, valeurs=None):
        v = valeurs or {}
        try:
            if operation == "multiplicateur_critique":
                m = calc.crit_multiplier(v["base"], v.get("bonus_relatifs", []), v.get("bonus_absolus", []))
                out = {"multiplicateur": round(m, 3)}
                if "chance" in v:
                    out["facteur_moyen"] = round(calc.average_crit_factor(v["chance"], m), 3)
                    out["niveaux"] = {str(k): round(p, 3) for k, p in calc.crit_tiers(v["chance"]).items()}
                return out
            if operation == "retrait_armure":
                a = v.get("armure", 2700)
                return {"reduction_avant": round(calc.enemy_armor_dr(a), 4),
                        "multiplicateur_de_degats": round(calc.armor_strip_multiplier(a, v["retrait"]), 3)}
            if operation == "cout_capacite":
                return {"cout": round(calc.ability_cost(v["cout_base"], v["efficacite"]), 2)}
            if operation == "stat_capacite":
                return {"total": round(calc.ability_stat(v.get("bonus", [])), 4)}
            if operation == "energie_max":
                return {"energie_max": round(calc.max_energy(v["base_rang30"], v.get("bonus", [])), 2)}
            if operation == "shield_gate":
                return {"duree_s": round(calc.shield_gate_duration(v["bouclier"], v.get("catalyzing", False)), 3)}
            if operation == "pv_effectifs":
                return {"pv_effectifs": round(calc.effective_health(v["sante"], v.get("armure", 0), v.get("bouclier", 0),
                                                                    v.get("autre_reduction", 0)), 1)}
            if operation == "cout_canalise":
                tot = calc.channel_total_cost(v["cout_initial"], v["drain"], v["secondes"], v.get("efficacite", 1.0),
                                              v.get("duree", 1.0), v.get("croissance", 1.0))
                return {"energie_totale": round(tot, 1),
                        "drain_par_seconde_au_depart": round(calc.channel_drain(v["drain"], v.get("efficacite", 1.0), v.get("duree", 1.0)), 2)}
            if operation == "tirages":
                return {"tirages": calc.tries_for(v["chance"], v.get("confiance", 0.5))}
        except KeyError as e:
            return {"erreur": f"valeur manquante : {e}", "aide": HELP_CALC}
        return {"erreur": f"opération inconnue : {operation}", "aide": HELP_CALC}

    # ------------------------------------------------------------------ appel générique
    def call(self, name, args):
        fn = getattr(self, name, None)
        if name.startswith("_") or not callable(fn) or name == "call":
            return {"erreur": f"outil inconnu : {name}", "outils": [s["function"]["name"] for s in SCHEMAS]}
        if name in ("valider_build", "enregistrer_loadout") and isinstance(args, dict) and "warframe" in args and "build" not in args:
            args = {"build": {k: v for k, v in args.items() if k not in ("nom", "raison", "synthese")},
                    **({k: args[k] for k in ("nom", "raison", "synthese") if k in args} if name == "enregistrer_loadout" else {})}
        try:
            return fn(**(args or {}))
        except TypeError as e:
            return {"erreur": f"arguments invalides pour {name} : {e}"}


EFFECTS_HINT = ("Ability Strength, Ability Duration, Ability Range, Ability Efficiency, Energy Max, Health, Shield Capacity, "
                "Armor, Critical Chance, Critical Damage, Status Chance, Melee Damage, Damage, Multishot, Fire Rate, Attack Speed, "
                "Casting Speed, Heat, Cold, Toxin, Electricity")
SYNONYMS = {
    "power strength": "Ability Strength", "strength": "Ability Strength", "puissance": "Ability Strength",
    "puissance de pouvoir": "Ability Strength", "power duration": "Ability Duration", "duration": "Ability Duration",
    "durée": "Ability Duration", "duree": "Ability Duration", "power range": "Ability Range", "portée": "Ability Range",
    "portee": "Ability Range", "power efficiency": "Ability Efficiency", "efficiency": "Ability Efficiency",
    "efficacité": "Ability Efficiency", "efficacite": "Ability Efficiency", "energy": "Energy Max", "énergie": "Energy Max",
    "energie": "Energy Max", "santé": "Health", "sante": "Health", "bouclier": "Shield Capacity", "shield": "Shield Capacity",
    "armure": "Armor", "dégâts critiques": "Critical Damage", "degats critiques": "Critical Damage", "crit damage": "Critical Damage",
    "chance critique": "Critical Chance", "crit chance": "Critical Chance", "statut": "Status Chance",
    "chance de statut": "Status Chance", "vitesse de lancement": "Casting Speed", "cast speed": "Casting Speed",
}

HELP_CALC = ("multiplicateur_critique {base, bonus_relatifs[], bonus_absolus[], chance?} ; retrait_armure {retrait, armure?} ; "
             "cout_capacite {cout_base, efficacite} ; stat_capacite {bonus[]} ; energie_max {base_rang30, bonus[]} ; "
             "shield_gate {bouclier, catalyzing?} ; pv_effectifs {sante, armure?, bouclier?, autre_reduction?} ; "
             "cout_canalise {cout_initial, drain, secondes, efficacite?, duree?, croissance?} ; tirages {chance, confiance?}. Les pourcentages sont des fractions : 90 % = 0.9, 183 % = 1.83.")


def _fn(name, desc, props, required):
    return {"type": "function", "function": {"name": name, "description": desc,
            "parameters": {"type": "object", "properties": props, "required": required}}}


S = {"type": "string"}
SCHEMAS = [
    _fn("fiche_mod", "Fiche exacte d'un mod par son nom anglais : effets au rang max, coût, polarité, avertissement s'il n'existe pas en jeu.",
        {"nom": S}, ["nom"]),
    _fn("chercher_mods", "Trouve les mods qui donnent un effet (texte anglais, ex. 'Critical Damage', 'Ability Range').",
        {"effet": S, "pour": {"type": "string", "description": "optionnel : Melee, Warframe, Rifle, Pistol, Shotgun..."}}, ["effet"]),
    _fn("lister_documents", "Liste les fichiers de la base (wiki exporté, données, retours du joueur, patch notes). "
        "Dossiers : 00 - Etat de la base.md, 01-donnees, 02-wiki (warframes, armes, systemes, farm, augments, incarnon, contenu-recent), "
        "03-patch-notes, 04-retours-experience, 05-builds-proposes, 06-builds-joueur.", {"dossier": S}, []),
    _fn("lire_document", "Lit un document de la base en entier (par tranches). Pour lire la page d'une capacité, d'un système "
        "ou d'une note de patch trouvée avec chercher_doc ou lister_documents.", {"chemin": S, "debut": {"type": "integer"}}, ["chemin"]),
    _fn("proposer_build", "Build COMPLET calculé et vérifié par le programme depuis l'archétype qui correspond à l'objectif. "
        "À utiliser en premier pour une demande de build : il suffit ensuite de l'expliquer ou de l'ajuster.",
        {"warframe": S, "objectif": S, "defense": {"type": "string", "enum": ["bouclier", "persistence"]},
         "niveau": {"type": "string", "enum": ["debutant", "intermediaire", "endgame"]}}, ["warframe"]),
    _fn("archetypes", "Archétypes de build préparés pour une warframe (boucle de jeu, survie, énergie, noyau, choix, pièges). "
        "Déjà inclus dans dossier_build quand ils existent.", {"warframe": S}, ["warframe"]),
    _fn("dossier_build", "À APPELER EN PREMIER pour tout build : stats de la warframe, chiffres de ses 4 capacités, augments, "
        "retours du joueur sur cette frame, et meilleurs mods par stat (puissance, durée, portée, efficacité, survie).",
        {"warframe": S}, ["warframe"]),
    _fn("options", "Liste les choix possibles pour un emplacement : aura, exilus, arcanes (de warframe), helminth, compagnon, "
        "arcanes_melee, arcanes_principale, arcanes_secondaire.", {"categorie": S}, ["categorie"]),
    _fn("valider_build", "OBLIGATOIRE avant de présenter un build : vérifie chaque mod, signale les emplacements vides, calcule les "
        "totaux exacts, la capacité et les formas, et renvoie le tableau à recopier. Format du build : "
        "{warframe, role, source_energie, aura, exilus, mods:[8 noms], arcanes:[2 noms], helminth, focus, compagnon, "
        "armes:{principale, secondaire, melee, exaltees:[armes données par une capacité]}, fragments:[5 libellés de options(fragments)]}. Chaque arme peut être un nom, ou "
        "{nom, mods:[8], exilus, arcane} : l'outil calcule alors ses dégâts, critiques, statut et DPS.", {"build": {"type": "object"}}, ["build"]),
    _fn("noter_retour", "À appeler quand le joueur te corrige ou t'apprend un fait de jeu ou une préférence de build : "
        "enregistre sa remarque pour les prochaines conversations. sujet = la warframe, l'arme ou le thème.",
        {"sujet": S, "remarque": S}, ["sujet", "remarque"]),
    _fn("noter_regle", "Quand le joueur donne un avis sur un mod, un arcane ou un focus pour une warframe : enregistre-le avec SA RAISON. "
        "type = obligatoire (conseillé), interdit (déconseillé), focus ou note. si_role = le cas où l'avis s'applique "
        "(ex. 'nuke au 4'). Ce n'est pas une règle absolue : valider_build le rappellera.",
        {"warframe": S, "type": S, "nom": S, "raison": S, "si_role": S}, ["warframe", "type", "nom", "raison"]),
    _fn("lister_loadouts", "Liste les loadouts enregistrés par le joueur.", {}, []),
    _fn("ouvrir_loadout", "Ouvre un loadout du joueur : build, synthèse, historique, et ce qui a changé dans les données du jeu "
        "ou les notes de patch depuis sa sauvegarde. À appeler quand le joueur parle d'un de ses loadouts.", {"nom": S}, ["nom"]),
    _fn("enregistrer_loadout", "Enregistre une nouvelle version d'un loadout (build validé, synthèse, raison du changement). "
        "Seulement si le joueur le demande.", {"nom": S, "build": {"type": "object"}, "synthese": S, "raison": S}, ["nom", "build"]),
    _fn("fiche_warframe", "Stats de base, polarités, passif et capacités d'une warframe.", {"nom": S}, ["nom"]),
    _fn("fiche_arme", "Stats d'une arme : dégâts, critique, statut, cadence.", {"nom": S}, ["nom"]),
    _fn("chercher_armes", "Liste les armes d'une catégorie (principale, secondaire, melee), triées par critique, statut, dégâts, "
        "disposition, cadence ou portée. À utiliser pour CHOISIR une arme ; « nom » filtre par nom (ex. Prime, Incarnon).",
        {"categorie": S, "tri": S, "nom": S}, ["categorie"]),
    _fn("fiche_arcane", "Effet d'un arcane au rang max.", {"nom": S}, ["nom"]),
    _fn("ou_farmer", "Meilleures sources d'un objet (mod, arcane, ressource, plan) avec taux de drop.", {"objet": S}, ["objet"]),
    _fn("chercher_doc", "Cherche dans les retours d'expérience du joueur, la méthode de build et les mécaniques du jeu.",
        {"question": S}, ["question"]),
    _fn("calculer", "Fait un calcul exact. Opérations : " + HELP_CALC,
        {"operation": S, "valeurs": {"type": "object"}}, ["operation", "valeurs"]),
]
