# Banshee : retours de XeniX13 (build nuke au 4)

**Statut : retours de jeu de XeniX13 du 13/11/2026, donnés en corrigeant un build proposé par l'agent.** Pas encore un build complet de référence : ce sont des repères et leur logique, pas des règles. Jeu à la mise à jour 44.1.x.

## Ce que dit XeniX13 [retour de jeu]

- **Survie** : Banshee est trop fragile pour être jouée sur la santé et l'armure. On privilégie le **bouclier** pour encaisser.
- **Nuke au 4** : l'augment de Sound Quake, **Gaseous Quake**, est nécessaire pour nuker avec le 4. Sans lui, les dégâts ne suffisent pas et Sound Quake ne sert qu'au contrôle de foule.
- Un build sans cet augment, avec des armes de base, est un build de milieu de jeu (entrée du Steel Path), pas un build level cap.

- **Focus** : Zenurik est apprécié sur ce genre de build très gourmand en énergie ; l'agent avait mis Naramon à tort.
- **Arcane Battery** ne convient pas à Banshee : elle n'a pas assez d'armure pour obtenir un gros pool, et l'arcane augmente seulement l'énergie maximale sans en redonner. Il faut une **source d'énergie fiable** en plus.
- Ces avis sont aussi dans `regles-builds.json` (même dossier). Le contrôle des builds les rappelle avec leur raison, sans refuser le build.
- **Ce ne sont pas des règles absolues** (XeniX13, 13/11/2026) : il n'y a pas de recette unique. L'agent doit avoir la logique lui-même, et il existe sûrement d'autres façons de nuker avec Banshee, par exemple avec une capacité Helminth. Gaseous Quake est nécessaire **quand le nuke passe par Sound Quake**.

- **Gaseous Quake coûte de plus en plus cher** : le maintenir longtemps d'un seul coup revient très cher. On l'utilise en général 5 à 10 secondes, puis on le relance si besoin, pour éviter que la jauge d'énergie tombe à zéro.
- **Le passif compte** : les capacités de Banshee infligent 5 statuts Perforation aux ennemis à moins de 20 m, et ses armes sont silencieuses [donnée du wiki].
- Stats de base (capture de XeniX13, codex) : santé 270, bouclier 270, armure 135, énergie 215, course 1,15. Ce sont les valeurs au rang 0 ; au rang 30 l'énergie est de 265 (page Energy). Son armure faible fait que jouer sur l'armure n'est pas une bonne idée ; Nidus est l'exemple inverse, où Arcane Battery irait très bien.

## Vérifications dans la base [donnée]

- Réduction de dégâts des boucliers : la page Shield du wiki donne **50 %** pour les boucliers des warframes (XeniX13 pensait à 75 %, « à vérifier » : la base dit 50 %). Les boucliers ne profitent pas de l'armure.
- Shield gate : voir « Shield Gating » (durée selon le bouclier maximum, 1,33 s avec Catalyzing Shields).
- Coût de Gaseous Quake (page du wiki de l'augment) : 100 d'énergie au lancement puis 16 par seconde, multiplié par 1,2 chaque seconde, sans plafond ; le multiplicateur de dégâts (2,75x par seconde, cumulatif) plafonne à 24 736x après 10 s. Sans mod : environ 614 d'énergie pour 10 s. Avec Primed Flow, Banshee Prime a 755 d'énergie. Banshee est invulnérable et immobile pendant la canalisation ; la zone reste 6,25 s après l'arrêt.
- Gaseous Quake (Banshee, Zenurik, coût 9) : « Sound Quake Augment: Channel Gas Damage and Status Effect leaks with a 2.75x Damage Multiplier that increases every second on enemies in your sight. »
- Sonic Boom retire 70 % d'armure (valeur de base) ; Silence est la capacité de Banshee transférable au Helminth, donc elle ne peut pas être choisie comme Helminth sur Banshee.

## Erreurs de l'agent à ne pas refaire

- Empiler Vitality, Redirection et Steel Fiber sur Banshee.
- Proposer un build nuke au 4 sans Gaseous Quake.
- Mettre une capacité de Banshee (Silence) comme capacité Helminth sur Banshee.
- Inventer des noms d'armes ou de capacités : tout nom doit venir d'un outil.

## À compléter avec XeniX13 [à confirmer]

- Le build complet qu'il joue (mods, arcanes, Helminth, armes, compagnon, focus) et la place de Sonar.
- Comment il gère le bouclier au level cap (shield gate, Catalyzing Shields, ou autre).
