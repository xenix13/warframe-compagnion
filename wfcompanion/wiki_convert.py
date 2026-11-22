import sys, re, json, urllib.parse, urllib.request
from bs4 import BeautifulSoup, NavigableString

API = "https://wiki.warframe.com/api.php"
UA = {"User-Agent": "Mozilla/5.0"}

def fetch(title):
    from . import wiki_http
    d = wiki_http.api({"action": "parse", "page": title, "prop": "text|displaytitle", "redirects": 1})
    if "error" in d:
        raise RuntimeError(d["error"])
    return d["parse"]["title"], d["parse"]["text"]

DROP_CLASSES = {"navbox", "toc", "mw-editsection", "printfooter", "catlinks", "noprint",
                "navbox-inner", "reference", "mw-references-wrap", "hatnote"}


INVIS = dict.fromkeys([0x2061,0x2062,0x2063,0x2064,0x200b], None)

def _kids(e):
    return [c for c in e.children if getattr(c, "name", None)]

def _m(e):
    if isinstance(e, NavigableString):
        return str(e)
    n = e.name
    k = _kids(e)
    if n in ("mi", "mn", "mo", "mtext", "ms"):
        return e.get_text()
    if n == "mfrac" and len(k) >= 2:
        a, b = _m(k[0]).strip(), _m(k[1]).strip()
        wa = a if len(a) <= 1 else "(" + a + ")"
        wb = b if len(b) <= 1 else "(" + b + ")"
        return wa + "/" + wb
    if n == "msup" and len(k) >= 2:
        b, x = _m(k[0]), _m(k[1]).strip()
        return b + "^" + (x if len(x) <= 1 else "(" + x + ")")
    if n == "msub" and len(k) >= 2:
        b, x = _m(k[0]), _m(k[1]).strip()
        return b + "_" + (x if len(x) <= 1 else "(" + x + ")")
    if n == "msubsup" and len(k) >= 3:
        return _m(k[0]) + "_(" + _m(k[1]).strip() + ")^(" + _m(k[2]).strip() + ")"
    if n in ("munder", "munderover", "mover") and len(k) >= 2:
        base = _m(k[0])
        if n == "munder":
            return base + "_(" + _m(k[1]).strip() + ")"
        if n == "mover":
            return base + "^(" + _m(k[1]).strip() + ")"
        return base + "_(" + _m(k[1]).strip() + ")^(" + _m(k[2]).strip() + ")"
    if n == "msqrt":
        return "sqrt(" + "".join(_m(c) for c in e.children).strip() + ")"
    if n == "mroot" and len(k) >= 2:
        return "root_" + _m(k[1]).strip() + "(" + _m(k[0]).strip() + ")"
    if n == "mfenced":
        return "(" + ", ".join(_m(c) for c in k) + ")"
    if n == "mtable":
        rows = [_m(r) for r in k]
        return "{ " + " ; ".join(r for r in rows if r.strip()) + " }" if len(rows) > 1 else "".join(rows)
    if n == "mtr":
        return "  ".join(_m(c) for c in k)
    if n == "mtd":
        return "".join(_m(c) for c in e.children)
    if n in ("annotation", "annotation-xml", "mspace", "mphantom"):
        return " " if n == "mspace" else ""
    return "".join(_m(c) for c in e.children)

def mathtext(m):
    t = _m(m).translate(INVIS)
    return re.sub(r"\s+", " ", t).strip()

def txt(el):
    out = []
    for c in el.descendants:
        if isinstance(c, NavigableString):
            out.append(str(c))
        elif c.name == "br":
            out.append(" ")
    return re.sub(r"\s+", " ", "".join(out)).strip()

def render(el, lines, depth=0):
    for c in el.children:
        if isinstance(c, NavigableString):
            continue
        cls = set(c.get("class") or [])
        if cls & DROP_CLASSES or c.name in ("script", "style", "sup"):
            continue
        n = c.name
        if n in ("h1", "h2", "h3", "h4", "h5", "h6"):
            t = txt(c)
            t = re.sub(r"\[edit\]|\[modifier\]", "", t).strip()
            if t:
                lines.append("")
                lines.append("#" * min(int(n[1]) + 0, 6) + " " + t)
                lines.append("")
        elif n == "p":
            t = txt(c)
            if t:
                lines.append(t)
                lines.append("")
        elif n in ("ul", "ol"):
            li_render(c, lines, 0, n == "ol")
            lines.append("")
        elif n == "table":
            table_render(c, lines)
            lines.append("")
        elif n == "dl":
            for x in c.find_all(["dt", "dd"], recursive=False):
                t = txt(x)
                if t:
                    lines.append(("- " if x.name == "dd" else "") + t)
            lines.append("")
        elif n in ("div", "section", "span", "blockquote", "center", "figure"):
            if n == "figure":
                continue
            # leaf-ish div with only inline text
            if not c.find(["p", "ul", "ol", "table", "h1", "h2", "h3", "h4", "h5", "h6", "div", "dl"]):
                t = txt(c)
                if t:
                    lines.append(t)
                    lines.append("")
            else:
                render(c, lines, depth + 1)
        else:
            continue

def li_render(ul, lines, lvl, ordered):
    i = 0
    for li in ul.find_all("li", recursive=False):
        i += 1
        own = []
        subs = []
        for ch in li.children:
            if isinstance(ch, NavigableString):
                own.append(str(ch))
            elif ch.name in ("ul", "ol"):
                subs.append(ch)
            elif ch.name == "sup":
                continue
            else:
                own.append(txt(ch) if ch.name != "br" else " ")
        t = re.sub(r"\s+", " ", "".join(own)).strip()
        if t:
            lines.append("  " * lvl + (f"{i}. " if ordered else "- ") + t)
        for s in subs:
            li_render(s, lines, lvl + 1, s.name == "ol")

def table_render(tb, lines):
    rows = []
    for tr in tb.find_all("tr"):
        cells = tr.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        vals = [txt(c) for c in cells]
        if any(vals):
            rows.append(" | ".join(vals))
    if rows:
        lines.extend(rows)

def convert(html):
    soup = BeautifulSoup(html, "html.parser")
    for t in soup.select(".mw-editsection, .navbox, .toc, style, script, .reference, .printfooter, .catlinks"):
        t.decompose()
    for m in soup.find_all("math"):
        m.replace_with(NavigableString(" " + mathtext(m) + " "))
    root = soup.find("div", class_="mw-parser-output") or soup
    lines = []
    render(root, lines)
    out = "\n".join(lines)
    out = re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"
    return out

def build(source_url, outpath):
    title_part = source_url.split("/w/", 1)[1]
    title = urllib.parse.unquote(title_part)
    t, html = fetch(title)
    body = convert(html)
    head = f"# {t.replace('_',' ')} (wiki)\nSource : {source_url}\n\n"
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(head + body)
    return len(head + body)

if __name__ == "__main__":
    print(build(sys.argv[1], sys.argv[2]))
