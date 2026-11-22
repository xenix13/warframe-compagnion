# Coûts des capacités, capacités canalisées et ressources spéciales (toutes les warframes)

Source : pages Abilities du wiki, relevées automatiquement le 13/11/2026 pour 68 warframes et Necramechs. Relevé automatique : en cas de doute, la page de la capacité fait foi. Les mêmes données sont dans `01-donnees/couts-capacites.json`, que les outils de l'agent lisent.

## Comment lire les coûts (XeniX13, 13/11/2026, et wiki)

- **Coût fixe** : chaque capacité a son coût propre. Coût réel = coût de base x (2 - efficacité), au minimum 25 % du coût de base. Il ne dépend pas de l'énergie max.
- **Capacité canalisée** : elle coûte de l'énergie tant qu'on la maintient (« +X/s »). Drain réel par seconde = X x (2 - efficacité) / durée.
- **Coût croissant** : certaines coûtent de plus en plus cher avec le temps (« +20-40/s », ou Sound Quake avec Gaseous Quake : voir `capacites-canalisees.json`). On les utilise par courtes périodes puis on les relance, pour ne pas vider la jauge.
- **Coût par action** : par tir, par ennemi, par cadavre, etc. (« +15/shot », « +10/corpse »).

## Warframes sans énergie ou avec une ressource propre

- **Baruuk** (énergie + jauge de Retenue (Restraint)) : Baruuk a de l'énergie pour ses capacités 1 à 3, mais son 4 (Serene Storm) n'en utilise pas : il se lance et se maintient avec la jauge de Retenue (Restraint). La jauge démarre pleine et doit être vidée pour utiliser le 4 : chaque attaque esquivée par Elude en retire 1,2 %, chaque ennemi touché par Lull 0,8 %, chaque ennemi désarmé par Desolate Hands 1,6 %. Serene Storm la remplit de 4 % à l'activation puis de 0,8 % par seconde. Jauge entièrement vidée : jusqu'à 50 % de réduction de dégâts.
- **Hildryn** (boucliers) : Hildryn n'a pas d'énergie : ses capacités consomment ses boucliers et surboucliers. L'efficacité réduit ces coûts en bouclier. Les orbes d'énergie lui rendent 25 de bouclier et relancent la recharge ; Equilibrium et Energy Conversion fonctionnent, mais Arcane Energize n'a aucun effet et Brief Respite ou le set Augur ne lui rendent pas de bouclier. Son shield gate dure 3,5 s à bouclier plein. Les nombres ci-dessous sont des coûts en bouclier.
- **Lavos** (temps de recharge) : Lavos n'a pas d'énergie et ses capacités ne consomment aucune ressource : elles sont gratuites, avec un temps de recharge entre deux utilisations. L'efficacité ne réduit pas un coût : elle joue sur la réduction de recharge donnée par Transmutation Probe et par l'augment Swift Bite. Une capacité Helminth sur Lavos coûte 0 énergie mais a 10 s de recharge. Les nombres ci-dessous sont des temps de recharge en secondes.

D'autres frames ont une jauge ou un compteur propre décrit dans leur passif (Atlas, Ember, Garuda, Gauss, Inaros, Nidus, Sevagoth, Temple, Uriel, Valkyr...) : voir le passif de chaque frame ci-dessous.

## Capacités canalisées ou à coût dans le temps (liste)

- **Ash**, 4 Blade Storm : 0 +6-12/mark
- **Baruuk**, 1 Elude : 25 +2.5/s
- **Bonewidow**, 4 Exalted Ironbride : 50 +2.5/s
- **Chroma**, 1 Spectral Scream : 10 +3/s
- **Chroma**, 4 Effigy : 50 +10/s
- **Cyte-09**, 4 Neutralize : 5 +10/shot +20/alt fire
- **Dante**, 1 Noctua : 5 +2/shot
- **Ember**, 2 Immolation : 50 +when at max heat: +1t/s-2 t = time at max heat in seconds
- **Ember**, 4 Inferno : 0 +10/enemy (max 10x)
- **Equinox**, 3 Pacify & Provoke : 10 +0.5/s/enemy +3/ability
- **Equinox**, 4 Mend & Maim : 50 +3.5/s
- **Excalibur**, 4 Exalted Blade : 25 +2.5/s +25/slide
- **Gara**, 4 Mass Vitrify : 75 +3-5/s
- **Gauss**, 1 Mach Rush : 15 +12.5/s
- **Hildryn**, 1 Balefire : 50 +100/shot +200/charge shot (coûts en bouclier)
- **Hildryn**, 3 Haven : 250 +5/s/ally +25/s/enemy (coûts en bouclier)
- **Hildryn**, 4 Aegis Storm : 100 +25/s +25/s/enemy +50/dodge (coûts en bouclier)
- **Ivara**, 2 Navigator : 25 +3/s +2/s2
- **Ivara**, 3 Prowl : 25 +1-3/s
- **Ivara**, 4 Artemis Bow : 50 +15/shot
- **Jade**, 4 Glory On High : 25 +5/s +25/alt fire
- **Mesa**, 4 Peacemaker : 25 +15/s
- **Mirage**, 4 Prism : 50 +10/s
- **Nekros**, 3 Desecrate : 10 +10/corpse
- **Oberon**, 3 Renewal : 25 +3.5/s
- **Oraxia**, 4 Silken Stride : 25 +5/s
- **Revenant**, 4 Danse Macabre : 25 +20-40/s
- **Sevagoth**, 3 Gloom : 50 +.75-7.5/s
- **Titania**, 4 Razorwing : 25 +5/s
- **Valkyr**, 4 Hysteria : 25 +5/s
- **Voidrig**, 4 Guard Mode : 50 +5/s
- **Wisp**, 4 Sol Gate : 25 +12-24/s
- **Wukong**, 4 Primal Fury : 10 +5/s
- **Zephyr**, 1 Tail Wind : 25 -12.5 (airborne) +5/s hovering

## Détail par warframe

### Ash

- Ressource : énergie
- Coûts : 1 Shuriken = 25 ; 2 Smoke Screen = 35 ; 3 Teleport = 25 ; 4 Blade Storm = 0 +6-12/mark
- Passif (wiki) : Slash procs inflicted by Ash's weapons and abilities deal 25% more damage and last 50% longer. - Damage bonus stacks additively with other Status Damage.   - For example, when using Ash, a weapon that deals 100 damage with Bane of Grineer will have a Slash proc that deals (100 * (1 + 0.3)) * 0.35 * (1 + 0.3) * (1 + 0.25) = 73.94 damage per tick. - Bleed duration bonus stacks additively with status duration mods such as Lingering Torment. - Works in Archwing missions. Note that Railjack Slash status effect Tear has a base 20s duration and is not a DoT.
  - Blade Storm : - Ash toggles a state of intense focus as he searches for targets to assassinate. During targeting mode, enemies within 50 meters from Ash that are seen near the aiming reticle become highlighted and tagged with a death mark above their head, consuming 12 energy per enemy.
  - Blade Storm : - Reactivating Blade Storm with no marks will toggle off targeting mode instead.

### Atlas

- Ressource : énergie
- Coûts : 1 Landslide = 25 ; 2 Tectonics = 50 ; 3 Petrify = 75 ; 4 Rumblers = 100
- Passif (wiki) : Wielding explosive power and incredible stamina, Atlas strengthens his insurmountable durability through battle. Atlas possesses various passive mechanics highlighted in the tabs below: Strong as the mountain, Atlas is immune to Knockdown while in contact with the ground. - Knockdown immunity does not apply while in the air. - Does not apply to pushback effects. - Does not prevent the recoiling effect from firing powerful Archguns such as Corvas, Velocitus, and Larkspur in non-Archwing missions. - Works in Archwing missions. Rubble is a pickup item unique to Atlas that drops from petrified ene

### Banshee

- Ressource : énergie
- Coûts : 1 Sonic Boom = 25 ; 2 Sonar = 50 ; 3 Silence = 75 ; 4 Sound Quake = 75
- Passif (wiki) : All of Banshee's abilities inflict 5 Puncture Status Effects to all enemies within 20 meters of her. Additionally, all of her equipped weapons, including Gunblades such as Redeemer, and weapons equipped on Sentinels should they be present, are treated as silent.

### Baruuk

- Ressource : énergie + jauge de Retenue (Restraint). Baruuk a de l'énergie pour ses capacités 1 à 3, mais son 4 (Serene Storm) n'en utilise pas : il se lance et se maintient avec la jauge de Retenue (Restraint). La jauge démarre pleine et doit être vidée pour utiliser le 4 : chaque attaque esquivée par Elude en retire 1,2 %, chaque ennemi touché par Lull 0,8 %, chaque ennemi désarmé par Desolate Hands 1,6 %. Serene Storm la remplit de 4 % à l'activation puis de 0,8 % par seconde. Jauge entièrement vidée : jusqu'à 50 % de réduction de dégâts.
- Coûts : 1 Elude = 25 +2.5/s ; 2 Lull = 50 ; 3 Desolate Hands = 75 ; 4 Serene Storm = pas de coût en énergie
- Passif (wiki) : Baruuk's tolerance for violence wanes as his hand is forced by his foes. Restraint is a resource unique to Baruuk that provides up to 50% Damage Reduction when the meter is completely depleted. - Restraint meter is displayed in the lower-right on the HUD, above the ability icons. - Restraint meter starts fully filled, and is depleted using Baruuk's abilities:   - Each attack evaded through Elude erodes 1.2% from the meter.   - Each enemy affected by Lull erodes 0.8% from the meter.   - Each enemy disarmed by Desolate Hands erodes 1.6% from the meter. - Baruuk's fourth ability Serene Storm util
  - Elude : | 1 25 +2.5/s | Elude Dodge all incoming projectiles, but only while not attacking. Use again to deactivate this ability. Introduced in Update 24.2 (2018-12-18) | Strength:N/A
  - Elude : Misc: 100% (dodge chance) 0.2 s (reactive delay) 1.2% (Restraint erosion per attack dodged)
  - Serene Storm : | 4 | Serene Storm With his Restraint eroded, Baruuk commands the Desert Wind to deliver powerful radial strikes with his fists and feet. Each moment commanding the storm restores his Restraint. Introduced in Update 24.2 (2018-12-18) | Strength:100 / 125 / 200 / 250 ( Impact damage) 10% / 15% / 20% / 25% (damage reduction)
  - Serene Storm : - Baruuk foregoes his restraints to empower his fists with volatile energies, commanding the Desert Wind and wielding it as his melee Exalted Weapon. While Serene Storm is active, Baruuk also receives 10% / 15% / 20% / 25% Damage Reduction against enemy attacks, and slows enemies within a 3 meter radius by 50%.

### Bonewidow

- Ressource : énergie
- Coûts : 1 Meathook = 25 ; 2 Shield Maiden = 25 ; 3 Firing Line = 50 ; 4 Exalted Ironbride = 50 +2.5/s
  - Exalted Ironbride : - Exalted Ironbride drains 2.5 energy per second and will remain active until Bonewidow's energy is depleted or the ability is deactivated by pressing the ability key again.

### Caliban

- Ressource : énergie
- Coûts : 1 Razor Gyre = 25 ; 2 Sentient Wrath = 50 ; 3 Lethal Progeny = 50 ; 4 Fusion Strike = 100
- Passif (wiki) : Versatile and resilient, Caliban and allies within his Affinity Range gain Adaptive Armor that builds damage resistance against the highest damage type received from enemy attacks, stacking 5% per hit up to a cap of 50%. If Caliban or his allies do not receive damage for 5 seconds, their Adaptive Armor loses 2% per second until fully removed. - Passive bonus value is displayed as a Buff icon beside Caliban's hitpoint indicators.   - Impact, Puncture, Slash, Cold, Electricity, Heat, Toxin, Blast, Corrosive, Magnetic, Radiation, Viral, and Tau damage types stack their respective resistances sepa

### Chroma

- Ressource : énergie
- Coûts : 1 Spectral Scream = 10 +3/s ; 2 Elemental Ward = 50 ; 3 Vex Armor = 75 ; 4 Effigy = 50 +10/s
- Passif (wiki) : It's taking longer than I calculated. Find out if we can reupload the imgur reference images to the wiki for posterity Chroma possesses an extra midair jump and bullet jump. Wings matching Chroma's energy colors will form during these maneuvers. Chroma can alter his abilities to match any basic (uncombined) elemental attribute of the player's choice. Customizing Chroma's primary emission color determines what abilities he starts with. Color choices are grouped into four categories with each category corresponding to a given element: - red, magenta, brown, orange and bright yellow hues being He
  - Spectral Scream : - Hold down the ability key (default 1 ) to expend 10 Energy to activate Spectral Scream. While active, Chroma holsters his weapons away and continuously exhales elemental energy in a cone 4 / 5 / 6.5 / 10 meters long that inflicts 200 / 250 / 300 / 400 Heat, Electricity, Toxin, or Cold damage per second with a 100% status chanc
  - Spectral Scream : - Spectral Scream consumes 3 energy per second while active and will remain active until Chroma's energy is depleted or the ability is deactivated by pressing the ability key again.
  - Effigy : - Effigy drains 10 energy per second while active and will remain active until Chroma's energy is depleted, the sentry's health is depleted, or the ability is deactivated by pressing the ability key again.
  - Effigy : - When deactivated, Chroma can teleport his pelt from anywhere onto himself. This will stop movement and interrupt any action Chroma is doing, such as reloading, leaving a player vulnerable.

### Citrine

- Ressource : énergie
- Coûts : 1 Fractured Blast = 25 ; 2 Preserving Shell = 50 ; 3 Prismatic Gem = 75 ; 4 Crystallize = 100
- Passif (wiki) : Citrine emits a healing aura within a radius of 50 meters, granting the Geoluminesence buff to herself and allies that continuously recover a base 5 Health points per second. Whenever she picks up a regular Health Orb, Dispensary produced Empowered variant, or Universal Orb, regeneration rate is permanently increased by 0.1 points, up to a maximum heal rate of 25 points per second after collecting 200 Health Orbs. - Until her passive reach max stacks, Citrine innately can always collect Health Orbs to increase her passive healing even when unharmed. - Allies gain or lose Geoluminesence wheneve

### Cyte-09

- Ressource : énergie
- Coûts : 1 Seek = 25 ; 2 Resupply = 50 ; 3 Evade = 75 ; 4 Neutralize = 5 +10/shot +20/alt fire
- Passif (wiki) : Cyte-09 gains Practiced Aim when he kills an enemy by damaging their Weak Points, increasing his Critical Chance against weak points by 1% up to a maximum of 300%, lasting for the entirety of a mission. - Critical chance bonus is additive to similar mods such as Point Strike. - Additional critical chance from Cyte-09's passive can raise the Critical Tier of his equipped weapon.

### Dagath

- Ressource : énergie
- Coûts : 1 Wyrd Scythes = 25 ; 2 Doom = 50 ; 3 Grave Spirit = 75 ; 4 Rakhali's Cavalry = 100
- Passif (wiki) : Dagath feeds from the souls of the deceased, granting her a 35% chance to activate Abundant Abyss when picking up Health Orbs or Energy Orbs to increase their effective yield by +300%. The passive has no cooldown and can activate on each orb collected. - This applies to:   - Health Orbs — 50 health becomes 200 health   - Dispensary's Empowered Health Orbs — 100 health becomes 400 health   - Small Energy Orbs — 25 energy becomes 100 energy   - Large Energy Orbs — 50 energy becomes 200 energy   - Universal Orbs — 25 health and 25 energy becomes 100 health and 100 energy     - Note that when pick

### Dante

- Ressource : énergie
- Coûts : 1 Noctua = 5 +2/shot ; 2 Light Verse = 25 ; 3 Dark Verse = 25 ; 4 Final Verse = 50
- Passif (wiki) : Enemies slain by Noctua's primary fire, page fragments, and alt-fire are scanned into the Codex upon death, with each enemy death recording 1 scan entry. Enemy types with completed Codex research become permanently debuffed with Chronicler's Mark, which grants Dante's equipped weapons, including the Noctua itself, and Final Verse's Wordwarden Noctua copies an extra 50% Status Chance versus these foes. - Status chance bonus is multiplicative to a weapon's total status chance after mods and other bonuses are applied.   - For example, Noctua with Scorch equipped will have 40% status chance, or 40
  - Noctua : - Dante expends 5 energy to equip his Exalted Weapon tome sidearm, the Noctua, replacing his equipped secondary weapon. Press the ability key again (default 1 ) to deactivate and return his secondary weapon to the swap weapon cycle (default F ).
  - Noctua : - Casting and deactivating Noctua are full-body animations that allow uninterrupted movement and parkour Maneuvers.

### Ember

- Ressource : énergie
- Coûts : 1 Fireball = 25 ; 2 Immolation = 50 +when at max heat: +1t/s-2 t = time at max heat in seconds ; 3 Fire Blast = 75 ; 4 Inferno = 0 +10/enemy (max 10x)
- Passif (wiki) : Reveling in the heat of combat, Ember gains 5% extra Ability Strength for every enemy burning with an active Heat status effect within Affinity Range. - Buff values appear above Immolation's heat gauge. - Works in Archwing missions.
  - Immolation : - Ember expends 50 Energy to surround herself in a swirling torrent of protective flame that burns stronger with each moment. While immolated, a thermometer appears above the ability icons, gradually rising in temperature. Ember gains 10% / 20% / 30% / 40% Damage Reduction on cast displayed as a percent (%) next to the thermomet
  - Immolation : - Once Immolation reaches maximum heat, Ember drains energy at an increasing rate of 0.4 energy per second to sustain Immolation. The energy drain growth is uncapped.

### Equinox

- Ressource : énergie
- Coûts : 1 Metamorphosis = 25 ; 2 Rest & Rage = 25 ; 3 Pacify & Provoke = 10 +0.5/s/enemy +3/ability ; 4 Mend & Maim = 50 +3.5/s
- Passif (wiki) : When Equinox collects Health Orbs or Energy Orbs, 10% of the restored amount is converted into additional Energy and Health respectively. - Equinox's passive stacks additively with Equilibrium, for a total conversion of 120%. - Allows for the pickup of orbs while the associated resource pool is full, for the purpose of conversion. - The effect of Arcane Pulse does not apply to health from converted energy orbs. - The effects of Arcane Energize and Energy Pulse do not apply to energy from converted health orbs. - Works in Archwing missions. Equinox can shift between two forms to alter her abili
  - Pacify & Provoke : - Equinox emits a crippling or empowering aura with a radius of 10 / 12 / 14 / 16 meters. Pacify & Provoke will remain active indefinitely until deactivated by casting Metamorphosis, by running out of Energy, or by pressing the ability key again (default 3 ).
  - Pacify & Provoke : - Despite being a channeled ability, this does not interrupt energy regeneration from Energy Siphon, Energy Nexus, Dreamer's Bond, Wellspring and is not affected by Ability Duration.
  - Mend & Maim : | 4 50 +3.5/s | Mend & Maim In Night-Form, allies' Shields are replenished with each nearby enemy killed. In Day-Form, enemies are inflicted with Slash Status Effect. Deactivate while in Night-Form to restore Health and Shields for Equinox and allies. Deactivate while in Day-Form to cast a wave of slashing force. Introduced in U
  - Mend & Maim : Strength: 10 / 15 / 20 / 25 (shields per kill)

### Excalibur

- Ressource : énergie
- Coûts : 1 Slash Dash = 25 ; 2 Radial Howl = 50 ; 2 Radial Blind = 50 ; 3 Radial Javelin = 75 ; 4 Exalted Blade = 25 +2.5/s +25/slide
- Passif (wiki) : Excalibur and Excalibur Prime has improved mastery in the Tenno art of the blade, receiving +10% Attack Speed and +10% damage bonuses for melee attacks while wielding the following weapons: - Swords, such as the Skana. - Dual Swords, such as the Dual Skana. - Nikana (Weapon Type), such as the Dragon Nikana. - Rapiers, such as the Destreza. - Exalted Blade - Bonuses are additive to mods such as Pressure Point and Fury. Excalibur Umbra exhibits sentience, allowing him to remain active in combat even when a player uses Operator form, acting similarly to a Specter. - Umbra can receive damage and h
  - Exalted Blade : - Performing a slide attack will also drain 25 energy to cast a Judged Severance, a diminished version of Radial Blind that Blinds and Stuns enemies within 5m for 6 seconds, as well as disabling security cameras.
  - Exalted Blade : - Exalted Blade consumes 2.5 energy per second while active and will remain active until Excalibur's energy is depleted or the ability is deactivated by pressing the ability key again.

### Follie

- Ressource : énergie
- Coûts : 1 Forced Perspective = 15 ; 2 Shadowgraph = 25 ; 3 Self Portrait = 50 ; 4 Plein Air = 75
- Passif (wiki) : Follie's abilities splatter thick viscous Inkblot onto enemies, applying a 50% Slow for 10 seconds. While coated in ink, slain foes have a 20% chance to congeal an ink balloon that pops, dropping a random mixture of 3 Health Orbs and Energy Orbs. - Affects Overguard protected enemies. - Is not dismissed by Nullifier fields. - Ability Synergy:   - Self Portrait and Plein Air apply Inkblot and pause its duration on affected enemies, until they leave the ink effigy's ink pool or detach from the ink balloon.   - Follie's signature Enkaus splatter an Inkblot glob on its alternate fire mode and can 

### Frost

- Ressource : énergie
- Coûts : 1 Freeze = 25 ; 2 Ice Wave = 50 ; 3 Snow Globe = 50 ; 4 Avalanche = 100
- Passif (wiki) : Frost's abilities have their Cold status effect duration increased by 100%. Frost's Fortifying Freeze passive increases his Armor by 50 per enemy afflicted by a Cold status effect within Affinity Range. - The armor buff works in Archwing missions. - Main article: Biting Frost Biting Frost is a Warframe Augment Mod for Frost's passive, gaining increased Critical Chance and Critical Damage on enemies frozen by 10 Cold status effects. Rank | Crit Chance | Crit Damage | Cost 0 | +130% | +130% | 6 1 | +150% | +150% | 7 2 | +175% | +175% | 8 3 | +200% | +200% | 9

### Gara

- Ressource : énergie
- Coûts : 1 Shattered Lash = 25 ; 2 Splinter Storm = 50 ; 3 Spectrorage = 75 ; 4 Mass Vitrify = 75 +3-5/s
- Passif (wiki) : When casting an ability, Gara's glass body has 15% chance to Blind enemies within 12 meters for 10 seconds, exposing them to Melee Finisher attacks. Blind chance increases by 20% until the blind triggers. - Can affect enemies with Overguard. - Can affect enemies inside a Nullifier Bubble. - Enemies must be within Line of Sight of Gara to be blinded, but do not have to face toward Gara. - Can refresh blind duration on currently blinded enemies when the passive procs again. - Affects enemies crystallized by Mass Vitrify. - Melee finisher damage benefits from the damage multipliers of Splinter St
  - Mass Vitrify : - Gara expends 75 Energy and coats herself in a shell of hardened glass, becoming immobile and Invulnerable to damage as she unleashes a radial ring of molten glass that expands outward and downward. The molten glass ring's initial horizontal radius from Gara is 2 meters, which expands horizontally at a rate of 3 meters per seco
  - Mass Vitrify : - Can be recast while active to expand molten glass and create a new barrier. Only 1 barrier may remain active per player.

### Garuda

- Ressource : énergie
- Coûts : 1 Dread Mirror = 25 ; 2 Blood Altar = 50 ; 3 Bloodletting = pas de coût en énergie ; 4 Seeking Talons = 100
- Passif (wiki) : The more Garuda kills, the more vicious her attacks become; Garuda gains 5% additional Weapon Damage and Melee Damage for each kill or assisted kill, up to a maximum of 100%, which begins to slowly decay after 5s. - Damage bonus is multiplicative to all other damage multipliers, such as Eclipse and Minelayer (Overdriver), and faction damage bonuses, such as Bane of Grineer and Roar. - Damage bonus is a Universal Weapon Bonus, which allows it to affect certain abilities. Check the Universal Weapon Bonuses page for a list of affected abilities.   - Of the abilities in Garuda's kit, Dread Mirror'
  - Bloodletting : - Bloodletting is a powerful ability to combine with Helminth-infused toggled abilities that constantly drain energy, the most notable being Sevagoth's Gloom as it provides Garuda with another self-healing ability besides Blood Altar to constantly regenerate her energy reserves.

### Gauss

- Ressource : énergie
- Coûts : 1 Mach Rush = 15 +12.5/s ; 2 Kinetic Plating = 50 ; 3 Thermal Sunder = 50 ; 4 Redline = 100
- Passif (wiki) : To achieve supersonic speed, Gauss draws upon both his Energy reserves and his state-of-the-art electrokinetic battery to fuel his abilities. Gauss has access to 80% of the battery in his default state; activating Redline grants access to 100% of the battery. The battery, displayed as a gauge meter above his ability icons, acts as a secondary resource that charges or drains depending on the ability he uses: Passive - +0.66% battery per meter that Gauss moves. - +?% battery per second while reviving an ally in Bleedout. - -3% battery if Gauss falls Out of Bounds. - -15% battery per second if Ga
  - Mach Rush : - Mach Rush consumes 12.5 energy per second while active and will remain active until Gauss's energy is depleted or he stops sprinting by releasing the ability key.
  - Mach Rush : - Mach Rush's energy drain is not converted into shields by Augur Mods.

### Grendel

- Ressource : énergie
- Coûts : 1 Feast = 25 ; 2 Nourish = 50 ; 3 Pulverize = pas de coût en énergie ; 4 Regurgitate = pas de coût en énergie
- Passif (wiki) : Devouring his prey whole, Grendel slowly digests the enemies he swallows via Feast. Each enemy still alive in Grendel's belly passively grants him 250 Armor, to a maximum of 1,250 bonus armor at the 5 enemy cap. - Passive bonus value is displayed above Grendel's ability icons. - Gourmand provides an additional 150 armor bonus per enemy at max rank to Grendel's passive, increasing the armor bonus to 400 per enemy and the total armor bonus to 2,000 at enemy cap. - Armor bonus is added after armor mods such as Steel Fiber. For example, Grendel with a rank 10 Steel Fiber and one enemy alive in his
  - Pulverize : - Grendel consumes 0 energy to curl up into a roving sphere that changes his movement controls into a directional physics-based roll. As he roves, Grendel gorges upon enemies inside his stomach, inflicting 25 Toxin damage per second while healing him 50 / 100 / 150 / 200 health per second over 5 seconds which slowly diminishes t
  - Pulverize : - Pulverize consumes 3 energy per second on an empty stomach while active and will remain active until Grendel's energy is depleted or the ability is deactivated by pressing the ability key again. Should Grendel run out of energy during Pulverize, he will automatically unfurl and become stunned in a dizziness animation for 2 sec

### Gyre

- Ressource : énergie
- Coûts : 1 Arcsphere = 25 ; 2 Coil Horizon = 50 ; 3 Cathode Grace = 75 ; 4 Rotorswell = 100
- Passif (wiki) : Gyre's abilities gain a flat 10% Critical Chance per active Electricity status proc affecting an individual enemy to deal 2.0x Critical Damage against that enemy. - Bonus stacks additively with Cathode Grace, increasing the overall ability critical chance at lower Electricity status stack counts. - Passive and Cathode Grace combined provide up to a maximum of 300% ability critical chance.   - From the passive alone, a minimum of 30 Electricity procs will reach the capped ability critical chance. - Gyre's abilities can reach orange and red critical multipliers to inflict 3.0x and 4.0x ability c

### Harrow

- Ressource : énergie
- Coûts : 1 Condemn = 25 ; 2 Penance = 50 ; 3 Thurible = 25 ; 4 Covenant = 100
- Passif (wiki) : Harrow possesses 200% Overshields capacity, granting him a maximum of 2,400 Overshields, and spawns into missions with 100% Energy filled, identical to how the mod Preparation works. - Works in Archwing missions.

### Hildryn

- Ressource : boucliers. Hildryn n'a pas d'énergie : ses capacités consomment ses boucliers et surboucliers. L'efficacité réduit ces coûts en bouclier. Les orbes d'énergie lui rendent 25 de bouclier et relancent la recharge ; Equilibrium et Energy Conversion fonctionnent, mais Arcane Energize n'a aucun effet et Brief Respite ou le set Augur ne lui rendent pas de bouclier. Son shield gate dure 3,5 s à bouclier plein. Les nombres ci-dessous sont des coûts en bouclier.
- Coûts : 1 Balefire = 50 +100/shot +200/charge shot ; 2 Pillage = 150 ; 3 Haven = 250 +5/s/ally +25/s/enemy ; 4 Aegis Storm = 100 +25/s +25/s/enemy +50/dodge
- Passif (wiki) : Hildryn utilizes her advanced Shielding systems to power all of her abilities. Although she has no Energy capacity, her shields boast additional passive benefits and defensive capabilities: - Hildryn's Shield Gating is more advanced than other Warframes, bolstering her defenses:   - Overshields protect Hildryn's Health pool from damage types that normally bypass shields to directly affect health, such as Toxin damage (e.g. Mutalist Osprey, Toxic Ancient), and Combat Discipline's health loss per kill.   - Hildryn's Shield Gating grace period is 3.5 seconds when fully charged.     - This passive
  - Balefire : - Requires shields to activate and consumes shields per shot.
  - Haven : - Hildryn expends 250 shields or overshields to overcharge her Shield Matrix to continuously link to allies and enemies alike. When targets are in her direct line of sight and within a 8 / 10 / 12 / 15 meter radius, Hildryn drains 5 Overshield/Shield points per second for every ally linked, and 25 Overshield/Shield points per se
  - Haven : - Casting Haven is a full body animation that stops Hildryn's grounded movement and other actions, while deactivating Haven does not play an animation nor stop Hildryn's actions.
  - Aegis Storm : | 4 100 +25/s +25/s/enemy +50/dodge | Aegis Storm Take the skies and rain Balefire rockets down on the enemy. Nearby enemies are blasted into the air where they will create an Energy Orb every few seconds. When shields run out the enemies are smashed into the ground. Introduced in Update 24.4 (2019-03-08) | Strength:100 / 125 / 
  - Aegis Storm : - The Operator can still be used while in Aegis Storm to do these actions without deactivating the ability.

### Hydroid

- Ressource : énergie
- Coûts : 1 Tempest Barrage = 25 ; 2 Tidal Surge = 50 ; 3 Plunder = 75 ; 4 Tentacle Swarm = 50
- Passif (wiki) : Enemies damaged by Hydroid are permanently more vulnerable to Corrosive Status, with initial status reducing armor by 50% rather than 26%, allowing Corrosive Status to reach 100% armor reduction at full stacks. As long as Hydroid has damaged the enemy, the Corrosive Status Effects can be applied from any source, not just from Hydroid's weapons or abilities, and will receive the benefit. - Works in Archwing missions. - Affected enemies are marked with a translucent water-dripping Corrosive symbol over their head, and a splashing sound is played when a new enemy is affected. The symbol color is 

### Inaros

- Ressource : énergie
- Coûts : 1 Desiccation = 25 ; 2 Sandstorm = 25 ; 3 Scarab Shell = pas de coût en énergie ; 4 Scarab Swarm = 100
- Passif (wiki) : On fatal injury and entering Bleedout, Inaros entombs himself into a Sarcophagus and incarnates as a sand version of himself, able to revive himself by melee attacking (default E ) enemies and siphoning their life force. Alternatively, allies may manually revive Inaros by interacting with his Sarcophagus. - The revive meter that appears on the reticle is filled by ?% for every melee hit.   - Attacks from Swarm Kavats spawned by Scarab Swarm also contribute to the revive meter. - The sand incarnation will only use Unarmed attacks and cannot use other weapons. - The sand incarnation does not res
  - Scarab Shell : Misc: 5% (status protection cost) ? m (charging damage radius) ? (damage per tick) Stagger on hit 2,500 HP (total health cost) 2 HP (min. health threshold) ∞ (armor bonus duration) 25 HP (health drain per percent charge) 4.67s (time to full armor bonus)
  - Scarab Shell : - The armor buildup will end once the bonus armor is fully filled, Inaros only has 2 health left, or the ability is manually deactivated.

### Ivara

- Ressource : énergie
- Coûts : 1 Quiver = 25 ; 2 Navigator = 25 +3/s +2/s2 ; 3 Prowl = 25 +1-3/s ; 4 Artemis Bow = 50 +15/shot
- Passif (wiki) : Ivara's innate enemy Radar has a larger radius, detecting enemies and displaying their position on the minimap within 50 meters rather than the usual 30 meters. - This effect stacks with (Primed) Animal Instinct, Enemy Radar, Enemy Sense, Stealth Drift, and Vigilante Pursuit, increasing her detection range to 191 meters, or more with squad members equipped with the aura Enemy Radar and/or Coaction Drift. - Works in Archwing missions, enemy detection range increases from 180 to 320 archwing meters.   - The range discrepancy exists likely because everything is minified in archwing but the passiv
  - Navigator : - Navigator consumes 25 energy when a projectile is fired after activating the ability or when Navigator takes control of a projectile in flight. It then drains 3 energy per second which increases by an additional 2 energy per second for every second a projectile is actively controlled. Navigator will end if the projectile impac
  - Navigator : - The energy drain growth accelerates the energy drain while a projectile is actively controlled. As an example, Navigator's energy drain will be equal to 3 energy per second the instant a projectile becomes influenced by the ability. If the projectile is controlled for a total of 5 seconds, the energy drain will have increased 
  - Prowl : - Ivara expends 25 energy to activate her cloak, turning Ivara and her Companion transparent, rendering them invisible to enemies. While active, Ivara gains 10% / 20% / 30% / 40% bonus damage on headshots at the cost of 0.5x Movement Speed. Ivara also becomes capable of pickpocketing enemies: if standing beside an enemy with Pro
  - Prowl : - Prowl consumes 1 point of energy per second while stationary and consumes 3 energy per second while walking or rolling. Additionally, melee attacks consume 2 energy per hit, and taking damage consumes 10 energy per hit. Prowl will end if Ivara's energy is depleted, if certain maneuvers are performed that break the cloak, or th
  - Artemis Bow : - Each shot consumes 15 energy. Artemis Bow will end if Ivara's energy falls below the energy cost per shot or if deactivated by pressing the ability key again.
  - Artemis Bow : - Artemis Bow does not have a continuous energy drain.

### Jade

- Ressource : énergie
- Coûts : 1 Light's Judgment = 25 ; 2 Symphony Of Mercy = 50 ; 3 Ophanim Eyes = 50 ; 4 Glory On High = 25 +5/s +25/alt fire
- Passif (wiki) : Where sacred light shines the song of life begins, as the shadow of time marches evermore toward deathly silence. As The Anointed, Jade possesses two passives: - Jade possesses 2 Aura mod slots in her Arsenal loadouts to assist herself and her squadmates.   - This also includes increased mod capacity from both Auras (+28 from two maxed Auras, or +32 / +36 with Steel Charge and/or Power Donation), allowing Jade more modding space with less need for Polarization, as well as granting her more potential Starting Energy. - Enemies that enter Light's Judgment well and Glory on High's primary fire at
  - Glory On High : - Has a fixed casting cooldown of 1.5 seconds, unaffected by fire rate, reload speed, or casting speed.
  - Glory On High : - Glory on High consumes 5 energy per second while active and will remain active until Jade's energy is depleted, or the ability is deactivated by pressing the ability key again.

### Khora

- Ressource : énergie
- Coûts : 1 Whipclaw = 25 ; 2 Ensnare = 50 ; 3 Venari = pas de coût en énergie ; 4 Strangledome = 100
- Passif (wiki) : - For more information on Khora's Kavat, please refer to the tabs below and visit the Venari ability article. Khora's ferocious Kavat, Venari, fights alongside her with steadfast zeal. Venari is an exclusive Companion for the Khora Warframe, integrated as her signature passive ability. Venari will spawn beside Khora when the player first enters a mission, as a permanent companion that lasts until killed. While Venari is alive, Khora passively gains a 15% movement speed boost. If Venari is killed, she will respawn beside Khora after 45 seconds, or instantly if summoned via the third ability for
  - Venari : Misc: 120 s (mark duration) 45 s (respawn time) 2.5 s (snare duration) 5 (hits per snare) 3 s (Attack & Protect cooldowns) < 90% HP (missing health threshold) 10 m (Heal aura radius) 65 s (Venari self-heal mark duration)
  - Venari : - Khora commands her loyal Kavat companion Venari to prioritize a target on the aiming reticle for 25 energy, leaving Venari's mark above the target for 120 seconds. Once commanded, Venari chases the marked target if nearby or teleports to it if far away, while refreshing the special effect for her battle posture if it is on coo

### Koumei

- Ressource : énergie
- Coûts : 1 Kumihimo = 25 ; 2 Omikuji = 50 ; 3 Omamori = 75 ; 4 Bunraku = 100
- Passif (wiki) : Dare to tempt her fate, risk all in this game of chance, soon shall she succeed. Every 1 minute, fate selects one of Koumei's equipped weapons to impart randomized Status Effects when dealing Damage for 1 minute. - Koumei's primary, secondary, or melee weapon icon with a circle timer is shown beside her five dice above her ability icons. - Can select weapon types that Koumei does not have equipped. - Has no effect on Multishot. - Works in Archwing missions but the secondary weapon buff is useless. Casting an ability rolls The Five Fates, up to 5 six-sided dice displayed above Koumei's ability 

### Kullervo

- Ressource : énergie
- Coûts : 1 Wrathful Advance = 25 ; 2 Recompense = 50 ; 3 Collective Curse = 75 ; 4 Storm Of Ukko = 100
- Passif (wiki) : All melee weapons equipped by Kullervo gain +75% Heavy Attack Efficiency and +100% Heavy Attack Wind Up Speed, in addition to a stylized Melee Combo Counter permanently displayed above his ability icons. - Heavy Attack Efficiency bonus works in Archwing missions. - Recompense successful hits on enemies add 1 melee combo per dagger, excluding missed daggers striking Kullervo himself. - Melee weapon attacks and ability dagger hits spread by Collective Curse add 1 melee combo per hit. - Storm of Ukko's direct damage adds 1 melee combo per tick. Unlike most Warframes, when Kullervo ranks up he rec

### Lavos

- Ressource : temps de recharge. Lavos n'a pas d'énergie et ses capacités ne consomment aucune ressource : elles sont gratuites, avec un temps de recharge entre deux utilisations. L'efficacité ne réduit pas un coût : elle joue sur la réduction de recharge donnée par Transmutation Probe et par l'augment Swift Bite. Une capacité Helminth sur Lavos coûte 0 énergie mais a 10 s de recharge. Les nombres ci-dessous sont des temps de recharge en secondes.
- Coûts : 1 Ophidian Bite = 8 ; 2 Vial Rush = 5 ; 3 Transmutation Probe = 10 ; 4 Catalyze = 30
- Passif (wiki) : Valence Block Purifying himself from all ailments, Lavos cleanses all active negative Status Effects and gains status immunity for 10 seconds upon collecting an Energy or Universal Orb. Picking up an Energy or Universal Orb has a cooldown of 5 seconds. - Buff duration is renewed to full upon collecting a new orb. - Valence Block buff icon and timer are shown beside Lavos' shield and health indicators. - While activated, three serpent-like energy particle effects encircle Lavos' body. - If Lavos is injured with missing health, Universal Orbs are collectible to heal him with no cooldown period i

### Limbo

- Ressource : énergie
- Coûts : 1 Banish = 25 ; 2 Stasis = 50 ; 3 Rift Surge = 50 ; 4 Cataclysm = 100
- Passif (wiki) : - Main article: Rift Plane Limbo's abilities allow access to the Rift plane ("Rift", for short), an alternate dimension to the normal environment, or material plane. Interaction between the Rift and material planes is highly limited. Generally, for both players and enemies, weapons will not function across planes, but Abilities will. Anyone in the Rift can be forcibly removed from it by entering a Nullifier's bubble. Any player can leave the Rift voluntarily by performing a Roll, Sidespring, or Backspring. Enemies that transition between planes will receive Knockdown and 300 Impact damage, una

### Loki

- Ressource : énergie
- Coûts : 1 Decoy = 25 ; 2 Invisibility = 50 ; 3 Switch Teleport = 25 ; 4 Radial Disarm = 100
- Passif (wiki) : Loki's Wall Latch duration is increased to a maximum of 60 seconds, ten times longer than any other Warframe.

### Mag

- Ressource : énergie
- Coûts : 1 Pull = 25 ; 2 Magnetize = 50 ; 3 Polarize = 75 ; 4 Crush = 100
- Passif (wiki) : Mag automatically Vacuums Pickups that are within 8 meters towards her. - The passive does not stack with mods like Vacuum or Fetch, making it useless if these mods are used, since they override her passive due to providing more range.

### Mesa

- Ressource : énergie
- Coûts : 1 Ballistic Battery = 25 ; 2 Shooting Gallery = 50 ; 3 Shatter Shield = 75 ; 4 Peacemaker = 25 +15/s
- Passif (wiki) : Mesa has improved proficiency with secondary weapons, and gains a health bonus at the expense of not having a melee weapon equipped: - +15% fire rate with dual wielded sidearms. - +25% reload speed for one handed sidearms. - +50 health when no melee weapon is equipped.   - Works in Archwing missions and you can still have an Archmelee.
  - Peacemaker : - Holstering the Regulators upon deactivation, however, is not affected.
  - Peacemaker : - Peacemaker does not trigger "On Equip" mods like Vigorous Swap on either activation or deactivation.

### Mirage

- Ressource : énergie
- Coûts : 1 Hall Of Mirrors = 25 ; 2 Sleight Of Hand = 50 ; 3 Eclipse = 25 ; 4 Prism = 50 +10/s
- Passif (wiki) : Mirage has an increased proficiency when performing several Maneuvers: - Sliding lasts 85% longer - +50% faster Maneuver Speed
  - Prism : - Prism drains 10 energy per second while active and will remain active for the ability's full duration, until Mirage's energy is depleted, or the ability is deactivated by pressing the ability key again.
  - Prism : - When the ability expires or is manually deactivated (default 4 ), the prism will explode in a bright flash of light that Blinds enemies within 8 / 12 / 15 / 25 meters for 7 / 10 / 12 / 15 seconds.

### Narin

- Ressource : énergie
- Coûts : 1 Neote = 25 ; 2 Naraemagi = 50 ; 3 Hakchum = 75 ; 4 Nurinarim = 25
- Passif (wiki) : Enemies killed by any source, while afflicted with Cold Status Effects from Narin, have a 1% chance per Cold status effect (10% chance at 10 Cold status) to drop a Sangodae Cold Ammo rune. Ammo runes remain indefinitely until picked up; up to 5 ammo runes may be active at once, with the newest spawned removing the oldest. - Sangodae ammo runes are client-side pickups, which can be collected separately by Narin herself and allied Warframes. - Ammo runes are represented as floating runic globes containing a crane and bullets symbol. - Narin's Companion-inflicted Cold status effects do not activa

### Nekros

- Ressource : énergie
- Coûts : 1 Soul Punch = 25 ; 2 Terrify = 75 ; 3 Desecrate = 10 +10/corpse ; 4 Shadows Of The Dead = 100
- Passif (wiki) : A master of death, Nekros and his Companions regenerates 5 Health when an enemy dies within 10 meters of him. - Works in Archwing missions but is hard to trigger.
  - Desecrate : - Nekros expends 10 energy to emit an aura of dark power to consume all corpses within a radius of 10 / 15 / 20 / 25 meters. Consumed corpses have a 30% / 40% / 50% / 60% chance to spawn a health orb and a 22.5% / 32% / 42.5% / 54% chance to roll the corpse's drop table again to produce additional loot. After a 2 second delay on
  - Desecrate : - Despite being a channeled ability, this does not interrupt energy regeneration from any source including Energy Siphon and Wellspring, and it is unaffected by Ability Duration.

### Nezha

- Ressource : énergie
- Coûts : 1 Fire Walker = 25 ; 2 Blazing Chakram = 25 ; 3 Warding Halo = 75 ; 4 Divine Spears = 100
- Passif (wiki) : Nezha slides 60% faster and goes 35% farther. These effects additively stack with Cunning Drift, Maglev and Streamlined Form. Nezha's passive can be disabled with Controlled Slide.

### Nidus

- Ressource : énergie
- Coûts : 1 Virulence = 40 ; 2 Larva = 25 ; 3 Parasitic Link = 25 ; 4 Ravenous = 3
- Passif (wiki) : The Infestation dwelling within Nidus mutates rapidly when used against his foes, fueling his abilities and yielding various symbiotic benefits. Mutation Stacks are a resource unique to Nidus, indicated by the Mutation counter and gauge displayed in the lower-right on the HUD, above the ability icons. - The gauge is divided into 5 sections which represent the number of hits dealt to enemies via Nidus's abilities, while the counter at the center of the gauge keeps track of the number of Mutation stacks up to a maximum of 200.   - When generating Mutation, the sections light up clockwise. Once a

### Nokko

- Ressource : énergie
- Coûts : 1 Stinkbrain = 25 ; 2 Brightbonnet = 50 ; 3 Reroot = 50 ; 4 Sporespring = 75
- Passif (wiki) : Upon receiving fatal damage, if Nokko has at least one Stinkbrain or Brightbonnet placed, he will trigger Vital Decay to transform into his Invulnerable Sprodling form instead of entering Bleedout. While in this form, Nokko will revive if he can reach one of his active mushrooms within 15 seconds; failing to reach a mushroom in time will result in immediate death. Reviving has a 3-second animation, during which Nokko is invulnerable and gains 100% Health and Shields. Once reborn, Nokko remains invulnerable for an additional 1 second. - If Nokko does not have any active mushrooms upon receiving

### Nova

- Ressource : énergie
- Coûts : 1 Null Star = 25 ; 2 Antimatter Drop = 50 ; 3 Wormhole = 75 ; 4 Molecular Prime = 100
- Passif (wiki) : Enemies killed by Nova while Slowed have a 15% chance to drop a Health Orb; enemies killed while sped-up have a 15% chance to drop an Energy Orb. The slow/speed-up can be from any source, including Nova's Molecular Prime.

### Nyx

- Ressource : énergie
- Coûts : 1 Mind Control = 25 ; 2 Psychic Bolts = 50 ; 3 Chaos = 75 ; 4 Absorb = 75
- Passif (wiki) : Nyx gains Thrive in Chaos whenever enemies within Affinity Range are afflicted with Confusion (from Radiation status effect or Mind Control), increasing her primary and secondary weapon Critical Chance by 40% per enemy up to a maximum of 200% from 5 enemies. - The bonus is additive to mods like Pistol Gambit and Point Strike. - Works in Archwing missions.

### Oberon

- Ressource : énergie
- Coûts : 1 Smite = 25 ; 2 Hallowed Ground = 50 ; 3 Renewal = 25 +3.5/s ; 4 Reckoning = 100
- Passif (wiki) : Guarded by nature, when Oberon picks up a regular Health Orb, Dispensary produced Empowered variant, or Universal Orb, he blesses himself and allies within Affinity Range with Righteous Negation for up to 3 charges. Incoming damage is blocked to consume a charge while also becoming Invulnerable for 0.25s (0.5s on the final charge). Charges last indefinitely until consumed. - More Oberons will not increase the max charge count. - Affected allies include Warframes, and Companions.   - Each guarded ally consumes charges individually and does not reduce the charges on other guarded allies.   - Whe
  - Renewal : - Oberon expends 25 energy to channel a blessed field, granting Iron Renewal to himself and allies within Affinity Range, granting the following effects:
  - Renewal : - Renewal consumes 3.5 energy per second while active. Renewal will remain active until Oberon's energy is depleted or the ability is deactivated by pressing the ability key again.

### Octavia

- Ressource : énergie
- Coûts : 1 Mallet = 25 ; 2 Resonator = 50 ; 3 Metronome = 75 ; 4 Amp = 100
- Passif (wiki) : Octavia creates musical masterpieces from the Mandachord affixed to her arms that empowers her abilities. She possesses various passive mechanics highlighted in the tabs below: - For an in-depth guide to the Mandachord by the developers, see Mandachord/Developer's Guide. - To access the Mandachord menu, open the Arsenal in your ship, equip Octavia, click on the Warframe's Appearance tab, and select Mandachord at the bottom-right of the screen. - Once inside the Mandachord menu, the player's view will switch to first-person and look downward at the expanded Mandachord on Octavia's left arm. - T

### Oraxia

- Ressource : énergie
- Coûts : 1 Mercy's Kiss = 25 ; 2 Webbed Embrace = 50 ; 3 Widow's Brood = 50 ; 4 Silken Stride = 25 +5/s
- Passif (wiki) : An apex predator patiently prowls, hidden in plain sight. Perform Wall Latch (default hold RMB near a wall) to activate Predator’s Lurk, rendering Oraxia and her Companion Invisible for 8 seconds. - Passive timer is shown as a Buff icon beside Oraxia's hitpoints indicator. - Predator's Lurk can have its duration refreshed when Oraxia releases then reuses wall latch again. - Invisibility does not break when Oraxia stops wall latching or attacks with her weapons and abilities. - When used on a vertical surface or ceiling, Silken Stride's Silken Thread web-sling allows Oraxia to automatically wal
  - Silken Stride : - While active, Oraxia laces her primary and secondary weapons' magazine ammo with potent venom, causing each weapon hit to inflict an Extra Hit of 10% / 20% / 30% / 40% Toxin damage (20% / 40% / 60% / 80% while Wall Latching) with 100% status chance; however, Oraxia is unable to equip her melee weapon. Enemies killed by Oraxia'
  - Silken Stride : - Silken Stride consumes 5 energy per second while active, and will remain active until Oraxia's energy is depleted or the ability is deactivated manually.

### Protea

- Ressource : énergie
- Coûts : 1 Grenade Fan = 25 ; 2 Blaze Artillery = 50 ; 3 Dispensary = 75 ; 4 Temporal Anchor = 100
- Passif (wiki) : Every 4th ability cast by Protea gains an additive 100% Ability Strength bonus. The power recorder displayed on the HUD above her ability icons is charged by 1 power bar per ability cast. Once fully charged with 3 power bars, the leftmost slot glows intensely and the bonus ready message is shown above. - After the bonus is applied, the power recorder empties to reset the cycle. - Abilities can be cast in any combination to empower a desired ability with the passive bonus. - Passive bonus grants improvements to the following aspects of each ability:   - Grenade Fan's Shrapnel Vortex damage per 

### Qorvex

- Ressource : énergie
- Coûts : 1 Chyrinka Pillar = 25 ; 2 Containment Wall = 50 ; 3 Disometric Guard = 75 ; 4 Crucible Blast = 100
- Passif (wiki) : All Primary, Secondary, and melee weapons wielded by Qorvex gain Core Exposure, granting them a +3 Punch Through bonus. - Works in Archwing missions. This also applies to some subsumed abilities' projectiles, including: - Null Star (without the Neutron Star augment) - Main article: Universal Weapon Bonuses

### Revenant

- Ressource : énergie
- Coûts : 1 Enthrall = 25 ; 2 Mesmer Skin = 50 ; 3 Reave = 50 ; 4 Danse Macabre = 25 +20-40/s
- Passif (wiki) : When Revenant's Shield is fully depleted, he emits a radial pulse over 7.5 meters inflicting 100 Blast damage with maximum 75% Damage Falloff. - Works in Archwing missions but can not inflict Knockdown. Additionally, harnessing the essence of Eidolons, Revenant is immune to the Magnetic night waters of the Plains of Eidolon.
  - Danse Macabre : - While active, all damage received by Revenant is stored into a total damage pool. The stored damage is displayed as a buff. The current displayed value is added to each beam as a flat damage bonus.
  - Danse Macabre : - Revenant is able to move with reduced movement speed while channeling Danse Macabre.

### Rhino

- Ressource : énergie
- Coûts : 1 Rhino Charge = 25 ; 2 Iron Skin = 50 ; 3 Roar = 75 ; 4 Rhino Stomp = 100
- Passif (wiki) : If Rhino falls far enough to incur a Hard Landing (even if he avoids the animation, such as by sliding), the ground impact will discharge a shockwave that deals Impact damage and Knockdown in a 6 meter area of effect. This stacks with Heavy Impact. There is a max 90% Damage Falloff at the edge of the shockwave's radius. - There is no effect when Kavat's Grace is installed.

### Saryn

- Ressource : énergie
- Coûts : 1 Spores = 25 ; 2 Molt = 50 ; 3 Toxic Lash = 50 ; 4 Miasma = 75
- Passif (wiki) : Status Effects inflicted by Saryn's weapons and abilities last 25% longer. - Duration bonus stacks additively with status duration mods such as Lasting Sting. - Works in Archwing missions.

### Sevagoth

- Ressource : énergie
- Coûts : 1 Reap = 25 ; 2 Sow = 50 ; 3 Gloom = 50 +.75-7.5/s ; 4 Exalted Shadow = pas de coût en énergie
- Passif (wiki) : Intertwined forever in life and death, Sevagoth and his Shadow exhibit numerous unique properties and interactions, highlighted in the tabs below: On fatal injury and entering Bleedout, Sevagoth's body petrifies into a broken tombstone as his Shadow manifests itself. Control the Shadow to collect the souls of 5 enemies by casting Consume via the ability, quick melee, or fire weapon buttons with a targeted enemy on the aiming reticle (default 2 , E and LMB respectively), reviving Sevagoth upon a full harvest. Alternatively, allies may manually revive Sevagoth by interacting with his tombstone. 
  - Gloom : Misc: 95 % (slow cap) 10 (energy drain enemy cap) 0.1 %/s (Death Well gain per second per enemy)
  - Gloom : - While enemies are in range, Gloom consumes 0.75 energy per enemy per second, stacking up to a cap of 10 enemies for a maximum drain amount of 7.5 energy per second, to sustain the ability until Sevagoth's energy is depleted or the ability is deactivated by pressing the ability key again.
  - Exalted Shadow : Misc: 5 s (Invincibility duration on cast) 5 m (Shadow summoned propulsion) 5 % (Death Well gain per enemy for Reap, Sow and Death's Harvest) 0.1 %/s (Death Well gain per second per enemy for Gloom) 1% HP (Death Well drain to health conversion)
  - Exalted Shadow : - The player must be directly controlling Sevagoth with Exalted Shadow deactivated to gain Death Well percentage from the eligible Abilities noted above.

### Sirius & Orion

- Ressource : énergie
- Coûts : 1 Coronal Ejection = 15 ; 2 Jade Stars = 50 ; 3 Light's Sanctuary = 50 ; 4 Celestial Clash = 100
- Passif (wiki) : As one and the same from different alternate timelines, Sirius & Orion exhibit numerous unique properties and interactions, highlighted in the tabs below:

### Styanax

- Ressource : énergie
- Coûts : 1 Axios Javelin = 15 ; 2 Tharros Strike = 25 ; 3 Rally Point = 75 ; 4 Final Stand = 100
- Passif (wiki) : Styanax's weapon Critical Chance bonus increases by 1% per 40 Shield points, based on his current total including Overshields. Passive bonus is doubled on Speargun primary Weapons, such as Styanax's signature Afentis ( Prime), Ferrox ( Tenet), and Javlok. - Passive bonus value is displayed as a Buff icon called Hoplite beside Styanax's hitpoint indicators. - Critical chance bonus percentage changes in real time to reflect Styanax's shield pool. - Critical chance bonus applies to all weapon types including primary, secondary, and melee. Stacks additively with Mods. - While Styanax has a Speargu

### Temple

- Ressource : énergie
- Coûts : 1 Pyrotechnics = 25 ; 2 Overdrive = 25 ; 3 Ripper's Wail = 50 ; 4 Exalted Solo = 75
- Passif (wiki) : Temple tracks their rhythmic mayhem by keeping in sync with the Backbeat metronome, shown below their aiming reticle. The metronome's pendulum swings from left to right and vice-versa at a pace of 78 BPM, while passing through a central zone that doubles as a fuel gauge for Lizzie, the living Techrot guitar wielded during Exalted Solo. When in the zone, the pendulum's bulb above its needle lights up. Cast an ability while the Backbeat is in the zone to amplify Temple's ability with a 50% Ability Efficiency, fuel up the gauge by 55 ammunition, and earn an extra effect specific to each ability: 

### Titania

- Ressource : énergie
- Coûts : 1 Spellbind = 25 ; 2 Tribute = 25 ; 3 Lantern = 75 ; 4 Razorwing = 25 +5/s
- Passif (wiki) : Frolicking and fluttering about, Titania passively possesses +25% Bullet Jump and Rolling distance. Casting her abilities rejuvenates Titania and her allies within 15 meters, granting them the Upsurge buff which regenerates 4 Health points per second for 20 seconds. - Upsurge is granted at the start of Titania's cast animations.   - The duration of the heal is refreshed on successive ability casts. - Upsurge buff icon is displayed with a duration timer next to the shield and health indicators, at the top-right of the HUD.   - An icon also appears next to each allied player affected by Upsurge.
  - Razorwing : - Railjack Intrinsic bonuses do not affect Razorwing, with the exception of the Rank 8 Tactical Intrinsic "Archwing Tactical Blink", which reduces Razorwing's Archwing Blink cooldown by 25%.
  - Razorwing : - Cast animation of 1.4 seconds and deactivation of 1.0 second are affected by Casting Speed.

### Trinity

- Ressource : énergie
- Coûts : 1 Well Of Life = 25 ; 2 Energy Vampire = 50 ; 3 Link = 75 ; 4 Blessing = 100
- Passif (wiki) : Trinity and allies in her Affinity Range gain Lifegiver, which increases their Health equal to 50% (25% in Conclave) of Trinity's total Energy pool. - Lifegiver can be increased by energy pool Mods, such as Flow, Primed Flow, and Archon Flow, as well as Azure Archon Shard. - Works in Archwing missions but scales off the Archwing energy pool.

### Uriel

- Ressource : énergie
- Coûts : 1 Infernalis = 25 ; 2 Remedium = 50 ; 3 Demonium = 75 ; 4 Brimstone = 75
- Passif (wiki) : Uriel commands the Legion comprised of three fiendish Demons: Catenach, Gulphagor, and Vythelas. Demons are flying Health-based intangible Summons unlocked by Uriel's abilities gaining Rank, spawning with Uriel into the mission lasting indefinitely until killed, after which they automatically resurrect in 60 seconds. Demons draw enemy fire with their notable Threat Level whilst following Uriel wherever he roams, and perform specific devilish deeds to assist and amplify Uriel. Uriel's Legion possesses various unique and shared attributes highlighted in the tabs below: - Demons' maximum Health s

### Valkyr

- Ressource : énergie
- Coûts : 1 Rip Line = 25 ; 2 Warcry = 75 ; 3 Paralysis = 25 ; 4 Hysteria = 25 +5/s
- Passif (wiki) : - For the mod, see Rage. Valkyr - Valkyr gains Rage from:   - Melee attack: 3% per hit   - Melee kill or assisted kill: 12%   - Finisher or Parazon Mercy Kill: 27% - After not building Rage for 5 seconds, the damage bonus decays at a non-linear rate dependent on the amount of Rage Valkyr has, with the following formula:   - { λ =0.016 ; n =(ln(1000λ))/λ ; d(t) ={{ e^(−λt), if 0≤t≤n ; e^(−λn)−0.001(t−n), if t>n } ; Bonus(t) =⌊300⋅d(t)⌋ }     - Above 18%, the meter decays by half over 43 seconds. Below 18%, the meter decays by 0.3% every second. - Bonus damage is additive with mods like Pressure
  - Hysteria : - Hysteria consumes 5 energy per second while active and will remain active until either Valkyr's energy is depleted or the ability is deactivated by pressing the ability key again.
  - Hysteria : - Hysteria's energy drain is not converted into shields by Augur Mods.

### Vauban

- Ressource : énergie
- Coûts : 1 Tesla Nervos = 25 ; 2 Minelayer = 25 ; 3 Photon Strike = 50 ; 4 Bastille = 100
- Passif (wiki) : An inventor by nature, the process of creation necessitates demolition and deconstruction. Vauban inflicts 25% bonus damage with his weapons and abilities against enemies that are incapacitated. - Enemies are considered incapacitated from:   - Electricity status effect's stun, including from an attached Tesla Nervos   - Heat status effect's panicking   - Cold status effect's frozen on 10 stacks     - Note that enemies must be in the crowd control animation, simply having the status effect does not count.   - Minelayer's Tether-Flechette Orb coil   - Bastille's lifting prison   - Bastille's vor

### Voidrig

- Ressource : énergie
- Coûts : 1 Necraweb = 25 ; 2 Storm Shroud = 50 ; 3 Gravemines = 75 ; 4 Guard Mode = 50 +5/s
  - Guard Mode : - Guard Mode then drains 5 energy per second and will remain active until Voidrig's energy is depleted or or the ability is deactivated by pressing the ability key again.

### Volt

- Ressource : énergie
- Coûts : 1 Shock = 15 ; 2 Speed = 25 ; 3 Electric Shield = 50 ; 4 Discharge = 100
- Passif (wiki) : Traveling along the ground between Volt's attacks (by walking, running, or sliding) will build up static energy, adding bonus Electricity damage toward Volt's next weapon attack or ability cast. For every 1 meter traveled, 10 points of Electricity damage are added, accumulating to a maximum of 1000 bonus damage. - Volt's passive is named Static Discharge by the Transistor Shield augment. - Does not combine with single elements or elemental mods on weapons; the bonus Electricity damage type remains separate. - Is not discharged by most Helminth injected abilities or Shocking Speed sparks. - Non

### Voruna

- Ressource : énergie
- Coûts : 1 Shroud Of Dynar = 25 ; 2 Fangs Of Raksh = 50 ; 3 Lycath's Hunt = 75 ; 4 Ulfrun's Descent = 100
- Passif (wiki) : Like a blood moon striding across the starlit night, Voruna never hunts alone. Safeguarded by her four loyal wolves, she may freely invoke their protective passives anytime during a mission. Hold down the ability button (default 1 , 2 , 3 , 4 ) to invoke 1 passive into the UI indicator above the ability icons. Wolf passives persist indefinitely until switched, undergoing a cooldown (Ulfrun's Descent), or revoked by holding down the ability key again; while a passive is selected, the corresponding wolf skull on Voruna's body glows with energy, as a flying wolf skull orbits around her. - Shroud 

### Wisp

- Ressource : énergie
- Coûts : 1 Reservoirs = 25 ; 2 Wil-O-Wisp = 35 ; 3 Breach Surge = 50 ; 4 Sol Gate = 25 +12-24/s
- Passif (wiki) : Wisp weaves between dimensions whilst she is airborne, gaining a cloak that renders her and her Companions completely invisible to enemies indefinitely until she lands or fires a weapon. Wisp's cloak will reactivate 0.5 seconds after the player stops firing, provided they are still airborne. - The cloak does not wear off immediately after landing, allowing Wisp to constantly remain invisible.   - Hard Landings will dissipate the cloak immediately. - Silenced weapons will still remove her invisibility. - Invisibility is not affected by Melee weapon strikes, allowing Wisp to freely use them with
  - Sol Gate : - Damage Ramp is a per-damge-type, per-enemy debuff that persists until the ability is deactivated.
  - Sol Gate : - Wisp recoils backward when the ability deactivates.

### Wukong

- Ressource : énergie
- Coûts : 1 Celestial Twin = 25 ; 2 Cloud Walker = 25 ; 3 Defy = 50 ; 4 Primal Fury = 10 +5/s
- Passif (wiki) : Wukong has learned five techniques to avoid death whenever he takes fatal damage. Wukong will be randomly allowed 3 of these techniques per mission, each will make Wukong avoid entering bleedout upon taking fatal damage, Invulnerable for 2 seconds, restore 50% health, and provide a unique buff: - Primal Forces: 300% Elemental Damage for 60 seconds. - Heavenly Cloak: Invisibility for 30 seconds.   - Invisibility does not reveal Wukong when he attacks. - Cosmic Armour: Invulnerable for 30 seconds. - Monkey Luck: Enemies killed yield extra loot drops for 60 seconds.   - Additional loot retrieval 
  - Primal Fury : - Primal Fury consumes 5 energy per second while active and will remain active until Wukong's energy is depleted or the ability is deactivated by pressing the ability key again.
  - Primal Fury : - Primal Fury's energy drain is not converted into shields by Augur Mods.

### Xaku

- Ressource : énergie
- Coûts : 1 Xata's Whisper = 25 ; 2 Grasp Of Lohk = 50 ; 3 The Lost = 75 ; 4 The Vast Untime = 100
- Passif (wiki) : Shifting their pieces unpredictably, Xaku has a 25% Dodge chance to harmlessly phase through incoming enemy weapon attacks, while protected by a 25% Damage Reduction against area of effect damage. Passive dodge chance and area damage reduction both raise to 75% while The Vast Untime is activated. - Enemy attacks affected by the dodge passive include hitscan, bullets, projectiles, and melee attacks. Explosions that occur near Xaku are not dodged, instead Xaku will receive damage reduction against them. - Evasion (such as from Agility Drift) and Xaku's dodge chances are separate mechanics that d

### Yareli

- Ressource : énergie
- Coûts : 1 Sea Snares = 25 ; 2 Merulina = 25 ; 3 Aquablades = 75 ; 4 Riptide = 100
- Passif (wiki) : Everflowing with the seas, whenever Yareli moves for at least 1.5 seconds, she gains the Critical Flow buff that increases Critical Chance on her secondary Weapon by 200%. Critical Flow lasts until Yareli stops moving for 1 second. - Critical Flow additively stacks with other pistol critical chance mods such as Pistol Gambit to increase the secondary weapon's base critical chance stat. - The condition of movement to activate and sustain Critical Flow involves the player's input of the movement keys (default W A S D ), falling from heights, or certain Maneuvers such as Bullet Jumping, Aim Glidi

### Zephyr

- Ressource : énergie
- Coûts : 1 Tail Wind = 25 -12.5 (airborne) +5/s hovering ; 2 Airburst = 50 -25 in air ; 3 Turbulence = 75 ; 4 Tornado = 100
- Passif (wiki) : While airborne, Zephyr falls slower and is more maneuverable, and her equipped weapons gain a 150% Critical Chance bonus that additively stacks to the bonuses of critical chance Mods. The reduced gravity portion of her passive can be disabled with Anchored Glide.
  - Tail Wind : - While Zephyr is airborne, holding down the ability key then releasing it (default 1 ) causes Zephyr to expend 12.5 energy then drain 5 energy per second to immediately arrest her momentum then sustain her altitude in a continuous hover. While hovering in the air, Zephyr may attack with, switch and reload her weapons, as well a
  - Tail Wind : - Hover Glide's energy drain is not converted into shields by Augur Mods.
