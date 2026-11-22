# Overguard (wiki)
Source : https://wiki.warframe.com/w/Overguard

Overguard

An Eximus unit with Overguard health

Information

Icon

Introduced

Update 31.5 (2022-04-27)

Overguard grants additional Health protection and Knockdown immunity as long as an amount remains.—In-Game Description

Overguard is a special health buffer that grants immunity to most crowd control effects.

## Mechanics

Overguard
Impact | —
Puncture | —
Slash | —
Cold | —
Electricity | —
Heat | —
Toxin | —
Blast | —
Corrosive | —
Gas | —
Magnetic | —
Radiation | —
Viral | —
True | —
Void | +50%
Tau | —

Overguard is an additional layer of defense that protects Health and/or Shields from being damaged. It is neutral to all damage types except for a 50% vulnerability from Void damage, though there are a few sources that increase damage dealt to Overguard:

- Magnetic Status Effect amplifies all damage dealt to Overguard in the same way it does to Shields: 100% damage on the first stack, 25% on subsequent stacks up to a maximum of 325% after 10 stacks. In addition, when Overguard breaks, the target receives Electricity damage equal to 3% of their total Overguard per Magnetic stack up to a maximum of 30% at 10 stacks.
- Damage Vulnerability applies normally to Overguard.
- Beast Companion (Kubrows, Kavats, Predasites, and Vulpaphylas)'s Assassin Posture increases their damage to Overguard by 300%.
- Sunika Kubrow's Unleashed increases their damage to Overguard by 300%.
- Oberon's Smite instantly removes Overguard.
- Vauban's Photon Strike deals 200% more damage to Overguard.
- Hound's Null Audit removes 50% of an Eximus's Overguard.
- Secondary Fortifier lets secondary weapons and Arch-guns deal up to 8x increased damage to enemy Overguard.

Overguard is not affected by Damage Reduction from armor or abilities such as Splinter Storm or Damage type resistance effects such as Adaptation and Caliban's passive. However, abilities or effects with Damage Redirection, such as Link, Warding Halo, or Shield of Shadows will apply their effect to Overguard. Rolling will also apply its damage reduction to Overguard. Enemies can still have their shields and armor stripped while their Overguard is active.

### Player

On players, Overguard will negate all Status Effects, including Stagger and Knockdown. It additionally has a 0.5 second invulnerability gate when fully depleted, preventing any excess damage from leaking into their shield or health pool. Even enemy crowd control effects that still affect players with Primed Sure Footed (such as fire waves by Arson Eximus) will be ignored with Overguard. However, grapple hooks from enemies such as a Scorpion will still interrupt the player for a moment and pull them in.

Only Warframes, Companions, Specters, and Eidolon Lures are able to receive Overguard. Consequently, it cannot be given to Defense Objects.

If the user has no Shields active ( Inaros and Nidus by default), Energy conversion from damage to Health effects ( Rage, Hunter Adrenaline, Necramech Rage, and Kinetic Diversion) will allow damage to Overguard granted from an ally to be converted to energy. Kullervo, despite having no shields, cannot reliably benefit from this due to receiving Overguard for himself from Recompense.

### Enemy

On enemies, they can receive Status Effects but while their Overguard is active they will completely ignore the crowd control effects of Stagger, Knockdown, Stun, Mind Control, Confusion (including Radiation procs), Slow, Ragdoll, Blind, and Lifted, and can normally only receive a maximum of 4 Cold procs.

Enemies do not have any invulnerability gating when their Overguard is depleted.

Overguard is independent of enemy health and shield scaling. Overguard will scale by level but will be the same amount across all Eximus enemy types.

Because of their immunity to crowd control, Overguarded enemies are a threat that should be prioritized; crowd control will still affect their allies and they will still target Confused units which helps level the playing field. If afflicted by Radiation, their allies without Overguard can target them which in turn causes the Overguarded enemy to fire back. In the case of Ancient Protector and The Severed Warden, which provide Overguard to their own allies but not themselves while alive, they will still receive crowd control as normal and should be targeted instead. Shooting off a Nox's helmet will immediately remove their Overguard.

#### Scaling

This section is transcluded from Enemy Level Scaling § Overguard. To change it, please edit the transcluded page.

Overguard is a unique health buffer to Eximus, though normal units can get overguard in unique situations (like after a Overguard Exodamper is destroyed during Void Armageddon). All Eximus units have a base Overguard of 12.

- f_1(x)=1+0.0015(x−1)^4 Lower endpoint curve
- f_2(x)=1+260(x−1)^(0.9) Upper endpoint curve

Stat scaling between 45-50 inclusive is interpolated from the two functions using smoothstep.

- Overguard Multiplier=f32(f_1(Current Level)+f32(f32(f_2(Current Level)−f_1(Current Level))×s)) Where the Overguard Multiplier is the value that multiplies an enemy's base overguard to its current overguard.

## Enemies with Overguard

- All Eximus except Archwing, Warden, and Prosecutor Eximus units. Their base Overguard is 12.
- Ancient Protector/Corrupted Ancient - Grants itself and nearby enemies Overguard equal to 9x of the Ancient Protector's health.
- Archon Amar - In Archon Hunts, gains an extremely small amount of Overguard when protected by his clones and heat wall. Depleting the Overguard will cancel the ability.
- Archon Boreal - In Archon Hunts, gains an extremely small amount of Overguard when protected by his screech. Depleting the Overguard will cancel the ability.
- Archon Nira - In Archon Hunts, gains an extremely small amount of Overguard when protected by her frontal barrier and toxic field. Depleting the Overguard will cancel the ability.
- Corpus Cestra Target
- Corpus Sniper Target
- Corpus Supra Target
- Corpus Trencher Target
- Dax Malleus - Only in The Undercroft/The Circuit.
- Kuva Trokarian
- Nox (except Demolisher Nox) - Breaking the Nox's glass helmet will immediately remove all of its Overguard.
- Scaldra Dedicant - Breaking the Dedicant's glass ampule on its abdomen will immediately remove all of its Overguard.
- The Severed Warden - Grants and continually replenishes nearby enemies with Overguard. Cannot provide Overguard to themselves.
- Thrax Centurion
- Thrax Legatus
- Deep Archimedea/Temporal Archimedea ("Bolstered Belligerents" Risk Variable) - All enemies have Overguard equal to 50% of their max health.
- Void Armageddon - All Grineer and Corpus units receive Overguard upon destroying an Overguard Exodamper for the remainder of the round.

## Crowd Control That Bypasses Overguard

It's taking longer than I calculated.

This page is actively being worked on and may not be completely correct. Please assist in making this page accurate by adding more info. For guidance on performing research, see WARFRAME Wiki:Research.

- Cold procs (up to 4 stacks)
- Void procs bullet effect
- Silence status effect from Banshee's Silence or Dante's Noctua with Noctua Swarm.
  - Will silence through Overguard, but does not apply the asssociated stun from those abilities.
- Loki's Switch Teleport - will not make enemy disoriented upon teleport
- Effects that Taunt or have increased Threat Level (i.e. presence of Overguard will not affect Enemy Behavior):
  - Loki's Decoy
  - Nyx's Chaos
  - Octavia's Mallet
  - Titania's Razorflies
  - Dante's Noctua Swarm
- Volt's Discharge will stop enemy movement, but will not affect their actions.
- Follie's Shadowgraph - Defense Capsule will distract part of enemies
- Dax enemies (Dax Arcus, Dax Equitem, Dax Gladius, Dax Herald, and Dax Malleus) suffer a forced knockdown if their special attacks are interrupted by gunfire. Overguard does not stop this knockdown.
- While Radiation can't directly affect enemies with Overguard, if another enemy without Overguard is irradiated and shoots the enemy with Overguard, they will turn to target them instead of the player. However, as soon as they stop firing at the Overguarded enemy, the Overguarded enemy will resume firing at players

## Abilities That Have Unique Interactions With Overguard

This is a short list of Warframe abilities that will slow enemies with Overguard until it is removed, after which the ability will affect them like normal:

- Vauban's Bastille's Vortex
- Zephyr's Tornados
- Gyre's Coil Horizon Vortex

## Sources of Player Overguard

Abilities

 | 2 25 | Light Verse Dante's vitalizing composition grants him and his allies Overguard and restores their Health. Introduced in Update 35.5 (2024-03-27) | Strength:+ 200 / 250 / 300 / 350 Overguard gain 7,500 / 10,000 / 12,500 / 15,000 Overguard cap + 14 / 16 / 18 / 20 % HP healed based on max health
Duration:N/A
Range:20 m ally buff radius
Misc: 1 s (Invulnerability duration on cast) +1 Final Verse Light page

Info

- Dante expends 25 energy to inscribe a circle of protection, granting himself 1 second of Invulnerability, then 200 / 250 / 300 / 350 Overguard to a cap of 7,500 / 10,000 / 12,500 / 15,000 points and heals 14% / 16% / 18% / 20% of max Health for himself and allies within 20 meters.
- Can be recast immediately once the circle of protection is fully drawn.
- Casting Light Verse is a full-body animation that allows uninterrupted movement and parkour Maneuvers.

Maximization

Light Verse

 | 4 50 | Final Verse Dante must compose two other Verses before his Final Verse. TRIUMPH: Two Light Verses cast in succession invigorate allies with a buff that increases Health and grants Overguard. Kills and assists briefly regenerate Overguard. Dante must compose two other Verses before his Final Verse. TRAGEDY: Two Dark Verses cast in succession attack enemies. Damage Over Time from Slash, Heat and Toxin Status Effects accumulates in a single blast. Dante must compose two other Verses before his Final Verse. WORDWARDEN: A Light Verse followed by a Dark Verse supports allies with copies of Noctua. Noctua copies synchronize their attacks with their designated ally's attacks. Dante must compose two other Verses before his Final Verse. PAGEFLIGHT: A Dark Verse followed by a Light Verse summons Paragrimms that swoop at enemies, making them vulnerable to Status Chance and Status Damage, as well as drawing enemy attacks away from allies. Introduced in Update 35.5 (2024-03-27) | Strength: + 2,250 / 2,500 / 2,750 / 3,000 Overguard gain 7,500 / 10,000 / 12,500 / 15,000 Overguard cap + 85 / 90 / 95 / 100 /s Overguard regen on kills and assists Duration: 30 / 35 / 40 / 45 s Range: 15 / 20 / 25 / 30 m Misc:1 s Invulnerability duration on cast Cannot cast without 2 Light pages 2 s Overguard regen timer Strength: 5,000 / 5,500 / 6,000 / 6,500 base Slash damage 2.25 / 2.5 / 2.75 / 3 x status detonation damage multiplier Duration: N/A Range: 15 / 20 / 25 / 30 m Misc:1 s Invulnerability duration on cast Cannot cast without 2 Dark pages Stagger on hit Detonate Slash, Heat, and Toxin status damage-over-time into total damage single burst 1 billion (damage cap) Strength: N/A Duration: 30 / 35 / 40 / 45 s Range: 15 / 20 / 25 / 30 m Misc:1 s Invulnerability duration on cast Cannot cast without 1 Light then 1 Dark pages 35 / 40 / 45 / 50 % damage copied 1 Noctua copy limit per ally Strength: 150 / 200 / 250 / 300 Slash damage per hit 35 / 40 / 45 / 50 % status chance vulnerability 35 / 40 / 45 / 50 % status damage increase Duration: 30 / 35 / 40 / 45 s 15 / 20 / 25 / 30 s status vulnerability duration Range: N/A Misc:1 s Invulnerability duration on cast Cannot cast without 1 Dark then 1 Light pages 3 Paragrimms limit 30m Paragrimm attack range Slash status and Stagger per hit
Strength: + 2,250 / 2,500 / 2,750 / 3,000 Overguard gain 7,500 / 10,000 / 12,500 / 15,000 Overguard cap + 85 / 90 / 95 / 100 /s Overguard regen on kills and assists
Duration: 30 / 35 / 40 / 45 s
Range: 15 / 20 / 25 / 30 m
Misc:1 s Invulnerability duration on cast Cannot cast without 2 Light pages 2 s Overguard regen timer
Strength: 5,000 / 5,500 / 6,000 / 6,500 base Slash damage 2.25 / 2.5 / 2.75 / 3 x status detonation damage multiplier
Duration: N/A
Range: 15 / 20 / 25 / 30 m
Misc:1 s Invulnerability duration on cast Cannot cast without 2 Dark pages Stagger on hit Detonate Slash, Heat, and Toxin status damage-over-time into total damage single burst 1 billion (damage cap)
Strength: N/A
Duration: 30 / 35 / 40 / 45 s
Range: 15 / 20 / 25 / 30 m
Misc:1 s Invulnerability duration on cast Cannot cast without 1 Light then 1 Dark pages 35 / 40 / 45 / 50 % damage copied 1 Noctua copy limit per ally
Strength: 150 / 200 / 250 / 300 Slash damage per hit 35 / 40 / 45 / 50 % status chance vulnerability 35 / 40 / 45 / 50 % status damage increase
Duration: 30 / 35 / 40 / 45 s 15 / 20 / 25 / 30 s status vulnerability duration
Range: N/A
Misc:1 s Invulnerability duration on cast Cannot cast without 1 Dark then 1 Light pages 3 Paragrimms limit 30m Paragrimm attack range Slash status and Stagger per hit

Info

- Cast Light Verse and/or Dark Verse to fill in 2 pages that complete the Final Verse. Cannot be cast without two pages. Once the story is written, Dante fulfills the narrative by expending 50 energy on cast, which grants him 1 second of Invulnerability during casting and materializes one of four stories based on page order: Triumph, Tragedy, Wordwarden, or Pageflight, while removing both pages from the storybook display above the ability icons. Each story lasts for 30 / 35 / 40 / 45 seconds with a range of 15 / 20 / 25 / 30 meters.
  - The specific story ability icon appears above the storybook display when two pages are filled, with the pages visually glowing.
  - Replace filled pages from the right to left by recasting Light or Dark Verses to create the desired story combination.
  - Stories with active duration appear as ability buff timers beside Dante's hitpoints indicator.
- All stories can be recast while active.
- Casting Final Verse is a full-body animation that allows uninterrupted movement and parkour Maneuvers.
- Dante's four favored chapters exhibit diverse effects involving protection, damage, summoning, and debuffing:

Triumph

- Written with two Light pages (default 2 twice). Triumph bestows 2,250 / 2,500 / 2,750 / 3,000 Overguard to Dante and his allies instantly in story range. While story duration is active, each kill or assisted kill made by Dante or his allies' weapons and abilities will regenerate their personal Overguard pools by 85 / 90 / 95 / 100 points over 2 seconds. Overguard granted by Triumph is capped to 7,500 / 10,000 / 12,500 / 15,000 total points.
- Ability Synergy: Overguard generated by Light Verse and Triumph are combined into a single pool with two separate maximum values affected by Ability Strength.
- Overguard from Triumph does not apply to rescued hostage in Rescue missions.

Tragedy

- Written with two Dark pages (default 3 twice). Tragedy inflicts 5,000 / 5,500 / 6,000 / 6,500 Slash damage and Stagger to all enemies within story range and in Line of Sight. Enemies hit by Tragedy while debuffed with active Slash, Heat, or Toxin Status Effect will instantly receive the full damage from all damage ticks of the procs, multiplied by 2.25x / 2.5x / 2.75x / 3x; status effects are removed after inflicting damage.
  - Damage is capped at 1 billion.
  - Line-of-sight extends from Dante's model and from the player camera perspective.
    - Enemies directly on screen, ran behind cover moments before the check, those already behind cover with partial body exposure, and standing on different height elevations are all eligible targets.
    - Enemies to the sides and back of the camera view are detected via raycast lines to their head, torso and feet.
    - Line-of-sight check is ignored for enemies within 5 meters of Dante.

Wordwarden

- Written with first Light and last Dark pages (default 2 then 3 ). Wordwarden summons 1 spectral Noctua companion that floats beside Dante and his allied Warframes in story range on cast for its story duration, attacking enemies struck by its warded player's weapons for 35% / 40% / 45% / 50% of the original Noctua's damage amplified by its modded stats, including Status Chance for its equipped Physical and Elemental damage types.
  - Wordwarden fires a homing Noctua energy projectile toward the warded player's target. The projectile has travel time and can be blocked by obstacles in the environment, unless modded with Punch Through stat.
    - Projectile is not affected by Multishot.
  - Targets the enemy last struck by its warded player, firing a maximum of once every 0.333 seconds.
    - Fire rate of 3 is not affected by fire rate bonuses.
    - Wordwarden targets the enemy's head hitbox if the player's attack was a headshot, and otherwise targets the center of the enemy hitbox.
  - Will not use the Alternate Fire and thus cannot trigger Invocation Mods. Will also not trigger Canticle Mods.
  - Can trigger mods and Arcanes such as Archon Stretch (provided the Exalted Noctua has Electricity modded onto it) or Secondary Encumber.
    - Galvanized Shot's damage bonus does not scale correctly. On direct hits and homing fragments, it acts like the base damage is 200 (rather than 125), regardless of ability strength.
- Ability Synergy:
  - Kills from Wordwarden Noctua passively scan enemies into the Codex. Wordwarden Noctua also gains 50% Status Chance against enemies that have been fully scanned.
  - Wordwarden inherits Mods placed on Noctua and splits page fragments on hit that charge the held Noctua's alt-fire.
  - Inherits Noctua's stats, including the effects of Ability Strength on Noctua's base damage.
- Notes:
  - Damage dealt by the extra hit of Xata's Whisper or a Blast status effect can cause Wordwarden to attack.
  - If a Helminth ability is subsumed over Noctua, Wordwarden can still be cast. Ability strength and mods installed on Noctua will still function as normal.

Pageflight

- Written with first Dark and last Light pages (default 3 then 2 ). Pageflight summons 3 spectral Paragrimms with high Threat Level that fly around for the story duration and attack enemies within 30 meters, dealing 150 / 200 / 250 / 300 Slash damage, status, and Stagger. Enemies hit by Paragrimms also receive 35% / 40% / 45% / 50% Status Chance vulnerability and 35% / 40% / 45% / 50% increased Status Damage for 15 / 20 / 25 / 30 seconds.
  - Status chance vulnerability is multiplicative to other sources of status chance, increasing a weapon's total status chance after mods and other bonuses are applied. It does not increase Pageflight's Slash statuses per Paragrimm hit.
    - Does not affect the number of statuses from forced status procs, such as those in many melee combos, Epitaph's cold proc on uncharged shot AoE, or Daikyu's impact proc on hit.
  - Status damage increase is multiplicative to other sources of status damage.
  - Enemies debuffed by the Paragrimms are visually surrounded by an upsurging double helix.
- Pageflight Paragrimms are Summons with diverse properties and behaviors:
  - Invulnerable and intangible, able to phase through enemy attacks, solid entities and obstacles in the environment.
  - Are affected by Summoner's Wrath, Arcane Camisado, and Theorem Infection.
    - Slash status effects from the Paragrimms do not double dip on the Summoner's Wrath bonus, despite it being a faction damage bonus (bug).
  - Fly above Dante when no enemies are detected in range, and return to him when farther away than range.
  - Detect enemies in range without direct line-of-sight.
  - Prefer striking different targets to apply status vulnerability, while able to focus their combined attacks on a lone enemy. Once all enemies in range are debuffed, the Paragrimms prioritize attacking enemies closest to Dante himself.
  - Strike each target by flying through them, then encircling back along their flight path.
- Ability Synergy: Pageflight's status chance vulnerability increases Dark Verse's Slash status stacks per hit.

Maximization

Final Verse
Triumph Overguard on kill/assist: | /2s

 | 2 50 | Recompense Kullervo surrounds himself with daggers. Each dagger that strikes an enemy restores his health, but each dagger that misses an enemy strikes Kullervo, dealing a bit of damage. When Kullervo has max Health, he receives Overguard from struck enemies. Introduced in Update 33.5 (2023-06-21) | Strength:200 / 300 / 400 / 500 Slash damage per dagger hit + 250 / 275 / 300 / 325 HP or Overguard per dagger hit - 20 / 25 / 30 / 35 Overguard or HP drained per missed dagger 10,000 max Overguard
Duration:N/A
Range:5 / 6 / 7 / 8 m dagger orbit radius
Misc: 10 daggers 5 s dagger airtime 1 s invulnerability time 3 daggers max per enemy Slash and Stagger status on hit 3 HP self damage threshold +1 melee combo per dagger hit on enemy

Info

- Kullervo expends 50 Energy to unsheathe 10 daggers that quickly expand into a horizontal orbit spanning 5 / 6 / 7 / 8 meters and surround him for 5 seconds. On cast, Kullervo also becomes Invulnerable for 1 second. When enemies enter the orbit, the daggers home in to stab them, with each individual enemy stabbed by a maximum of 3 daggers; each dagger inflicts 200 / 300 / 400 / 500 Slash damage, with guaranteed Slash and Stagger status effects to its target, then heals Kullervo by 250 / 275 / 300 / 325 Health points or grants him equal Overguard points if already at full health, capped to a maximum of 10,000 Overguard.
  - Health and Overguard points are gained the moment each dagger strikes an enemy.
  - Daggers do not require direct line of sight and will bypass terrain and obstacles in the environment to strike their targets.
- Daggers that strike enemies are removed from orbit, while daggers without targets will gradually turn and sheathe back into Kullervo when Recompense expires, with each dagger damaging him by 20 / 25 / 30 / 35 Overguard points or health points if Overguard is absent. Kullervo cannot be killed by his daggers and remains alive at a minimum health threshold of 3 points.
- Each direct dagger strike against enemies increases Kullervo's Melee Combo Counter by 1 hit.
  - Combo gain is increased by Combo Count Chance effects such as Quickening, True Punishment, Exodia Triumph, and Naramon's Opening Slam.
  - An ascending suspenseful audio cue plays as the daggers turn and fly back to Kullervo.
- Cannot be recast while active.
- Casting Recompense is an upper-body animation that allows movement and Maneuvers while restricting other actions.
- Recompense is dispelled by Kullervo entering an ability nullification zone, which immediately turn his remaining daggers around and sheathe into him inflicting no damage. If Kullervo falls out of bounds, the remaining daggers will inflict damage upon him.
  - Kullervo's earned Overguard cannot be dispelled and lasts until drained by enemy or self damage.

Kit Interactions

- Overguard from Recompense is protected by Wrathful Advance's Invulnerability during wind up.
- Recompense's dagger damage spreads through enemies under Collective Curse when striking a cursed target.
  - Does not count as extra hits to Kullervo's melee combo counter, nor grant extra health or Overguard.

Augment

- Main article: Volatile Recompense

Volatile Recompense is a Warframe Augment Mod for Kullervo's Recompense that has the surrounding daggers continuously rotate around him for a duration while inflicting Blast damage and status.

Rank | Blast Damage | Duration | Cost
0 | 1000 | 10s | 6
1 | 1000 | 15s | 7
2 | 1000 | 20s | 8
3 | 1000 | 25s | 9

Maximization

Volatile Recompense?

Recompense

 | 2 50 | Naraemagi Recover Shields by absorbing Cold Status Effect from nearby enemies. Gain Overguard if at full Shields. Gain Ice for each enemy hit. Introduced in Update 44.0 (2026-09-23) | Strength:40 / 50 / 60 / 75 Shields Restored or Overguard granted 9,000 / 11,000 / 13,000 / 15,000 Overguard Cap
Duration:N/A
Range:10 / 12 / 13 / 14 meters
Misc: +5% Ice per cast +1% Ice per hit

Info

- Narin expends 50 Energy to absorb all Cold Status Effects from enemies within a radius of 10 / 12 / 13 / 14 meters and Line of Sight, restoring 40 / 50 / 60 / 75 Shields per stack of Cold status absorbed. If Shields are full, Overguard is generated instead, up to a cap of 9,000 / 11,000 / 13,000 / 15,000 Overguard.
  - Absorbed Cold statuses are removed from enemies.
  - Naraemagi cannot be cast without at least one Cold-afflicted enemy in targeting range.
  - Does not generate Overshields.

Kit Interactions

- Sangodae ammo guarantees Cold status on primary and secondary weapon attacks for Naraemagi to absorb.
- Neote stacks 10 Cold status to maximize Shields and Overguard generation.
- Hakchum stacks 7 Cold status on landing and 1 per second to continuously enable Naraemagi casting.
- On cast, Naraemagi generates 5% Ice for Nurinarim, plus an additional 1% Ice for each enemy hit by the ability.

Tips & Tricks

- Combine repeated casts of Neote and Naraemagi to rapidly build Ice for Nurinarim.
- Dive with Hakchum to stack 7 Cold statuses on enemies in the landing zone, and use the ice storm to continuously apply Cold status per second, generating a constant supply of statuses for Naraemagi to absorb.
  - Hakchum's ice storm applies Cold to all enemies in range even through walls, allowing Narin to locate nearby hidden enemies via damage numbers.
- Though Naraemagi cannot be cast during Nurinarim, the sword dance's frost aura stacks 2 Cold status per second, allowing Naraemagi to absorb them once Nurinarim is deactivated.
- Pairs well with Arcane Ice Storm as removing cold statuses from enemies allows Narin to immediately reapply more cold status and stack the arcane's effect, rather than needing to wait for the cold status to decay from 10 stacks.

Maximization

Cold procs absorbed:

Naraemagi
Shield or Overguard: | / Cold proc

Localization

Language | Official Translation
(PT) Brazilian Portuguese | Recuperará Escudos ao absorver Efeitos de Status Glacial dos inimigos próximos. Se estiver com os Escudos cheios, Guarda Reforçada será concedida. Também fornecerá Gelo para cada inimigo atingido.

 | 2 50 | Psychic Bolts Nyx unleashes a volley of psychic bolts that track and strike nearby enemies with telekinetic precision. When enemies are slain, additional bolts scatter to new targets. Striking foes weakens their defenses and transfers a portion to Nyx. Introduced in Update 6.0 (2013-01-29) | Strength:20 / 40 / 60 / 80 % (defense reduction) 5 / 10 / 15 / 20 % (Infested speed penalty) 25 (armor steal) 75 (shield steal) 500 (Overguard steal) 1,000 (armor steal cap) 7,500 (Overguard steal cap)
Duration:5 / 7 / 9 / 11 s (defense reduction duration) 20 s (armor steal duration)
Range:N/A
Misc: 3 / 4 / 5 / 6 (number of bolts) 2 (additional bolts on kill) 60 m (targeting range) 100 % (aura nullification) 100 % (defense reduction cap)

Info

- Nyx expends 50 energy to launch 3 / 4 / 5 / 6 flying bolts of telekinetic energy toward her aiming reticle, which psychically seek out nearby enemies within her Line of Sight (based on player camera) and 60 meters. Each psychic bolt dissipates and applies a Stagger on successful hit, temporarily removing enemy Armor and Shields by 20% / 40% / 60% / 80% and Slowing Infested by 5% / 10% / 15% / 20% for 5 / 7 / 9 / 11 seconds. When striking an enemy with armor, shields and/or Overguard, Nyx steals 25 armor per enemy to a cap of 1,000 points while lasting for 20 seconds, 75 shields per enemy and can flow into Overshields, and 500 Overguard to a cap of 7,500 points.
  - An enemy that dies while afflicted by Psychic Bolts will spread 2 additional bolts.
    - Secondary bolts will strike enemies in Line of Sight of the killed enemy.
  - Defense strip is capped at 100% at 125% Ability Strength.
    - Enemies can still gain bonus shield buffs (such as from Shield Ospreys), which are added after the shield strip value. This bonus shield buff can not be removed by Psychic Bolts.
  - Defense steal duration can be refreshed upon stealing additional defenses.
  - Each Enemy can only have defenses stolen once; repeated casts will not provide additional armor, shields, or Overguard if an enemy has been affected by Psychic Bolts before.
  - Slow on Infested units is capped at 80% at 400% Ability Strength.
  - Slow can apply even to enemies with Overguard.
    - Ancient Healers, can remove the Slow effect from all nearby enemies and sometimes themselves.
  - Bolts phase through obstacles in the environment.
  - Bolts will disappear after traveling for a few seconds if they do not strike targets.
  - Bolts will occasionally headshot, triggering universal headshot conditions such as Arcane Precision.
- Can be recast while enemies are still debuffed. Recasting will cancel the effect on previous remaining targets.
- Targeted enemies will briefly radiate energy as a visual indicator, and an audio cue will be played.
- Psychic Bolts is a one-handed action. As such, it can be used while performing various maneuvers and actions without interruption.

Augment

- Main article: Pacifying Bolts

Pacifying Bolts is a Warframe Augment Mod for Nyx that allows Psychic Bolts to temporarily stun enemies and inflict a Radiation status effect, while creating 3 additional bolts.

Rank | Stun Duration | Cost
0 | 4s | 6
1 | 6s | 7
2 | 8s | 8
3 | 10s | 9

Tips & Tricks

- With one player using Corrosive Projection, 100% armor strip can be achieved at 103% Ability Strength.
- With one player using Shield Disruption, 100% shield strip can be achieved at 103% Ability Strength.

Maximization

Pacifying Bolts?

Psychic Bolts
Armor stolen: | /armored enemy
Shield stolen: | /shielded enemy
Overguard stolen: | /Overguarded enemy

 | 2 50 | Iron Skin Rhino hardens his skin, insulating himself from all damage and gaining Overguard. Introduced in Vanilla (2012-10-25) | Strength:400 / 600 / 800 / 1200 (base Overguard) ? / 1.25 / 1.75 / 2.50x (armor multiplier)
Duration:N/A
Range:N/A
Misc: 1.5 / 2 / 3 / 3 s (invulnerability duration)

Info

- Rhino expends 50 energy to harden his skin, receiving Overguard equal to 400 / 600 / 800 / 1200 plus 100% / 125% / 175% / 250% of his total armor. Upon activation, Rhino is invulnerable for 1.5 / 2 / 3 / 3 seconds, during which all incoming damage is absorbed and added to the Overguard.
  - Iron Skin's Overguard uses the following equation: Overguard = ([Base Overguard + (Armor Multiplier × Total Armor)] × Ability Strength) + Absorbed Damage where Total Armor = (Base Armor × [1 + Armor Mods]) + Additive Armor.
    - Note that the base armor value is different between Rhino and Rhino Prime; while Rhino has 240 Base Armor, Rhino Prime has 290 Base Armor.
      - As an example for Rhino:
        - With a maxed Steel Fiber and Intensify, a Rank 3 Iron Skin cast by Rhino will have an initial Overguard of (1200 + (2.5 × 240 × 2)) × 1.3 = 3,120 before absorbing damage.
      - Modifying that equation for Rhino Prime:
        - With a maxed Steel Fiber and Intensify, a Rank 3 Iron Skin cast by Rhino Prime will have an initial Overguard of (1200 + (2.5 × 290 × 2)) × 1.3 = 3,445 before absorbing damage.
  - As the Overguard is tied to the Iron Skin ability buff, ability-nullifying effects will immediately remove it, unlike Overguard gained by Recompense or Secondary Fortifier.
- For Rhino Prime, Iron Skin's visual effects will take into account the chosen accent color.

Kit Interactions

- While Iron Skin is active, damage from Rhino Charge will have a 100% status chance for Blast effects.

Augment

- Main article: Iron Shrapnel

Iron Shrapnel is a Warframe Augment Mod usable in both PvE and Conclave for Rhino's Iron Skin that when active allows it to be detonated by pressing the ability key (default 2 ), unleashing a radial AoE attack that deals a portion of its remaining Overguard as Puncture damage.

Rank | Damage | Detonation Range | Cost
0 | 40% | 8m | 6
1 | 60% | 8m | 7
2 | 80% | 8m | 8
3 | 100% | 8m | 9

Tips & Tricks

- Iron Skin can be removed early by:
  - Entering the bubble of a Nullifier Crewman (Corrupted)
  - Entering the aura range of Combas & Scrambuses
  - Being dispelled by Stalker
  - Falling out of the map.
  - Host Migration
- With a Streamline or Fleeting Expertise mod, Rhino can cast Iron Skin immediately after the first Energy Drain tick in order to give himself a "shield" of sorts.
- It is possible to gain a significant amount of Overguard by standing in the path of a Death Orb beam during the invulnerability phase. Be warned however, as the beam can quickly deplete the extra Overguard if the player does not move out of the way once the invulnerability phase ends.
- Standing below a Jade light produced by Jade light Eximus or the shockwave produced by Blitz Eximus can gain huge amounts of Overguard if timed correctly.
- Using Rhino Charge with Ironclad Charge installed before casting Iron Skin can significantly boost its Overguard by boosting Rhino's armor.
  - Ironclad Charge's armor bonus is applied to Iron Skin as long as Iron Skin's casting was started in the duration of the buff.
    - Iron Shrapnel can help by providing the ability to re-cast Iron Skin at any given time, even with extremely lowered ability duration as long as you cast Iron Skin right after a Rhino Charge.
- Arcane Tanker and Parasitic Armor can also provide significant armor boosts, allowing for large amounts of Overguard when combined with Iron Skin.

Maximization

Current Armor:
Iron Shrapnel?

Iron Skin

Bugs

- Migrating hosts will completely remove Iron skin, regardless of the level it was at.
- If Rhino manages to activate Iron Skin as he falls backwards and enters bleedout, his bleedout timer will reach zero and he will never die. He will remain in bleedout until he is revived.
- Using Iron Skin while on a conveyor would make Rhino immoble.

Mods

- Icy Avalanche
- Intrepid Stand
- Rumbled ( Atlas only)
- Healing Flame ( Ember only)
- Rhythm Guard ( Temple only)
- Pack Leader (Companion only)
- Primed Pack Leader (Companion only)

Miscellaneous

- Arcane Circumvent - 50% of max enemy Overguard stolen on roll, max 10,000 Overguard
- Secondary Fortifier - 1% stolen Overguard on secondary weapon damage, max 15,000 Overguard
- Archgun Deployer - 2,000 Overguard on deployment
- Decree - Killer's Confidence
- Riding Intrinsic Rank 6 - Steadfast Dismount
- Rift Waters

## Notes

- Players with Overguard will be immune to energy draining effects such as the Ancient Disruptor's aura, Disruption's energy drain debuff, Netracells' Exhaustion Keyglyph, Deep and Temporal Archimedea's Concussive Drain and Energy Exhaustion Personal Modifiers.
- When a source of Overguard has a 'maximum' Overguard amount, that source cannot restore Overguard above that level. Combining multiple sources of Overguard does affect max Overguard.

## Sources of Crowd Control

It's taking longer than I calculated.

This page is actively being worked on and may not be completely correct. Please assist in making this page accurate by adding more info. For guidance on performing research, see WARFRAME Wiki:Research.

Note that non-CC effects (e.g. damage, armor/shield removal) of these abilities will still apply to enemies with active Overguard.

This section is transcluded from Buff & Debuff/Debuffs/CC. To change it, please edit the transcluded page.

## Crowd Control Debuffs

Name | Target | Description
Blinded | Enemy | The target is temporarily stuck in a blinded state, staggering backwards and with smoke emitting from their eyes. Finishers can be performed on blinded enemies. Excalibur's Radial Blind Gara's passive Inaros's Desiccation Mesa's Muzzle Flash Mirage's Sleight of Hand and Prism Oberon's Reckoning Revenant's Blinding Reave Wisp's Breach Surge (does not enable Finishers) Out Of Sight Exalted Blade's slide attack Vaykor Sydon's passive While holding Narmer Deacon's Narmer Veil during Archon Hunt
Blinded | Player | The player is temporarily stuck in a blinded state, their HUD is flashed white. Denial Bursa's flash beams
Confusion | Enemy | The target will become confused and indiscriminately attack its enemies and allies. Nyx's Chaos Radiation proc
Converted | Enemy | The target will change side, being friendly to the Tenno and start attacking their own faction. Note that this does not guarantee them being invulnerable to friendly fire by allied Tenno. Nyx's Mind Control Revenant's Enthrall Xaku's The Lost (Accuse sub-ability)
Disarmed | Enemy | The target permanently loses its currently equipped weapon, with slight differences depending on the unit affected. Baruuk's Desolate Hands and most attacks of Serene Storm Khora's Venari when set to Protect posture Loki's Radial Disarm Mag's Magnetized Discharge Titania's Spellbind Xaku's Grasp of Lohk Halikar ( Wraith) when thrown Disarming Purity mod for the Panthera/ Panthera Prime Chesa Kubrow's Neutralize Repo Audit for Hounds Zenurik's Disarming Sling
Disarmed | Player | Applied to players, Disarm removes the weapon currently held by the Warframe. The player can still switch to any remaining weapons they may be carrying. The Warframe's disarmed weapon will be dropped on the ground, indicated by a yellow waypoint, and can be retrieved. Players will not lose their disarmed weapon should they fail to retrieve it before completing the mission. Grineer Drahk Masters, who use the Halikar
Jammed | Enemy | The target's guns are jammed, forcing them into an animation where they try to unjam their guns. Mag's Counter Pulse Mesa's Shooting Gallery
Knockdown | Enemy | The target is knocked off their feet and falls on their back. Ground Finishers can be performed on these enemies. Atlas' Titanic Rumbler Banshee's Sonic Boom Excalibur's Slash Dash Gauss' Mach Rush Garuda's Dread Mirror Gyre's rolling Coil Horizon Hydroid's Tempest Barrage Khora's Venari (Protect posture) Limbo's Banish Mag's Magnetize Nezha's Divine Spears Nova's passive, Neutron Star, and Molecular Prime Oberon's Smite and Reckoning Revenant's passive Rhino's passive Zephyr's Tail Wind (Dive bomb) Heavy Impact Sunika Kubrow's Savagery Lambeo Moa's Shockwave Actuators Arcane Eruption Jumping + sliding into an enemy Hard Landings Cobra & Crane air attacks Archgun Deployer
Knockdown | Player | The player is knocked off their feet and falls on their back. Grineer Commander (Elite Shield Lancer) Shield Lancer Scorpion Hellion Bailiff Bombard Heavy Gunner Napalm Nox Ghoul Devourer Mordda Turret Corpus Shockwave MOA Anti MOA Railgun MOA Mine Osprey Amalgam Satyr Laser Barrier Infested Leaper Swarm Mutalist MOA Tar Mutalist MOA Ancient Disruptor Ancient Healer Toxic Ancient Juggernaut (Behemoth) Other Conculyst
Paralyzed, Disabled, Stuck | Enemy | The target is stuck in a particular position. Atlas' Path of Statues, Petrify and Rumblers' initial cast Frost's passive, Freeze's direct hit, Snow Globe if the target is inside the bubble when the ability is activated, Chilling Globe and Avalanche. Gara's Mass Vitrify's expansion phase. Garuda's Blood Altar Harrow's Condemn Hildryn's Aegis Storm Inaros' Scarab Swarm Khora's Ensnare Limbo's Stasis Mag's Fracturing Crush Nidus' Parasitic Link Rhino's Rhino Stomp Vauban's Bastille Volt's Discharge Wukong's Celestial Stomp Xaku's The Lost (Gaze sub-ability) Sahasa Kubrow's Ferocity Sunika Kubrow's Savagery and Unleashed Exodia Epidemic Vitrica's glassing ability
Paralyzed, Disabled | Player | The player is stuck in a particular position. Manic Nauseous Crawler Void Angel's impaling ground slam, also forcing the Operator/Drifter out of their Warframe
Ragdolled | Enemy | The target is immediately sent to a ragdoll state. Atlas' Landslide (every third sucessive strike) and Tectonics Banshee's Sonic Boom Gauss' Mach Rush and Redline Gyre's detonated Coil Horizon Hydroid's Tidal Surge Khora's Whipclaw Mag's Pull Nekros' Soul Punch Rhino's Rhino Charge Valkyr's Rip Line Vauban's Minelayer (Tether coil) Yareli's Riptide Zephyr's Airburst Wyrm's Crowd Dispersion Harpak's alt fire Paracyst's alt fire Sonicor Kestrel's charged attack Any melee ground slam attack Void Sling Vazarin's Void Snare
Sleep | Enemy | The target is in a standing sleeping state and will not perform any action. Baruuk's Lull Equinox's Rest & Rage (Rest) Ivara's Quiver (Sleep arrow) Aero Mod Set bonus Normal hits from Cobra & Crane if wielded by Baruuk Magus Lockdown
Slowed | Enemy | The target's movement and actions are slowed. Chroma's Spectral Scream, Elemental Ward, and Effigy (Cold) Equinox's Peaceful Provocation Frost's Freeze, Ice Wave, Ice Wave Impedance, and Snow Globe Nekros' Creeping Terrify Nova's Molecular Prime Sevagoth's Gloom Titania's Tribute (Entangle buff) Valkyr's Warcry Xaku's The Vast Untime Cold proc Coolant Leak Endoparasitic Vector Artax In addition, the following slows count as time disruption, which is not prevented by Overguard: Rhino's Rhino Stomp Zenurik's Temporal Drag
Slowed | Player | The player's movement and actions are slowed. All Ghoul enemies upon death (Toxic clouds that proc Cold) Any enemy wielding a Glaxion like some Corpus Targets Denial Bursa's energy orbs Scyto Raknoid Tar Mutalist MOA's thick tar Maggot Cold proc Equipping a Hobbled Dragon Key
Stagger | Enemy | The target is momentarily staggered, interrupting their current action. Ash's Smoke Screen Banshee's Sound Quake Chroma's Elemental Ward (Electric) and Effigy Equinox's Mend & Maim (Maim) Excalibur's Radial Javelin Garuda's Dread Mirror, Blood Altar, and Seeking Talons Gauss' Kinetic Plating while Redline is active Hildryn's Haven Loki's Decoy (when decoy shoots at enemies), Switch Teleport, and Radial Disarm Mesa's Staggering Shield Nezha's Warding Halo Nidus' Virulence Nyx's Pacifying Bolts and Chaos Octavia's Resonator Revenant's Mesmer Skin Rhino's Piercing Roar Saryn's Miasma Trinity's Energy Vampire Vauban's Tesla Nervos Volt's Shock and Shocking Speed Wisp's Reservoirs (Shock mote) Xaku's The Lost (Accuse sub-ability) Yareli's Aquablades Acidic Spittle Live Wire Pounce Opticor ( Opticor Vandal) Electricity proc Impact proc
Stagger | Player | The player is momentarily staggered, interrupting their current action. Commander Roller Melee parries by Bailiff and Guardsman Volatile Runner Kyta Raknoid Upon breaking Reinforced Glass on Corpus Ship tilesets
Stun | Enemy | The target is momentarily stunned, interrupting their current action. Players can perform front/back Finishers on stunned enemies. Ash's Teleport Banshee's Silence Valkyr's Paralysis Wukong's Cloud Walker Paralytic Spores Retribution Caustacyst's charged attack Sigma & Octantis's air attack Tatsu's seeking projectiles (passive) Zakti's dart's explosion Charged attacks with any Sparring melee Naramon's Sling Stun Justice effect from Steel Meridian weapons/mods
Suspended, Incapacitated | Enemy | The target stays in an extended ragdoll state midair (or underwater) and it is unable to move. Hydroid's Undertow and Tentacle Swarm Inaros' Sandstorm Khora's Strangledome Mag's Crush Nidus' Larva Titania's Spellbind and Lantern Trinity's Well of Life Vauban's Bastille Zephyr's Tornado Desert Wind's slide attack Orvius's charged attack
Taunt/Attracted | Enemy | The enemy will have its attention diverted towards the target with the higher Threat Level. Atlas' Titanic Rumbler Gara's Spectrorage Khora's Strangledome Loki's Decoy Mirage's Hall of Mirrors Nekros' Shadows of the Dead Nidus' Ravenous Nyx's Chaos and Absorb Octavia's Mallet Saryn's Molt Titania's Razorwing Wukong's Defy Guardian Derision The target will halt its current action and mindlessly move towards a point. Ivara's Quiver (Noise arrow when enemies are unalerted) Titania's Lantern Djinn's Fatal Attraction
Terrified | Enemy | The target is terrified and tries to run away from the caster. Nekros' Terrify Raksa Kubrow's Howl

## Bugs

- Blocking with melee weapons will not build the combo counter or prevent damage while Overguard is active.
- Auto block and manual block with melee equipped disabled during Overguard.

## Patch History

Update 42.0 (2026-03-25)

- Fixed player Overguard being able to take damage during invulnerability caused by Nyx’s Absorb, Excalibur’s Slash Dash, Dagath’s Rakhali's Cavalry, and Qorvex’s Crucible Blast.
- Fixed boss fights with multiple targets (ie. Prime Vanguard) sharing the same Overguard bar and Status Effects in their HUD health indicators, instead being visually distinct from one another.
  - Also fixed vertical alignment issues between bosses’ health bars when changing resolution.

Update 38.5 (2025-03-19)

- Bolstered Badguys gives 75% less Overguard to Techrot Babaus.
- Reduced the duration of Overguard provided by Ancient Protectors from 20s to 15s. This Overguard will now also decay 3s after the Ancient has died, if the remaining duration is longer than 3s.
  - Also prevented all Ancients from receiving Overguard from Ancient Protectors (including the Ancient Protector themselves).
  - Enemies with innate Overguard can no longer receive Overguard from the Ancient Protector's ability.
  - Related fixes:
    - Fixed staggers and other animation-breaking states not preventing the Overguard ability from being cast.
    - Fixed Ancient Protectors being able to cast their Overguard ability while in Grendel's stomach.
- Updated tooltip for Magnetic Status to communicate the bonus damage against Overguard.
- Fixed Overguard not applying to The Severed Warden’s arms.

Hotfix 38.0.8 (2025-02-06)

- Fixed Ancient Protectors giving Overguard to the spectral forms of Thrax Centurion and Thrax Legatus.

Hotfix 38.0.6 (2025-01-09)

- Fixed Companions not dying after triggering Sacrifice and Martyr Symbiosis if they have Overguard.

Update 37.0 (2024-10-02)

- Celestial Stomp no longer stuns crowd control-immune enemies, such as Eximus units, to bring Celestial Stomp in line with similar crowd-controlling abilities.
- Molecular Prime Changes:
  - Added a Tap / Hold functionality: Tap to cast a Slowing effect on enemies. Hold to cast a Speed-Up effect instead.
  - Bonus damage multiplier now applies to Overguard, Health, and Shields.
    - Previously it only applied to enemy Health!
    - This multiplier has also been added to the Ability screen so players can better understand Molecular Prime’s mechanics.
  - Speed-Up effect will bypass crowd control immunity (ex: enemies with Overguard).
- Unleashed (SUNIKA Kubrow):
  - Instead of targeting "VIP" enemies, a category which is somewhat poorly defined and doesn't come up very often, this will now target Eximus units, doing 300% damage against Overguard.
- Beast melee Postures! Have you ever wished to have a little more control over specifically how your pet chooses to engage with enemies? Then check out these new melee Posture Mods that shape the behavior of your Beasts:
  - Assassin Posture: Your pet will prefer to attack Eximus and VIP enemies. Increases damage to Overguard done by your pet by 300%.
    - Can be acquired with Conservation tags from The Business’ “Trade Tags” menu in Fortuna, Venus.
- The following abilities now apply their Damage Vulnerability against enemy Shields and Overguard (previously they only applied to enemy Health):
  - Xaku’s Vast Untime
  - Mag’s Magnetize
  - Titania’s Beguiling Lantern Augment
  - Bonewidow’s Firing Line
  - Gara’s Mass Vitrify
  - Gara’s Splinter Storm
  - Nezha’s Blazing Chakram
  - Nova’s Molecular Prime

Hotfix 36.0.5 (2024-07-20)

- Fixed Overguard preventing players from parrying.

Update 36.0 (2024-06-18)

Magnetic

Magnetic has received a few buffs to increase its effectiveness against Shields and to hammer home the power fantasy of overloading enemy Shields.

Magnetic Changes:

- Upon Shield/Overguard Breaking a target, the enemy will now be dealt Electric Status damage for a percentage of Max Shields/Overguard per Magnetic stack while also forcing an Electric Status Effect.
- Magnetic stacks on an enemy with Overguard now allow for bonus damage to Overguard, similar to how Magnetic affects Shields.

Ember Changes

Fire Blast (3rd Ability):

- Augment Mod Changes:
  - Healing Flame: Now converts all over healing (gaining Health points while as max Health) into Overguard.
    - Description now reads: “Each enemy hit heals by 25 to 50 depending on current Immolation level. With Ember, over healing grants you Overguard.”
    - This only applies to Ember herself and not to Fire Blast on other Warframes via Helminth.

Stat UI Changes & Fixes

- Added a Void Damage tooltip in the Operator stats UI to show its efficacy stat and Status Effect description.
  - Now reads: “Damage Efficacy: X damage to Zariman.
  - Status Effect: Highly effective against enemies with Overguard Health and Sentients as it resets their damage adaptation. Void creates a bullet attractor sphere on the target that attracts and concentrates further attacks.”.
  - Added an Overguard tooltip to Rage, Archwing, Necramech and Hunter Adrenaline Mods, due to their new interactions with Overguard as of Update 35.5.6.

TOP FIXES

- Fixed the Pack Leader Mod reducing the amount of Overguard on a Companion if they already have the Mod's max amount (+1200).
- Fixed being able to apply 5 Puncture Stacks to VIP enemies with Overguard, instead of the intended 3.

Update 35.6 (2024-05-15)

- Fixed players with Overguard being affected by the Gruzzling’s slow AOE.

Hotfix 35.5.6 (2024-04-10)

Updated Overguard Interactions With Vex Armor, Rage, & Hunter Adrenaline

As announced last week, we’ve changed how Overguard interacts with effects that benefit from receiving damage on Warframe to make it more co-op friendly. Specifically, Chroma’s Vex Armor and the Rage and Hunter Adrenaline Mods. The conversations regarding Dante’s abilities with Overguard became a driving factor to look at these interactions and find ways in which we can make them work to benefit co-op play. Overall, these changes aim to create a harmonious arrangement between the often unpredictable Overguard gains from allies and Vex Armor, Rage, and Hunter Adrenaline.

The following changes are in addition to their existing functionality.

Chroma’s Vex Armor

Previously, Overguard would prevent Chroma from benefiting from his Vex Armor buffs (since it blocked damage on Health and Shields). So, we’ve made the following change to allow players to receive the buffs through all sources of Overguard:

Now: Melee kills now grant a 15% Armor increase and ranged kills a 15% increase to Weapon Damage (doubled to 30% for ranged weak point kills).

This has the additional perk of self-sufficiency where players have far more control over the buffs, instead of having to rely on the unpredictability of damage dealt by enemies.

Rage and Hunter Adrenaline

Previously, Overguard granted by allies could prevent you from gaining Energy from these Mods (since it blocked damage dealt to Health). So, in an effort to create a more co-op friendly experience between the two, we’ve made the following change:

Now, Rage and Hunter Adrenaline can convert the Damage on Overguard granted by allies to Energy while Shields are inactive.

More specifically, they will trigger when the last source of Overguard originates from an ally (includes spawned allies, such as Specters). This allows shield-less Warframes, such as Inaros and Nidus, to be able to regenerate Energy via these Mods when they would have previously been blocked by Overguard granted by allies.

Here are the exact stat details:

- Rage: +40% (same effectiveness as the base functionality) of Damage on Overguard granted by allies to Energy while Shields are inactive.
- Hunter Adrenaline: +45% (same effectiveness as the base functionality) of Damage on Overguard granted by allies to Energy while Shields are inactive.

NOTE: Warframes that grant themselves Overguard, like Kullervo or Rhino, will not be able to trigger Rage and Hunter Adrenaline from their own Overguard. Only Overguard granted by allies is eligible because this is the only interaction that is potentially disruptive to your build (i.e your ally puts Overguard onto your Rage-Build Nidus).

Necramech Rage and Kinetic Diversion (Archwing) have also had the same changes applied to them with Overguard interactions:

- Necramech Rage: Convert +15% of Damage on Overguard gained from allies to Energy.
- Kinetic Diversion: Convert +40% of Damage on Overguard gained from allies to Energy.

General Overguard Change:

- Frost’s Icy Avalanche Augment Mod will now grant Overguard to non-player allies in radius (i.e. Sentinels, Companions, Specters).

Hotfix 35.5.3 (2024-04-04)

Missed Notes from Update 35.5.0:

Observant Tenno may have noticed some Abilities are no longer interacting with Crowd Control immune foes the same way. This is due to a change that went out with Dante Unbound, but was unfortunately missed in Patch Notes. These particular interactions fell outside of the intended design of CC immunity, so we have removed these outliers to restore expected behaviors.

Enemies with Crowd Control immunity (ex: Overguard) have had the following interactions removed:

- Frost's Ice Wave Impedance Augment (specifically the frozen trail that slows them)
- Rhino’s Stomp (slow effect)
- Primary Obstruct (weapon jamming)
- Exodia Epidemic (enemy suspension)
- Zenurik Temporal Drag (slow effect)
- Wisp’s Breach Surge (blind)
- Halikar (disarm)
- Mesa’s Muzzle Flash (blind)
- Proboscis Cernos (stun and pull)
- Mag’s Counter Pulse Augment (robotics disabling and disarm)
- Mag’s Fracturing Crush Augment (immobilization)
- Malicious Code (immobilization)

Player Overguard Changes:

- Players with Overguard will no longer be pulled towards Trauma Clamps in the Undercroft.

Update 35.5 (2024-03-27)

- Fixed the Rakta Dark Dagger and Sancti Magistar not giving Shields and Health respectively for damage dealt to enemy Overguard (it previously only counted damage dealt to enemy Shields & Health).

Hotfix 35.1.2 (2024-02-28)

- Players with Overguard are now immune to the slow effect from enemy Necramech’s Necraweb ability.
- Fixed Overguard earned on Warframe in Duviri from the Killer’s Confidence Decree causing players to be indefinitely invulnerable in the Undercroft.
  - Now, Overguard earned from the Decree will be cleared from Warframe after entering the Undercroft.

Hotfix 34.0.6 (2023-10-30)

- Fixed enemies with Overguard being pulled by Magus Anomaly.
  - Enemies with Overguard are immune to crowd control abilities/effects, and should not be affected by Magus Anomaly until after Overguard has been removed.

Update 34.0 (2023-10-18)

- Companions can now gain Overguard (behaves the same as player Overguard).
- Gaining Overguard now provide more gradual feedback in the health bar instead of instantly changing.
- Fixed Overguard disappearing from the UI while riding K-Drive/Merulina.
- Fixed enemies with Overguard being affected by the Malicious Code Parazon Mod when they should be immune to crowd control effects.

Hotfix 33.6.4 (2023-08-15)

- Player Overguard now protects against Arctic Eximus’ slow auras.
- Overguard granted by Styanax’s Intrepid Stand Augment Mod is now capped at 15k (at 100% Ability Strength), which scales with Ability Strength.
  - Outside of maintaining the status quo (excluding Rhino’s Iron skin, which requires skillful timing to scale), the Augment allowed for infinite amounts of Overguard to be stacked effortlessly and quickly, which could trivialize challenging content and limit future design space. The survivability and team support element that players have been enjoying on Styanax is still preserved, just at a more practical level to encourage more dynamic play.
- Overguard granted by Frost’s Icy Avalanche Augment Mod now stacks on cast (up to 15k, which scales with Ability Strength) instead of keeping the highest value from the original or recast.

Update 33.6 (2023-07-27)

Player Overguard Improvements

With Duviri came the first instance of Warframes using Overguard, and The Seven Crimes of Kullervo solidified this mechanic as a part of various Warframes’ kits.

Now that players have access to Overguard consistently, we have made some adjustments to improve the quality of life in this new health state:

Consistent Proc Immunity Due to the variety of sources of Overguard, there were occasionally inconsistencies in how it behaved in regard to Proc Immunity. With Echoes of Duviri, all sources of Player Overguard will offer Full Proc Immunity while active.

Overguard Depletion Protection Similar to Shields, Player Overguard will now offer a brief moment of invulnerability (currently 0.5s) once depleted. This window will prevent players with Overguard from being one-shot, as damage to Overguard will no longer carry over into your Health or Shield pool once depleted.

Upon launch, we will closely monitor feedback on this mechanic change to see if further adjustments are needed.

NOTE: This Overguard Depletion Protection applies only to Player Overguard, not Overguard seen on enemies.

Hit Impact Visuals Similar to taking damage to your Health or your Shields, Overguard now has its own unique appearance when attacked. Damage will no longer cause blood splatters while Overguard is active, and we have added a unique metallic hit effect that better communicates having a layered shell protecting you.

Additionally, players will no longer flinch while taking damage with Overguard active.

(NOTE: This has no gameplay function other than looking cool)

Hotfix 33.5.3 (2023-06-23)

- Fixed moving in slow motion after interacting with ally slowing effects (like Vauban’s Vortex and/or Zephyr’s Tornado) while Overguard is active.
  - This was particularly prevalent with Rhino (Iron Skin), Frost (with the Icy Avalanche Augment Mod), Kullervo (Recompense), and Atlas (Rumbled Augment Mod) as their abilities grant Overguard.
- Fixed several issues with Warframe Overguard reducing the effectiveness of the following supportive abilities/effects:
  - Fixed Gara’s Splinter Storm damage reduction being capped at 50% instead of the intended 90%.
  - Fixed Trinity’s Blessing healing over time for a fixed amount instead of restoring the full intended amount on cast.
  - Fixed Garuda’s Blood Altar not healing.
  - Fixed Mirage’s Eclipse damage reduction being capped at 50% instead of the intended 95%.
  - Fixed Hydroid’s Curative Undertow Augment Mod being capped at 100 Health.
  - Fixed Nezha’s Warding Halo damage reduction being capped at 50% instead of the intended 90%.
  - Fixed Volt’s Capacitance Augment Mod (Discharge) being capped at 250 Shields and not granting Overshields.
  - Fixed Baruuk’s Desolate Hands damage reduction being capped at 50% instead of the intended 90%.
  - Fixed Harrow’s Penance heal being capped at 50 health/s.
  - Fixed Equinox’ Mend & Maim heal being capped at 500 Health over 5 seconds.
  - Fixed Sancti Magistar’s heal being capped at 500 Health over 5 seconds.
  - Fixed Vazarin’s Protective Sling capping at 500 Health over 5 seconds and not providing damage immunity.

Update 33.5 (2023-06-21)

OVERGUARD ON WARFRAME ABILITIES

Overguard as a Warframe defense mechanism was introduced in Drifter Intrinsics and Decrees with The Duviri Paradox update - it grants additional Health protection and provides Knockdown Immunity while active.

Overguard has virtually the same function (Health buffs and immunities*) as the listed abilities and Augment Mods, so in an effort to expose the mechanic more and establish familiarity with Overguard as a whole (as it also appears on enemies) we have made it the visual indicator for them.

- Rhino’s Iron Skin
- Atlas’ Rumbled Augment Mod
- Frost’s Icy Avalanche Augment Mod

*The base defensive properties of these abilities and Augment Mods have not changed!

This change also has the added benefit of allowing “On Damaged” Mods and Arcanes to apply to all of the above! Prior to this change, the aforementioned abilities would make the player "invulnerable" until the added survivability was depleted. Now, Mods and Arcanes like Adaptation and Arcane Avenger can now be triggered when damage is taken to Overguard, because it is treated similarly to Health and Shields.

The HUD Overguard element has also had slight upgrades for the purposes of registering for these abilities and Augment Mods:

Hotfix 33.0.11 (2023-05-24)

- Fixed Grendel’s Regurgitate slowing enemies with Overguard.
  - Enemies with Overguard are intended to be immune to slow effects. However, if Overguard is cleared while Regurgitate’s slow is active, then it will apply to the target for the remaining duration.

Update 33.0 (2023-04-26)

- Fixed Dethcube’s Vaporize Mod not respecting Overguard’s crowd control immunity and bypassing their defenses to deal damage.

Update 32.3 (2023-02-15)

- Fixed the Parazon Mercy Kill Health threshold UI indicator showing over Overguard if you hit an enemy with enough Impact procs (which was confusing since you cannot Mercy Kill enemies with Overguard active).

Hotfix 32.2.4 (2022-12-07)

- Fixed rare case of inconsistent damage being dealt to Overguard.

Hotfix 32.0.3 (2022-09-14)

- Updated the Overguard depletion sound FX on Eximus units.

Update 32.0 (2022-09-07)

OVERGUARD LIFESTEAL CHANGES:

On the introduction of Overguard, we mentioned that we would be improving how some ability mechanics function with Overguard, this is a continuation of those efforts. So we have made several changes, the majority of which cover how Overguard reacts with lifesteal.

- Fixed Garuda's Blending Talons Augment not triggering when hitting an enemy with Overguard is affected by a Slash Status Effect.
- Fixed Gauss's Kinetic Plating not generating battery when melee attacking enemies with Overguard.
- Fixed Protea's Temporal Anchor not counting damage to Overguard when building up damage for the temporal implosion blast.
- Fixed Zephyr's Tailwind Target Fixation Augment not counting enemies with Overguard when building up extra damage.
- Fixed Hema not restoring health on headshots against enemies with Overguard.
- Fixed Hirudo not restoring health on critical hits against enemies with Overguard.
- Fixed enemies affected by Frost’s Avalanche not losing any armor while Overguard is active.

If there are any other cases where Lifesteal isn’t applying from Overguard, please let us know on the Forums and we will take a look!

Update 31.6 (2022-06-09)

- Modified Overguard ratios to bring Eximus Units Overguard down and slightly increase their Health/Shields to balance out the reduction.
  - Reduced Eximus Overguard by 50% and transferred the 50% to their Health pool.
    - While this may read as a big increase to the Health pool, it is not a 1-to-1 trade due to the overall pool sizes of Overguard vs Health. Imagine you have a watermelon (Overguard) and half an orange (Health). I take away half a watermelon and I give you half an orange - and together we eat a fruit salad. For clarity: Overguard has a larger pool than Health, so reducing it by half still amounts to less HP across Eximus Units across all HP values. By increasing the amount of Health and Shields an Eximus Unit has, it also increases the window for successful Mercy kills.
  - Increased Shield Scaling multiplier by 50%
- Nox Eximus Helmets can now be destroyed when Overguard is active. Breaking their helmet will remove Overguard entirely!
  - Note that Nox Damage resistance has been decreased and armor increased to balance this change. This change applies to both Nox Eximus and base Nox enemies.
- Fixed Overguard counting as Health and taking damage from Viral Status Effect.
  - Overguard situates itself in a new category of “protection”. It differs from Shields, Armor, and Health. That said, Viral Status Effects affecting Overguard was unintentional and has been changed to not only fit the original design for Viral damage, but also Overguard.
    - We originally mentioned in the Eximus Reborn Dev Workshop that the only Status Effect that would work on Eximus while Overguard is present is Cold Status Effects (up to 4 stacks!).
- Lifesteal now works on damage dealt to Overguard.
  - Considering Overguard is another health pool for an Eximus/Thrax and that Lifesteal already works on Health and Shields, Overguard is now susceptible to Lifesteal to give players another way to tactically engage with them. The fights with Eximus can be quite challenging, so having another avenue of survivability is always encouraged!
    - This change was also made in mind to Lifesteal survivability builds, it would be too difficult to lose all of your survivability when encountering many enemies with Overguard at one time (from either Void Armageddon or an Ancient Protector etc.)
    - Additionally, there are some Weapons and abilities that aren’t strictly classified as Lifesteal that won’t currently work, but will in a future update! This currently affects specific conditions for the:
      - Hema
      - Hirudo
      - Garuda’s Blending Talons augment
      - Gauss’ Kinetic Plating
      - Protea’s Temporal Anchor
      - Zephyr’s Target Fixation augment
    - If there are any other cases where Lifesteal isn’t applying from Overguard, please let us know on the Forums and we will take a look!
- Fixed Baruuk being unable to damage Eximus units with his Serene Storm waves.
- Kuva Trokarian enemies are receiving some changes to make them feel like more of a threat when they appear in-mission.
  - Similar to their Thrax compatriots, these foes are intended to add an extra level of difficulty to the player’s gameplay loop, so these tweaks are made with that goal in mind.
    - Added Overguard to the Kuva Trokarian (but at a lesser value than the Eximus Overguard)

Hotfix 31.5.8 (2022-05-11)

- Fixed Equinox’s Maim being able to chain stagger Eximus units with Overguard active.
  - Overguard as it was designed is resistant to CC, any form of stagger proc present with Warframe abilities is unintended at this time. It’s worth noting that we’re exploring some options on the topic of Overguard and its CC resistance.
- Fixed the Aero mod set bonus putting to sleep ability immune enemies (Eximus with Overguard).

Update 31.5 (2022-04-27)

- Introduced.
