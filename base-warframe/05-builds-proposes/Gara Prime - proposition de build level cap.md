# Gara Prime : proposition de build level cap (non testée en jeu)

**OBSOLÈTE (13/11/2026) : ne pas utiliser.** Cette proposition de l'assistant est fausse : elle faisait de Gara un tank, suppose un mod qui n'existe pas en jeu (Primed Streamline) et compte sur de l'efficacité qui n'existe pas. Le vrai build, testé en jeu, est dans « 04-retours-experience/Gara Prime - build expert XeniX13 » (nuke à longue portée avec Shattered Lash et Mass Vitrify).

Statut : **proposition de l'assistant, calculée à partir de la base de données, jamais testée en jeu.** À corriger par XeniX13 : ses tests priment sur tout ce qui est écrit ici. Méthode suivie : voir « Methode - construire un build level cap ».
Hypothèses non vérifiées : capacité de 60 (rang 30 + réacteur) et polarités posées librement avec des formas.

**Corrections reçues de XeniX13 (13/11/2026) et relectures de la base :**
- Les auras d'énergie comme Energy Siphon ne sont presque jamais jouées (inutiles) : il y a de meilleurs moyens de regagner de l'énergie sans gâcher l'aura. L'aura Energy Siphon de cette proposition est **retirée** (voir section 7).
- Gara a des mods d'augment (Mending Splinters, Shattered Storm, Spectrosiphon) que cette proposition n'utilise pas encore.
- Les boucliers donnent une période d'invulnérabilité quand ils sont détruits (shield gating). Les boucliers ont aussi 50 % de réduction de dégâts native, et l'armure ne les protège pas (page Shield de la base). Ces points n'étaient pas dans les calculs d'origine.
- Une version 2 est en attente des choix de XeniX13 (boucliers, augment).

## 1. Pourquoi Gara et quel rôle

- Gara Prime (rang 30) : 445 PV, 370 boucliers, 200 armure, 225 énergie.
- Défense différente de Nidus : pas de réserve de PV ni de limiteur de dégâts, mais :
  - **Splinter Storm (2)** sur soi : réduction de dégâts de 70 % x puissance, **plafonnée à 90 %**, atteinte à partir de **128,6 % de puissance** ; elle s'applique aux boucliers, aux PV et à l'overshield.
  - **Mass Vitrify (4)** : Gara est **invulnérable** pendant le lancement et l'expansion de l'anneau, puis l'anneau se solidifie en mur qui bloque tirs et ennemis.
  - Passif : chance d'aveugler les ennemis proches quand elle lance une capacité.
- Moteur de dégâts : un coup de Shattered Lash (1) sur son propre mur le fait exploser ; 50 % des dégâts de l'explosion s'ajoutent de façon permanente aux dégâts par seconde de Splinter Storm, tant que celui-ci dure. Mass Vitrify relance la durée de Splinter Storm.
- Faiblesses : PV bas, énergie gourmande (aucune génération), dégâts physiques (Impact, Perforation, Tranchant) divisés par l'armure ennemie, animations de lancement qui immobilisent.

## 2. Build proposé

Capacité utilisée supposée : 60. Coûts avec polarité adaptée (moitié du coût de base, arrondi au supérieur).

| Emplacement | Mod (base de données) | Effet | Polarité idéale | Coût |
|---|---|---|---|---|
| 1 | Umbral Intensify | +44 % puissance | umbra | 8 |
| 2 | Transient Fortitude | +55 % puissance, -27,5 % durée | madurai | 8 |
| 3 | Primed Continuity | +55 % durée | madurai | 7 |
| 4 | Primed Streamline | +55 % efficacité | naramon | 7 |
| 5 | Primed Flow | +185 % énergie max | naramon | 7 |
| 6 | Primed Redirection | +180 % capacité de bouclier | vazarin | 8 |
| 7 | Energy Nexus | +3 énergie/s | naramon | 5 |
| 8 | Stretch | +45 % portée | naramon | 5 |
| Exilus | Power Drift | +15 % puissance, +30 % résistance aux renversements | zenurik | 5 |
| Aura | à choisir (Energy Siphon retiré) | voir section 7 | | |

Total d'environ 60 hors aura. Cela fait beaucoup de formas : à ajuster selon ce que tu as déjà posé.

- **Arcanes** : Arcane Expertise (100 % des bonus de puissance s'appliquent aux boucliers max) et Arcane Barrier (restaure tous les boucliers, 6 % de chance quand les boucliers sont touchés, 6 s de délai).
- **Helminth** : Spectrorage (3) remplacée par **Tharros Strike** (Styanax) : 25 énergie, retire 50 % x puissance de l'armure et des boucliers ennemis (retrait total à **200 % de puissance**), repousse, étourdit 2 s et soigne 50 à 100 PV par ennemi touché.
- **Shattered Lash** (config à part, à tester) : Primed Pressure Point (+165 % dégâts de mêlée) et Spoiled Strike (+100 %, la baisse de vitesse d'attaque ne gêne pas car la cadence suit la vitesse de lancement) ; arcane Melee Exposure (+60 % de dégâts Corrosif par lancement de capacité, jusqu'à 240 %), qui s'ajoute aux dégâts de l'explosion (le Corrosif peut aussi retirer de l'armure par statut, avec 30 % de chance de statut sur Shattered Lash) ; Melee Retaliation (+30 % de dégâts de mêlée par 200 boucliers, jusqu'à 420 %) si on garde les boucliers hauts.

## 3. Calculs (script de vérification, formules de la base)

Statistiques : puissance 214 %, durée 127,5 %, efficacité 155 %, portée 145 %, énergie 641.

| Point | Valeur |
|---|---|
| Boucliers | 370 x (1 + 1,8 + 1,14) = environ 1 458 (Expertise ajoute les 114 % de puissance des mods) |
| PV / armure | 445 PV, armure 200 (réduction d'armure 40 %) |
| Réduction Splinter Storm | 70 % x 2,14 = 150 %, plafonnée à **90 %** (marge de 85 points de puissance) |
| Réduction totale sur les PV | 1 - 0,1 x 0,6 = **94 %** ; sur les boucliers : 90 % |
| Dégâts bruts avant mort (une réserve) | PV : environ 7 400 ; boucliers : environ 14 600 ; total environ 22 000 |
| Splinter Storm | durée 28 s, rayon 3,6 m, 535 dégâts/s de base, vulnérabilité ennemie +75 % |
| Mass Vitrify | rayon max 2R + 9RD = 19,5 m, expansion 5,8 s (invulnérable), effet 20,4 s, vulnérabilité ennemie +107 %, segment de mur d'environ 5 560 PV, explosion de segment d'environ 1 710 |
| Tharros Strike | retrait de 107 % : **armure et boucliers ennemis retirés en un lancement** (seuil 200 % ; marge de 14 points) |
| Coûts d'énergie | Storm 32,3 ; Vitrify 48,4 + environ 23 d'expansion (pire cas) ; Lash 16,1 ; Tharros 16,1 |
| Rotation (Vitrify, 2 Lash, Tharros par 28 s) | environ 120 énergie, soit 4,3 énergie/s |
| Autonomie | 641 / (4,3 - 3 d'Energy Nexus) = environ 500 s sans aura d'énergie ; Zenurik Wellspring (3 à 5 énergie/s) couvrirait toute la rotation |

- La formule du rayon de Mass Vitrify a été recoupée avec la base : à portée et durée de 100 %, 2 + 9 = 11 m (valeur du rang max).
- Sans Power Drift, la puissance tombe à 199 % : Tharros Strike ne retire plus que 99,5 % et il faut deux lancements.

## 4. Avantages et inconvénients

Avantages
- Défense par réduction de dégâts à 90 % qui ne dépend ni du nombre de PV ni de l'armure, avec invulnérabilité à la demande pendant Mass Vitrify.
- Boucliers à 1 458 protégés par Arcane Barrier, utiles contre ce qui ne contourne pas les boucliers.
- Tharros Strike comble la faiblesse « physique contre armure » (x10 de dégâts au maximum d'après la formule d'armure) pour 25 d'énergie au lieu de 75 pour Spectrorage.
- La marge de puissance sur le plafond de 90 % laisse de la place pour la puissance de dégâts.

Inconvénients et ce qui est perdu
- **PV bas (445)** : les attaques qui ignorent les boucliers (Toxin, statuts) frappent des PV peu nombreux. Alternative : Vitality (+100 % PV) à la place de Stretch porte la réserve de PV à environ 14 800 dégâts bruts, au prix de la portée (mur de 13,5 m au lieu de 19,5 m).
- **Spectrorage perdue** : plus de miroirs (qui attirent les ennemis, détournent leur attention des joueurs et ajoutent 50 % de leurs dégâts à Splinter Storm) et moins de dégâts accumulés.
- **Énergie** : dépend d'Energy Nexus ; sans lui, environ 2 minutes d'autonomie (641 / 4,3 = 149 s sans aucune régénération).
- Les lancements de Splinter Storm et de Tharros Strike immobilisent Gara ; Nullifiers : une bulle fait s'arrêter Mass Vitrify.

## 5. Variantes

| Variante | Effet |
|---|---|
| Sans Transient Fortitude (puissance 159 % avec Power Drift) | Durée 155 % : Storm 34 s, mur de 23,1 m ; mais Tharros Strike retire 80 % seulement (deux lancements) et la vulnérabilité de Vitrify tombe à 80 % |
| Spectrorage gardée, Tharros Strike abandonnée | Contrôle des ennemis et plus de dégâts accumulés, mais plus de retrait d'armure ni de soin |
| Vitality à la place de Stretch | Environ 29 400 dégâts bruts avant mort au total (voir plus haut), mur de 13,5 m |

## 6. À tester ou à corriger par XeniX13

- Les ennemis du niveau visé infligent-ils plus de 22 000 dégâts bruts en une rafale ? (aucune formule de dégâts ennemis dans la base)
- Compatibilité Umbral Intensify + Transient Fortitude (supposée d'après le test de XeniX13 sur Nidus).
- Plafond d'efficacité : absent de la base ; le build reste à 155 %.
- Un seul coup de Lash fait-il exploser tout le mur, et de combien monte réellement le DPS de Splinter Storm ?
- Tharros Strike subsumée : la puissance modifiée s'applique-t-elle bien (XeniX13 l'a confirmé pour les autres capacités Helminth), et le soin dépend-il de la puissance ?
- Un meilleur choix pour l'emplacement de Stretch, des mods de Lash, et l'ordre d'application de la réduction de dégâts avec les boucliers.
- Des formas à poser pour les polarités.

## 7. Comparaisons : énergie et aura (règle de XeniX13 : toujours comparer)

Besoin : la rotation consomme environ 4,3 énergie/s ; Energy Nexus en donne 3.

| Option | Gain | Coût | Verdict |
|---|---|---|---|
| Energy Siphon (aura) | +0,6 énergie/s, autonomie de 500 s à 940 s | emplacement d'aura | rejeté : trop faible, gâche l'aura |
| Zenurik Wellspring (Focus, pas de mod) | 3 à 5 énergie/s pendant 20 à 30 s par passage dans le puits (5 à 8 s de durée du puits) | Focus Zenurik, lancer la première capacité de l'Opérateur | meilleur sur le papier : couvre la rotation seul (5 > 4,3) ; à confirmer en jeu |
| Energy Nexus (mod, retenu) | +3 énergie/s | un emplacement de mod (5 de capacité) | retenu ; peut être retiré si Wellspring suffit |
| Equilibrium (mod) | les orbes de santé donnent +110 % d'énergie | un emplacement, dépend des orbes | rejeté : dépend de la présence d'orbes de santé |
| Hunter Adrenaline / Rage | convertissent des dégâts subis en énergie | un emplacement ; avec -90 % de dégâts reçus, presque rien à convertir | rejeté pour Gara |

Aura candidate à la place (à trancher) :

| Aura | Effet | Effet pour Gara | Remarque |
|---|---|---|---|
| Growing Power | +25 % de puissance pendant 6 s à chaque statut de ton arme | 214 % -> 239 % ; marge sur le seuil de 200 % de Tharros Strike : 39 points au lieu de 14 | demande une arme qui applique des statuts (le Coda Bubonico convient) |
| Steel Charge | +60 % de dégâts de mêlée | Shattered Lash compte comme une frappe de mêlée : environ +16 % de dégâts sur Lash et l'explosion du mur (calcul additif avec Primed Pressure Point +165 % et Spoiled Strike +100 %) | coût 1 ; bénéficie aussi aux alliés |
| Corrosive Projection | -18 % d'armure ennemie | faible avec Tharros Strike (retrait total) | utile avant le premier lancement |
| Brief Respite | convertit 150 % de l'énergie dépensée en boucliers | environ 120 énergie par 28 s = 180 boucliers, soit environ 6 boucliers/s | négligeable face à 1 458 boucliers |

## 8. Corrections de calcul issues de la base

- Boucliers : la page Shield indique 50 % de réduction native, sans protection de l'armure, et que le Toxin ignore les boucliers. Si cette réduction se multiplie avec les 90 % de Splinter Storm (non confirmé), les boucliers de 1 458 absorbent environ 29 000 dégâts bruts, et non 14 600. Total avec les PV : environ 36 600 dégâts bruts.
- Overguard : n'est pas réduit par l'armure ni par Splinter Storm (page Overguard) : l'Overguard ne profite pas des 90 %.
- Shield gating : une fois les boucliers à zéro, brève invulnérabilité (Catalyzing Shields la porte à 1,33 s ; la durée de base n'est pas dans la base). Les boucliers recommencent à se recharger 4 s après le dernier coup pris pendant le gate (1 s si seulement partiellement entamés). Vitesse de recharge : (15 + 5 % des boucliers max) x (1 + bonus) par seconde, soit environ 88 par seconde ici (16,6 s pour se remplir sans bonus).
- Dégâts ennemis : multiplicateur de 1 + 0,015 x (niveau - niveau de base) puissance 1,55 (page Damage). La base ne contient pas les dégâts de base des ennemis, donc pas de dégâts bruts par coup au niveau visé.
