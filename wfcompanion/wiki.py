"""Rafraîchit les pages du wiki de la base : une page n'est retéléchargée que si sa révision a changé."""
import glob, os, re, urllib.parse

from . import wiki_convert as wc, wiki_http

DEFAULT_DIRS = ["02-wiki/systemes", "02-wiki/farm", "02-wiki/contenu-recent"]
_TRANS = re.compile(r"^\(?[A-Za-z]{2,3}(-[A-Za-z]+)?\)? (Arabic|Chinese|Czech|Danish|Dutch|English|Finnish|French|German|"
                    r"Greek|Hebrew|Hindi|Hungarian|Indonesian|Italian|Japanese|Korean|Norwegian|Polish|Portuguese|Romanian|"
                    r"Russian|Spanish|Swedish|Thai|Turkish|Ukrainian|Vietnamese|Latin|Catalan|Bulgarian|Serbian|Croatian|"
                    r"Slovak)[^|]*\| ")


def _api(params):
    return wiki_http.api(params)


def _source(path):
    with open(path, encoding="utf-8") as f:
        f.readline(); second = f.readline()
    if second.startswith("Source :") and "/w/" in second:
        return second.replace("Source :", "").strip()
    return None


def revisions(titles):
    """titre demandé -> revid actuel (suit les redirections)."""
    res = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = _api({"action": "query", "prop": "revisions", "rvprop": "ids", "redirects": 1, "titles": "|".join(chunk)})
        q = d.get("query", {})
        back = {t: t for t in chunk}
        for n in q.get("normalized", []): back[n["to"]] = back.get(n["from"], n["from"])
        for r in q.get("redirects", []): back[r["to"]] = back.get(r["from"], r["from"])
        for p in q.get("pages", []):
            if p.get("revisions"): res[back.get(p["title"], p["title"])] = p["revisions"][0]["revid"]
    return res


def refresh(base, state, dirs=None, log=print):
    dirs = dirs or DEFAULT_DIRS
    pages = {}
    for d in dirs:
        for p in glob.glob(os.path.join(base, d, "*.md")):
            src = _source(p)
            if src:
                pages[p] = (src, urllib.parse.unquote(src.split("/w/", 1)[1]).replace("_", " "))
    revs = revisions(sorted({t for _, t in pages.values()}))
    known = state.setdefault("wiki_revisions", {})
    changed = []
    for p, (src, title) in sorted(pages.items()):
        rel = os.path.relpath(p, base).replace("\\", "/")
        rev = revs.get(title)
        if rev is None:
            log(f"  wiki : page introuvable, gardée telle quelle : {title}")
            continue
        if known.get(rel) == rev:
            continue
        try:
            wc.build(src, p)
        except Exception as e:  # une page en erreur ne bloque pas les autres
            log(f"  wiki : échec pour {title} : {e}")
            continue
        with open(p, encoding="utf-8") as f:
            lines = [l for l in f.read().split("\n") if not _TRANS.match(l.strip())]
        with open(p, "w", encoding="utf-8") as f:
            f.write(re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n")
        known[rel] = rev
        changed.append(rel)
    return changed
