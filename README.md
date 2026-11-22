# Compagnon Warframe

Un compagnon pour construire ses builds Warframe : on discute avec l'IA, le build apparaît dans l'éditeur, on l'affine en
parlant, on l'enregistre. Les builds sont calculés par un « robot » (règles de jeu écrites dans le code) ; le petit modèle
d'IA ne fait que comprendre la demande et expliquer. Tout tourne sur le PC, sans clé d'API.

## Installation (Windows 10/11)

1. Télécharge **CompagnonWarframe-Setup-x.y.z.exe** dans les [Releases](https://github.com/xenix13/warframe-compagnion/releases/latest).
2. Lance-le (pas besoin de droits administrateur), puis ouvre **Compagnon Warframe** depuis le bureau.

Au premier lancement, l'outil prépare les données du jeu puis télécharge le modèle d'IA (llama.cpp + Qwen3 1.7B,
environ 1,8 Go). Rien d'autre à installer : ni Python, ni Ollama, ni clé d'API. Le modèle tourne sur le processeur
(le plus sûr) ; `lancer.bat --gpu` essaie la carte graphique.

## Installation en une commande (variante PowerShell)

Dans PowerShell :

```
irm https://raw.githubusercontent.com/xenix13/warframe-compagnion/main/install.ps1 | iex
```

Le script installe Python si besoin, l'outil dans `%LOCALAPPDATA%\CompagnonWarframe`, le modèle intégré
(llama.cpp + Qwen3 1.7B, environ 1,8 Go, **sans Ollama**), les données du jeu, et crée le raccourci
« Compagnon Warframe » sur le bureau. Relancer la commande met l'outil à jour sans toucher aux loadouts ni au modèle.

Options (avant la commande) : `$env:COMPAGNON_OPTIONS="--leger"` (modèle 0.6B pour un PC modeste), `"--gpu"` (version carte graphique ; par défaut le modèle tourne sur le processeur, sans carte
graphique), `"--sans-ia"` (robot seul) ; `$env:COMPAGNON_DOSSIER="D:\Jeux\Compagnon"` pour un autre dossier.

Installation à la main : télécharger le dépôt, puis `installer.bat`, puis `lancer.bat`.

Sources et licences : voir `SOURCES.md`.

---

## Mise à jour des données et moteur de calcul

Première brique du futur compagnon : il garde la base `base-warframe` à jour et fournit des calculs fiables, que l'agent appellera au lieu de calculer « de tête ».

## Ce que fait la mise à jour

1. Télécharge les sources **seulement si elles ont changé** (cache ETag) : données du jeu (mods, arcanes, warframes, armes, ressources) et tables de drop officielles, toutes publiées par WFCD sur GitHub.
2. Si quelque chose a changé : reconstruit la base SQLite `companion-data/warframe.sqlite`, les fichiers `01-donnees/farm/Farm - *.md` et `01-donnees/mods/*.md`.
3. Rafraîchit les pages du wiki de `02-wiki/systemes`, `02-wiki/farm` et `02-wiki/contenu-recent` dont la révision a changé.
4. Écrit `00 - Etat de la base.md` (dates des données) pour que l'agent sache de quand date ce qu'il lit.

Quand rien n'a changé, l'exécution prend 2 à 3 secondes : on peut la lancer à chaque ouverture de l'app.

**Jamais touchés** : `Mod Set Mod.md` (complété à la main), `Farm - Principes et limites.md`, `03-patch-notes`, `04-retours-experience`, `05-builds-proposes`, et les pages wiki des armes et warframes.

## Installation (Windows)

1. Python 3.10 ou plus récent (cocher « Add to PATH »).
2. Dans ce dossier : `pip install -r requirements.txt`
3. Premier lancement, à la main : double-clic sur `mise-a-jour.bat`, ou :
   ```
   python -m wfcompanion.update --base "E:\IA\warframe\base-warframe"
   ```
   Le premier lancement télécharge environ 30 Mo et rafraîchit toutes les pages wiki suivies (environ 1 minute).
4. Relancer l'indexation RAG d'Open WebUI après une mise à jour qui a changé des fichiers.

Options : `--no-wiki` (sans le wiki), `--force` (tout reconstruire), `--data <dossier>` (par défaut `E:\IA\warframe\companion-data`).

## Lancement automatique (planificateur de tâches)

Chaque jour à 9 h 07, par exemple :
```
schtasks /Create /TN "Warframe - mise a jour base" /SC DAILY /ST 09:07 /TR "\"E:\IA\warframe\companion\mise-a-jour.bat\""
```

## Moteur de calcul (`wfcompanion/calc.py`)

Formules validées par le wiki ou par tes mesures en jeu, avec tests (`python -m unittest discover -s tests`) :
- multiplicateur et niveaux de critique (vérifié : 3,2x vers 5,0x avec Organ Shatter) ;
- réduction de dégâts d'armure ennemie et gain du retrait d'armure ; réduction de dégâts du joueur ; PV effectifs ;
- durée du shield gate ;
- stats de capacités, coût en énergie (coût x (2 - efficacité), minimum 25 %), énergie au rang 30, fragment violet ;
- nombre de tirages pour obtenir un drop ;
- lecture des effets de mods (« +99% Ability Strength »), les effets conditionnels étant mis de côté.

## Agent avec outils (`compagnon.bat`)

Un modèle local Ollama qui **appelle des outils** au lieu de deviner : dossier de build d'une warframe (capacités chiffrées, augments, retours du joueur, meilleurs mods par stat), fiche d'un mod, recherche de mods par effet, fiche de warframe, d'arme et d'arcane, sources de farm, recherche dans tes retours d'expérience et la doc, et calculs exacts.

```
compagnon.bat
compagnon.bat --model <nom du modèle Ollama>
compagnon.bat --question "où farmer Organ Shatter ?"
```

- Pour un build, le modèle doit remplir un loadout complet (aura, Exilus, 8 mods, 2 arcanes, Helminth, focus, compagnon, 3 armes) et le faire **valider par le code** (`valider_build`) : mods inexistants, doublons, familles qui ne se cumulent pas, emplacements vides, totaux exacts, capacité et formas. Tant que ce n'est pas valide, sa réponse est refusée.
- Quand tu le corriges, l'agent note ta remarque dans `04-retours-experience/Retours du joueur notés par l'agent.md` (statut « dit par le joueur ») et la retrouve aux conversations suivantes.
- Modèle conseillé d'après les essais du 13/11/2026 : `gemma4:12b`. `gpt-oss:20b` sature le contexte avec sa réflexion et produit des appels d'outils mal formés.
- Ollama doit être lancé. Le modèle doit savoir appeler des outils (« tools ») : la page du modèle sur ollama.com l'indique.
- Les appels d'outils s'affichent (`[outil] ...`) : c'est ce qui permet de voir si le modèle travaille bien. `--quiet` les masque.
- La recherche dans la doc est réindexée au lancement dès qu'un fichier de la base a changé : tes nouveaux retours d'expérience sont pris en compte tout de suite.
- `--ctx 8192` réduit la mémoire utilisée si la VRAM manque (défaut : 16384).
- Un seul modèle, utilisé de façon séquentielle ; pas besoin de modèle d'embeddings.

## Données relevées dans le wiki (dans `base-warframe/01-donnees`)

- `couts-capacites.json` : pour chaque warframe, le coût de ses capacités, celles qui sont canalisées (coût par seconde ou par action), sa ressource propre (Hildryn, Lavos, Baruuk) et son passif.
- `capacites-canalisees.json` : capacités dont le coût croît avec le temps (ex. Sound Quake avec Gaseous Quake). Se complète à la main.
- `augments-notes.json` : notes de fonctionnement des augments.

Le contrôle des builds s'en sert pour dire ce qu'un build coûte vraiment en énergie.

## Interface (`interface.bat`)

Deux onglets :
- **Compagnon** : la discussion à gauche, l'éditeur de build à droite. Tu demandes un build (« je débute, propose-moi un build pour Atlas », « build Atlas Prime level cap »), le compagnon répond et le build apparaît aussitôt dans l'éditeur. Tu peux ensuite l'affiner en parlant (« remplace Blind Rage par Streamline ») ou à la main dans l'éditeur, puis « Enregistrer le loadout ». Il répond aussi aux questions de farm et de mécaniques.
- **Mes loadouts** : builds enregistrés, synthèse, historique, vérification après une mise à jour du jeu.

Le compagnon adapte le build au niveau du joueur (débutant, palier, endgame) et pose une ou deux questions sur ce qu'il possède (mods corrompus, Orokin Reactor…). Les réponses sont gardées dans `04-retours-experience/profil-joueur.json`.

Avec un petit modèle local : `interface.bat --model qwen3:4b --think off`.

### Détails de l'éditeur

Un constructeur de build dans le navigateur, façon Overframe, branché sur la même base et le même contrôle que l'agent :

```
interface.bat --model gemma4:12b
interface.bat --api-url https://<fournisseur>/v1 --model <modèle>
```

La page s'ouvre sur http://localhost:8765. On choisit la warframe, puis l'aura, l'Exilus et les 8 mods (fenêtre de recherche filtrée : seuls les mods compatibles et existants en jeu s'affichent, augments en premier), les arcanes, le Helminth, le focus, le compagnon et les armes. Les totaux, la capacité, les formas, les erreurs et les conséquences calculées se mettent à jour à chaque changement. Le panneau de discussion envoie la question à l'agent avec le build affiché ; quand l'agent propose un build, un bouton le charge dans l'éditeur. Chaque arme (onglets Principale, Secondaire, Mêlée) a son Exilus, ses 8 mods (seuls les mods compatibles avec l'arme s'affichent) et son arcane ; l'interface calcule ses dégâts par type (éléments combinés dans l'ordre des mods), critique, statut, multitir, DPS en rafale et soutenu, sans les bonus conditionnels. Quand la warframe a une arme exaltée (Exalted Blade, Shattered Lash, Landslide Fists, Regulators, Diwata…), un onglet « Exaltée » apparaît : elle se mode à part (8 mods, Exilus, arcane de son type depuis l'Update 38.5) et a son propre calcul. Les règles propres à chaque arme exaltée (dégâts multipliés par la puissance de la frame, portée par la portée de capacité, combo de capacité) sont dans `base-warframe/01-donnees/armes-exaltees.json`, à compléter après vérification en jeu. Pour Garuda, l'onglet Mêlée est verrouillé sur ses griffes : ce n'est pas une arme exaltée, mais elles prennent l'emplacement de mêlée. Les 5 fragments d'Archonte comptent dans les totaux (puissance, durée, santé, bouclier, armure, énergie) et dans les armes (dégâts critiques de mêlée, avec le doublement du violet au-dessus de 500 d'énergie max). Chaque emplacement de mod de la warframe a un sélecteur de polarité : quand tu en poses, la capacité et les formas sont calculées avec tes polarités. Sans `--model`, l'éditeur marche mais la discussion est désactivée. Les images viennent du CDN de WFCD (connexion Internet nécessaire pour les voir).

## Petit modèle local (1 à 2 milliards de paramètres)

Les builds sont calculés par le robot (code) ; le modèle ne fait que comprendre la demande (en JSON) et expliquer.
Un petit modèle suffit donc.

1. Installer Ollama : https://ollama.com/download
2. Lancer `installer-modele.bat` (télécharge `qwen3.5:2b` une seule fois) ; `installer-modele.bat leger` pour `qwen3.5:0.8b`.
3. Lancer `interface.bat` : `--model auto` prend le premier petit modèle installé (qwen3.5:2b, qwen3:1.7b, qwen3.5:0.8b,
   gemma4:e2b, llama3.2…), et le télécharge s'il n'y en a aucun. Pour un autre modèle : `interface.bat --model gemma4:12b`.

Avec un petit modèle, l'interface coupe la réflexion (`--think off`), réduit le contexte à 8192 et force les réponses JSON
(option `format: json` d'Ollama). Sans Ollama, l'interface marche quand même : le robot construit et explique seul.

## Loadouts enregistrés (`base-warframe/06-builds-joueur/<nom>/`)

Un loadout garde le build, une **synthèse** de l'explication (objectif et rôle, boucle de jeu, mécaniques clés, survie, énergie, points faibles, alternatives, à tester), la conversation avec l'agent et **toutes les versions**.

- Panneau « Loadouts » de l'interface : « Enregistrer » ajoute une version au loadout ouvert, « Enregistrer sous… » en crée un nouveau. La raison du changement est demandée et gardée dans l'historique.
- « Rédiger la synthèse avec l'agent » remplit la synthèse ; elle reste modifiable à la main avant d'enregistrer.
- « Ouvrir » recharge le build et la conversation : l'agent reprend avec le contexte du loadout.
- « Vérifier après une mise à jour » compare l'instantané pris à la sauvegarde (effets des mods et arcanes, stats des armes, stats et coûts de la warframe) à la base actuelle, et liste les notes de patch postérieures qui citent un élément du build. L'agent propose alors un build mis à jour en gardant l'intention du loadout ; un bouton le charge dans l'éditeur. Il faut que `mise-a-jour.bat` ait tourné pour que la base soit à jour.
- Chaque version peut être rechargée depuis l'historique.
- `loadout.json` contient tout ; `<nom>.md` est une fiche lisible, indexée pour la recherche de l'agent.
- Depuis la discussion, l'agent a aussi les outils `lister_loadouts`, `ouvrir_loadout` et `enregistrer_loadout`.

## Archétypes de build (`base-warframe/01-donnees/archetypes/<warframe>.json`)

Pour chaque warframe : rôle et interactions de ses capacités, augments, et 2 à 4 archétypes (objectif, boucle de jeu, survie, énergie, mods indispensables, choix à comparer, pièges). L'agent les reçoit avec le dossier de build ; le contrôle demande de suivre le noyau d'un archétype ou de justifier l'écart (champ `hors_archetype`).

Ils ne s'écrivent pas à la main : `generer-archetypes.bat --model gemma4:12b` les déduit, hors ligne, des pages de capacités du wiki, des augments et des principes généraux du joueur (qui valent pour toutes les frames). Le code vérifie que chaque nom cité existe et redemande une correction sinon. Prévoir quelques minutes par warframe avec un modèle local ; une IA en ligne marche aussi (`--api-url`). Options : `--frame Gara` (une seule), `--force` (refaire). Un fichier marqué `"relu_par_le_joueur": true` n'est jamais écrasé : il suffit de corriger un archétype généré et de passer ce champ à true.

## Avis du joueur (`04-retours-experience/regles-builds.json`)

Ce que tu dis à l'agent sur un mod, un arcane ou un focus est gardé **avec ta raison et le cas où ça s'applique**. Ce ne sont pas des règles absolues : il n'y a pas de recette unique pour un build. Le contrôle ne refuse pas un build pour ça ; il rappelle l'avis, et l'agent doit le suivre ou expliquer pourquoi son build fait autrement (autre capacité, autre Helminth). L'agent les ajoute avec l'outil `noter_regle` ; tu peux aussi modifier le fichier à la main. La clé `*` vaut pour toutes les warframes.

Pour un build, l'agent doit d'abord chercher plusieurs pistes (capacité + augment, capacité + arme, capacité Helminth d'une autre warframe) avant d'en développer une.

## IA en ligne gratuite (conseillé)

Un grand modèle en ligne raisonne bien mieux qu'un petit modèle local : il construit les builds lui-même, en lisant la base (toutes les pages du wiki exporté, les données, tes retours, les patch notes) avec les outils `chercher_doc`, `lister_documents` et `lire_document`, et chaque build passe par le même contrôle avant d'apparaître dans l'éditeur.

| Fournisseur | Lancement | Clé gratuite | Fichier de la clé |
|---|---|---|---|
| Google Gemini (par défaut) | `interface-en-ligne.bat` | https://aistudio.google.com/apikey | `cle-gemini.txt` |
| Groq | `interface-en-ligne.bat --cloud groq` | https://console.groq.com/keys | `cle-groq.txt` |
| OpenRouter | `interface-en-ligne.bat --cloud openrouter` | https://openrouter.ai/keys | `cle-openrouter.txt` |

1. Crée la clé sur le site (compte Google suffisant pour Gemini, sans carte bancaire), colle-la seule dans le fichier indiqué, dans ce dossier.
2. Double-clic sur `interface-en-ligne.bat`. Le modèle est choisi tout seul parmi ceux que le fournisseur propose (le plus récent de la famille « flash » pour Gemini) ; `--model <nom>` pour en imposer un.

Gemini est conseillé : son offre gratuite accepte de longs échanges (l'agent envoie beaucoup de texte à chaque étape), Groq est plus rapide mais plafonne vite le nombre de jetons par minute. Quand un plafond est atteint, l'agent attend puis réessaie. Ne partage jamais les fichiers de clé. D'après OpenRouter (comparatif de 2026), Google peut utiliser les échanges de l'offre gratuite pour entraîner ses modèles hors Union européenne, Royaume-Uni et EEE ; Groq et OpenRouter disent ne pas le faire.

## Pas encore fait

- Notes de patch automatiques (il faut confirmer la source exacte).
- Pages wiki des armes et warframes, et fichiers `01-donnees/armes` et `01-donnees/warframes`.
- Série de questions de test pour comparer les modèles, optimiseur de build, postures de mêlée, rang des mods, dépôt central.
