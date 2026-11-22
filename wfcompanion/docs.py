"""Index plein texte (SQLite FTS5) des documents de la base : retours d'expérience, méthode, mécaniques du wiki.

Sert à l'outil « chercher_doc » de l'agent, sans modèle d'embeddings : ça marche sur n'importe quelle machine.
Les retours d'expérience et la méthode passent en premier dans les résultats (priorité au vécu du joueur).
"""
import glob, os, re, sqlite3

# (sous-dossier ou fichier, priorité : plus petit = plus important)
SCOPES = [("04-retours-experience", 0), ("06-builds-joueur", 0), ("05-builds-proposes", 1), ("00 - Etat de la base.md", 0),
          ("01-donnees/farm/Farm - Principes et limites.md", 1), ("02-wiki/systemes", 2),
          ("02-wiki/warframes", 2), ("02-wiki/augments", 2), ("01-donnees/warframes", 2), ("02-wiki/farm", 2), ("02-wiki/contenu-recent", 2),
          ("02-wiki/incarnon", 3), ("02-wiki/armes", 3), ("01-donnees/arcanes", 3), ("03-patch-notes", 3),
          ("01-donnees/focus", 2), ("01-donnees/Compagnons.md", 2), ("01-donnees/armes", 3), ("01-donnees/mods", 3),
          ("01-donnees/farm", 3)]
CHUNK = 1800


def _files(base):
    for scope, prio in SCOPES:
        p = os.path.join(base, scope)
        if os.path.isfile(p):
            yield p, prio
        else:
            for f in sorted(glob.glob(os.path.join(p, "**", "*.md"), recursive=True)):
                yield f, prio


def signature(base):
    """Change dès qu'un fichier est ajouté, retiré ou modifié : évite de réindexer pour rien."""
    n, newest = 0, 0.0
    for f, _ in _files(base):
        n += 1; newest = max(newest, os.path.getmtime(f))
    return f"{n}:{newest:.3f}"


def ensure(base, db_path):
    sig = signature(base)
    if os.path.exists(db_path):
        con = None
        try:
            con = sqlite3.connect(db_path)
            row = con.execute("SELECT v FROM meta WHERE k='sig'").fetchone()
            if row and row[0] == sig: return 0
        except sqlite3.Error:
            pass
        finally:
            if con is not None: con.close()  # indispensable sous Windows : un fichier ouvert ne peut pas être remplacé
    return build(base, db_path, sig)


def _chunks(text):
    """Découpe par titres puis par taille, en gardant le titre courant en tête de chaque morceau."""
    title, buf, size = "", [], 0
    for line in text.split("\n"):
        if line.startswith("#"):
            if buf: yield title, "\n".join(buf)
            title, buf, size = line.lstrip("# ").strip(), [], 0
            continue
        if size + len(line) > CHUNK and buf:
            yield title, "\n".join(buf); buf, size = [], 0
        while len(line) > CHUNK:  # lignes géantes (tableaux du wiki)
            yield title, line[:CHUNK]; line = line[CHUNK:]
        buf.append(line); size += len(line) + 1
    if buf: yield title, "\n".join(buf)


def build(base, db_path, sig=None):
    tmp = db_path + ".tmp"
    if os.path.exists(tmp): os.unlink(tmp)
    con = sqlite3.connect(tmp)
    con.execute("CREATE VIRTUAL TABLE docs USING fts5(file, title, body, prio UNINDEXED, tokenize='unicode61 remove_diacritics 2')")
    n = 0
    for path, prio in _files(base):
        rel = os.path.relpath(path, base).replace("\\", "/")
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        for title, body in _chunks(text):
            if body.strip():
                con.execute("INSERT INTO docs VALUES(?,?,?,?)", (rel, title, body, prio)); n += 1
    con.execute("CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT)")
    con.execute("INSERT INTO meta VALUES('sig', ?)", (sig or signature(base),))
    con.commit(); con.close()
    _replace(tmp, db_path)
    return n


def _replace(tmp, dest):
    import gc, time
    for attempt in range(5):
        try:
            os.replace(tmp, dest); return
        except PermissionError:
            gc.collect(); time.sleep(0.3)
    raise RuntimeError(f"Impossible de remplacer {dest} : le fichier est utilisé par un autre programme. "
                       "Ferme les autres fenêtres du compagnon puis relance.")


def search(db_path, query, limit=4, max_chars=900, file_like=None):
    words = [w for w in re.findall(r"[\w'-]+", query.lower()) if len(w) > 2]
    if not words: return []
    con = sqlite3.connect(db_path)
    try:
        return _search(con, words, limit, max_chars, file_like)
    finally:
        con.close()


def _search(con, words, limit, max_chars, file_like):
    out = []
    # d'abord tous les mots, puis au moins un : un petit modèle formule souvent mal sa requête
    for expr in (" AND ".join(f'"{w}"' for w in words), " OR ".join(f'"{w}"' for w in words)):
        try:
            rows = con.execute("SELECT file, title, body, prio FROM docs WHERE docs MATCH ? AND file LIKE ? "
                               "ORDER BY bm25(docs, 2.0, 4.0, 1.0) * (1.0 - 0.15 * prio) LIMIT ?",
                               (expr, file_like or "%", limit)).fetchall()
        except sqlite3.OperationalError:
            rows = []
        for f, t, b, _ in rows:
            item = {"fichier": f, "titre": t, "extrait": b[:max_chars]}
            if item not in out: out.append(item)
        if len(out) >= limit: break
    return out[:limit]
