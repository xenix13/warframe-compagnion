# Banshee Prime : proposition de build nuke (Gaseous Quake), avis de l'assistant

Statut : **proposition de l'assistant du 13/11/2026, non testée en jeu.** Construite avec la méthode, les retours de XeniX13 (« Banshee - retours de XeniX13 ») et les données de la base. Tous les totaux viennent du moteur de calcul. XeniX13 décide, ses tests priment.

Objectif retenu : nuker la map en solo comme en escouade, Steel Path et au-delà, avec une survie par le bouclier.

## Pistes envisagées

| Piste | Pièce clé | Point fort | Point faible |
|---|---|---|---|
| A (retenue) | Gaseous Quake + Roar (Helminth) | Dégâts quasi illimités après 10 s, invulnérable pendant la canalisation | Immobile, a besoin de ligne de vue |
| B | Gaseous Quake + Nourish (Helminth) | Énergie x2,1 sur les orbes et sources | Environ 35 % de dégâts en moins que Roar |
| C | Sonar + arme, Roar | Mobile, Sonar x9,15 sur les points faibles | Dépend entièrement de l'arme |

## Build (piste A)

| Emplacement | Choix | Rôle dans la boucle |
|---|---|---|
| Aura | Brief Respite | 150 % de l'énergie dépensée devient du bouclier |
| Exilus | Power Drift | +15 % de puissance |
| Mod 1 | Gaseous Quake | Le nuke |
| Mod 2 | Primed Flow | Réserve de 755 : deux cycles de 10 s |
| Mod 3 | Primed Continuity | Réduit le drain de la canalisation |
| Mod 4 | Umbral Intensify | Puissance |
| Mod 5 | Augur Secrets | Puissance + set Augur |
| Mod 6 | Augur Message | Durée + set Augur |
| Mod 7 | Augur Reach | Portée + set Augur |
| Mod 8 | Stretch | Portée |
| Arcanes | Arcane Energize, Molt Augmented | Énergie ; puissance qui monte avec les kills |
| Helminth | Roar (de Rhino), à la place de Silence | Bonus de dégâts de faction, compté deux fois sur les statuts Gaz |
| Focus | Zenurik | Source d'énergie |

Totaux [calcul] : puissance 183 %, durée 179 %, portée 175 %, efficacité 100 %. Capacité 67, coût des 8 mods 61, 1 forma au minimum.

## Chiffres clés [calcul]

- Sonic Boom : 70 % x 1,83 = retrait d'armure **total** dans un cône de 26 m.
- Sonar : multiplicateur x9,15 sur les points faibles (5 x 1,83), portée 61 m, 54 s. Les nuages de Gaz de Gaseous Quake peuvent toucher ces points faibles (wiki).
- Roar subsumé : 30 % x 1,83 = +55 % de bonus de faction, compté deux fois sur les dégâts des statuts.
- Gaseous Quake : zone de 35 m. Multiplicateur 157x à 5 s, 1 189x à 7 s, 24 736x (plafond) à 10 s, soit environ 9 millions de dégâts Gaz par seconde à 10 s, hors statuts et hors Roar.
- Coût d'un cycle : 189 à 5 s, 247 à 7 s, 387 à 10 s, pour une réserve de 755.
- Bouclier : 120 % (set Augur à 3 pièces) + 150 % (Brief Respite) = 270 % de l'énergie dépensée. Un cycle de 10 s rend environ 1 045 de bouclier.

## Boucle de jeu

1. Sonic Boom sur le groupe (armure retirée), puis Sonar.
2. Roar avant de canaliser.
3. Gaseous Quake : 5 s en contenu normal, 10 s au level cap. La zone reste 6,25 s après l'arrêt avec le multiplicateur atteint.
4. Relâcher, se replacer, relancer.

## Survie

- Invulnérable pendant la canalisation.
- Chaque cycle rend du bouclier puis des surboucliers ; shield gate de 1,37 s à bouclier plein.
- Les ennemis dans la zone sont staggerés à chaque impulsion.
- Point de rupture : entre deux canalisations, avec 135 d'armure. Alternative : Augur Accord à la place de Stretch (bouclier 629, shield gate 1,80 s, 4e pièce Augur) au prix de la portée (130 %, zone de 26 m).

## Alternatives chiffrées

- **Blind Rage à la place d'Augur Secrets** : puissance 258 % (+41 % de dégâts), mais efficacité 45 % : un cycle de 10 s coûte 600 au lieu de 387, une seule canalisation complète par réserve, et une pièce Augur en moins. Non retenu : au plafond de 10 s les dégâts sont déjà énormes, l'énergie est le vrai goulot.
- **Molt Efficiency à la place de Molt Augmented** : +36 % de durée tant que les boucliers sont actifs, ce qui réduit le drain ; à préférer si l'énergie manque.
- **Nourish à la place de Roar** (piste B) : énergie x2,1, si Zenurik et Energize ne suffisent pas.

## À vérifier en jeu

- Le bouclier au rang 30 (370 supposé) et les valeurs exactes dans l'arsenal.
- Si 5 s suffisent en Steel Path et combien de secondes il faut au level cap.
- Armes et compagnon : non choisis, selon l'arsenal du joueur. Rôle attendu : une arme qui gère les cibles hors de la ligne de vue ou les Nullifiers, un compagnon qui ramasse les orbes.
