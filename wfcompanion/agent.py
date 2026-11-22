"""Agent en ligne de commande : un modèle local (Ollama) qui appelle les outils au lieu de deviner.

    python -m wfcompanion.agent --base "E:\\IA\\warframe\\base-warframe"
    python -m wfcompanion.agent --base ... --model qwen3:8b --question "où farmer Organ Shatter ?"

Le modèle ne tourne qu'une fois à la fois (séquentiel) : comprendre, appeler des outils, répondre.
"""
import argparse, json, os, re, sys, urllib.error, urllib.request

from . import cloud, db, docs, mods_md, net
from .sources import SOURCES
from .tools import SCHEMAS, Toolbox

SYSTEM = """Tu es un compagnon expert de Warframe pour un joueur francophone expérimenté. Réponds en français.

RÈGLES (obligatoires) :
1. Ne cite JAMAIS de mémoire un nom d'arme, de mod, d'arcane, une stat, un taux de drop ou une formule. Tout doit venir d'un outil. Si aucun outil ne le donne, dis que la base ne contient pas l'information.
2. Ne fais JAMAIS un calcul de tête : utilise « calculer ». Les pourcentages sont des fractions (90 % = 0.9).
3. Dans les outils, les noms sont en anglais et les stats s'appellent : Ability Strength (puissance), Ability Duration (durée), Ability Range (portée), Ability Efficiency (efficacité), Energy Max, Health, Shield Capacity, Armor, Critical Chance, Critical Damage, Status Chance.
4. N'appelle jamais deux fois le même outil avec les mêmes arguments. « chercher_doc » prend des mots-clés (ex. « nom de capacité augment »), jamais une phrase ni une question destinée au joueur.

PRINCIPE : il n'y a pas de build unique ni de vérité absolue. Le jeu permet presque tout ; un build est bon s'il est adapté à ce que le joueur veut faire (type de mission, niveau des ennemis, rôle). Oriente toujours le build d'après son objectif, et dis pour quelle tâche il est fait.

QUESTIONS AU JOUEUR :
- Demande vague (« un build pour telle warframe ») : pose UNE SEULE série de 3 à 5 questions courtes (contenu visé, rôle, capacité à mettre en avant, solo ou escouade, ce qu'il possède).
- Demande précise, ou joueur qui a déjà répondu : NE POSE PLUS DE QUESTIONS. S'il manque une information, fais une hypothèse raisonnable, écris-la (« Hypothèse : ... ») et propose le build.

POUR UN BUILD (loadout COMPLET, dans cet ordre) :
1. « dossier_build » avec le nom de la warframe : stats au rang 30, profil de survie, passif (il compte dans le build), capacités chiffrées, augments, retours du joueur, meilleurs mods par stat. S'il existe un retour du joueur sur cette frame, c'est un exemple daté : reprends sa logique, ne recopie pas la liste.
2. Cherche PLUSIEURS façons d'atteindre l'objectif avant d'en choisir une. Pour un nuke par exemple : telle capacité de la frame avec son augment, une autre capacité combinée à une arme, ou une capacité Helminth d'une autre warframe (« options » catégorie helminth). Écris 2 ou 3 pistes en une ligne chacune (la pièce clé, le point fort, le point faible), puis développe la meilleure. Il n'y a pas de recette unique : raisonne à partir des chiffres des capacités.
   Ensuite décide la boucle de jeu : ce qui tue, ce qui protège, d'où vient l'énergie. Les stats prioritaires en découlent.
3. « options » pour choisir l'aura, l'Exilus, les 2 arcanes, le Helminth et le compagnon (catégories : aura, exilus, arcanes, helminth, compagnon). Le Helminth est une capacité d'une AUTRE warframe. Pas d'aura d'énergie (Energy Siphon).
4. Remplis TOUS les champs : role, source_energie, aura, exilus, 8 mods, 2 arcanes, helminth, focus, compagnon, 3 armes (principale, secondaire, melee). Les « avis_du_joueur » du dossier ne sont pas des règles absolues : comprends leur raison, applique-la si elle vaut pour ta piste, sinon explique pourquoi tu fais autrement. Une source d'énergie doit redonner de l'énergie (un plus gros maximum ne suffit pas).
5. « valider_build » avec le build complet. Corrige et rappelle-le tant que le statut n'est pas « complet et valide ». Les totaux, la capacité et les formas viennent de cet outil, jamais de toi.
   Certaines capacités sont canalisées : elles coûtent de l'énergie à chaque seconde, parfois de plus en plus (voir « cout_en_energie » et « fonctionnement » des augments, et « calculer » opération cout_canalise). Dis au joueur combien de secondes canaliser.
   Lis les « consequences_calculees » : elles disent ce que tes choix donnent vraiment sur cette frame. Si un choix rapporte peu (mod d'armure sur une frame à faible armure, arcane qui dépend d'une stat basse), remplace-le.
6. Réponse finale : recopie tel quel le tableau renvoyé par « valider_build », donne les totaux et les formas, puis explique :
   - la boucle de jeu et la chaîne de synergies (chaque pièce sert au moins deux éléments du build) ;
   - la survie au level cap (tuer avant d'être touché, invulnérabilité, invisibilité, shield gate, réduction de dégâts) : la santé et l'armure seules ne suffisent pas ;
   - les autres pistes envisagées et pourquoi tu ne les as pas retenues ;
   - pour 3 choix importants, l'alternative comparée avec ses chiffres ;
   - ce qui est [hypothèse] ou [à tester en jeu]. Le joueur décide, ses tests priment.
Pour modder une arme, mets-la sous la forme {nom, mods:[8], exilus, arcane} dans valider_build : il calcule ses dégâts par type, critiques, statut et DPS (sans les bonus conditionnels). Les mods d'arme se trouvent avec chercher_mods (pour = Rifle, Shotgun, Pistol, Melee). Pour choisir une arme, utilise « chercher_armes » (catégorie principale, secondaire ou melee), puis « fiche_arme » ; justifie-la par son rôle dans la boucle du build (ce que la frame ne fait pas). Demande au joueur quelles armes il possède si c'est décisif. FORME DE LA RÉPONSE DE BUILD : le tableau du build, puis 4 parties courtes : Boucle de jeu, Survie, Énergie, À tester en jeu. Ne parle jamais de validation, de contrôle, de règles, du système ni des outils : le programme affiche lui-même si le build est vérifié. Pas de phrase de remplissage. DÉFENSE : la santé seule ne tient pas à haut niveau. Défense par le bouclier (shield gate, Brief Respite, set Augur), combinable avec santé et armure ; OU Arcane Persistence, qui retire tout le bouclier : alors tout sur la santé et l'armure. Persistence demande une armure de base correcte ; avec peu d'armure, elle ne vaut le coup que si la frame a beaucoup de santé ET une capacité qui la rend insensible aux effets de statut. RETOUCHE : si le joueur demande de changer quelque chose dans le build affiché (fourni avec son message), pars de ce build, change seulement ce qu'il demande, revalide avec valider_build et explique l'effet du changement en 2 ou 3 lignes. NIVEAU DU JOUEUR : pour un débutant ou un joueur intermédiaire (« palier », « début du Steel Path »), évite ce qui est long ou difficile à obtenir (Primed, Umbral, Archon, Galvanized, augments de syndicat, Helminth, arcanes, focus pour un débutant) ; demande s'il a des mods corrompus ou un Orokin Reactor ; passe niveau à proposer_build. BUILD : construis-le toi-même en raisonnant (dossier_build, options, lire_document pour les pages de capacités et de mécaniques, retours du joueur) ; proposer_build peut te donner un point de départ calculé quand il existe, à critiquer. Valide toujours avec valider_build : c'est ce qui affiche le build dans l'éditeur du joueur. DOCUMENTS : toute la base est lisible avec chercher_doc, lister_documents et lire_document ; lis les pages utiles au lieu de deviner. REPÈRES : si dossier_build contient « archetypes », ce sont des pistes préparées à l'avance pour cette frame (boucle de jeu, pièges) : utiles, mais pas obligatoires ni toujours justes ; juge par toi-même. EXIGENCES DE BASE DU JOUEUR (avant tout choix de mod) : 1) la frame survit par elle-même ; 2) sauf build spécifique demandé, elle convient au maximum de contenu (solo et escouade, toutes missions, Steel Path level cap) ; 3) elle est autonome en énergie (montre que l'énergie gagnée couvre le coût de la boucle) ; 4) ses capacités mises en avant sont adaptées à l'objectif (ex. chasse d'Archonte = gros DPS mono-cible). Si un point n'est pas rempli, dis-le et explique pourquoi. MODS DE SURVIE (santé, bouclier, armure) : ni obligatoires ni interdits ; un tel mod vaut sa place seulement s'il sert le build : synergie de survie (ex. Redirection + Arcane Aegis), capacité qui en dépend, ou ressource propre de la frame (Hildryn : bouclier = énergie, donc plus de capacités lancées). Explique toujours ce choix. ARMES EXALTÉES : si fiche_warframe ou dossier_build indique « armes_exaltees » (Exalted Blade, Shattered Lash, Landslide Fists, Regulators…), cette arme est donnée par une capacité et se mode à part (arcane possible depuis l'Update 38.5) : mets-la dans armes.exaltees [{nom, mods:[8], exilus, arcane}] ; certaines dépendent aussi de la puissance ou de la portée de la frame (les remarques de valider_build le disent). Les armes exaltées de mêlée d'Ash, Atlas, Gara et Khora ont leur propre compteur de combo (dégâts jusqu'à x12) : Blood Rush et Weeping Wounds y sont forts car leur bonus de critique ou de statut monte avec ce combo ; valider_build donne les stats à combo 12x si le build utilise cette capacité. Garuda : ses griffes (Garuda Talons) ne sont pas exaltées, elles occupent l'emplacement de mêlée (armes.melee), aucune autre arme de mêlée possible. Si la base ne permet pas de justifier un choix (helminth, compagnon), écris-le comme [hypothèse].

Les noms des capacités viennent UNIQUEMENT du dossier (ne les invente pas, ne les traduis pas).

REMARQUES DU JOUEUR : quand il te corrige ou t'apprend quelque chose sur le jeu (« on ne joue pas cette frame sur l'armure », « tel augment est obligatoire »), appelle d'abord « noter_retour » avec sa remarque, et « noter_regle » pour chaque avis précis sur un mod, un arcane ou un focus (avec sa raison et le cas où il s'applique), puis corrige le build et REVALIDE-le avec « valider_build ». Un augment se met dans les 8 mods, à la place d'un autre.

LOADOUTS : le joueur enregistre ses builds. S'il parle de « mon build X » ou « mon loadout », appelle « lister_loadouts » puis « ouvrir_loadout » : tu y trouves le build, sa synthèse et les changements du jeu depuis la sauvegarde. Pour le mettre à jour, garde son intention, revalide-le, et n'appelle « enregistrer_loadout » que si le joueur le demande.

FARM : « ou_farmer », au moins deux sources, le nombre de tirages, et rappelle que la vitesse du farm n'est pas dans les tables.

Sois concis et structuré."""

NO_MORE_QUESTIONS = ("\n\n(Rappel du système : tu as déjà posé tes questions au joueur. N'en pose plus aucune. "
                     "S'il manque une information, fais une hypothèse, annonce-la, puis utilise les outils et propose le build complet.)")

MAX_ROUNDS = 18
MAX_TOOL_CHARS = {"dossier_build": 18000, "options": 9000, "valider_build": 6000, "chercher_armes": 5000}
DEFAULT_TOOL_CHARS = 3500


class ModelError(RuntimeError):
    pass


class OutOfMemory(ModelError):
    """La carte graphique n'a pas assez de mémoire libre pour charger le modèle avec ce contexte."""


MIN_CTX = 4096
OOM_HINT = ("La carte graphique manque de mémoire pour charger le modèle. Ferme le jeu et les autres modèles "
            "(commande « ollama ps » pour les voir, « ollama stop <modèle> » pour les décharger), "
            "ou choisis un modèle plus petit.")


META = re.compile(r"(valid|contr[ôo]le(?! de (la )?foule)|le syst[èe]me|valider_build|appel identique|règles? du jeu|conforme aux règles|outil)", re.I)


def _clean_answer(answer, validated):
    """Retire ce que le modèle dit de la validation et du système (le programme affiche le statut lui-même)."""
    lines, skip = [], False
    for line in answer.split("\n"):
        if re.match(r"\s*#*\s*\**\s*(pourquoi ce build est valide|statut)", line, re.I):
            skip = True; continue
        if skip and (line.strip() == "" or line.lstrip().startswith(("-", "*", "•"))) and (META.search(line) or line.strip() == ""):
            continue
        skip = False
        if META.search(line) and not line.lstrip().startswith("|"):  # on retire la phrase, pas toute la ligne
            kept = [x for x in re.split(r"(?<=[.!?])\s+", line) if not META.search(x)]
            line = " ".join(kept).strip()
            if not line or re.fullmatch(r"[\W_]*", line): continue
        lines.append(line)
    out = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return ("✅ Build vérifié par le programme (mods, capacité, totaux).\n\n" + out) if validated else out


LAST_USAGE = {}  # jetons réellement comptés par Ollama au dernier appel : sert à mesurer la place prise dans le contexte
REPLY_RESERVE = 3500  # jetons gardés libres pour la réflexion et la réponse (un build complet en appel d'outil est long)


def ollama_chat(host, model, messages, tools, options=None, think=None, debug=False, fmt=None):
    body = {"model": model, "messages": messages, "stream": False, "keep_alive": "30m",  # pas de rechargement entre deux questions
            "options": {"temperature": 0.2, "num_ctx": 16384, **(options or {})}}
    if tools: body["tools"] = tools
    if fmt: body["format"] = fmt  # « json » : Ollama force une réponse JSON valide (utile aux petits modèles)
    if think: body["think"] = True if think == "on" else (False if think == "off" else think)
    req = urllib.request.Request(host.rstrip("/") + "/api/chat", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=900) as r:
            full = json.loads(r.read())
        if debug:
            m = full.get("message", {})
            print(f"  [debug] fin={full.get('done_reason')} jetons_entree={full.get('prompt_eval_count')} "
                  f"jetons_sortie={full.get('eval_count')} contenu={len(m.get('content') or '')} car. "
                  f"reflexion={len(m.get('thinking') or '')} car. outils={len(m.get('tool_calls') or [])}")
        n = LAST_USAGE.get("n", 0) + 1
        LAST_USAGE.clear()
        LAST_USAGE.update(n=n, prompt=full.get("prompt_eval_count"), out=full.get("eval_count"), done=full.get("done_reason"),
                          secondes=round((full.get("total_duration") or 0) / 1e9, 1),
                          lecture_s=round((full.get("prompt_eval_duration") or 0) / 1e9, 1),
                          reflexion=len((full.get("message") or {}).get("thinking") or ""),
                          chars=sum(len(m.get("content") or "") + len(json.dumps(m.get("tool_calls") or "")) for m in messages)
                                + len(json.dumps(tools or [], ensure_ascii=False)))
        return full["message"]
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        if re.search(r"out of memory|failed to allocate|cudaMalloc failed|requires more system memory", detail, re.I):
            raise OutOfMemory(f"Ollama a répondu HTTP {e.code} (mémoire insuffisante) : {detail}")
        raise ModelError(f"Ollama a répondu HTTP {e.code} : {detail}")


# petits modèles conseillés, du meilleur au plus léger (tous gèrent le français) ; le premier installé est pris
PETITS_MODELES = ["qwen3.5:2b", "qwen3:1.7b", "qwen3.5:0.8b", "gemma4:e2b", "llama3.2:3b", "llama3.2:1b"]
MODELE_PAR_DEFAUT = "qwen3.5:2b"


def ollama_pull(host, model, log=print):
    """Télécharge un modèle dans Ollama (comme « ollama pull »), en affichant l'avancement."""
    req = urllib.request.Request(host.rstrip("/") + "/api/pull", data=json.dumps({"model": model, "stream": True}).encode(),
                                 headers={"Content-Type": "application/json"})
    last = ""
    with urllib.request.urlopen(req, timeout=3600) as r:
        for line in r:
            try: ev = json.loads(line)
            except ValueError: continue
            if ev.get("error"): raise ModelError(f"téléchargement de {model} impossible : {ev['error']}")
            st = ev.get("status", "")
            if ev.get("total"): st += f" {100 * (ev.get('completed') or 0) // ev['total']} %"
            if st != last: log(f"  {model} : {st}"); last = st


def choose_model(host, wanted="auto", log=print):
    """« auto » : le premier petit modèle conseillé déjà installé, sinon téléchargement du modèle par défaut."""
    try: have = ollama_models(host)
    except Exception as e:
        raise ModelError(f"Ollama ne répond pas sur {host} : installe-le depuis https://ollama.com/download puis relance ({e})")
    if wanted and wanted != "auto":
        if not any(m == wanted or m.split(":")[0] == wanted for m in have):
            log(f"Modèle {wanted} absent : téléchargement (une seule fois)…"); ollama_pull(host, wanted, log)
        return wanted
    for m in PETITS_MODELES:
        if m in have: return m
    log(f"Aucun petit modèle installé : téléchargement de {MODELE_PAR_DEFAUT} (une seule fois)…")
    ollama_pull(host, MODELE_PAR_DEFAUT, log)
    return MODELE_PAR_DEFAUT


def ollama_models(host):
    with urllib.request.urlopen(host.rstrip("/") + "/api/tags", timeout=10) as r:
        return [m["name"] for m in json.loads(r.read()).get("models", [])]


class Agent:
    def __init__(self, toolbox, chat, log=None):
        """chat(messages, tools) -> message du modèle. Injecté pour pouvoir tester sans modèle."""
        self.tb, self.chat, self.log = toolbox, chat, log
        self.messages = [{"role": "system", "content": SYSTEM}]
        self.asked = False  # le modèle a-t-il déjà posé ses questions ?
        self.building = False  # un build est-il en cours dans cette conversation ?
        self.ctx_tokens = 16384
        self.ctx_box = None  # {"n": contexte envoyé à Ollama}, partagé avec la fonction de discussion

    def _trim(self, hard=False):
        """Garde la conversation sous la taille du contexte : les vieux résultats d'outils sont abrégés en premier.
        Le rapport caractères/jeton est mesuré sur le dernier appel à Ollama (sinon 2,5) ; la liste des outils compte aussi."""
        cpt = 2.5
        if LAST_USAGE.get("prompt") and LAST_USAGE.get("chars"):
            cpt = max(1.8, min(4.0, LAST_USAGE["chars"] / LAST_USAGE["prompt"]))
        free = self.ctx_tokens - REPLY_RESERVE - (1500 if hard else 0)
        budget = int(free * cpt) - len(json.dumps(SCHEMAS, ensure_ascii=False))
        size = lambda: sum(len(m.get("content") or "") + len(json.dumps(m.get("tool_calls") or "")) for m in self.messages)
        tools = [i for i, m in enumerate(self.messages) if m["role"] == "tool" and m.get("name") != "dossier_build"]
        dossiers = [i for i, m in enumerate(self.messages) if m["role"] == "tool" and m.get("name") == "dossier_build"]
        for i in dossiers[:-1]:  # seul le dossier le plus récent reste entier
            if len(self.messages[i]["content"]) > 500:
                self.messages[i]["content"] = self.messages[i]["content"][:350] + " …(dossier ancien abrégé)"
        for keep in (2, 1, 0):
            for i in (tools[:-keep] if keep else tools):
                if size() <= budget: return
                c = self.messages[i]["content"]
                if len(c) > 500:
                    self.messages[i]["content"] = c[:350] + " …(résultat ancien abrégé : rappelle l'outil si besoin)"

    def _say(self, t):
        if self.log: self.log(t)

    def _model(self, tools):
        """Appelle le modèle ; une erreur du serveur (souvent un appel d'outil mal formé) est retentée une fois."""
        self._trim()
        while True:
            try:
                return self._model_once(tools)
            except OutOfMemory as e:
                box = self.ctx_box
                if not box or box["n"] <= MIN_CTX:
                    raise OutOfMemory(OOM_HINT + f"\n\nDétail : {e}") from None
                box["n"] = max(MIN_CTX, box["n"] // 2); self.ctx_tokens = box["n"]
                self._say(f"  [modèle] mémoire graphique insuffisante : nouvel essai avec un contexte de {box['n']} jetons")
                self._trim()

    def _model_once(self, tools):
        try:
            return self.chat(self.messages, tools)
        except (cloud.CloudError, OutOfMemory):
            raise
        except ModelError as e:
            self._say(f"  [modèle] erreur, nouvel essai : {e}")
            self.messages.append({"role": "user", "content": "Ton dernier appel d'outil était mal formé. "
                                  "Recommence avec un seul appel d'outil simple, ou réponds directement."})
            try:
                return self.chat(self.messages, tools)
            finally:
                pass

    def ask(self, text):
        self.messages.append({"role": "user", "content": text + (NO_MORE_QUESTIONS if self.asked else "")})
        player_text = text.split("\n\n(Build affiché")[0].split("\n\n(Le build affiché")[0].strip()
        seen, empty, building, validated, pushes, last_issues = set(), 0, False, None, 0, []
        arch_gap, arch_pushed = "", False
        looks_like_build = lambda t: "| Mod" in t or "| Aura" in t or "Emplacement" in t
        is_question = lambda t: "?" in t and not looks_like_build(t)
        for _ in range(MAX_ROUNDS):
            n_before = LAST_USAGE.get("n", 0)
            msg = self._model(SCHEMAS)
            if LAST_USAGE.get("n", 0) != n_before and LAST_USAGE.get("secondes"):  # où part le temps : lecture du contexte, réflexion, réponse
                u = LAST_USAGE
                self._say(f"  [modèle] {u['secondes']} s (lecture {u.get('lecture_s')} s de {u.get('prompt')} jetons, "
                          f"{u.get('out')} jetons écrits" + (f", dont réflexion {u['reflexion']} car." if u.get("reflexion") else "") + ")")
            msg = {k: v for k, v in msg.items() if k != "thinking" or not (msg.get("content") or msg.get("tool_calls"))}
            self.messages.append(msg)
            calls = msg.get("tool_calls") or []
            if not calls:
                answer = (msg.get("content") or "").strip()
                if not answer:
                    # réponse vide : fréquent avec les modèles « à réflexion » (tout est parti dans la réflexion)
                    empty += 1
                    think = (msg.get("thinking") or "").strip()
                    self._say(f"  [modèle] réponse vide (essai {empty})" + (f" ; réflexion : {think[:300]}" if think else ""))
                    self.messages.pop()
                    if LAST_USAGE.get("done") == "length" or (LAST_USAGE.get("prompt") or 0) > self.ctx_tokens - REPLY_RESERVE:
                        self._say(f"  [modèle] contexte plein ({LAST_USAGE.get('prompt')} jetons sur {self.ctx_tokens}) : anciens résultats abrégés")
                    self._trim(hard=True)
                    if empty >= 3:
                        return ("Le modèle n'a rien répondu après 3 essais. Essaie un autre modèle (--model) "
                                "ou relance avec --debug pour voir ce qu'il renvoie.")
                    self.messages.append({"role": "user", "content": "Ta réponse était vide. Appelle un outil "
                                          "(dossier_build pour un build) ou écris ta réponse au joueur."})
                    continue
                if is_question(answer) and validated is None:
                    # le modèle demande des précisions : c'est permis une fois ; ensuite il doit construire avec les réponses
                    if not self.asked:
                        self.asked = True
                        return answer
                    if pushes < 3:
                        pushes += 1
                        self._say("  [contrôle] questions déjà posées : renvoi au modèle pour qu'il construise le build")
                        self.messages.append({"role": "user", "content":
                            f"Le joueur a déjà répondu à tes questions. Ses réponses : « {player_text[:600]} ». Ne repose aucune "
                            "question. Pour ce qui manque, fais une hypothèse et annonce-la. Construis maintenant le build "
                            "(dossier_build sur la warframe dont parle le joueur, puis valider_build)."})
                        continue
                    return answer
                if (building or (self.building and looks_like_build(answer))) and validated != "complet et valide" and pushes < 3:
                    pushes += 1
                    self._say("  [contrôle] build non validé : renvoi au modèle")
                    self.messages.append({"role": "user", "content":
                        "Ton build n'est pas encore validé. " + (("Problèmes à corriger : " + " ; ".join(last_issues)[:900] + ". ") if last_issues else "")
                        + "Appelle valider_build avec le build COMPLET et CORRIGÉ : {warframe, role, source_energie, aura, exilus, "
                        "mods:[8], arcanes:[2], helminth, focus, compagnon, armes:{principale, secondaire, melee}}."})
                    continue
                if False and validated == "complet et valide" and arch_gap and not arch_pushed:  # désactivé : le joueur ne veut pas imposer d'archétype
                    arch_pushed = True
                    self._say("  [contrôle] build valide mais hors des archétypes préparés : renvoi au modèle")
                    self.messages.append({"role": "user", "content":
                        f"Ton build est valide mais ne suit aucun archétype préparé ({arch_gap}). Reprends le noyau de "
                        "l'archétype qui correspond à l'objectif du joueur et revalide ; ou, si ton choix est voulu, ajoute "
                        "au build le champ hors_archetype avec la raison, revalide, et explique-la au joueur."})
                    validated = None
                    continue
                if looks_like_build(answer) or validated is not None:
                    answer = _clean_answer(answer, validated == "complet et valide") or answer
                if (looks_like_build(answer) or validated is not None) and validated != "complet et valide":
                    answer = ("**ATTENTION : ce build n'a PAS été validé par le contrôle.** Le modèle n'a pas réussi à le corriger. "
                              + (f"Problèmes restants : {'; '.join(last_issues)[:600]}\n\n" if last_issues else "\n\n") + answer)
                if validated == "complet et valide": self.asked = False  # build livré : la demande suivante peut reposer des questions
                elif "?" in answer: self.asked = True
                return answer
            for c in calls:
                fn = c.get("function", {})
                name, args = fn.get("name"), fn.get("arguments") or {}
                if isinstance(args, str):
                    try: args = json.loads(args)
                    except json.JSONDecodeError: args = {}
                key = (name, json.dumps(args, sort_keys=True, ensure_ascii=False).lower())
                if key in seen:
                    result = {"erreur": "appel identique déjà fait : le résultat ne changera pas. Change d'outil ou d'arguments, "
                                        "ou réponds avec ce que tu as."}
                else:
                    seen.add(key)
                    result = self.tb.call(name, args)
                    if name == "dossier_build" and "erreur" not in result: building = self.building = True
                    if name == "valider_build":
                        building = self.building = True; validated = result.get("statut")
                        last_issues = result.get("erreurs", []) + ["manquant : " + m for m in result.get("manquants", [])]
                        arch_gap = result.get("archetype_non_suivi") or ""
                        self._say(f"  [contrôle] {validated} ; erreurs : {len(result.get('erreurs', []))} ; "
                                  f"manquants : {', '.join(result.get('manquants', [])) or 'aucun'}")
                self._say(f"  [outil] {name}({json.dumps(args, ensure_ascii=False)})" + ("  -> " + result["erreur"][:90] if isinstance(result, dict) and "erreur" in result else ""))
                out = json.dumps(result, ensure_ascii=False)
                limit = MAX_TOOL_CHARS.get(name, DEFAULT_TOOL_CHARS)
                if len(out) > limit: out = out[:limit] + " …(tronqué)"
                self.messages.append({"role": "tool", "tool_name": name, "name": name, "content": out})
        self.messages.append({"role": "user", "content": "Tu as assez d'informations : réponds maintenant, sans appeler d'outil."})
        final = (self._model([]).get("content") or "").strip()
        return final or "Le modèle n'a pas produit de réponse finale. Relance avec --debug pour voir ce qu'il renvoie."


def open_toolbox(base, data):
    sqlite_path = os.path.join(data, "warframe.sqlite")
    if not os.path.exists(sqlite_path):
        raise SystemExit("Base absente : lance d'abord mise-a-jour.bat")
    if db.needs_rebuild(sqlite_path):
        print("Le programme a changé : reconstruction de la base et des fichiers de mods...")
        raw = os.path.join(data, "raw")
        for name, url in SOURCES.items():  # nouvelles sources ajoutées par une mise à jour du programme
            if not os.path.exists(os.path.join(raw, name)):
                try: net.fetch_if_changed(url, os.path.join(raw, name), {})
                except Exception as e: print(f"  source indisponible : {name} ({e})")
        db.build(raw, sqlite_path)
        mods_md.build(raw, os.path.join(base, "01-donnees", "mods"))
    docs_path = os.path.join(data, "docs.sqlite")
    n = docs.ensure(base, docs_path)  # réindexe seulement si un fichier de la base a changé
    if n: print(f"Doc réindexée : {n} extraits.")
    return Toolbox(sqlite_path, docs_path, base)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Compagnon Warframe (modèle local Ollama + outils).")
    ap.add_argument("--base", required=True)
    ap.add_argument("--data", default=None)
    ap.add_argument("--model", default=None, help="modèle Ollama (défaut : le premier installé)")
    ap.add_argument("--host", default="http://localhost:11434")
    ap.add_argument("--question", default=None, help="pose une seule question puis quitte")
    ap.add_argument("--ctx", type=int, default=16384, help="taille du contexte en jetons (8192 si la VRAM manque, 24576 ou 32768 si elle le permet)")
    ap.add_argument("--api-url", default=None, help="IA en ligne compatible OpenAI, ex. https://.../v1 (sinon Ollama local)")
    ap.add_argument("--api-key", default=None, help="clé de l'IA en ligne (ou variable WF_API_KEY, ou fichier cle-api.txt)")
    ap.add_argument("--cloud", default=None, choices=sorted(cloud.PRESETS), help="IA en ligne gratuite prête à l'emploi : groq, gemini, openrouter")
    ap.add_argument("--think", default=None, help="réflexion du modèle : off, on, low, medium, high (selon le modèle)")
    ap.add_argument("--debug", action="store_true", help="affiche ce que le modèle renvoie à chaque appel")
    ap.add_argument("--quiet", action="store_true", help="ne pas afficher les appels d'outils")
    a = ap.parse_args(argv)
    base = os.path.abspath(a.base)
    data = a.data or os.path.join(os.path.dirname(base), "companion-data")
    tb = open_toolbox(base, data)
    online = cloud.resolve(a)
    if online:
        a.api_url, key, a.model = online
        print(f"IA en ligne : {a.api_url}   modèle : {a.model}")
        chat_fn = lambda m, t: cloud.chat(a.api_url, key, a.model, m, t, a.debug)
        if a.ctx == 16384: a.ctx = 65536  # les modèles en ligne ont un grand contexte
    else:
        try:
            models = ollama_models(a.host)
        except Exception as e:
            raise SystemExit(f"Ollama ne répond pas sur {a.host} ({e}). Lance Ollama puis réessaie.")
        model = a.model or (models[0] if models else None)
        if not model:
            raise SystemExit("Aucun modèle installé dans Ollama (ollama pull <modèle>).")
        if model not in models:
            print(f"Attention : « {model} » n'est pas dans la liste d'Ollama : {', '.join(models)}")
        print(f"Modèle : {model}   (modèles disponibles : {', '.join(models)})")
        box = {"n": a.ctx}
        chat_fn = lambda m, t: ollama_chat(a.host, model, m, t, {"num_ctx": box["n"]}, a.think, a.debug)
    agent = Agent(tb, chat_fn, log=None if a.quiet else print)
    agent.ctx_tokens = a.ctx
    if not a.api_url: agent.ctx_box = box
    if a.question:
        print(agent.ask(a.question)); return
    print("Pose ta question (« quit » pour sortir).")
    while True:
        try: q = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt): break
        if not q: continue
        if q.lower() in ("quit", "exit"): break
        try:
            print("\n" + agent.ask(q))
        except Exception as e:
            print(f"Erreur : {e}")


if __name__ == "__main__":
    sys.exit(main())
