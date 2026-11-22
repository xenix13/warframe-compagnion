"""Avis du joueur sur les builds : ce qu'il a dit, avec sa raison et le cas où ça s'applique.

Ce ne sont PAS des règles absolues (XeniX13, 13/11/2026 : « il n'y a pas vraiment de règles pour les builds, l'agent doit
avoir la logique lui-même »). Le contrôle ne refuse pas un build pour ça : il rappelle l'avis et sa raison, et l'agent
doit soit le suivre, soit expliquer pourquoi son build fait autrement (autre capacité, autre Helminth...).

Fichier : <base>/04-retours-experience/regles-builds.json (lisible et modifiable à la main).
    {"Banshee": {"obligatoires": [{"nom": "...", "si_role": "nuke", "raison": "..."}],
                 "interdits":    [{"nom": "...", "raison": "..."}],
                 "focus": {"nom": "Zenurik", "raison": "..."},
                 "notes": ["..."]}}
Une règle sous « * » s'applique à toutes les warframes.
"""
import datetime, json, os

FILE = os.path.join("04-retours-experience", "regles-builds.json")


def load(base):
    try:
        with open(os.path.join(base, FILE), encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save(base, data):
    path = os.path.join(base, FILE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def for_frame(base, frame):
    """Règles applicables à une warframe (les siennes + les règles générales « * »)."""
    data = load(base) if base else {}
    out = {"obligatoires": [], "interdits": [], "focus": None, "notes": []}
    for key in ("*", frame):
        r = data.get(key) or {}
        out["obligatoires"] += r.get("obligatoires", [])
        out["interdits"] += r.get("interdits", [])
        out["notes"] += r.get("notes", [])
        if r.get("focus"): out["focus"] = r["focus"]
    return out


def add(base, frame, kind, nom, raison, si_role=None):
    data = load(base)
    r = data.setdefault(frame, {})
    today = datetime.date.today().strftime("%d/%m/%Y")
    if kind == "focus":
        r["focus"] = {"nom": nom, "raison": raison, "date": today}
    elif kind == "note":
        r.setdefault("notes", []).append(f"{raison} ({today})")
    elif kind in ("obligatoire", "interdit"):
        lst = r.setdefault(kind + "s", [])
        lst[:] = [x for x in lst if x.get("nom", "").lower() != nom.lower()]
        item = {"nom": nom, "raison": raison, "date": today}
        if si_role: item["si_role"] = si_role
        lst.append(item)
    else:
        return False
    save(base, data)
    return True


def check(rules, role, used_names, focus):
    """Renvoie les avis du joueur que le build ne suit pas (à suivre ou à justifier, jamais bloquants)."""
    errors = []
    used = {n.lower() for n in used_names}
    role = (role or "").lower()
    for o in rules["obligatoires"]:
        cond = (o.get("si_role") or "").lower()
        if cond and cond not in role: continue
        if o["nom"].lower() not in used:
            errors.append(f"« {o['nom']} » est conseillé par le joueur" + (f" quand le build est : {cond}" if cond else "") + f". Raison : {o.get('raison', '')}")
    for i in rules["interdits"]:
        if i["nom"].lower() in used:
            errors.append(f"« {i['nom']} » est déconseillé par le joueur ici. Raison : {i.get('raison', '')}")
    f = rules.get("focus")
    if f and focus and f["nom"].lower() not in focus.lower():
        errors.append(f"le joueur préfère le focus {f['nom']} ici. Raison : {f.get('raison', '')}")
    return errors
