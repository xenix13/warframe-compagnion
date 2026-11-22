# Méthode : construire un build level cap (toutes frames et armes)

Source : méthode tirée des retours en jeu de XeniX13 pendant la construction du build Nidus Prime (config C et Coda Bubonico). À appliquer à toute frame. En cas de contradiction, les tests en jeu de XeniX13 passent avant les calculs et avant les builds génériques.

## 0. Règle absolue : toujours comparer ses choix

- Pour **chaque** choix (mod, aura, arcane, capacité Helminth, arme, compagnon, polarité), présenter au moins deux alternatives avec leur coût (emplacement, capacité, forma, énergie) et leurs chiffres, puis dire pourquoi l'option retenue l'emporte. Un choix sans comparaison n'est pas recevable.
- **Auras** : les auras d'énergie (Energy Siphon, +0,6 énergie par seconde) sont presque jamais jouées, car inutiles : elles gâchent un emplacement d'aura qui peut servir à un vrai bonus (exemple : Growing Power sur Nidus). Pour regagner de l'énergie, préférer Energy Nexus, Zenurik Wellspring (sans emplacement de mod), Equilibrium, etc., et les comparer.
- Source : retour de XeniX13 du 13/11/2026, après la première proposition sur Gara Prime.

## 0 bis. Règle de fond : penser en chaîne de synergies

Un build n'est pas une liste de bons mods : c'est une **boucle de jeu** où chaque élément en sert d'autres. Source : retour de XeniX13 du 13/11/2026 (« la synergie entre tous les éléments de gameplay et de build »), à partir de son Gara Prime (voir « Gara Prime - build expert XeniX13 »).

Procédure :
1. **Trouver le rôle réel de la frame dans le build du joueur** (nuke, tank, soutien, contrôle) et la boucle de jeu qui en découle, avant de choisir quoi que ce soit.
2. **Lister tout ce qui entre dans la boucle** : stats de la frame, interactions entre ses capacités (par exemple Mass Vitrify rafraîchit Splinter Storm et son anneau brisé par Shattered Lash nourrit l'augment), mods de la frame, arme (ou capacité qui compte comme arme), arcanes, fragments d'Archonte, capacité Helminth, focus de l'Opérateur, compagnon.
3. **Pour chaque pièce, écrire au moins deux liens** avec le reste : ce qu'elle apporte et ce qu'elle débloque ou renforce. Exemples : Primed Flow donne l'énergie **et** active le doublement du fragment violet (énergie max au-dessus de 500) ; la portée agrandit l'arme **et** l'anneau ; la vitesse de lancement donne du confort **et** rafraîchit le Splinter Storm ; Naramon Power Spike protège le combo ; Nourish donne de l'énergie **et** une ligne de dégâts Viral.
4. **Chercher la pièce sans lien** : elle est suspecte (mod ou arcane qui ne sert à rien dans la boucle). Chercher aussi la pièce **redondante** : ne pas empiler une stat qu'une synergie fournit déjà. Exemple de XeniX13 (13/11/2026) : sur Shattered Lash, Weeping Wounds donne déjà la chance de statut avec le combo, donc Jugulus Barbs (+60 % de statut) est remplacé par Organ Shatter (dégâts critiques).
5. **Chercher le goulot** de la boucle (énergie, combo, portée, survie) et vérifier que le build le comble : l'efficacité faible de Gara n'est pas un défaut parce que l'énergie vient des orbes et du pool.
6. **Reconstruire les chiffres** affichés par le jeu avec les formules de la base : si tout retombe juste, la lecture du build est correcte.
7. **Défense au level cap** : la défense classique seule ne suffit jamais (XeniX13). Combiner plusieurs filets (tuer avant d'être touché, réduction ou invulnérabilité des capacités, invisibilité, compagnon).

## 0 ter. Les quatre exigences de base d'une warframe

Source : règle donnée par XeniX13 le 15/11/2026. Elle passe avant le choix des mods.

1. **Survivre par elle-même** : la frame doit tenir seule, sans dépendre d'un allié ni d'un soigneur. Dire d'où vient sa survie (capacités, shield gate, armure, invisibilité, arcanes, compagnon).
2. **Couvrir le maximum de contenu** : sauf si le joueur demande un build spécifique, le build doit fonctionner dans la plupart des missions (solo et escouade, défense, survie, missions ouvertes, Steel Path au level cap).
3. **Être autonome en énergie** : la frame doit se fournir elle-même en énergie (focus Zenurik, Helminth qui en redonne, arcanes, mods, ressource propre comme Hildryn), sans compter sur un allié ni sur la chance de trouver des orbes. Montrer le calcul : coût de la boucle de jeu par rapport à l'énergie gagnée.
4. **Des capacités adaptées à l'objectif** : choisir les capacités mises en avant selon ce que le joueur veut faire. Exemple : chasse d'Archonte = gros DPS mono-cible ; défense d'escouade = contrôle et protection.

Un build qui ne remplit pas l'un de ces points doit le dire clairement et expliquer pourquoi (build spécifique demandé par le joueur, par exemple).

## 1. Principe : sans défense, pas de level cap

La défense se pense avant les dégâts. Elle se compose de quatre couches ; un bon build en combine plusieurs et sait où elles cassent.

| Couche | Idée | Exemple (Nidus) |
|---|---|---|
| Encaisser | PV, armure, réduction ou limitation des dégâts | Arcane Persistence : dégâts plafonnés à 500 par seconde si l'armure dépasse 700 ; réserve de PV d'environ 24 000 mesurée |
| Éviter | Esquive, invisibilité, contrôle de foule, distance, tuer avant d'être touché | Portée et Larva (2) qui regroupent les ennemis ; Nullifiers et Eximus évités |
| Soigner | Soin de capacité, soin du compagnon, vol de vie | Ravenous (4) ; compagnon avec Hunter Recovery |
| Condition de survie | Un lien ou une condition sans lesquels le reste s'effondre | Parasitic Link (3) maintenu sur l'allié (le compagnon Helminth Charger) |

Règles :
- Chiffrer chaque couche (valeur en PV, en armure, en PV/s) et ne pas se fier à l'impression.
- Chercher le **point de rupture** de chaque couche et prévoir un plan B. Exemples vus :
  - Persistence : Feu retire 50 % de l'armure et Corrosif jusqu'à 80 %, d'où un objectif d'environ 1400 d'armure pour rester au-dessus de 700 ;
  - le lien parasitaire est perdu si le compagnon (le Panzer) meurt, **sauf avec le Chargeur Helminth** (d'après XeniX13) ;
  - Nullifiers et Eximus.
- Les réductions de dégâts partielles (Adaptation : 90 % sur le seul type majoritaire) valent peu à haut niveau face à un limiteur comme Persistence.

## 2. Procédure pour construire ou améliorer un build

1. **Identité de la frame** : ce qu'elle fait le mieux, ce qui scale avec la puissance, la portée, la durée, l'efficacité. Nidus : puissance et portée (plus de portée = plus d'ennemis attrapés et plus de stacks).
2. **Choisir la condition de survie** et la sécuriser en premier (voir la section 1).
3. **Fixer les stats prioritaires** et ne dépenser les formas que pour elles. Vérifier les seuils connus (Bellicose, Persistence, plafond d'efficacité).
4. **Choisir les mods** en vérifiant les incompatibilités (une famille de mods ne se cumule pas : Umbral Intensify et Archon Intensify s'excluent), les conditions de déclenchement (Archon Intensify ne se déclenche pas à pleine santé) et les coûts de capacité.
5. **Choisir l'arme et le compagnon pour combler les faiblesses de la frame**, pas pour répéter ses forces. Exemple : le Coda Bubonico en Corrosif + Viral sert d'applicateur de debuffs (armure retirée, dégâts de santé amplifiés) pour les pouvoirs de Nidus ; mesure de XeniX13 : environ 600 000 à plus de 2 000 000 sur Virulence (1).
6. **Choisir l'Helminth** pour boucher un trou : comparer les capacités avec la formule des dégâts. Le retrait d'armure ennemie pèse plus que la plupart des buffs de dégâts (x1,9 à x2,6) : réduction de dégâts ennemie = 90 % × racine carrée de (armure / 2 700), donc x2,15 à 24 % de retrait, x3,64 à 50 %, x5,98 à 80 % (Corrosif au maximum) et x10 au retrait total (page Armor complète, réimportée le 13/11/2026).
7. **Calculer et vérifier** : reconstruire les stats de l'arsenal à partir de la base de données, comparer avec les mesures du joueur, traiter chaque écart comme une hypothèse à noter.
8. **Peser les avantages, les coûts et le confort** : une variante plus puissante peut coûter du confort (résistance aux renversements, vitesse, mod pratique). Donner les chiffres des deux côtés ; le joueur décide.
9. **Étiqueter l'information** : calculé, mesuré en jeu, ou à tester.

## 3. Pièges déjà rencontrés (à ne pas refaire)

- Proposer un mod qui n'existe pas en jeu : la version « Expert » +165 % d'Organ Shatter (le fichier source contient des variantes rang 10 que le jeu n'a pas pour les mods normaux ; seuls les Primed et quelques mods uniques en ont : une variante Expert d'un mod normal est suspecte). Autre cas : (Primed Streamline, présent dans les données mais sans date de sortie) : vérifier qu'un mod est réellement obtenable avant de le recommander, et signaler les entrées douteuses.
- Imposer un archétype défensif à une frame qui joue autrement : pour Gara, XeniX13 ne tank pas, il **tue avant d'être touché** (Shattered Lash à 31 m, anneau de Mass Vitrify brisé, 45 % d'efficacité grâce à Blind Rage). Chercher d'abord le rôle réel de la frame (nuke, tank, soutien, contrôle) avant de construire la défense autour.
- Craindre un manque d'énergie sans regarder les sources : Equilibrium, Nourish (Helminth) et les orbes des ennemis tués suffisent (retour de XeniX13 du 13/11/2026).
- Les statistiques de l'arsenal n'incluent que les effets directs : pas les cumuls de kills (Galvanized Steel) ni les arcanes à déclencheur, mais bien les buffs dont la condition est déjà remplie (XeniX13, 13/11/2026). Ne pas attribuer une valeur affichée à un effet conditionnel.
- Une valeur de l'arsenal qui ne se reconstruit pas (« 4,7x ▸ 3,2x » sur la Pique, XeniX13 13/11/2026) peut être un bug d'interface. Utiliser les mesures cohérentes (3,2x ▸ 5,0x après Organ Shatter confirme base 2x et +0,9) et ne pas inventer de source pour le reste.
- Lire une capture d'arsenal sans la vérifier : reconstruire ses chiffres avec les formules de la base (puissance, portée, dégâts) est la preuve que la lecture est bonne.

- Estimer les PV avec la mauvaise formule (modèle additif donnant 8 300 au lieu des 24 000 mesurés) : se fier d'abord aux mesures du joueur.
- Supposer qu'un bonus s'applique alors qu'il ne s'applique pas (Link Vitality ne fonctionne pas avec le lien de Nidus).
- Annoncer une survie chiffrée sans compter les soins externes (compagnon avec Hunter Recovery).
- Mal interpréter le vocabulaire du joueur (« larves » = asticots des mods Strain et de Ravenous).
- Déduire l'usage d'une arme des stats seules (le Coda est joué pour son statut ; le critique n'est qu'un mode de renfort sur le tir principal).
- Les mods en français : demander le nom anglais en cas de doute plutôt que deviner.
- Données absentes de la base : ce qui manque encore (comportement exact de certains compagnons, mods d'un compagnon, durée d'une invisibilité) doit être signalé au lieu d'être inventé. Les mods de fusil à pompe et les bonus de set (dont Umbra) ont été réimportés le 13/11/2026.

## 4. Forme d'une réponse de build

1. Rôle de la frame et de l'arme, et condition de survie.
2. Tableau du build (mods, shards, Helminth, arme, compagnon) avec les coûts.
3. Calculs clés (stats, soin, plafond de dégâts, énergie) avec la formule utilisée.
4. Avantages, inconvénients et confort, avec les alternatives chiffrées.
5. Ce qui reste à tester en jeu.

## 5. Donner un avis sur un build existant (objectif de XeniX13)

Objectif exprimé par XeniX13 (13/11/2026) : l'assistant doit pouvoir dire « avec ce build, tel autre mod, arcane, fragment ou compagnon synergiserait mieux ». Un avis n'est pas une critique générale : c'est une proposition chiffrée, comparée et honnête sur ses limites.

Procédure :
1. **Comprendre d'abord** : rôle de la frame, boucle de jeu et priorités du joueur (par exemple : investir dans les dégâts critiques). Reconstruire ses chiffres avec la base ; ne rien proposer tant que la lecture n'est pas exacte.
2. **Dire ce qui est déjà bon** et pourquoi (les synergies existantes), pour ne pas défaire ce qui marche.
3. **Parcourir tous les leviers**, pas seulement les mods : mods de la frame, mods de l'arme, arcanes de la frame et de l'arme, fragments d'Archonte, capacité Helminth, compagnon et ses mods, focus, aura, polarités et formas. Chercher dans la base les éléments qui servent la **priorité du joueur** et qui profitent d'une condition **déjà remplie** par le build (exemple : un arcane qui demande l'invisibilité, alors que le Kubrow Huras la fournit).
4. **Chiffrer chaque piste contre l'existant** : coût (emplacement, capacité, forma), gain en pourcentage, ce qui est perdu (par exemple Molt Augmented contre Crepuscular), et sur quelle partie des dégâts (coup direct, explosion, durée, énergie, survie).
5. **Classer** les pistes (gain, coût, risque) et donner un verdict net sur chacune, y compris « ne pas changer » avec la raison.
6. **Étiqueter** : calculé, hypothèse, ou à tester en jeu. Dire précisément ce que la base ne permet pas de savoir (uptime, comportement d'un compagnon).
7. **Laisser le joueur décider** : ses tests priment. Noter son choix et sa raison dans 04-retours-experience ; ranger les avis de l'assistant à part, dans 05-builds-proposes.

Exemple : « Gara Prime - pistes d'amelioration (avis de l'assistant) ».

## 6. Dialogue : poser les bonnes questions avant de proposer

Source : XeniX13, 13/11/2026. L'agent doit mener un échange, pas déverser un build.

- **Demande précise** (exemple : « réfléchis un build Banshee pour nuker, faire du contenu endgame, tout en profitant de Sonar ») : réfléchir d'abord à la boucle de jeu (section 0 bis), proposer une direction, et ne poser que les questions dont la réponse **change vraiment** le build (ce qu'il possède, le niveau visé, une préférence ambiguë).
- **Demande vague** (exemple : « un build Banshee ») : ne pas proposer tout de suite. Poser plusieurs questions ciblées pour cerner le type de build (nuke, soutien, contrôle, tank), puis proposer.
- Questions utiles : contenu visé (niveau cap, Arbitrations, Steel Path, Archon...) ; rôle (nuke, soutien, contrôle) ; capacité à mettre en avant ; solo ou escouade ; arme, arcanes, fragments, compagnon et capacité Helminth déjà disponibles ; formas et Aura/Exilus libres ; contraintes de confort (énergie, vitesse, effets).
- Poser 3 à 5 questions maximum, les plus utiles d'abord, et ne pas redemander ce que la base ou la conversation donne déjà.
- Toujours donner un avis et des alternatives comparées (section 0), même quand des questions restent ouvertes.

## 7. Les builds sont périssables : reconstruire, ne jamais recopier

Source : XeniX13, 13/11/2026. Les builds qu'il montre (Nidus, Gara, etc.) changent à chaque mise à jour, car le jeu reçoit beaucoup de reworks. L'agent doit rester capable de **construire quelque chose de cohérent même quand le build de référence est dépassé**, et ne pas faire du copier-coller.

**Ce qui dure et ce qui change**
- Dure : les formules (dégâts, armure, critiques, portée), la logique des synergies, le rôle de la frame, les priorités du joueur (défense au level cap, tuer avant d'être touché, etc.), la méthode de ce document.
- Change : les valeurs des mods et arcanes, leur existence, leur coût, la disponibilité, les capacités des frames, les armes. Chaque build de 04-retours-experience porte une date et une version du jeu : c'est un **exemple de raisonnement**, pas une vérité actuelle.

**Procédure quand on s'appuie sur un build existant**
1. Lire la date du build et la comparer aux notes de patch en base (03-patch-notes). Chercher dans les notes postérieures le nom de la frame, de chaque capacité, de chaque mod, arcane, arme et fragment du build. Lister ce qui a changé. Si les notes de patch de la base s'arrêtent avant la date du jour, le dire : il peut y avoir des changements que l'agent ne connaît pas.
2. Revérifier chaque élément dans les données actuelles (01-donnees) : le mod existe-t-il (voir les étiquettes ATTENTION), quelles sont ses valeurs et son coût. **Pour les chiffres, les données actuelles l'emportent sur la note ; pour l'intention (rôle, boucle, priorités), la note du joueur l'emporte.**
3. Extraire du build l'**intention** : le rôle de la frame, la boucle de jeu, le goulot qu'elle comble, la fonction de chaque emplacement (par exemple « donne de la portée pour que la Pique touche à 31 m », « donne la chance de critique via le combo »). Ne pas garder la liste de mods comme point de départ.
4. Reconstruire : pour chaque fonction, chercher dans les données actuelles les meilleures façons de la remplir, **comparer au moins deux options** chiffrées (section 0), appliquer la chaîne de synergies (0 bis) et recalculer les chiffres (formules, section 2). L'option du build de référence est une candidate parmi d'autres, pas la réponse d'office.
5. Si un élément a été modifié, supprimé ou n'existe plus, le dire clairement (« X a changé à la mise à jour N : avant …, maintenant … »), proposer un remplaçant et dire ce qui est perdu ou gagné.
6. Dans la réponse, séparer : ce qui vient du build de référence et reste valable, ce qui a été adapté et pourquoi, ce qui n'est pas vérifié. Adapter à ce que le joueur possède (mods, formas, fragments, arcanes) et à ce qu'il veut faire.
7. Même quand rien n'a changé, expliquer le raisonnement et vérifier les chiffres au lieu de recopier la liste.
8. Quand le joueur modifie un build, ajouter la nouvelle version dans 04-retours-experience avec la date et la version du jeu, en gardant l'ancienne en historique.

## 8. Après le build : où se procurer ce qui manque

Une fois le build proposé, lister ce que le joueur doit encore obtenir (mods, arcanes, fragments, ressources, plans) et dire où le farmer avec les fichiers « Farm - … » de 01-donnees/farm, en suivant la méthode de « Farm - Principes et limites » (comparer au moins deux sources, dater les tables, étiqueter les estimations de vitesse).

## 9. Il n'y a pas de vérité unique dans un build

Source : XeniX13, 13/11/2026.

- Le jeu est très permissif : on peut monter presque n'importe quoi sur une frame ou une arme. Il n'existe pas « le » build d'une frame, ni de règle absolue. Il existe une **logique** qui permet de builder à peu près n'importe quel objet du jeu.
- Certains builds sont plus forts que d'autres, mais un build moins fort peut être **mieux adapté** à une tâche ou à une mission précise.
- Conséquence : le build se décide à partir de **ce que le joueur veut faire**. Quand le souhait n'est pas clair, poser des questions ou demander de préciser (type de mission, niveau des ennemis, rôle, solo ou escouade) avant d'orienter le build.
- Les retours du joueur sur une frame (« Gaseous Quake pour nuker au 4 », « Banshee se joue au bouclier ») sont des repères avec leur raison, valables dans leur cas. Ils n'interdisent pas d'autres pistes (autre capacité, capacité Helminth, arme).
- L'agent doit donc : chercher plusieurs pistes, dire pour quelle tâche chacune est faite, en développer une, et rester capable d'en proposer une autre si le joueur change d'objectif.

## 10. Coût en énergie : capacités à coût fixe, canalisées, à coût croissant

Source : XeniX13, 13/11/2026, et pages du wiki de la base.

- **Coût fixe** : chaque capacité a son propre coût (sauf les frames sans énergie comme Lavos et Hildryn). Coût réel = coût de base x (2 - efficacité), au minimum 25 % du coût de base. Exemple de XeniX13 : une capacité à 100 coûte 155 à 45 % d'efficacité. Ce montant ne dépend pas de l'énergie max de la frame.
- **Capacités canalisées** : elles coûtent de l'énergie **tant qu'on les maintient** (exemple : le 4 d'Excalibur). Le drain par seconde est réduit par la durée et par l'efficacité : drain x (2 - efficacité) / durée.
- **Coût croissant** : certaines coûtent de plus en plus cher à mesure qu'on les maintient. Exemple : Sound Quake de Banshee avec Gaseous Quake coûte 100 au lancement, puis 16 par seconde multiplié par 1,2 à chaque seconde, sans plafond ; les dégâts, eux, plafonnent après 10 s. XeniX13 : on canalise 5 à 10 secondes, puis on relance si besoin, pour ne pas vider la jauge.
- Pour un build : compter l'énergie d'un cycle complet (lancement + secondes de canalisation), la comparer à la réserve et à la source d'énergie, et dire au joueur combien de temps canaliser. L'outil « calculer » (opération cout_canalise) et le contrôle des builds font ce calcul ; les valeurs connues sont dans `01-donnees/capacites-canalisees.json`.
- **Frames sans énergie ou avec une ressource propre** (XeniX13, 13/11/2026) : Hildryn (ses capacités consomment ses boucliers), Lavos (pas de coût, des temps de recharge), Baruuk (de l'énergie pour ses capacités 1 à 3, mais son 4 demande de vider sa jauge de Retenue). Pour elles, les mods et arcanes d'énergie ne s'évaluent pas comme d'habitude. D'autres frames ont une jauge propre décrite dans leur passif.
- Relevé complet pour toutes les warframes (coûts, capacités canalisées, ressources, passifs) : `01-donnees/warframes/Couts des capacites et ressources speciales (toutes les warframes).md` et `01-donnees/couts-capacites.json`.
