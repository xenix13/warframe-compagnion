"""Génère les archétypes de build de chaque warframe, hors ligne, avec un modèle plus gros que celui du joueur.

Le joueur n'écrit pas les archétypes : un modèle les déduit des capacités (wiki de la base), des augments (données du jeu)
et des PRINCIPES généraux du joueur, qui valent pour toutes les frames. Le code vérifie ensuite que chaque nom cité existe.
Un fichier relu par le joueur (« relu_par_le_joueur »: true) n'est jamais écrasé.

    python -m wfcompanion.archetypes_gen --base <base> --model gemma4:12b            (toutes les frames sans archétype)
    python -m wfcompanion.archetypes_gen --base <base> --model gemma4:12b --frame Gara
    python -m wfcompanion.archetypes_gen --base <base> --api-url https://.../v1 --model <modèle en ligne>
"""
import argparse, datetime, glob, json, os, re, sys, urllib.request

from . import agent as ag, cloud

PRINCIPES = """PRINCIPES DU JOUEUR (valent pour toutes les warframes) :
1. Une warframe doit survivre par elle-même, couvrir le maximum de contenu (sauf build spécifique), être autonome en énergie,
   et ses capacités mises en avant doivent servir l'objectif (ex. chasse d'Archonte = gros DPS mono-cible).
2. Un build est une boucle de jeu : chaque pièce sert au moins deux autres. Une pièce sans lien est suspecte.
3. Défense au level cap : la santé seule ne tient pas. Défense par le bouclier (shield gate, Brief Respite, set Augur),
   combinable avec santé et armure ; OU Arcane Persistence (armure > 700) qui retire tout le bouclier : tout sur santé et armure.
   La défense vient aussi des capacités (invulnérabilité, réduction de dégâts, contrôle, invisibilité).
4. Énergie : il faut une vraie source (Zenurik, Helminth, arcanes, ressource propre de la frame). Arcane Battery augmente
   seulement l'énergie max (0,30 par point d'armure) : utile seulement si la frame a beaucoup d'armure. Nourish multiplie
   l'énergie gagnée par les autres sources, il n'en crée pas. Les auras d'énergie sont presque inutiles.
5. Mods de santé, bouclier ou armure : seulement s'ils servent le build (synergie, capacité qui en dépend, ressource de la frame).
6. Capacités canalisées ou à coût croissant : on les relance au lieu de les tenir longtemps.
7. Armes exaltées : modées à part ; certaines suivent un combo de capacité (jusqu'à 12x) où Blood Rush et Weeping Wounds brillent.
8. Il n'y a pas de build unique : proposer 2 à 4 archétypes avec des objectifs différents."""

SCHEMA_TXT = """Réponds UNIQUEMENT par un objet JSON de cette forme :
{"warframe": "...", "passif": "une phrase",
 "capacites": {"<nom exact de la capacité>": {"type": ["dégâts"|"contrôle"|"défense"|"soutien"|"mobilité"|"invocation"|"buff"], "cout": "...",
   "monte_avec": ["puissance", "durée", ...], "notes": ["interaction importante", ...]}},
 "augments": {"<nom exact de l'augment>": "ce qu'il change, en une phrase"},
 "archetypes": [{"id": "court-en-minuscules", "nom": "...", "objectif": "contenus et rôle visés",
   "boucle_de_jeu": ["étape 1", "étape 2", ...], "capacite_centrale": "<nom exact>",
   "survie": ["d'où vient la survie"], "energie": ["d'où vient l'énergie"],
   "noyau": {"mods": ["<noms exacts de mods, au plus 3, indispensables>"]},
   "choix": [{"quoi": "...", "pourquoi": "...", "options": ["...", "..."]}],
   "stats_cibles": {"puissance": "haute|moyenne|basse", "duree": "...", "portee": "...", "efficacite": "..."},
   "pieges": ["..."]}]}
Utilise seulement les noms de capacités, d'augments et de mods donnés ou que tu connais avec certitude. Écris en français.
Marque [à vérifier] ce dont tu n'es pas sûr."""


def _frame_context(tb, base, frame):
    f = tb.fiche_warframe(frame)
    if "erreur" in f: return None, None
    name = re.sub(r"\s+(Prime|Umbra)$", "", f["nom"])
    parts = [f"WARFRAME : {name}", "STATS (rang 0) : " + json.dumps(f.get("rang_0_donnees_du_jeu"), ensure_ascii=False),
             "PASSIF : " + str(f.get("passif") or "")[:400]]
    for p in sorted(glob.glob(os.path.join(base, "02-wiki", "warframes", name, "Capacit*.md"))):
        with open(p, encoding="utf-8", errors="replace") as fh: txt = fh.read()
        parts.append(f"--- {os.path.basename(p)[:-3]}\n" + txt.split("\n", 2)[-1][:2200])
    if len(parts) == 3:
        parts += [f"--- {c['nom']} : {c.get('description')}" for c in f.get("capacites", [])]
    aug = [(r["name"], json.loads(r["data"])) for r in tb.con.execute(
        "SELECT name, data FROM mods WHERE compat = ? COLLATE NOCASE AND variant = ''", (name,))]
    parts.append("AUGMENTS : " + "; ".join(f"{n} : {tb._mod_card(d)['effets_rang_max']}" for n, d in aug))
    ex = tb.armes_exaltees(f["nom"])
    if ex: parts.append("ARMES EXALTÉES : " + ", ".join(x["nom"] for x in ex))
    cost = tb.costs_data(name)
    if cost: parts.append("COÛTS ET RESSOURCE : " + json.dumps(cost, ensure_ascii=False)[:800])
    return name, "\n".join(parts)


def _ask(a, messages):
    if a.api_url:
        key = a.api_key or os.environ.get("WF_API_KEY")
        if not key and os.path.exists("cle-api.txt"):
            with open("cle-api.txt", encoding="utf-8") as fh: key = fh.read().strip()
        return cloud.chat(a.api_url, key, a.model, messages, None).get("content") or ""
    body = {"model": a.model, "messages": messages, "stream": False, "format": "json", "keep_alive": "30m",
            "options": {"temperature": 0.3, "num_ctx": a.ctx}}
    if a.think: body["think"] = a.think != "off"
    req = urllib.request.Request(a.host.rstrip("/") + "/api/chat", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=1800) as r:
        return json.loads(r.read())["message"].get("content") or ""


def _parse(txt):
    m = re.search(r"\{.*\}", txt, re.S)
    return json.loads(m.group(0)) if m else None


def check(tb, d, abilities):
    """Noms inconnus : capacités, augments, mods du noyau. Renvoie la liste des problèmes."""
    bad = []
    for c in (d.get("capacites") or {}):
        if c.lower() not in abilities: bad.append(f"capacité inconnue « {c} » (les vraies : {', '.join(sorted(abilities))})")
    for n in (d.get("augments") or {}):
        if "erreur" in tb.fiche_mod(n): bad.append(f"augment inconnu « {n} »")
    for a in d.get("archetypes") or []:
        for n in (a.get("noyau") or {}).get("mods", []):
            if "erreur" in tb.fiche_mod(n): bad.append(f"mod du noyau inconnu « {n} » (archétype {a.get('id')})")
        if (a.get("capacite_centrale") or "").lower() not in abilities | {""}:
            bad.append(f"capacité centrale inconnue « {a.get('capacite_centrale')} »")
    if not d.get("archetypes"): bad.append("aucun archétype")
    return bad


def generate(tb, base, frame, a, log=print):
    name, ctx = _frame_context(tb, base, frame)
    if not name: return log(f"{frame} : warframe inconnue")
    path = os.path.join(base, "01-donnees", "archetypes", name + ".json")
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as fh: old = json.load(fh)
        except (OSError, json.JSONDecodeError): old = {}
        if old.get("relu_par_le_joueur"): return log(f"{name} : relu par le joueur, jamais écrasé")
        if not a.force: return log(f"{name} : déjà généré (--force pour refaire)")
    abilities = {c["nom"].lower() for c in tb.fiche_warframe(name).get("capacites", [])}
    msgs = [{"role": "system", "content": PRINCIPES + "\n\n" + SCHEMA_TXT},
            {"role": "user", "content": ctx + "\n\nDéduis les archétypes de build de cette warframe à partir de ses capacités, "
                                              "de ses augments et des principes."}]
    d, bad = None, ["pas de réponse"]
    for attempt in range(2):
        try:
            d = _parse(_ask(a, msgs))
        except (json.JSONDecodeError, OSError, cloud.CloudError) as e:
            log(f"{name} : réponse illisible ({e})"); d = None
        if not d: continue
        bad = check(tb, d, abilities)
        if not bad: break
        msgs += [{"role": "assistant", "content": json.dumps(d, ensure_ascii=False)},
                 {"role": "user", "content": "Corrige ces noms (utilise seulement des noms exacts) et renvoie tout le JSON : " + " ; ".join(bad)}]
    if not d: return log(f"{name} : échec")
    for x in d.get("archetypes") or []:  # un nom resté inconnu sort du noyau
        x.setdefault("noyau", {})["mods"] = [n for n in x["noyau"].get("mods", []) if "erreur" not in tb.fiche_mod(n)]
    d.update(warframe=name, relu_par_le_joueur=False, date=datetime.date.today().isoformat(),
             statut=f"généré automatiquement par {a.model} le {datetime.date.today():%d/%m/%Y}, non relu par le joueur : moins sûr qu'un archétype relu"
                    + (f" ; problèmes restants : {'; '.join(bad)}" if bad else ""))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh: json.dump(d, fh, ensure_ascii=False, indent=1)
    log(f"{name} : {len(d.get('archetypes') or [])} archétypes" + (f" ({len(bad)} problèmes restants)" if bad else ""))


def main():
    ap = argparse.ArgumentParser(description="Génère les archétypes de build (hors ligne)")
    ap.add_argument("--base", required=True)
    ap.add_argument("--data", default=None)
    ap.add_argument("--model", required=True)
    ap.add_argument("--frame", action="append", help="une warframe (répétable) ; par défaut toutes")
    ap.add_argument("--force", action="store_true", help="refaire les archétypes générés (jamais ceux relus par le joueur)")
    ap.add_argument("--host", default="http://localhost:11434")
    ap.add_argument("--api-url", default=None)
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--ctx", type=int, default=16384)
    ap.add_argument("--think", default=None)
    a = ap.parse_args()
    data = a.data or os.path.join(os.path.dirname(os.path.abspath(a.base)), "companion-data")
    tb = ag.open_toolbox(a.base, data)
    frames = a.frame or sorted({re.sub(r"\s+(Prime|Umbra)$", "", r["name"]) for r in tb.con.execute("SELECT name FROM warframes")})
    for f in frames:
        generate(tb, a.base, f, a)


if __name__ == "__main__":
    main()
