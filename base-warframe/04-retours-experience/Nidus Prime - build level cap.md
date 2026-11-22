# Nidus Prime - build level cap (retours d'expérience en jeu)

Source : tests en jeu de XeniX13 (priorité sur les données brutes et les builds génériques en cas de contradiction).
Version du jeu de référence : Update 44.1 (retouche de Nidus de l'Update 43 incluse).
Statut : build cohérent, capable d'aller à haut niveau, mais pas un build « niveau expert ». À améliorer avec d'autres tests.

## Principes de survie à haut niveau

### Arcane Persistence (pilier du build)
- Persistence retire les boucliers (Nidus n'en a pas) et plafonne les dégâts reçus à 500 par seconde, **à condition d'avoir plus de 700 d'armure**.
- Pour que Persistence reste réellement active, il faut **environ 1400 d'armure** de base :
  - un statut **Feu** (Heat) réduit l'armure de 50 % : 1400 → 700, Persistence reste active ;
  - le statut **Corrosif** réduit l'armure de 80 % avec toutes les stacks (rare d'avoir toutes les stacks sur soi, mais possible).
- Conséquence : viser environ 1400 d'armure (Umbral Fiber, etc.) et ne pas se contenter de 700.

### Adaptation : pas recommandée à haut niveau
- Adaptation ne réduit de 90 % que le **type de dégât majoritaire**.
- Exemple : une arme qui fait 9 Tranchant / 9 Impact / 10 Perforation devient 9 / 9 / 1. Seule la Perforation est réduite.
- À haut niveau, les dégâts sont tels que ce n'est pas intéressant, surtout avec Persistence qui, contrairement à Adaptation, ne réduit pas les dégâts mais les **limite**.

### Soin de Ravenous (4)
- Ce n'est pas un soin permanent, et pas aussi efficace qu'estimé : à 300 % de puissance, on est à peu près à **200-250 PV/s**.
- À comparer aux 500 PV/s de dégâts que Persistence laisse passer : le soin ne couvre pas tout.

## Parasitic Link (3) : le lien est une condition de survie à haut niveau
- Il est **plus intéressant sur un allié que sur un ennemi** : bonus de dégâts d'arme + augmentation de la puissance de capacité, pour Nidus comme pour l'allié.
- Avec un build simple, Nidus atteint rapidement **400 % de puissance** pour la mêlée.
- Sur un allié (squad, compagnon, spectre), cela permet aussi d'obtenir ces bonus sans devoir verrouiller un ennemi.

## Compagnon : Panzer Vulpaphyla
- Idéal d'après les tests : il **répand l'élément Viral**, qui à stack max donne **+250 % de dégâts supplémentaires sur la santé**.
- **Problème** : quand le Panzer meurt, il devient une pseudo-sentinelle grâce à son mod signature, ce qui lui permet de continuer à travailler pendant sa mort. Mais **le lien avec Parasitic Link est perdu**, alors que ce lien est une condition de survie à haut niveau.
- Les « larves » désignent ici les asticots (maggots) générés par les **mods du set Strain** (« souches ») et par **Ravenous** (4).
- Devoir dépendre de ces larves pour les dégâts n'est **pas une solution viable en jeu** : on est contraint par l'IA du jeu. Elle a été grandement améliorée récemment, donc elle reste fiable, mais en pratique moins forte que prévu. À retester avec d'autres combinaisons que celles déjà essayées.

## Corrosif et Archon Shards
- **2 Emerald tauforgés** suffisent à atteindre le nombre de stacks de Corrosion nécessaire pour retirer l'armure de presque tout le jeu.
- Seuls les mobs spéciaux et les boss ont besoin de plus de 13 stacks de Corrosion pour un retrait total de l'armure. Sinon, **92 % de réduction d'armure** est largement suffisant en jeu.

## Gain de stacks de Mutation depuis la retouche
- On gagne beaucoup plus vite des stacks qu'avant. Tant que des ennemis restent sur Virulence (1), les stacks continuent de monter.
- **Insatiable est donc rarement joué** aujourd'hui.
- Les stats qui comptent le plus : **puissance et portée**. Plus de portée = Larva (2) attrape plus d'ennemis, et Virulence (1) va plus loin, donc on stack plus vite.

## Corrections apportées au build proposé initialement
| Point | Proposé | Correction |
|---|---|---|
| Umbral Intensify + Archon Intensify | Les deux ensemble | **Impossible** : c'est l'un ou l'autre |
| Archon Intensify | Actif en continu via les soins | Ne se déclenche **plus si on est à pleine santé** |
| Insatiable | Mod retenu | Rarement joué depuis la retouche |
| Adaptation | Mod retenu | À éviter à haut niveau (réduit seulement le dégât majoritaire) |
| Archon Continuity | Mod retenu | Inutile sur Nidus, sauf si on joue l'augment du 2e pouvoir : son bonus ne sert que sur un pouvoir qui fait du Toxin, or les larves (asticots des mods Strain et de Ravenous) font du corrosif/explosif, pas de Toxin |
| Soin Ravenous | ~195 PV/s | ~200-250 PV/s à 300 % de puissance, non permanent |
| Parasitic Link | Sur un ennemi (90 % de redirection) | Plutôt sur un **allié** (dégâts + puissance) |

## Armes de mêlée recommandées (confort de jeu)
Nidus est une frame assez lente. Pour l'agrément de jeu, on joue souvent :
- **Okina Incarnon**, avec la vitesse de déplacement en modificateur ;
- **Praedos**, qui donne un talent de vitesse de parcours.

## À tester
- Autres combinaisons de compagnons que celles déjà testées (le Panzer pose le problème du lien perdu à sa mort).
- Un build à environ 1400 d'armure pour garder Persistence active sous Feu.
- Reste du build initial jugé « ok » mais pas celui que XeniX13 aurait choisi personnellement.
