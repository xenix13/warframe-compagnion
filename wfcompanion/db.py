"""Base structurée SQLite : ce que liront le moteur de calcul, l'agent et l'interface.

Chaque table garde quelques colonnes indexées et l'objet complet en JSON (colonne data),
pour ne rien perdre des données sources.
"""
import json, os, re, sqlite3

SCHEMA_VERSION = "4"  # à augmenter quand la structure ou le contenu calculé change

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE IF NOT EXISTS mods(unique_name TEXT PRIMARY KEY, name TEXT, type TEXT, compat TEXT,
  polarity TEXT, rarity TEXT, base_drain INT, fusion_limit INT, is_exilus INT, is_augment INT,
  mod_set TEXT, variant TEXT, introduced TEXT, tradable INT, data TEXT);
CREATE TABLE IF NOT EXISTS arcanes(unique_name TEXT PRIMARY KEY, name TEXT, type TEXT, rarity TEXT, data TEXT);
CREATE TABLE IF NOT EXISTS warframes(unique_name TEXT PRIMARY KEY, name TEXT, type TEXT, health REAL, shield REAL,
  armor REAL, power REAL, is_prime INT, data TEXT);
CREATE TABLE IF NOT EXISTS weapons(unique_name TEXT PRIMARY KEY, name TEXT, category TEXT, type TEXT, data TEXT);
CREATE TABLE IF NOT EXISTS companions(unique_name TEXT PRIMARY KEY, name TEXT, type TEXT, data TEXT);
CREATE TABLE IF NOT EXISTS drops(item TEXT, place TEXT, kind TEXT, rarity TEXT, chance REAL, qty TEXT);
CREATE INDEX IF NOT EXISTS i_mods_name ON mods(name);
CREATE INDEX IF NOT EXISTS i_arc_name ON arcanes(name);
CREATE INDEX IF NOT EXISTS i_wf_name ON warframes(name);
CREATE INDEX IF NOT EXISTS i_wp_name ON weapons(name);
CREATE INDEX IF NOT EXISTS i_drops_item ON drops(item);
"""


def _load(raw, name):
    p = os.path.join(raw, name)
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def mod_variant(m):
    from .mods_md import weak_variant
    u = m.get("uniqueName", "")
    return weak_variant(u) or ("Expert" if "/Expert/" in u else "")


def place_kind(place):
    if place.endswith(" Relic"): return "relique"
    if ("Rotation" in place or ("/" in place and "(" in place) or "Bounty" in place
            or place in ("Sorties", "Arbitrations")):
        return "mission"
    return "ennemi_ou_activite"


def build(raw, db_path):
    tmp = db_path + ".tmp"
    if os.path.exists(tmp): os.unlink(tmp)
    con = sqlite3.connect(tmp)
    con.executescript(SCHEMA)
    for m in _load(raw, "Mods.json"):
        if not m.get("name"): continue
        intro = (m.get("introduced") or {}).get("date")
        con.execute("INSERT OR REPLACE INTO mods VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            m["uniqueName"], m["name"], m.get("type"), m.get("compatName"), m.get("polarity"), m.get("rarity"),
            m.get("baseDrain"), m.get("fusionLimit"), int(bool(m.get("isExilus") or m.get("isUtility"))),
            int(bool(m.get("isAugment"))), m.get("modSet"), mod_variant(m), intro, int(bool(m.get("tradable"))),
            json.dumps(m, ensure_ascii=False)))
    for a in _load(raw, "Arcanes.json"):
        con.execute("INSERT OR REPLACE INTO arcanes VALUES(?,?,?,?,?)",
                    (a["uniqueName"], a["name"], a.get("type"), a.get("rarity"), json.dumps(a, ensure_ascii=False)))
    for w in _load(raw, "Warframes.json"):
        con.execute("INSERT OR REPLACE INTO warframes VALUES(?,?,?,?,?,?,?,?,?)", (
            w["uniqueName"], w["name"], w.get("type"), w.get("health"), w.get("shield"), w.get("armor"),
            w.get("power"), int(bool(w.get("isPrime"))), json.dumps(w, ensure_ascii=False)))
    for f in ("Primary.json", "Secondary.json", "Melee.json"):
        for w in _load(raw, f):
            con.execute("INSERT OR REPLACE INTO weapons VALUES(?,?,?,?,?)",
                        (w["uniqueName"], w["name"], w.get("category"), w.get("type"), json.dumps(w, ensure_ascii=False)))
    # armes exaltées des warframes (Exalted Blade, Shattered Lash, Landslide Fists…) et griffes de Garuda : rangées dans la
    # catégorie de leur emplacement (Melee, Primary, Secondary) pour les mods et le calcul ; type « Exalted Weapon »
    for w in _load(raw, "Misc.json"):
        if (w.get("type") == "Exalted Weapon" and w.get("uniqueName", "").startswith("/Lotus/Powersuits/")
                and w.get("exaltedSlot") in ("Melee", "Primary", "Secondary")):
            w = dict(w, category=w["exaltedSlot"])
            con.execute("INSERT OR REPLACE INTO weapons VALUES(?,?,?,?,?)",
                        (w["uniqueName"], w["name"], w["category"], w["type"], json.dumps(w, ensure_ascii=False)))
    for f in ("Sentinels.json", "Pets.json"):
        if not os.path.exists(os.path.join(raw, f)): continue
        for w in _load(raw, f):
            con.execute("INSERT OR REPLACE INTO companions VALUES(?,?,?,?)",
                        (w["uniqueName"], w["name"], w.get("type"), json.dumps(w, ensure_ascii=False)))
    for x in _load(raw, "drops_all.slim.json"):
        place = re.sub(r"<[^>]+>", "", x["place"]).strip()
        item = x["item"].strip(); qty = None
        mq = re.match(r"^([\d,]+)X (.+)$", item)
        if mq: qty, item = mq.group(1), mq.group(2)
        try: ch = float(x["chance"])
        except (TypeError, ValueError): continue
        con.execute("INSERT INTO drops VALUES(?,?,?,?,?,?)", (item, place, place_kind(place), x.get("rarity"), ch, qty))
    info = _load(raw, "drops_info.json")
    con.execute("INSERT OR REPLACE INTO meta VALUES('drops_timestamp',?)", (str(info.get("timestamp")),))
    con.execute("INSERT OR REPLACE INTO meta VALUES('schema',?)", (SCHEMA_VERSION,))
    con.commit(); con.close()
    from .docs import _replace
    _replace(tmp, db_path)


def needs_rebuild(db_path):
    """Vrai si la base est absente ou construite par une ancienne version du programme."""
    if not os.path.exists(db_path): return True
    con = sqlite3.connect(db_path)
    try:
        row = con.execute("SELECT value FROM meta WHERE key='schema'").fetchone()
        return not row or row[0] != SCHEMA_VERSION
    except sqlite3.Error:
        return True
    finally:
        con.close()


# --- requêtes simples pour l'agent et l'interface ---------------------------------

def connect(db_path):
    con = sqlite3.connect(db_path, check_same_thread=False)  # l'interface web l'utilise depuis plusieurs threads, sous verrou
    con.row_factory = sqlite3.Row
    return con


def find_mod(con, name, include_variants=False):
    q = "SELECT * FROM mods WHERE name = ? COLLATE NOCASE"
    if not include_variants: q += " AND variant = ''"
    return [dict(r) for r in con.execute(q, (name,))]


def best_sources(con, item, limit=5):
    out = {}
    for kind in ("ennemi_ou_activite", "mission", "relique"):
        rows = con.execute("SELECT place, rarity, chance, qty FROM drops WHERE item = ? COLLATE NOCASE AND kind = ?"
                           " GROUP BY place, chance ORDER BY chance DESC LIMIT ?", (item, kind, limit)).fetchall()
        if rows: out[kind] = [dict(r) for r in rows]
    return out
