# Farm : principes, méthode de réponse et limites

Source : tables de drop officielles (WFCD warframe-drop-data, version du 24/10/2026) et pages du wiki importées le 13/11/2026 (dossier 02-wiki/farm). Tout ce qui est marqué [connaissance générale] n'est pas dans la base et doit être vérifié.

## 1. Où chercher dans la base

- Un mod, un arcane, une ressource, un plan : fichiers « Farm - mods », « Farm - arcanes », « Farm - ressources », « Farm - plans », « Farm - autres » (classés par ordre alphabétique, plusieurs fichiers par catégorie).
- Mod absent des fichiers « Farm - mods » : voir « Farm - mods sans table de drop » (Primed chez Baro Ki'Teer, Galvanized chez le vendeur des Arbitrations, mods Archon chez Chipper, etc.).
- Fragments d'Archonte : page « Archon Shard » (02-wiki/systemes) section Acquisition, et « Archon Hunt ».
- Mécaniques : 02-wiki/farm (Rotation, Void Relic, Void Fissure, Baro Ki'Teer, Primed Mods, Temporal Archimedea, Deep Archimedea, Arbitrations, Bounty, Nightwave, Syndicate, Endo, Kuva, Ayatan, Steel Path, boosters).

## 2. Lire les taux

- **Ennemi** : le taux affiché est la chance d'obtenir l'objet en tuant un ennemi (déjà multiplié par le taux de drop de l'ennemi). Exemple : Organ Shatter, Terra Jackal, 7,59 % par ennemi tué.
- **Attention à l'étiquette « Ennemis »** dans les fichiers de farm : elle regroupe aussi des récompenses d'activités qui ne sont pas des ennemis (Deep et Temporal Archimedea, coffres des Netracells, Descendia, coffres de l'Icebind, Arbitration Shield Drone, etc.). Un nom qui ne ressemble pas à un ennemi est une activité ou un coffre : le taux est alors celui du tirage dans cette récompense.
- **Mission** : le taux est celui de l'objet dans la table de la rotation indiquée (A, B, C), tiré à chaque récompense de cette rotation. Dans une mission sans fin, les tables A, B, C tournent à intervalles fixes (ex. Survie : récompense A aux minutes 5 et 10, B à la minute 15, selon le wiki « Rotation ») ; pour les caches et les vaults de Spy, la rotation dépend du numéro. Pour les bounties, une rotation dure 150 minutes pour tous les bounties multi-étapes.
- **Relique** : la liste donne les reliques qui contiennent l'objet (état Intact). Raffiner augmente la chance des raretés élevées. La base ne dit pas si une relique est « vaulted » (retirée) : le vérifier.
- **Boosters** : d'après le wiki « Rotation », les boosters de ressources, de drop et de mods, le charme du Kavat Smeeta, le Steel Path et la True Master's Font n'ont **aucun effet sur les récompenses de rotation**. Ils jouent sur les drops d'ennemis et de ramassage en mission (le wiki « Neurodes » précise que les boosters ne s'appliquent pas aux récompenses de fin de mission ni de bounty).

## 3. Méthode pour répondre à « où farmer X ? » (toujours comparer)

1. Trouver X dans les fichiers de farm. Si X n'y est pas, dire que la base n'a pas de table de drop pour lui, lister les familles possibles (vendeur, Baro, Arbitrations, quête, événement) et renvoyer au wiki, sans inventer.
2. Identifier le type de source : ennemi, récompense de mission, relique, vendeur, fragment d'Archimedea, etc.
3. Pour les **ennemis** : comparer les 3 à 5 meilleures sources par taux par kill **et** par facilité de les rencontrer (zone ouverte ou mission, présence de l'ennemi en nombre, niveau requis, accès : Steel Path, planète débloquée, réputation).
4. Pour les **missions** : comparer par taux dans la rotation, en tenant compte de la durée pour atteindre la rotation (une rotation A n'arrive pas à la même vitesse qu'une rotation C) et de la mission (endurance, simple, boss).
5. Calculer le nombre de tirages attendus : nombre de tirages pour 50 % de réussite = ln(0,5) / ln(1 - c) et pour 90 % = ln(0,1) / ln(1 - c), où c est la chance d'un tirage (ex. c = 7,59 % donne environ 9 ennemis tués pour 50 %). Dire que c'est un calcul.
6. Donner **au moins deux options**, avec l'avantage et le coût de chacune, et laisser le joueur choisir. Préciser ce qui est calculé et ce qui est estimation (vitesse du farm).
7. Dire la date des tables (24/10/2026) : si une mise à jour majeure est sortie depuis (voir 03-patch-notes), avertir que les taux ont pu changer.

## 4. Limites connues (à dire au joueur, ne pas contourner)

- La **vitesse** d'un farm (kills par minute, durée d'une mission) n'est pas dans les tables : tout classement « le plus rapide » est une estimation, à étiqueter comme telle et à corriger par les retours du joueur (04-retours-experience).
- Les **inventaires de vendeurs** (Baro Ki'Teer, Teshin, syndicats, Arbitrations) et les **événements** changent : la base donne la logique et les prix de référence du wiki, pas l'inventaire du jour.
- Les **récompenses d'Archimedea, de Netracells, de Nightwave** et les sources par réputation sont décrites dans les pages du wiki importées, pas dans les tables de drop.
- **Où trouver un ennemi** : les tables donnent le nom de l'ennemi (Raptor, Jackal, Terra Jackal, etc.) mais pas sa zone ni sa faction. La base n'a pas de table « ennemi → lieu » : si le joueur ne sait pas où trouver l'ennemi, l'agent doit le dire plutôt que deviner, et chercher la page de l'ennemi sur le wiki.
- **Disponibilité dans le temps** : des offres liées à un événement (ex. la boutique Praghasa de l'opération Taubound, 375 Moonflesh par fragment tauforgé, d'après la page « Archon Shard ») peuvent être terminées : la base ne dit pas si elles sont actives. Le signaler.
- Pour un objet absent des tables de drop, ne jamais deviner la source.
