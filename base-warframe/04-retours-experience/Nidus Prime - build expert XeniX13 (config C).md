# Nidus Prime - build expert de XeniX13 (config C, level cap)

**Statut du build : daté, exemple de raisonnement.** Valide à la date du 13/11/2026 (jeu à la mise à jour 44.1.x ; dernières notes de patch en base : 27/10/2026). Les mods, arcanes, frames et armes sont susceptibles de changer à chaque mise à jour : s'en servir pour comprendre le rôle, la boucle de jeu et la logique de chaque choix, puis **reconstruire** avec les données actuelles (voir « Methode - construire un build level cap », section 7), sans copier la liste.

Source : captures d'arsenal de XeniX13 (Update 44.1), interface en français ; traductions vérifiées dans la base.
Ce build est celui que joue XeniX13. Il **prime sur tout build proposé par l'assistant** (voir aussi `Nidus Prime - build level cap.md`).
Légende : [vu] = lu sur les captures ; [calcul] = calculé avec les formules de la base ; [hypothèse] = à confirmer en jeu.

## Loadout Warframe (Nidus Prime rang 30, capacité 7/74 restants)

| Slot | Nom en jeu (FR) | Mod (EN) | Coût affiché |
|---|---|---|---|
| Aura | Pouvoir Grandissant | Growing Power (+25 % de puissance 6 s sur statut d'arme) | - |
| Exilus | Bien Chaussé Accru | Primed Sure Footed (+100 % résistance aux renversements) | 8 |
| 1 | Continuité Accrue | Primed Continuity (+55 % durée) | 7 |
| 2 | Virulence Grouillante | Teeming Virulence (augment de Virulence : 4 ennemis touchés = bonus de chance critique de l'arme principale 15 s) | 11 |
| 3 | Adrénaline du Chasseur | Hunter Adrenaline (45 % des dégâts reçus sur la santé convertis en énergie) | 6 |
| 4 | Super-Étendu | Overextended (+90 % portée, -60 % puissance) | 6 |
| 5 | Vitalité Parasitaire | Parasitic Vitality (augment de Parasitic Link : +4 % PV max par stack de Mutation pendant le lien) | 5 |
| 6 | Colère Aveugle | Blind Rage (+99 % puissance, -55 % efficacité) | 8 |
| 7 | Intensité Umbra | Umbral Intensify (+44 % puissance, avant bonus de set) | 8 |
| 8 | Fibre d'Umbra | Umbral Fiber (+100 % armure, avant bonus de set) | 8 |

- Arcanes : **Arcane Persistance** (Arcane Persistence) et **Arcane Belliqueux** (Arcane Bellicose, +6 % puissance par 250 PV max, jusqu'à +72 %).
- Archon Shards (5 emplacements, 4 occupés) : Amber tauforgé +37,5 % vitesse de lancement ; Azure tauforgé +225 armure ; Crimson tauforgé +15 % puissance ; Azure tauforgé +75 énergie max ; **1 emplacement vide** (il manque un Crimson tauforgé +15 % puissance).
- Inventaire de shards au moment de la capture : Amber 2, Azure 10, Emerald 3, Topaz 3, Violet 2, aucun Crimson.
- Stats d'arsenal [vu] : Santé 925, Bouclier 0, Armure 1 432, Énergie 265, Sprint 1,25 ; Durée 155 %, Efficacité 45 %, Portée 190 %, Puissance 246 %.

## Loadout du compagnon : Chargeur Helminth (config B, capacité 2/60 restants)

Rôle : cible de Parasitic Link (le lien doit rester actif : c'est la condition de survie, voir plus bas).
Stats d'arsenal [vu] : Santé 720, Bouclier 340, Armure 400, Temps de récupération 60 s.

| Nom en jeu (FR) | Mod (EN) | Effet (base) | Coût affiché |
|---|---|---|---|
| Éruption de Souche | Strain Eruption | les asticots explosent à leur mort : 4 % de la santé actuelle de l'ennemi en dégâts Corrosifs dans 8 m | 5 |
| Lien Tenace | Tenacious Bond | kills à la tête : -3 s de récupération | 4 |
| Lien Capital | **Momentous Bond** (confirmé par XeniX13) | tuer un Eximus : +120 % dégâts élémentaires 30 s et -18 s de récupération | 9 |
| Récupérateur Débrouillard | Resourceful Retriever | 18 % de chance de doubler les ressources | 7 |
| Récupération du Chasseur | Hunter Recovery | le Warframe est soigné de +30 % des dégâts du compagnon | 5 |
| Piétinement | Trample | charge de 160 dégâts ; +10 % dégâts mêlée / PV max / armure par ennemi touché 5 s | 3 |
| Chef de Meute Accru | Primed Pack Leader | +183 PV par coup, +2 200 Overguard max | 7 |
| Lien Contagieux | Contagious Bond | le statut d'un ennemi tué par le compagnon se propage à 50 % dans 9 m | 9 |
| Lien Duplex | Duplex Bond | clones du compagnon à chaque 100 énergie dépensés (3 max, 30 s) | 5 |
| Va chercher | Fetch | collecte d'objets à 13,5 m | 4 |

Synergie : Hunter Adrenaline (Warframe) + Hunter Recovery (compagnon) forment le set Hunter. Le compagnon n'a aucun mod de vie ni d'armure : sa santé vient de Parasitic Vitality, d'après [hypothèse].

## Vérification des stats d'arsenal [calcul]

- Durée 155 % = 100 + 55 (Primed Continuity) ✓
- Portée 190 % = 100 + 90 (Overextended) ✓
- Efficacité 45 % = 100 - 55 (Blind Rage) ✓
- Énergie 265 = 190 + 75 (Azure tauforgé) ✓
- Capacité utilisée 67 sur 74 ✓ ; compagnon 58 sur 60 ✓
- Puissance 246 % : 100 + 99 (Blind Rage) - 60 (Overextended) + 18 (Bellicose à 925 PV, 3 paliers) + 15 (Crimson tauforgé) = 172, plus Umbral Intensify. Il manque donc 74 points, soit 44 × 1,68. Avec le bonus de set Umbral à ×1,3 : 57,2, total 229 %, il reste environ 17 points que je ne sais pas expliquer.
- Armure 1 432 = 525 × (1 + 1,3) + 225 : Umbral Fiber à +130 % (bonus de set Umbral ×1,3) colle exactement. La base dit seulement que le set « augmente le bonus de chaque mod », sans chiffre.
- Conclusion : le bonus de set Umbral est réel mais non chiffré dans la base ; les calculs ci-dessous partent des **valeurs affichées en arsenal**.

## Calculs en jeu [calcul]

Formules de la base :
- Parasitic Link sur un allié : bonus = 25 % × puissance ; puissance modifiée = puissance × (1 + bonus) ; le même bonus s'applique aux dégâts d'arme (multiplicatif avec Serration).
- Ravenous : soin 75 PV/s × puissance modifiée (calculé au lancement), purge des statuts à chaque pulsation ; coût de 3 stacks de Mutation (non affecté par l'efficacité).
- Virulence : remboursement d'énergie par ennemi = 1/4 du coût (plus l'efficacité est basse, plus il rembourse).
- Persistence : au-dessus de 700 d'armure, aucun coup ne dépasse 500 dégâts/s ; Magnétique et Nullifiers coupent la protection.

Puissance en jeu : en arsenal Bellicose ne compte que 18 % (925 PV). En jeu, avec plus de 3 000 PV, il monte à 72 % : **246 - 18 + 72 = 300 %**.

| Cas | Puissance avant lien | Puissance avec lien | Bonus dégâts d'arme | Soin de Ravenous |
|---|---|---|---|---|
| Sans Growing Power | 300 % | **525 %** | +75 % | **394 PV/s** |
| Avec Growing Power | 325 % | **589 %** | +81 % | **442 PV/s** |

- Vie [hypothèse] : XeniX13 mesure environ **24 000 PV** avec un build de puissance similaire. Le bonus additif (4 % × 200 stacks) ne donne que 8 325 PV. L'hypothèse qui colle le mieux est que le bonus de Parasitic Vitality **monte avec la puissance** : 925 × (1 + 0,04 × 200 × 3,0) = 23 125 PV (24 975 avec Growing Power). Autre piste, Abundant Mutation à 500 stacks en additif : 19 425 PV. Même effet espéré pour le compagnon : 720 × 25 = environ 18 000 PV.
- Umbral Vitality ne vaut donc que +4 % de PV face à Parasitic Vitality : elle n'a pas sa place dans ce build.
- Face au plafond de Persistence (500/s) : déficit de 106 PV/s sans Growing Power, 58 PV/s avec. À 24 000 PV, environ 226 s de tenue sous dégâts maximaux constants (environ 430 s avec Growing Power).
- Armure : 1 432, soit 716 sous Feu (-50 %) : Persistence reste active mais avec seulement **16 de marge** sur le seuil de 700. Sous Corrosif au maximum (-80 %) : 286, Persistence coupée.
- Énergie (efficacité 45 %) : Virulence coûte environ 89, Larva et Link environ 56. Virulence rembourse environ 22 par ennemi touché : rentable à partir de 4 ennemis. Hunter Adrenaline peut rendre jusqu'à 225 énergie/s au plafond de Persistence (45 % de 500, maximum théorique).
- Portée 190 % : Larva 22,8 m de rayon, Virulence 30,4 m, Ravenous 15,2 m de diamètre, lien allié 76 m, lien ennemi 38 m.
- Durée 155 % : Ravenous 62 s, Parasitic Link 93 s, Larva 10,85 s, champ de Virulence 7,75 s.

**Si le lien tombe** : les PV retombent à 925 et Bellicose à 18 %, soit environ 246 % de puissance et 184 PV/s de soin : environ 3 s de survie sous dégâts maximaux. Parasitic Link garde 3 à 4 s de marge avant de se rompre, d'où le rôle du Chargeur Helminth (récupération raccourcie par Tenacious Bond et Momentous Bond, PV via Parasitic Vitality, Overguard de Primed Pack Leader).

## Cinquième shard : Crimson tauforgé (+15 % puissance) [calcul]

| | Aujourd'hui | Avec le shard |
|---|---|---|
| Puissance en arsenal | 246 % | 261 % |
| Puissance au lien (sans / avec Growing Power) | 525 % / 589 % | **563 % / 629 %** |
| Soin de Ravenous (sans / avec Growing Power) | 394 / 442 PV/s | **422 / 472 PV/s** |
| Vie (hypothèse de la force, sans / avec GP) | 23 125 / 24 975 | environ 24 235 / 26 085 |
| Déficit face à Persistence (sans / avec GP) | 106 / 58 PV/s | 78 / 28 PV/s |

Obtention : trois Crimson fusionnés (Ascent Fusion, 100 Stela d'après le wiki) donnent un tauforgé.
En attendant, un Azure en armure comble le slot : tauforgé +225 (1 657 d'armure, 828 sous Feu, marge 128) ou normal +150 (1 582, 791 sous Feu, marge 91), sans gain de puissance.

## Pourquoi ce build bat le build initial de l'assistant

- Le build initial avait une puissance de 246 % (avec Bellicose) et 145 % de portée ; celui-ci a 300 % de puissance et 190 % de portée, au prix d'une efficacité de 45 %, compensée par Hunter Adrenaline et le remboursement de Virulence.
- Soin de Ravenous : 394 PV/s contre 298 PV/s pour le build initial.
- Le build initial incluait Umbral Vitality (négligeable ici), Rolling Guard et Stretch (portée +45 % seulement), et ne tirait pas parti de l'efficacité basse (Hunter Adrenaline, remboursement de Virulence).

## Variante Jade : Ophanim Eyes à la place de Ravenous (Helminth)

Source : XeniX13. Mods, arcanes, shards et compagnon **identiques** à la config C ci-dessus ; **seule la capacité remplacée par le Helminth change** (Ravenous, 4e pouvoir, remplacé par Ophanim Eyes de Jade).
Usage : mobs très blindés comme les Grineer.

Ophanim Eyes (base, rang max, version transférée par le Helminth, sans relevage d'alliés) :
- 50 énergie, cône de 70° sur 20 m, 30 s ; retire 10 %/s de l'armure et des boucliers, de façon permanente ; ralentit de 15 %/s (plafond 90 %, sans effet sur Overguard) ; 50 de dégâts Feu toutes les 0,5 s ; statut Feu une fois les défenses retirées.
- Appuyer à nouveau pendant la durée la rafraîchit au maximum ; maintenir la touche l'annule.

Avec ton build [calcul] :
- Coût : 50 / 0,45 = environ 111 énergie sur 265 ; durée 30 × 1,55 = 46,5 s ; portée 20 × 1,9 = 38 m si elle suit ta portée.
- Dégâts Feu : 50 × puissance par tick de 0,5 s. À 525 % (lien) : environ 262 par tick, 525/s ; avec le Crimson tauforgé (563 %) : environ 281 par tick. Négligeable au niveau max : l'intérêt de la capacité est le retrait de défenses et le ralentissement.
- Retrait de l'armure [retour de jeu] : il **monte bien avec la puissance**. XeniX13 lit **24 %/s** en arsenal (sans aucun buff, stats de base du build), ce qui correspond à 10 % × 246 % (puissance affichée en arsenal, Bellicose à 18 %) = 24,6 %. Retrait total en environ 4 s à ce rythme.
- [retour de jeu] La puissance, **y compris celle modifiée par le lien**, s'applique à tous les pouvoirs, Helminth compris. En jeu avec le lien (525 %) : environ **52 %/s**, retrait total en environ 1,9 s ; sans lien avec Bellicose au maximum (300 %) : 30 %/s, retrait total en environ 3,3 s.
- Ralentissement : 6 s pour atteindre le plafond de 90 %.

Ce qui change par rapport à Ravenous :
- Perte du soin de Ravenous (394 PV/s, 442 avec Growing Power), de la purge de statuts à chaque pulsation et des stacks de Mutation gagnés via les asticots de Ravenous ; Ravenous ne coûte plus 3 stacks.
- Retour de jeu de XeniX13 : ce n'est pas un problème en pratique. Les Nullifiers et les Eximus s'évitent facilement, et **le compagnon soigne le Warframe grâce à Hunter Recovery** (30 % des dégâts du compagnon, dont les explosions de Strain Eruption : 4 % de la santé actuelle de chaque ennemi proche). Ce soin n'est pas chiffrable avec la base (dépend de la vie des ennemis au niveau max).
- Sans le soin de Ravenous et sans Hunter Recovery, la tenue sous 500 PV/s constants serait d'environ 48 s avec 24 000 PV : ce chiffre n'est pas représentatif en jeu, vu le soin du compagnon.
- Sans changement : puissance (300 % avant lien, 525 % avec), bonus de dégâts d'arme du lien, PV via Parasitic Vitality, armure et marge sur Persistence, énergie, portée et durée.

## Helminth : comparatif des capacités pour ce build

Contexte [retour de jeu] : XeniX13 joue **trois variantes** du build selon l'ennemi, avec le même loadout et seule la capacité remplacée qui change (Ravenous) : **Ravenous** (soin), **Ophanim Eyes** (retrait d'armure, mobs blindés comme les Grineer) et **Roar** (dégâts). La puissance modifiée par le lien s'applique à tous les pouvoirs, Helminth compris : c'est la raison principale de ces variantes.

Pourquoi le retrait d'armure est le plus fort contre les mobs blindés [calcul, base : page Armor] : l'armure initiale des ennemis est plafonnée à 2 700 par le niveau, et la réduction de dégâts ennemie vaut 90 % × racine carrée de (armure nette / 2 700) (correction du 13/11/2026 : la page Armor était tronquée à l'import et la racine carrée avait été lue comme une division simple ; les multiplicateurs ci-dessous remplacent les anciens ×3,2 / ×3,7 / ×5,5). Un ennemi à armure maximale reçoit donc 10 % des dégâts. Multiplicateur de dégâts selon l'armure retirée : 24 % = ×2,15 ; 30 % = ×2,47 ; 50 % = ×3,64 ; 80 % (Corrosif au maximum) = ×5,98 ; 100 % = ×10. Un retrait partiel pèse donc moins que prévu, et le retrait total (×10) reste le plus fort. À titre de comparaison, Roar donne ×1,9 à 300 % de puissance et ×2,58 à 525 %.

Valeurs avec le build (coût divisé par l'efficacité de 45 %, durée ×1,55, portée ×1,9) :

| Capacité | Effet | Sans lien (300 %) | Avec lien (525 %) | Coût |
|---|---|---|---|---|
| Ravenous (Nidus) | soin 75 PV/s × puissance, purge des statuts | 225 PV/s | 394 PV/s | 3 stacks |
| **Ophanim Eyes** (Jade) | retrait de 10 % × puissance par seconde, ralentissement jusqu'à 90 %, Feu | 30 %/s (total en 3,3 s) | **52 %/s** (total en 1,9 s) | 111 énergie ; 46,5 s ; 38 m |
| **Roar** (Rhino) | +30 % × puissance de dégâts pour soi et les alliés, compagnon compris (confirmé par l'exemple du wiki : 253 % = +75,9 %) | +90 % (×1,9) | **+157,5 % (×2,58)** | 167 énergie ; 46,5 s ; 47,5 m |
| Tharros Strike (Styanax), non testé | retrait de 50 % × puissance de l'armure et des boucliers ; **total dès 200 % de puissance** ; étourdit 2 s ; +100 PV par ennemi | 100 % en un coup | 100 % en un coup | 56 énergie ; cône de 17 m |
| Xata's Whisper (Xaku), non testé | coup Void supplémentaire de 26 % × puissance du total de l'arme (hypothèse : monte avec la puissance) | +78 % | +136 % | 56 énergie ; 54 s |
| Remedium (Uriel), non testé | soin de 35 % de la vie max, invulnérable pendant le lancement, purge de statuts | 8 400 PV sur 24 000 (minimum) | idem, plus si la puissance s'applique | 111 énergie |

Notes :
- Roar, Eclipse et Xata partagent la limite « 1 capacité qui augmente les dégâts par Warframe » (base). Effet sur le bonus de dégâts du Link : inconnu.
- Roar profite au Chargeur Helminth, donc aussi à Hunter Recovery (soin du Warframe) et aux explosions de Strain Eruption.
- Tharros Strike vs Ophanim Eyes (mobs blindés) : Tharros retire tout au premier coup pour moitié moins d'énergie, mais sur 17 m, avec une animation qui interrompt le mouvement et un lancer par groupe ; Ophanim agit en continu sur 38 m et ralentit, mais demande environ 2 s (avec le lien).
- Non évaluées : les autres capacités de retrait d'armure (Hydroid, Nekros, Ash, Ember, Oberon).

## Points à confirmer en jeu

- Retrait d'armure d'Ophanim Eyes : les 24 %/s sont lus **en arsenal, sans aucun buff** (puissance de base du build, Bellicose à 18 %), ce qui correspond à 10 % × 246 %. XeniX13 confirme que la puissance modifiée par le lien s'applique aux pouvoirs Helminth : valeur attendue en jeu d'environ 52 %/s, non mesurée.
- Capacités Helminth marquées « non testé » dans le comparatif (Tharros Strike, Xata's Whisper, Remedium) : à tester en jeu.

- Hypothèse de la puissance sur Parasitic Vitality (24 000 PV mesurés contre 8 325 en additif).
- Valeur exacte du bonus de set Umbral (×1,3 sur l'armure ; environ 17 points de puissance inexpliqués).
- Teeming Virulence : la base indique +200 % de chance critique primaire 15 s, le patch note 43 indique 150 % (ancienne valeur 120 %).
- Durée de grâce de Parasitic Link : 3 s (patch note 43) ou 4 s (wiki).
- Ordre d'application du plafond de 500 PV/s de Persistence par rapport à la redirection de dégâts de Parasitic Link sur ennemi : à tester.

## Retour de test : Coda Bubonico en arme primaire (13/11/2026)

Source : tests en jeu de XeniX13 (priorité sur les calculs de l'assistant).

### Ce qui est conservé
- Le build Warframe de la config C reste **inchangé** : Teeming Virulence et Primed Sure Footed conservés.
- Variante essayée puis abandonnée : Transient Fortitude (+ Power Drift) à la place de Teeming Virulence et Primed Sure Footed. Elle donne plus de puissance (environ 712 % au Link au lieu de 525 % d'après le calcul), mais fait perdre du **confort** : plus de résistance aux renversements (Primed Sure Footed) et plus de Teeming Virulence.

### Configuration de l'arme
- **Coda Bubonico** (fusil à pompe Coda : 7 projectiles, Tranchant + Toxin de base, tir alternatif en rafale Viral avec explosion de 7 m et +9 s de durée de statut) en primaire.
- **Viral** : vient du **tir secondaire**, où il est natif (explosion Viral de 7 m) ; ce n'est pas un mod.
- **Corrosif** : sur le tir principal, les dégâts de Toxin sont amplifiés par la **fusion de Valence** (arme Coda), puis un mod de dégâts Électricité (« accru ») s'ajoute pour former Corrosif (Électricité + Toxin).
- Chance de statut : **18,3 % par projectile** au tir principal (14,7 projectiles par tir) et **environ 102 %** sur l'explosion Viral du tir secondaire (voir « Lecture de l'arsenal » plus bas).
- Rôle de l'arme : **applicateur de debuffs**, pas source principale de dégâts.
  - Corrosif : retire l'armure des ennemis blindés (Grineer, etc.).
  - Viral : amplifie tous les dégâts faits à la santé, y compris ceux de Virulence (1) et des larves.

### Lecture de l'arsenal (config A du Coda, capture de XeniX13, 13/11/2026)
- Bonus de Valence : **Poison +26,6 %**. Mods visibles : Cartouche Chargée Accrue, Enfer Galvanisé, Stock de Balles Accru, Décélération Critique, Accélération Galvanisée (exilus), À Bout Portant Accru, Barrage au Fusil à Pompe Amalgame, Habileté Galvanisée. Il reste un emplacement libre et **4 de capacité** restante.
- **Dernier mod prévu : Pompe Tactique** (vitesse de recharge), car le tir secondaire consomme beaucoup de munitions.
- Stats du tir principal affichées : cadence 8,78 ; tir multiple 14,7 ; chargeur 65 ; recharge 1,5 s ; chance critique 81 % ; dégâts critiques 3,5x ; statut 18,3 % par projectile ; Corrosif 493,7 ; Perforation 88,7 par projectile.
- Vérification avec la base (valeurs de base du Coda) :
  - chargeur 36 x 1,8 = 65 ;
  - tir multiple 7 x 2,1 = 14,7 ;
  - chance critique 27 % x 3 = 81 % ;
  - statut 10,14 % x 1,8 = 18,3 % (+80 %) ;
  - **explosion Viral du tir secondaire : 57 % x 1,8 = 102,6 %**, ce qui est le « 102 % » de XeniX13 (l'impact direct du tir secondaire : 61 % x 1,8 = 110 %) ;
  - recharge : 5,5 s de base contre 1,5 s affichés, soit environ +267 % de vitesse de recharge déjà en place.
- Répartition approximative des procs du tir principal (poids = dégâts par type ; Tranchant et Impact non visibles sur la capture, estimés avec le même multiplicateur que la Perforation, x6,82) : Corrosif environ 68 %, Tranchant 18 %, Perforation 12 %, Impact 2 %.
- Environ 2,7 procs par tir si tous les projectiles touchent, soit environ 1,8 procs de Corrosif par tir ; 10 stacks de Corrosif en environ 5 à 6 tirs sur une cible qui prend tous les projectiles (environ 1,3 s avec la montée en cadence).
- Munitions : chargeur de 65 ; la batterie se régénère à 9 munitions par seconde (donc environ 7 s pour se remplir de vide), après un délai de 1,5 s de base réduit par la vitesse de recharge. La vitesse de recharge agit sur la recharge manuelle et sur ce délai, pas sur le rythme de régénération. Avec environ +267 % déjà en place, un Pompe Tactique supplémentaire fait gagner peu de temps par recharge (de l'ordre de 0,1 à 0,2 s ; sa valeur exacte n'est pas dans la base).

### Résultat mesuré
- Test sur Virulence (1) avec Nidus boosté à pleines stacks : environ **600 000** de dégâts sans le Coda, plus de **2 000 000** avec le Coda, soit un multiplicateur d'environ **×3 à ×3,3 sur les dégâts globaux de Nidus**.

### Vérification par le calcul (base de données)
- Viral (Cold + Toxin) : +100 % de dégâts à la santé par stack, jusqu'à **+325 % à 10 stacks** (x4,25 au maximum), chaque stack ayant sa propre durée de 6 s.
- Corrosif (Electricity + Toxin) : -26 % d'armure par stack, 8 s par stack. Le retrait total demande davantage de stacks sur les cibles à armure maximale (voir « Corrosif et Archon Shards » dans la note des retours d'expérience).
- Le x3 à x3,3 mesuré représente environ 78 % du maximum théorique de x4,25 : cela correspond à une moyenne d'environ 6 à 7 stacks de Viral équivalents (estimation, en supposant +25 % par stack après la première), ou à une part de dégâts qui n'est pas amplifiée (armure, etc.).
- Le tir alternatif du Coda ajoute +9 s de durée de statut, soit environ 15 s pour Viral et 17 s pour Corrosif au lieu de 6 s et 8 s : il sert à maintenir les stacks.

### Teeming Virulence : utile sur le tir principal uniquement
- Le tir secondaire n'a que **5 % de chance critique** de base : Teeming Virulence n'y change presque rien.
- Sur le **tir principal**, XeniX13 passe en **full critique rouge** quand il doit tuer une cible plus difficile à tuer : c'est là que Teeming Virulence (bonus de critique du primaire après des coups de Virulence) sert vraiment.
- Le jeu normal repose sur le statut ; le critique est un mode de renfort pour les cibles dures.

### Points à confirmer
- Liste exacte des mods du Coda Bubonico (capture d'écran annoncée par XeniX13).
- Page « tir secondaire » de l'arsenal : types de dégâts de l'explosion. Si Valence (Poison) et le mod Électricité s'appliquent aussi à l'explosion, une partie devient Corrosif et la part de Viral dans les procs baisse (estimation grossière : environ 40 % de Viral) ; cela irait dans le sens du multiplicateur mesuré de x3,3 (environ 6 à 7 stacks de Viral) plutôt que x4,25.
- Valeur exacte de Pompe Tactique (mod de fusil à pompe absent de la base : le fichier des mods primaires ne reprend qu'un seul mod de fusil à pompe) et son coût par rapport aux 4 de capacité restante.
- Part de procs de Tranchant dans les statuts : elle dilue les procs Viral et Corrosif si la base physique reste importante.
- Nombre moyen de stacks de Viral et de Corrosif en combat.
