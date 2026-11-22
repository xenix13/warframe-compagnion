# Gara Prime : build expert de XeniX13 (Config A, Shattered Lash en arme principale du build)

**Statut du build : daté, exemple de raisonnement.** Valide à la date du 13/11/2026 (jeu à la mise à jour 44.1.x ; dernières notes de patch en base : 27/10/2026). Les mods, arcanes, frames et armes sont susceptibles de changer à chaque mise à jour : s'en servir pour comprendre le rôle, la boucle de jeu et la logique de chaque choix, puis **reconstruire** avec les données actuelles (voir « Methode - construire un build level cap », section 7), sans copier la liste.

Source : retour de jeu de XeniX13 du 13/11/2026 (captures de l'arsenal, rang 30) et explications. Ce build **remplace** la proposition « Gara Prime - proposition de build level cap » de l'assistant, qui était fausse sur le rôle de la frame. En cas de contradiction, ce document passe avant.

Étiquettes : [retour de jeu] = dit ou montré par XeniX13 ; [calcul] = recalculé avec la base de données et vérifié contre ses captures ; [à confirmer] = non vérifié.

## 1. Le principe du build [retour de jeu]

Gara Prime joue **Shattered Lash (capacité 1) comme une arme de mêlée à très longue portée**, pour détruire une carte entière d'un coup et tuer en un coup la plupart des menaces, peut-être toutes (XeniX13 : « je peux nuke une map entière en plus de oneshot la plupart des menaces du jeu, voire la totalité »).

Pourquoi ça marche, d'après la base [calcul] :
- Shattered Lash est une capacité mais **compte comme une frappe de mêlée** : elle profite des mods de mêlée, de l'aura Steel Charge, des arcanes de Warframe comme Arcane Fury, et d'Arcane Melee Exposure. Sa vitesse dépend de la vitesse de lancement, pas de la vitesse d'attaque (donc Spoiled Strike n'a aucun défaut).
- Chaque lancer qui touche un ennemi ajoute 20 points de combo, soit +1x de dégâts, jusqu'à x12 (220 points). Sans relancer, le combo disparaît après la durée de combo (12,5 s affichée sur la capture de l'arme).
- Mass Vitrify (4) crée un anneau de verre. Les ennemis qui le touchent sont cristallisés (vulnérabilité de dégâts de 50 % au rang max). Un coup de Shattered Lash sur l'anneau le fait exploser vers l'extérieur ; les dégâts de l'explosion profitent des mods de dégâts de base (Primed Pressure Point), des mods d'éléments (Arcane Melee Exposure) et du combo x12. L'explosion ne peut **pas** faire de critique ni de statut : les mods de critique et de statut servent au coup lui-même.
- L'augment **Shattered Storm** (équipé) : quand l'anneau est brisé par Shattered Lash, les ennemis frappés par le verre subissent Splinter Storm à 100 % de puissance.
- Si Splinter Storm est actif dans le rayon de l'explosion, 50 % des dégâts de l'explosion s'ajoutent définitivement aux dégâts par seconde de la tempête jusqu'à sa fin.

## 2. Config A de la frame (capacité 2/78 libre, rang 30) [retour de jeu]

Noms français lus sur la capture, correspondance anglaise déduite du coût, de l'effet et des statistiques (tous les chiffres tombent juste, voir section 4).

| Emplacement | Mod (anglais) | Coût | Effet utile |
|---|---|---|---|
| Aura | Steel Charge | +18 (capacité) | +60 % de dégâts de mêlée, donc de Shattered Lash |
| 1 | Primed Continuity (Continuité Accrue) | 7 | +55 % de durée |
| 2 | Equilibrium (Équilibre) | 14 | les orbes de santé donnent +110 % d'énergie |
| 3 | Overextended (Super-Étendu) | 6 | +90 % de portée, -60 % de puissance |
| 4 | Primed Flow (Flux Accru) | 7 | +185 % d'énergie max |
| 5 | Blind Rage (Colère Aveugle) | 8 | +99 % de puissance, -55 % d'efficacité |
| 6 | Shattered Storm (Tempête Cassante) | 9 | augment de Gara : Splinter Storm à 100 % sur les ennemis touchés par le verre |
| 7 | Stretch (Allonge) | 9 | +45 % de portée |
| 8 | Umbral Intensify (Intensité Umbra) | 16 | +44 % de puissance (le mod seul, sans le set) |

Emplacement Exilus : verrouillé (pas d'adaptateur Exilus posé) [retour de jeu : capture].

- Arcanes : **Arcane Fury** (sur critique : 60 % de chance de +180 % de dégâts de mêlée pendant 18 s) car Shattered Lash est de la mêlée ; **Molt Augmented** (+0,24 % de puissance par kill, jusqu'à 250 cumuls, soit +60 %).
- Helminth : **Nourish** (Grendel) à la place d'une capacité de Gara. Avec l'Helminth, l'énergie des orbes est multipliée par 1,3 à 1,6 (selon le rang) et les dégâts Viral des armes augmentent de 24 à 45 % (base). [retour de jeu : Nourish ajoute une ligne de dégâts Viral sur ses armes, donc aussi sur Shattered Lash, ce qui amplifie encore le coup.]
- Fragments d'Archonte [retour de jeu : capture] : **deux fragments jaunes (Amber) Tauforged : +37,5 % de vitesse de lancement chacun, soit +75 % au total** (additif avec Natural Talent) ; **un fragment violet (Violet) Tauforged : +37,5 % de dégâts critiques de mêlée, doublé quand l'énergie max dépasse 500** (501 ou plus), donc **+75 %** avec les 641 d'énergie max [calcul, page Archon Shard]. Le bonus est additif avec Organ Shatter et s'applique aux armes exaltées de la classe, donc à Shattered Lash. C'est une des raisons de Primed Flow : sans lui le bonus violet serait divisé par deux.
- Focus : **Naramon, passif Power Spike** : le combo décroît progressivement hors combat (de 20, 15, 10 ou 5 par palier selon le rang) au lieu de retomber à zéro d'un coup ; la décroissance dépend de la durée du combo [retour de jeu : sert à ne pas perdre le combo x12].
- Compagnon : **Kubrow Huras** avec sa compétence d'invisibilité **Stalk équipée** [retour de jeu] : le Kubrow et son maître sont invisibles quand une proie est à moins de 24 m (base). Joué « au cas où », car la défense seule ne suffit pas au level cap ; Hunt charge une cible. [à confirmer : les autres mods du Kubrow]
- Statistiques affichées : santé 445, bouclier 370, armure 200, énergie 641, sprint 1,38 ; durée 155 %, efficacité 45 %, portée 235 %, puissance 183 %.

## 3. Config de l'arme « Pique Cassante Prime » (= Shattered Lash) [retour de jeu]

Capacité 3/70. Statistiques affichées : portée 31,2 m, durée du combo 12,5 s, chance de critique 42 %, statut 48 %, coup d'estoc (tap) : Toxine 3 925,3 + Perforation 4 520,1 = 8 445,5 ; balayage (maintenir) : Toxine 3 925,3 + Tranchant 2 379 = 6 304,3. Exposition de Mêlée (arcane) équipée.

| Mod (nom français de la capture) | Anglais (déduit) | Coût | Effet |
|---|---|---|---|
| Acier Galvanisé | Galvanized Steel | 12 | +110 % de chance critique ; sur kill de mêlée +30 % de dégâts critiques, cumulable 4 fois |
| Coup de Sang | Blood Rush (traduction confirmée par XeniX13) | 7 | +40 % de chance critique par multiplicateur de combo |
| Frappe de Fièvre Accrue | Primed Fever Strike | 8 | +165 % de Toxine |
| ~~Barbillon Jugulus~~ **Fracas d'Organe** (changé le 13/11/2026, 02 h) | ~~Jugulus Barbs~~ **Organ Shatter** | 9 (7 en Madurai selon la polarité) | +90 % de dégâts critiques au rang 5 [retour de jeu : la version +165 % de la base n'existe pas en jeu] |
| Point de Pression Accru | Primed Pressure Point | 7 | +165 % de dégâts de mêlée |
| Surcharge d'État | Condition Overload | 8 | +80 % de dégâts de mêlée par type de statut sur la cible |
| Blessures Suintantes | Weeping Wounds | 9 | +40 % de chance de statut par multiplicateur de combo |
| Atteinte Accrue | Primed Reach | 7 | +3 m de portée |

Arcane de l'arme : **Arcane Melee Exposure** : à chaque lancer de capacité, +60 % de dégâts Corrosifs sur les frappes de mêlée pendant 25 s, cumulable jusqu'à +240 % (4 capacités lancées). Le Corrosif retire l'armure et s'ajoute à la base de dégâts.
Le slot du haut (« Pique Cassante », coût +10) est le slot spécial de la capacité, pas un mod de mêlée classique [à confirmer].

### Changement du 13/11/2026 : Barbillon Jugulus remplacé par Fracas d'Organe [retour de jeu]

Raison donnée par XeniX13 : « pas trop d'intérêt de monter la chance de statut alors que Weeping Wounds le fait déjà » ; Fracas d'Organe (Organ Shatter) est plus intéressant. Après test, il pense qu'il vaut mieux **investir dans les dégâts critiques** (priorité du build). Pistes de l'assistant : « 05-builds-proposes/Gara Prime - pistes d'amelioration (avis de l'assistant) ». Les chiffres de la capture (statut 48 %, Perforation 4 520,1, Toxine 3 925,3) sont ceux **d'avant** le changement.

Comparaison [calcul, hypothèses : fragment violet doublé +75 %, Galvanized Steel à 4 cumuls +120 %, tous les bonus de dégâts critiques dans le même total relatif, formule de la page Critical Hit : multiplicateur = base x (1 + bonus relatifs)] :
- Multiplicateur critique avant : 2 x (1 + 0,75 + 1,20) = **5,9x**. Avec Organ Shatter +90 % : 2 x 3,85 = **7,7x** (+31 %). (La version « +165 % » présente dans les données n'existe pas en jeu, confirmé par XeniX13 : seule la version +90 % est réelle.)
- Weeping Wounds donne +40 % de chance de statut par multiplicateur de combo : à partir d'environ x6, le statut dépasse 100 %, donc les +60 % de Jugulus Barbs ne servaient plus. Le Tranchant du balayage n'avait jamais profité des +90 % de Perforation (le balayage ne fait que du Tranchant).
- Blood Rush (+40 % de chance critique par multiplicateur) fait passer la chance de critique à environ 130 % au combo x12 (20 % x (1 + 1,10 + 0,40 x 11)) : tous les coups sont critiques, avec 30 % de chance d'un critique orange, dont le multiplicateur est 1 + 2 x (M - 1) (page Critical Hit). Les bonus de dégâts critiques valent donc encore plus.
- Ce qui est perdu : Jugulus ajoutait environ +7 % aux dégâts de l'explosion de l'anneau (+90 % de Perforation sur la part de 37,5 % de Perforation de l'explosion). **Organ Shatter n'aide pas l'explosion de l'anneau, qui ne peut pas faire de critique**, mais seulement le coup direct de Shattered Lash. Choix cohérent : le coup direct tue les menaces isolées, l'explosion tue déjà largement la foule.
- Le « 4,7x ▸ 3,2x » de la capture est l'affichage avant ▸ après d'une modification de build faite dans l'arsenal (voir section 4 : très probablement un bug d'affichage). Reste à vérifier les dégâts critiques affichés après le changement Jugulus → Organ Shatter.

## 4. Vérification contre la base [calcul]

Tous ces chiffres sont retrouvés exactement à partir de la base de données, ce qui valide la lecture du build :
- Puissance : 100 + 44 (Umbral Intensify) + 99 (Blind Rage) - 60 (Overextended) = **183 %**.
- Portée : 100 + 45 (Stretch) + 90 (Overextended) = **235 %**. Durée : 100 + 55 = **155 %**. Efficacité : 100 - 55 = **45 %**.
- Énergie : 225 x (1 + 1,85) = **641**.
- Portée de Shattered Lash : 12 m (rang max) x 2,35 = 28,2 m, + 3 m de Primed Reach = **31,2 m**, exactement l'affichage de la capture. Le Kubrow n'intervient pas dans cette portée.
- Chance de critique : 20 % x (1 + 1,10) = **42 %** (Blood Rush ne s'ajoute qu'avec le combo). Chance de statut : 30 % x (1 + 0,60) = **48 %**.
- Dégâts : base 400 x puissance 1,83 = 732 ; multiplicateur de mêlée 1 + 1,65 (Primed Pressure Point) + 0,60 (Steel Charge) = 3,25 ; 732 x 3,25 = **2 379** (Tranchant du balayage). Toxine : 2 379 x 1,65 = **3 925,35**. Perforation : 2 379 x 1,90 = **4 520,1**. Les trois chiffres de la capture sont exacts. Arcane Fury, Arcane Melee Exposure, Condition Overload et le combo ne sont pas dans l'affichage.

Ordre de grandeur de l'explosion d'un segment de l'anneau [calcul, hypothèses : combo x12, 4 cumuls d'Exposition de Mêlée, Fury active, puissance 183 % puis 243 % avec Molt Augmented au maximum] :
- physique : 400 x 1,83 x (1 + 1,65 + 0,60 + 1,80) x 12 = environ 44 000 (environ 59 000 à 243 %) ;
- Corrosif de l'arcane : environ 106 000 (environ 141 000 à 243 %) ;
- avec la vulnérabilité de 50 % de Mass Vitrify : **environ 225 000 à 300 000 par explosion** sur un ennemi cristallisé. À confronter à la santé des ennemis au niveau visé avec la page Enemy Level Scaling ; non fait, [à confirmer : niveau visé].

## 5. Défense du build [retour de jeu + calcul]

Principe [retour de jeu] : XeniX13 vise le **level cap sur tous ses builds**, et à ce niveau la défense classique ne suffit clairement pas. Le build ne cherche donc pas à encaisser : il **tue avant d'être touché**, avec trois filets de sécurité :
1. Splinter Storm (2) : 70 % de réduction de dégâts au rang max (jusqu'à 90 % avec assez de puissance, plafond atteint à 128,6 %, puissance affichée ici 183 %). Mass Vitrify rafraîchit sa durée, donc la réduction reste active.
2. Mass Vitrify (4) : Gara est invulnérable pendant le lancement et l'expansion de l'anneau (environ 11,8 s pour le rayon maximal, voir ci-dessous). Avec +75 % de vitesse de lancement, l'animation est très courte.
3. Kubrow Huras avec Stalk : invisibilité du joueur, qui s'ajoute aux deux premiers filets (« amplement suffisant » d'après XeniX13).

Rayon maximal de l'anneau : 2R + 9RD = 2 x 2,35 + 9 x 2,35 x 1,55 = **37,5 m**, expansion de 3 m/s, soit (37,5 - 2) / 3 = **11,8 s**. Shattered Lash porte à 31,2 m : XeniX13 peut relâcher l'anneau avant le rayon maximal (touche 4) ou se rapprocher du mur [à confirmer : à quel rayon il le fait].

Faiblesses connues dans la base : une bulle de Nullifier qui touche le verre le fait voler en éclats sans aucun dégât ; la plupart des boss et le Teralyst traversent l'anneau.

## 6. Énergie [retour de jeu + calcul]

XeniX13 : les sources d'énergie sont Equilibrium et Nourish, « amplement suffisant » malgré 45 % d'efficacité. L'efficacité faible n'est donc pas un problème dans ce build : la réserve (641) et les orbes d'énergie des ennemis tués (multipliés par Nourish) suffisent.

Coûts à 45 % d'efficacité [calcul, corrigé le 13/11/2026] : la formule du wiki (pages Energy et Abilities) est **coût = coût de base x (2 - efficacité)**, plafonnée à 25 % du coût de base (efficacité 175 %). Une première version de cette note divisait par l'efficacité (111, 167, 56) : c'était faux. Avec 2 - 0,45 = 1,55 : Splinter Storm 50 x 1,55 = **78** ; Mass Vitrify 75 x 1,55 = **116** (plus un drain de 3 à 5 par seconde pendant l'expansion, soit environ 4,7 à 7,8 par seconde) ; Shattered Lash 25 x 1,55 = **39** par lancer. Atteindre le combo x12 demande 11 lancers qui touchent, soit environ 430 d'énergie : c'est pourquoi les orbes comptent. [formule confirmée par XeniX13 le 13/11/2026 : une capacité à 100 d'énergie coûte 155 à 45 % d'efficacité ; le coût est un montant fixe propre à la capacité, il ne dépend pas de l'énergie max. Lavos et Hildryn n'utilisent pas d'énergie.] [à confirmer : rotation exacte, nombre de lancers avant de briser l'anneau]

## 7. Chaîne de synergies (comment lire ce build) [retour de jeu + calcul]

Chaque élément a un rôle dans la boucle, et sert au moins un autre élément :
- **Portée** (Overextended, Stretch, Primed Reach) : sert à la fois la portée de l'arme (31,2 m) et le rayon de l'anneau (2R + 9RD = 37,5 m). La **durée** (Primed Continuity) agrandit aussi l'anneau (le D de 2R + 9RD) et prolonge Splinter Storm.
- **Vitesse de lancement** (2 fragments Amber, +75 %) : lance Mass Vitrify très vite, ce qui rafraîchit Splinter Storm (2) et ajoute 50 % des dégâts de l'explosion à son DPS ; Shattered Lash devient très rapide, donc confortable, et le combo x12 se monte avant que le combo ne décroisse.
- **Combo** : chaque lancer qui touche ajoute +1x (jusqu'à x12). Blood Rush (+40 % de chance critique par multiplicateur) et Weeping Wounds (+40 % de statut par multiplicateur) montent avec lui ; Naramon Power Spike le conserve.
- **Dégâts** : puissance (Blind Rage, Umbral Intensify, Molt Augmented) multiplie la base ; mods de mêlée (Primed Pressure Point, Steel Charge, Arcane Fury) ; éléments (Primed Fever Strike Toxine, ligne Viral de Nourish, Corrosif d'Arcane Melee Exposure qui monte à chaque capacité lancée, d'où l'intérêt de lancer 1, 2, 3 et 4) ; critiques (Galvanized Steel, Blood Rush, fragment violet) ; Condition Overload (+80 % par type de statut présent : Toxine, Perforation, Tranchant, Corrosif, Viral...) ; vulnérabilité de 50 % des ennemis cristallisés.
- **Énergie** : Primed Flow (641) donne la réserve **et** active le doublement du fragment violet (au-dessus de 500) ; Equilibrium et Nourish (orbes x1,3 à x1,6) rechargent ; l'efficacité de 45 % (Blind Rage) est le prix de la puissance.
- **Défense** : tuer vite, Splinter Storm, invulnérabilité de Mass Vitrify, invisibilité du Kubrow.

Affichage de l'arsenal [mesuré, XeniX13, 13/11/2026] : en remplaçant Jugulus Barbs par Organ Shatter, l'arsenal affiche **dégâts critiques 3,2x ▸ 5,0x**. Cela confirme : base de Shattered Lash = 2x, et Organ Shatter = +0,9 (3,2 + 2 x 0,9 = 5,0). L'arsenal n'affiche que les effets directs (pas les cumuls de Galvanized Steel ni les arcanes à déclencheur), et Gladiator Might n'est pas équipé. La base affichée de 3,2x = 2 x (1 + 0,6) contient un **0,6 non expliqué** [à identifier : fragment violet compté en partie ? autre source constante ?]. Le « 4,7x ▸ 3,2x » vu sur une capture précédente reste inexpliqué (XeniX13 pense à un bug d'interface : la valeur n'a pas pu être retrouvée en modifiant les mods). Conséquence : le multiplicateur de 7,7x calculé plus haut (2 x (1 + 0,75 + 1,20 + 0,90)) ignore peut-être ce 0,6 ; à recalculer quand la source sera connue. Dans l'arsenal, le gain d'Organ Shatter est de +56 % (3,2x vers 5,0x), sans cumuls de Galvanized Steel.

## 8. Corrections pour l'assistant (à ne plus refaire)

- Mon erreur : j'avais fait de Gara un **tank** à base de Splinter Storm et de boucliers, avec Shattered Lash en appoint. Le vrai rôle de Gara dans ce build est le **nuke à longue portée** : l'anneau de Mass Vitrify brisé par Shattered Lash.
- **Primed Streamline n'existe pas en jeu** (confirmé par XeniX13). Ne jamais le proposer. Vérifier qu'un mod existe avant de le recommander (les données du jeu contiennent des entrées sans date de sortie).
- L'efficacité basse (45 %) n'est pas un défaut : Blind Rage donne +99 % de puissance, et l'énergie vient d'Equilibrium, de Nourish et des orbes. Ne pas imposer de l'efficacité par peur de manquer d'énergie.
- Ne pas supposer que les stats de défense (boucliers, PV) sont la priorité : ici la défense est de **tuer avant d'être touché**.
- Mon calcul de portée de Shattered Lash et de portée de l'anneau doit toujours passer par les formules de la base (12 m x portée ; 2R + 9RD).
- Le set Umbra complet (+77 % de puissance avec 3 pièces au lieu de +44 %) coûterait deux emplacements ; XeniX13 joue Umbral Intensify seul. Comparaison à refaire si besoin.
