# Feuille de route du compagnon Warframe

Décidé le 22/11/2026. But de l'outil : aider les jeunes joueurs et ceux qui ont du mal avec les mécaniques, avec des builds et des feuilles de route de farm adaptés à eux, et tourner chez tout le monde (petit modèle local, sans clé).

## Principe : un robot scripté construit, l'IA discute

- **Le robot (code)** connaît les mécaniques du jeu et construit le build. Il ne se trompe pas de nom, ne dépasse pas la capacité, compte l'énergie et la survie.
- **L'IA (petit modèle)** comprend la demande, pose les questions utiles (niveau, ce que le joueur possède), explique le build, et surveille que les données sont à jour et complètes.

## Organisation du code

```
wfcompanion/moteur/        mécaniques communes : étiquettes, règles de synergie, besoins par objectif
wfcompanion/modules/warframes/<frame>.py   seulement ce qui est propre à une frame (passif, augments, pièges)
wfcompanion/modules/armes/, compagnons/    même principe (plus tard)
```

- Les mécaniques communes (shield gate, armure, critique, énergie, combo, sets) restent dans le moteur : un rework de mécanique se corrige à un seul endroit.
- Une frame sans module marche quand même : étiquettes tirées automatiquement des pages de capacités du wiki (fiabilité « probable »).
- Chaque étiquette et chaque règle a un niveau de fiabilité : **confirmé**, **probable**, **à vérifier**. Le robot préfère ce qui est confirmé et le dit quand un choix repose sur une info incertaine.

## Où on en est (22/11/2026)

- Fait : `moteur/robot.py` décide la capacité centrale, les augments clés, le Helminth (et la capacité remplacée),
  les arcanes, les stats visées et la boucle de jeu. `optimizer.propose` s'en sert : plus besoin des fichiers d'archétypes.
- Modules relus : Atlas (`modules/warframes/atlas.py`) et les capacités du Helminth les plus utilisées (`modules/helminth.py`).
- Toutes les autres frames passent par la lecture automatique du wiki (fiabilité « probable ») : à relire une par une,
  en commençant par les plus jouées par les débutants. Une frame sans pages de capacités dans la base est « à vérifier ».
- Réglages à surveiller : les poids des synergies dans `moteur/regles.py` (Roar sort encore derrière Eclipse et Nourish).

## L'agent et le robot travaillent ensemble (22/11/2026)

- `pilote.py` : l'agent traduit la demande en JSON (`objectif`, `capacite_centrale`, `armes`, `contenu`, `imposes`, `interdits`) ;
  sans modèle, le code la reconnaît lui-même.
- Le robot compare des builds entiers (Helminth x capacité remplacée x paire d'arcanes x source d'énergie) et renvoie le
  meilleur plus 2 variantes, avec les exigences remplies ou non.
- L'agent relit (2 tours au plus) et répond `{"verdict": "ok"}` ou des corrections ; les noms inventés sont ignorés et une
  correction qui casse le build est refusée.
- Les retouches du joueur (« remplace Nourish par Roar ») passent par le même format, sans l'agent classique.
- Chaque correction est notée dans `04-retours-experience/relectures.jsonl` : à relire pour corriger les règles ou les modules.
- À faire : essayer la relecture avec qwen3:4b et gemma (temps, qualité du JSON) ; ajuster les consignes si besoin.

## Plus tard : les remarques des joueurs améliorent le robot

1. Dans l'application, l'IA transforme une remarque du joueur (« Roar ne sert à rien sur Landslide ») en **proposition** structurée (élément, avis, raison, date, statut « à vérifier »). Elle ne modifie jamais un module elle-même. Le robot l'utilise déjà chez ce joueur, avec moins de poids.
2. Bouton « Envoyer la suggestion » : ouvre une issue GitHub préremplie (`https://github.com/<compte>/<dépôt>/issues/new?title=...&body=...`). Pas de clé, pas de serveur : le joueur valide avec son compte GitHub.
3. Le mainteneur trie les issues ; une proposition juste devient une modification du module (pull request), qu'une IA peut préparer.
4. Au lancement, l'application télécharge les modules à jour depuis le dépôt (comme les données du jeu, seulement si quelque chose a changé).
5. GitHub Actions lance les tests (contrôle des builds, série de demandes types) sur chaque modification : une correction qui casse un build ne passe pas.

## Autres pistes notées

- Série de demandes de test (débutant, palier, level cap, farm, mécaniques) pour comparer les versions et les modèles.
- Feuille de route de farm calculée par le code (dépendances objet → composants → ressources → missions, runs attendus, durée par mission).
- Affiner un petit modèle (LoRA) sur le comportement (outils, méthode, format), jamais sur les builds eux-mêmes (périssables).
- IA sans clé : connexion à un compte (Puter), ou serveur hébergé par le mainteneur.
