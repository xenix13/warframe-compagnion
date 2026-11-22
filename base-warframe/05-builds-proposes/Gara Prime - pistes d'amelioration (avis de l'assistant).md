# Gara Prime : pistes d'amélioration (avis de l'assistant, à tester)

Statut : **avis de l'assistant, pas des faits.** Calculé avec la base de données à partir du build de XeniX13 (voir « 04-retours-experience/Gara Prime - build expert XeniX13 »). Aucune de ces pistes n'est testée en jeu : XeniX13 décide, ses tests priment. Date : 13/11/2026.

Correction [retour de jeu, 13/11/2026] : la version d'Organ Shatter à +165 % présente dans la base n'existe pas en jeu ; seule la version +90 % (coût 9) est réelle. Une piste fondée sur elle a été retirée.

Contexte [retour de jeu] : après test, XeniX13 pense qu'il vaut mieux **investir dans les dégâts critiques** (il a remplacé Jugulus Barbs par Organ Shatter). Il veut que l'assistant sache dire : « ce build serait mieux avec tel mod, tel arcane ou tel compagnon, pour mieux synergiser ».

Hypothèses de calcul : fragment violet doublé (+75 %), Galvanized Steel à 4 cumuls (+120 %), formule de la page Critical Hit : multiplicateur critique = base 2 x (1 + bonus relatifs) + bonus absolus ; critique de tier n = 1 + n x (M - 1).

## Ce qui est déjà très bon

- Tous les bonus critiques sont relatifs et s'additionnent dans le même total : Galvanized Steel, fragment violet, Organ Shatter. Chacun est donc rentable.
- Blood Rush amène la chance de critique à environ 130 % au combo x12 : tout est critique, donc l'investissement en dégâts critiques est le bon.
- Primed Flow active le doublement du fragment violet (énergie max au-dessus de 500) en plus de fournir l'énergie.

## Piste 1 : Arcane Crepuscular avec l'invisibilité du Huras (synergie à tester)

- Arcane Crepuscular : « tant que tu es invisible, +30 % de puissance et +3x de dégâts critiques finaux ». C'est un bonus **absolu** : il s'ajoute après les bonus relatifs (page Critical Hit).
- Le Kubrow Huras avec Stalk rend le joueur invisible (proie à moins de 24 m). C'est la condition de l'arcane, déjà remplie par le build.
- Comparaison avec Molt Augmented (+0,24 % de puissance par kill, jusqu'à +60 % après 250 kills), en supposant l'invisibilité active :

| | Molt Augmented | Crepuscular |
|---|---|---|
| Puissance | 2,43 (183 % + 60 %) | 2,13 (183 % + 30 %) |
| Multiplicateur critique (Organ Shatter +90 %) | 7,7x | 10,7x (+39 %) |
| Coup direct (puissance x critique, Organ Shatter +90 %) | 18,7 | 22,8 (+22 %) |
| Explosion de l'anneau (ne crit pas, proportionnelle à la puissance) | 100 % | 88 % (-12 %) |

- Verdict : meilleur pour le coup direct si l'invisibilité est active presque tout le temps, moins bon pour l'explosion. **À tester** : l'uptime réel de Stalk, et si l'invisibilité de Stalk déclenche l'arcane.

## Piste 2 : fragment d'Archonte rouge (Crimson) en plus

- Crimson Tauforged : +37,5 % de dégâts critiques de mêlée, bonus relatif qui s'ajoute à ceux déjà présents.
- Gain : multiplicateur 7,7x vers 8,45x (+9,7 %) avec Organ Shatter +90 %.
- Verdict : gain modeste mais sans coût de mod, si un emplacement de fragment est libre [à confirmer : emplacements libres ; XeniX13 utilise 2 Amber et 1 Violet].

## Piste 3 : arcane d'arme (Exposure à garder)

- Melee Exposure ajoute jusqu'à +240 % de Corrosif (stacks de 60 % à chaque capacité lancée) : environ 47 % des dégâts du coup direct et la majorité de l'explosion de l'anneau [calcul].
- Melee Duplicate (« sur critique de base, 100 % de chance de frapper une seconde fois ») donne au mieux x2 sur le coup direct, rien sur l'explosion, et n'est utile que sur les critiques de tier 1 : à ce rythme (130 % de chance de critique), seulement 70 % des coups. Verdict : Exposure reste meilleur.

## Piste 4 : compagnon

- Huras avec Stalk fournit l'invisibilité, donc la synergie de la piste 1. Je ne vois pas dans la base de compagnon qui apporte autant à ce build.
- Idée secondaire : le mod Fetch (BEAST, collecte des objets à 13,5 m) sur le Huras pour ramasser les orbes d'énergie et de santé que Nourish et Equilibrium multiplient [à tester : la base ne dit pas si Fetch ramasse les orbes].

## Ce que je ne conseille pas de changer

- Arcane Fury (+180 % de dégâts de mêlée sur critique, 60 % de chance) : avec Primed Pressure Point (+165 %) et Steel Charge (+60 %), le total de mêlée passe de 3,25 à 5,05, soit +55 %.
- Steel Charge en aura : retirer ses +60 % ferait perdre 18 % des dégâts de mêlée (3,25 contre 2,65).
- Overextended : sans lui, la puissance passerait de 183 % à 243 % (+33 % de dégâts de base) mais la portée tomberait à 175 % : portée de Shattered Lash 24 m au lieu de 31,2 m, anneau de 28 m au lieu de 37,5 m. Choix de XeniX13, cohérent avec son jeu à longue portée.
