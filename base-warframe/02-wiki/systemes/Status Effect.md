# Status Effect (wiki)
Source : https://wiki.warframe.com/w/Status_Effect

Status Effect

Health bar of an Elite Lancer with a single Impact proc, a Cold proc, and four Radiation procs

Values over 100% have a chance to inflict multiple Status Effects at once.

—In-game Description

A Status Effect, or commonly called a Proc, is an additional effect which may be triggered at random by a hit from a weapon or Warframe ability. Status Chance is the probability that a hit will inflict a status effect. The base duration of the Proc will depend on its type, and whether the target is an enemy or another Tenno. Warframe abilities usually have a high chance to proc, or in some cases, greater than or equal to 100% chance to inflict their status effect (e.g. Frost's Ice Wave ability).

Each damage type is associated with a status effect. Weapons that deal multiple damage types will have a separate chance to inflict its associated status effect on a target, and only one damage type can proc per hit, unless status chance is over 100%. These multiple status effects can also be referred to as Unique Status Effects.

For example, a weapon such as an unmodified Staticor deals solely Radiation damage. In addition to its damage, the Staticor also has a 28% status chance on each shot to cause a proc. On a successful proc, the enemy will receive the Radiation status effect, which causes Confusion over the duration of the effect.

Enemies also possess the ability to inflict status effects on players. For example, a Grineer Scorch has a chance to inflict the Ignite status effect with the Heat damage from his Ignis. Similarly, enemies are also able to inflict physical procs such as Bleeding (associated with Slash damage) bypassing the player's armor. Several Warframe abilities will grant immunity to status, (e.g. Oberon's Hallowed Ground ability). Any amount of Overguard will grant immunity as well.

## Status Effects

### General

Damage Type | Status Effect Internal Name | Status Effects
Impact | PT_KNOCKBACK | Knockback On Enemy: Causes target to flinch and staggers movement for 1 second and increases the health threshold at which they can be Parazon Mercy Killed by 8% per proc. Stacks up to 5 times. On Player: No effect.
Puncture | PT_FRAILTY | Weakened On Enemy: Reduces any damage dealt by 40% for 10 seconds. Stacks up to 5 times, with subsequent procs reducing damage by 10% to a total of 80%. The victim receives 5% increased weapon Critical Chance per proc up to 25% at max stacks. This bonus is additive after mods, but does not apply to area of effect damage or Warframe abilities. On Player: Reduces any damage dealt to 30% for 10 seconds.
Slash | PT_BLEEDING | Bleed On Enemy: Deals 35% of the base damage per second over 6 seconds. This damage bypasses Armor. On Player: Deals 10% of the base damage per second over 6 seconds. This damage bypasses Armor.
Heat | PT_IMMOLATION | Ignite On Enemy: Deals 50% of the base damage as Heat damage per second over 6 seconds while causing the target to panic for 4 seconds and gradually stripping up to 50% Armor. On Player: Deals 50% base Heat damage over 6 seconds and strips up to 50% Armor.
Cold | PT_CHILLED | Freeze On Enemy: Reduces Movement Speed, Fire Rate, and Attack Speed by 50% for 6 seconds. Stacks up to 10 times, with subsequent procs increasing slow by 5% to a total of 90% on the 9th stack. The target receives +0.1 increased Critical Multiplier on initial proc and +0.05 per subsequent proc to a maximum of +0.5 on the 9th stack. This bonus is additive after mods, but does not apply to area of effect damage. On the 10th stack, enemies become frozen solid, their Shield recharge is negated, and their received Critical Multiplier is increased to +1.0, for 3 seconds. On Player: Reduces Movement Speed, Fire Rate, and Attack Speed by 25% for 6 seconds.
Electricity | PT_ELECTROCUTION | Tesla Chain On Enemy: Deals 50% of the base damage as Electricity damage per second over 6 seconds to enemies within 3 meters of the target and stuns the affected target for 3 seconds. On Player: Deals 50% base Electricity damage to allies within 3 meters of the target.
Toxin | PT_POISONED | Poison Universal: Deals 50% of the base damage as Toxin damage per second over 6 seconds. This damage can bypass Shields.
Blast | PT_FLASHBANG | Detonate On Enemy: Deals 30% of base damage after 1.5 seconds. On maximum 10 stacks or when the target dies, premature detonation occurs and all stacks are dealt simultaneously as enemies within 5 meters are dealt 300% of base damage per proc. The increased damage from premature detonation only applies to surrounding enemies hit by the explosion, but not the initial target.
Corrosive | PT_CAUSTIC_BURN | Corrosion On Enemy: Reduces armor by 26% for 8 seconds. Stacks up to 10 times, with subsequent procs reducing armor by 6% to a total of 80%. On Player: Reduces armor by 26% for 8 seconds.
Gas | PT_ASPHYXIATION | Gas Cloud Universal: Deals 50% of the base damage as Gas damage per second over 6 seconds in a 3 meter radius. Stacks up to 10 times, with subsequent procs increasing radius by 0.3 meters to a total of 6 meters.
Magnetic | PT_MAGNETIZED | Disrupt On Enemy: Amplifies damage dealt to Shields and Overguard by 100% and nullifies shield regeneration for 6 seconds. Stacks up to 10 times, with subsequent procs increasing damage to shields by 25% to a total of 325%. On removing Shields or Overguard, inflict an Electricity proc equal to 3% of the target's maximum shields/overguard per Magnetic stack to a maximum of 30%. On Player: Amplifies damage dealt to shields by 100%, nullifies shield regeneration, drains 20 Energy per second and scrambles the interface for 4 seconds. Due to player overguard granting status immunity, procs do not result in additional damage.
Radiation | PT_RAD_TOX | Confusion On Enemy: Attacks any closest enemy and will be attacked in return while dealing 100% additional damage to allied units for 12 seconds. Stacks up to 10 times, with subsequent procs increasing damage by 50% to a total of 550%. On Player: Reduces firing accuracy, able to damage and be damaged by allies for 4 seconds.
Viral | PT_INFECTED | Virus On Enemy: Amplifies damage dealt to health by 100% for 6 seconds. Stacks up to 10 times, with subsequent procs increasing damage to health by 25% to a total of 325%. On Player: Amplifies damage dealt to health by 100% for 6 seconds.
Void | PT_RADIANT | Bullet Attractor On Enemy: Creates a 2.5 meter radius field which attracts projectiles for 3 seconds.
Tau | PT_SENTIENT | Status Vulnerability On Enemy: The victim receives 10% increased Status Chance per proc for 8 seconds up to 100% at 10 stacks.
True | N/A | No status effect.

### Independent from Damage

It's taking longer than I calculated.

Hidden status effects need more research

Very well. Keep your secrets.

This article/section contains unofficial information, concepts, or terminology derived from or based on community discussion, invention, or knowledge. It may be subjective and contain information or terminology that is not used by Digital Extremes or in official WARFRAME communications, and may not be an officially recognized concept.

Status Effect | Internal Name | Description
Big Stagger | PT_BIG_STAGGER | Universal: Target is staggered for a longer duration. Can be applied by 5 stack of Impact, as well as Opticor, Opticor Vandal, Vulkar, and Vulkar Wraith.
Countered | PT_COUNTERED | On enemy: Target recoils from a parry, opening them to Finishers. Only from parries performed by the Drifter in Duviri.
Disarmed | PT_DISARMED | Universal: Target is disarmed of their equipped weapon. Can be applied by Halikar and Halikar Wraith?
Impair (PvP only) | PT_ROOTS | Universal: Restricts the target's movement for 2 seconds, disabling jumps and decreases movement speed. After Impair duration ends, players will be immune to the same status effect and knockdowns for 2 seconds.
Knockdown | PT_KNOCKED_DOWN | Universal: Players and enemies fall to the ground. Counts as an individual status for Condition Overload, Galvanized Aptitude, Galvanized Savvy, and Galvanized Shot.
Lifted | PT_LIFT_HIT | Universal: Briefly suspends targets in mid-air. Counts as an individual status for Condition Overload, Galvanized Aptitude, Galvanized Savvy, and Galvanized Shot (or any bonus that uses Condition Overload (Mechanic)).
Microwave | PT_MICROWAVE_BURN | Universal: Enlarges an enemy's body part when shot at. Has infinite duration and counts as an individual status for Condition Overload, Galvanized Aptitude, Galvanized Savvy, and Galvanized Shot. Exclusive to Nukor and Kuva Nukor.
Parried | PT_PARRIED | ?
Ragdoll | PT_RAGDOLL | Universal: Body is launched into the air, incapacitating the player or enemy.
Silence | PT_SILENCED | Universal: Active abilities are disabled. Casting new abilities is prevented.
Sleep | PT_SLEEP | On enemy: Target is temporarily put to sleep.
Slow | PT_GLUE | 
Stagger | PT_STAGGERED | Universal: Players and enemies get staggered for a brief moment.
Stun | PT_STUNNED | Universal: Players and enemies get stunned in-place temporarily and cannot move or shoot. On Enemy: Target is opened to melee finishers for 3 seconds.
Void | PT_VOID | Resets Sentient adaptation. Not exclusive to Void Damage.

### Empyrean

This section is transcluded from Damage § Empyrean. To change it, please edit the transcluded page.

Empyrean game mode and Railjacks use an altered version of the damage system. Archguns and Archmelees deal 90.91% (10/11ths) reduced damage to space enemies, while Railjack Armaments and Tactical mods deal their full listed damage (before accounting for a target's resistances and vulnerabilities).

Physical and basic elemental damage types also apply different status effects to space-borne enemies, outlined in the chart below. The status effects normally caused by secondary elements ( Blast, Corrosive, Gas, Magnetic, Radiation, and Viral) do not exist in Empyrean space combat. These elements still increase the direct damage dealt by such Archwing weapons, but they do not affect the calculation for status proc weighting from the weapon's physical and primary elements.

This system does not apply to on-foot enemies, such as Ramsled boarding parties and Crewship and Points of Interest personnel, who will take damage and receive all appropriate status effects as normal.

Damage Type | Status Effects
Impact | Concuss Crew within an affected crewship have -50% accuracy and -30% damage for 6 seconds. Additional procs refresh the duration.
Puncture | Decompress Temporarily reduces the affect ship's shields by 8.5% and its current armor by 9% for 20 seconds. Additional procs stack multiplicatively.
Slash | Tear Affected ship receives 7.5% increased damage for 20 seconds. Additional procs stack multiplicatively.
Cold | Immobilize Affected ship's weapons are disabled and it slows 80% to a complete stop. Lasts for 6 seconds. Additional procs refresh the duration.
Electricity | Scramble Affected ship is unable to attack while it spirals erratically for 6 seconds, moving in a straight line. Additional procs refresh the duration.
Heat | Sear Affected ship receives damage over time for 5 seconds. Additional procs increase the amount of damage dealt over time.
Toxin | Intoxicate Affected ship attacks the closest enemy, and will be attacked by enemies in return, for 12 seconds. Additional procs refresh the duration.

## Status Chance

Status Chance can be a key factor in deciding on a weapon as some status effects are very powerful against certain enemies, while others may be less beneficial. For example, Corrosive procs are valued highly against heavily armored foes, but Magnetic procs have no benefit to enemies that lack shields or overguard.

The chance that a proc will occur can be directly increased with mods such as Rifle Aptitude. One can also increase the number of projectiles fired through multishot mods such as Split Chamber; this effectively increases the opportunities for an enemy to be procced per a given attack, and is reflected in the weapon's attributes box in the Arsenal screen, but does not change the status chance for each individual hit. Another indirect way of increasing the amount of procs is to increase fire rate, this also doesn't change the likelihood that a proc will occur per hit, but increases the number of possible procs in a given time frame.

When a weapon achieves a status chance higher than 100%, each hit may apply additional "unique" status effects. The type of each proc is independently drawn, so it is possible to apply the same status several times in one hit.

A specific status type shown at 100% status chance, when hovering over a weapon’s shown Status in the Arsenal, does not guarantee that status effect. An example of this would be a weapon that has 200% Status with only Heat and Impact status effects as possible options can still trigger two heat or two impact status effects regardless of their relative status chance values.

If a single attack hits multiple enemies, each enemy gets their own status roll to determine if they will receive a status effect from the attack and which status effect they will receive.

### Status Vulnerability

Status Vulnerability increases the Status Chance received from all other status effects. This means that if an enemy or player has Status Vulnerability, they will be more susceptible to status effects applied by weapons and abilities. The increase can stack with other sources of Status Chance, potentially leading to very high proc rates.

## Damage Distribution

Status effect procs will occur in proportion to the amount of base damage dealt by each of the present damage types on the weapon. For example, an unmodded Strun's highest physical damage type is Impact, thus it inflicts mostly Knockback procs.

Increasing the physical or elemental damage of a weapon does not increase the duration of the associated proc (e.g. enemies won't be confused longer if Radiation damage is increased).

When a hit procs, the chance for an individual damage type to proc in relation to the others is:

Proc Type Chance = Damage ÷ Total Damage

For example, if a weapon's damage is composed of 20 Impact, 5 Puncture, 10 Slash, 25 Heat, and 50 Corrosive, then its total damage is 20 + 5 + 10 + 25 + 50 = 110. Therefore, the chance for the individual damage types to proc will be:

 | Impact | Puncture | Slash | Heat | Corrosive
Damage | 20 | 5 | 10 | 25 | 50
Proc Type Chance | 18.18% | 4.55% | 9.09% | 22.73% | 45.45%

### Status Immunity Interactions

Proc type chances are not altered by enemy resistances or weaknesses to the damage components used in their computation; however, they are modified by enemy status immunities. When an attack procs a status effect on an enemy which is immune to a particular proc type, the respective damage type is excluded from proc type chance calculations for status effects on that enemy.

For example, if the weapon outlined above were used against an enemy with Corrosion status immunity (regardless of whether that enemy is also immune to Corrosive damage), the chances for the individual damage types to proc would change to the following values:

 | Impact | Puncture | Slash | Heat | Corrosive
Damage | 20 | 5 | 10 | 25 | 50
Proc Type Chance | 33.33% | 8.33% | 16.67% | 41.67% | N/A

## DoT Damage Scaling

- Main article: Damage over Time

If the initial hit is affected by the following, a resulting damage-dealing effect will also benefit accordingly:

- Damage Buffs and relevant Mods.
  - This includes for example total damage multipliers (e.g. Furious Javelin, Eclipse), additive damage bonuses (e.g. Serration or Vex Armor), and enemy debuffs (e.g. Molecular Prime, Rest & Rage).
    - Weakspots generated by Sonar or Detect Vulnerability only increase damage of the initial hit, not the resulting proc damage.
- Relevant elemental damage Mods (e.g. Hellfire, Malignant Force).
  - This only applies to elemental status effects, mods like Sawtooth Clip do not buff Slash status damage.
  - DoTs of combined status effects (i.e. Gas, Blast) are not buffed by their component mods (e.g. Thermite Rounds+Infected Clip).
    - The only way to buff them is by using literal elemental damage (e.g. Leaded Gas, Valence Formation).
    - This also works in reverse. For example: using Toxic Lash with Corrosive mods (e.g. Infected Clip and Stormbringer) will buff the forced Toxin DoT.
- Critical Hits and Stealth Damage Bonus.
- Status Damage bonuses (e.g. Rifle Elementalist).
- Melee Combo Counter and Sniper Combo Counter.
- Body part multipliers.
- Faction Damage Bonus (e.g. Bane of Infested, Roar).
  - Due to the nature of Faction Damage Bonuses, they are applied once more during the calculation of damaging status effects, even though they already affect the initial hit.
    - For example: a weapon with an innate 100 damage modded with Serration and Bane of Grineer, a Slash proc will deal the following damage per tick: Bleed per tick = 100 × (1 + 1.65) × 0.35 × (1 + 0.3) ^2 × (1 + 0.9) = 297.8202

## Status Duration

It's taking longer than I calculated.

Negative Duration Table is outdated.

Status effects have a duration over which they apply to their target, and some of them even deal Damage over Time. A status effect's duration can be increased or decreased with mods that affect status duration (e.g. Lasting Sting).

Damage-dealing status effects will benefit from modifiers on headshots and critical hits.

Damage Type | Default Duration | Increased Duration Status Effects
Stagger | 6 seconds | Increases duration of status, but does not increase duration of stagger animation.
Weakened | 10 seconds | Increases duration of weakened status.
Bleed | 6 seconds | Increases DoT duration.
Freeze Frozen | 6 seconds 3 seconds | Increases slow duration. Increases duration of fully frozen status and subsequent Cold status.
Tesla Chain | 6 seconds | Increases DoT duration. Stun duration is unaffected.
Ignite | 6 seconds | Increases DoT duration. Ramp up and ramp down times for armor strip lengthened.
Poison | 6 seconds | Increases DoT duration.
Detonate | 1.5 seconds | Increases fuse duration, delaying detonation.
Corrosion | 8 seconds | Increases armor strip duration.
Gas Cloud | 6 seconds | Increases gas cloud's duration.
Disrupt | 6 seconds | Increases duration of shield vulnerability and negation of shield regen. Subsequent Electricity proc on shield break has increased DoT duration with the stun unaffected.
Confusion | 12 seconds | Increases status and enemy damage bonus duration.
Virus | 6 seconds | Increases damage vulnerability duration.

### Negative Status Duration

Damage duration can be negative (over -100% duration through Riven Mods). This causes all proc effects which have a duration or deal damage over time to be nullified. All instant procs or those who deal instant damage occur. The following table shows this in more detail:

▾View Negative Status Duration Effects List ▾

Damage Type | Nullified Effect | Occurs Normally
Impact | Stagger | -
Puncture | Weakened | -
Slash | Bleed | -
Cold | Freeze | -
Electricity | Stun | Tesla Chain
Heat | Ignite | Panic animation occurs (but no flame)
Toxin | Poison | -
Blast | - | Effect expiry damage to target. Explosion occurs only if the triggering hit kills.
Corrosive | Corrosion | -
Gas | Toxin Cloud | -
Magnetic | Increased shield damage | Visual effects
Radiation | Confusion | -
Viral | Increased health damage | Visual effects

Note: The information above is based on this forum post from EDFScout and may need further confirmation. Non-consistent observations as mentioned in the post have been changed to the more likely effect, i.e. for impact stagger should not appear, but knockback, and for electricity stun should not be triggered.

## Status Damage

- Main article: Damage over Time

Slash, Heat, Toxin, Electricity, and Gas all deal Damage over Time. They have a base duration of 6 seconds, during which they will deal a tick of damage for every second that the effect is active. Area of effect statuses ( Electricity and Gas) will always start dealing damage ticks the moment it is procced on an enemy, while single target status effects ( Slash, Heat, Toxin) will have a 1 second delay before dealing their damage ticks. The table below illustrates this mechanic.

Time From Initial Proc | 0s | 1s | 2s | 3s | 4s | 5s | 6s
Damage Tick Occurred? | Slash | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️
Heat | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️
Toxin | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️
Electricity | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ❌
Gas | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ❌

Status Damage itself is any damage dealt through a Status Effect tick ( Slash, Heat, Toxin, Electricity, Gas, and Blast). Sources of Status Damage bonuses are multiplicative to other damage bonuses and additive to other sources of Status Damage bonuses.

- Stacks multiplicatively with bonuses like Faction Multipliers: Bane of Grineer and Roar
- Stacks additively with other Status Damage bonuses: Emerald Archon Shard stacks additively with Elementalist Mods

#### Sources of Status Damage

- Ash
- Boreal's Contempt
- Burning Hate
- Conductive Sphere
- Emerald Archon Shard
- Empowered Blades
- Galvanized Elementalist
- Melee Elementalist
- Pistol Elementalist
- Immunity Resistance
- Rifle Elementalist
- Shotgun Elementalist
- Riven Splicer 90% Status Damage as a possible spliced trait (base value is then further modified according to the attribute Value Formula)

- Emerald Archon Shard only gives Toxin Status Damage.
- Ash only gives Slash Status Damage.
- Conductive Sphere only gives Electricity Status Damage.

## Forced Procs

It's taking longer than I calculated.

This page is actively being worked on and may not be completely correct. Please assist in making this page accurate by adding more info. For guidance on performing research, see WARFRAME Wiki:Research.

Very well. Keep your secrets.

This article/section contains unofficial information, concepts, or terminology derived from or based on community discussion, invention, or knowledge. It may be subjective and contain information or terminology that is not used by Digital Extremes or in official WARFRAME communications, and may not be an officially recognized concept.

Forced Procs are status effects that are guaranteed to occur regardless of the status chance and damage distribution of the weapon. They are independent from normally occurring procs which can also take place alongside forced procs.

Note that this is not the same as having 100% status chance.

For melee weapons, information about forced procs on light attack combos can be viewed on Stance pages. For example, the Claws Stance mod Malicious Raptor in its Neutral Combo applies both Bleed and Knockback on its first two attacks, and then Lifted followed by Knockdown on its third attack.

Heavy attacks, aerial attacks, and finishers can also sometimes apply forced procs. These are stanceless moves, meaning their properties are determined by weapon type rather than stance, and will be the same for all weapons of that type. For example, all slides and aerial attacks of Scythe-type weapons will apply Knockback, and all heavy attacks will apply Bleed and Knockback.

Attacks that apply a forced proc are also capable of inflicting a regular status effect.

Forced procs have negative interactions with some Warframe abilities such as Zephyr's Tornado where forced procs do not apply to enemies caught within the tornadoes, and instead apply to the tornadoes themselves which can then proc the Status Effect the tornadoes are effected with.

## Multishot

When firing multiple pellets in a single attack, the status chance on a listed weapon in the Arsenal is the probability that each pellet will individually proc. For example, the Strun Wraith displays a 12% status chance, so each of its ten pellets has a 12% chance to individually proc.

### Average Procs

When you might apply more than one kind of status effect, or the applied effect is one which benefits from multiple applications in the same shot (e.g. Corrosive procs), it is helpful to know the average quantity of status effects triggered per shot (i.e. from a single click of the fire button). This value can be determined with the following formula:

Average Number of Procs Per Shot = Multishot × (Number of Forced Procs + Status Chance per Projectile)

Average Number of Procs per Second = Average Number of Procs Per Shot × Fire Rate

A table with example values to display the relation of status chance and multishot.

 | Arsenal Status Chance
 | 150% | 100% | 99% | 80% | 150% | 100% | 99% | 80%
Multishot | Chance per Pellet/Projectile | Average Procs per Shot
1.9 (using SC) | 150% | 100% | 99% | 80% | 2.85 | 1.9 | 1.88 | 1.52
3 (e.g. Exergis) | 150% | 100% | 99% | 80% | 4.5 | 3 | 2.97 | 2.4
5 (e.g. Sobek) | 150% | 100% | 99% | 80% | 7.5 | 5 | 4.95 | 4
10 (e.g. Strun Wraith) | 150% | 100% | 99% | 80% | 15 | 10 | 9.9 | 8
20 | 150% | 100% | 99% | 80% | 30 | 20 | 19.8 | 16

### Continuous Weapons

Despite Continuous Weapons firing only one beam after adding multishot (with damage instances merged), it will still proc status effects as if more than one projectile was visually present. This means that multishot benefits the average status chance of continuous weapons like any other weapon.

## Status Mods and Effects

Status chance mods affect the base status chance of the weapon, i.e. the status chance value displayed in the Codex that is the probability, for the unmodded weapon, that each projectile will inflict a status effect.

### Status Chance

- Catalyzer Link
- Galvanized Aptitude
- Hammer Shot
- High Voltage
- Malignant Force
- Proton Jet
- Rifle Aptitude
- Rime Rounds
- Thermite Rounds
- Crimson Archon Shard

- Frigid Blast
- Galvanized Savvy
- Motus Setup
- Nano-Applicator
- Scattering Inferno
- Shell Shock
- Shotgun Savvy
- Toxic Barrage
- Crimson Archon Shard

- Carnis Stinger
- Embedded Catalyzer
- Frostbite
- Galvanized Shot
- Jolt
- Jugulus Spines
- Pistol Pestilence
- Saxum Spittle
- Scorch
- Stunning Speed
- Sure Shot

- Carnis Mandible
- Drifting Contact
- Enduring Affliction
- Galvanized Elementalist
- Jugulus Barbs
- Melee Prowess
- Nira's Contempt
- Proton Snap
- Saxum Thorax
- Vicious Frost
- Virulent Scourge
- Volcanic Edge
- Voltaic Strike
- Weeping Wounds

- Chromatic Blade
- Reactive Storm

- Charged Bullets
- Contamination Casing
- Hypothermic Shell
- Magma Chamber
- Marked Target
- Modified Munitions

- Cryo Coating
- Infectious Injection
- Ion Infusion
- Sudden Impact
- Searing Steel

### Status Damage

- Ash's Passive
- Boreal's Contempt
- Burning Hate
- Conductive Sphere
- Emerald Archon Shard
- Empowered Blades
- Galvanized Elementalist
- Immunity Resistance
- Melee Elementalist
- Pistol Elementalist
- Rifle Elementalist
- Shotgun Elementalist

### Status Duration

- Augur Seeker
- Bubonico's alt fire explosion (+9s pre-mods)
- Continuous Misery
- Frenzied Posture
- Hunter Track
- Lasting Sting
- Lavos's Passive
- Lingering Torment
- Perpetual Agony
- Rapid Resilience
- Saryn's Passive
- Toxic Sequence

### Status Spread

- Contagious Bond
- Divine Retribution
- Fangs of Raksh
- Mecha Empowered
- Mecha Overdrive
- Mecha Pulse
- Mecha Recharge
- Secondary Irradiate
- Shivering Contagion
- Storm of Ukko

Last updated: Update 29.5 (2020-11-19)

## List of Ability Status Effects

Most Frames can make use of status effects via abilities. This list does not include CC status effects like Ragdoll for example.

This section is transcluded from Warframes Comparison/Ability Status Effects. To change it, please edit the transcluded page.

Name |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Universal
Ash |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Atlas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Banshee |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Baruuk |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Caliban |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Chroma |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Citrine |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Cyte-09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Dagath |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Dante |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Ember |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Equinox |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Excalibur |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Excalibur Umbra |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Follie |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Frost |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Gara |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Garuda |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Gauss |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Grendel |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Gyre |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Harrow |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Hildryn |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Hydroid |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Inaros |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | External Weapon
Ivara |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Jade |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Khora |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Koumei |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Kullervo |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Lavos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Limbo |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Loki |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Mag |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Mesa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Mirage |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Nekros |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Nezha |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Nidus |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Nova |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Nyx |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Oberon |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Octavia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Protea |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Qorvex |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Revenant |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Rhino |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Saryn |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Sevagoth |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Sirius & Orion |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Styanax |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Temple |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Titania |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Trinity |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Valkyr |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Vauban |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Volt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Voruna |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Wisp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Wukong |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Exalted Weapon
Xaku |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Yareli |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Zephyr |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | External Weapon

## Status Immunity

Players can achieve temporary total status immunity by equipping the below mods or using these abilities. For immunity towards individual status effects, please navigate towards the respective damage type page. Status immunity prevents new status effects from being applied to players, but does not remove existing status effects.

Note that sources of Invulnerability and Overguard also protect against status effects.

### Sources of Status Immunity

Abilities

 | N/A 50 | Hideous Resistance Grant yourself immunity to Status effects. Introduced in Update 30.5 (2021-07-06) | Strength:4 / 6 / 8 / 10 Charges
Duration:N/A
Range:N/A
Subsumable to Helminth

Info

- Expend 50 Energy to cleanse active Status Effects and become immune to the next 10 status effects.
- Does not remove status effects that were obtained during the casting animation.
- There is no grace period or delay between charge use, making them deplete rapidly sometimes.
- Cannot be recast while active.

Maximization

Hideous Resistance

 | 2 50 | Mesmer Skin Become enveloped in Sentient energy, redirecting damage and stunning all those who dare attack. Stunned enemies can be Enthralled at no energy cost. Introduced in Update 23.5 (2018-08-24) | Strength:3 / 4 / 5 / 6 (number of charges)
Duration:2 / 3 / 4 / 5 s (stun duration)
Range:N/A
Misc: 100% (reflected damage and status) 100% (Enthrall energy discount) 1 (ally buff charge)

Info Revenant expends 50 energy to surround himself in a shroud of Sentient energy that reflects 3 / 4 / 5 / 6 incoming enemy attacks; attackers receive 100% of the reflected damage and Status Effects, while also becoming stunned for 2 / 3 / 4 / 5 seconds. Upon consuming a charge, Revenant becomes Invulnerable for 1 second. Mesmer Skin lasts indefinitely until all charges are used.

- Casting speed is affected by Casting Speed.
- Number of remaining charges is displayed on the ability icon.
- For any non-integer the number of charges is rounded up to the next whole number. For example, 255% Ability Strength = 15.3 charges, this is rounded to 16. However in game the maximum charges will display 15, with the 16th charge displayed as 0.
- Revenant is immune to self-stagger, which does not consume a charge.
- Does not reflect damage dealt by status effects and objects created by enemies (e.g., Napalm flame patches)
- Does not negate damage from Explosive Barrels or Environmental Hazards, although they will not use up a charge.
  - Revenant's Health can still take damage, but will not be lowered below 2 and therefore cannot die as long as he has charges.
    - Therefore, Arcane Escapist can lose a stack while having active Mesmer Skin.
- Mesmer Skin converts knockdown from Shockwave MOA waves into a knockback.
- Mesmer Skin reflects damage from Scorpion and Ancient hookshots, as well as blocking their knockdown and pull effects.
- Can be recast while active to apply a new instance. Previously unused Mesmer Skin charges are removed during recast.
  - During recast when your charges are removed, there is a brief window when Revenant is completely vulnerable and can be killed. While it's unlikely that an enemy's attack will connect during this time, damaging auras and lingering damage areas can result in being one-shot if Revenant is within their range during a recast.
- Casting Mesmer Skin is a full body animation that interrupts grounded movement and other actions.
- Revenant visually grows a cluster of Eidolon tendrils on his left shoulder, emits fumes from his body and a shroud of white mist around his torso while Mesmer Skin is active. Allies that gain Mesmer Skin also exhibit these visual effects on their body.
- Eidolon tendrils and fumes color tinting are affected by Revenant's chosen Warframe energy color.

Kit Interactions

- Enthrall costs 0 energy to cast on an enemy stunned by Mesmer Skin.
- While Mesmer Skin is active, Reave restores 1 charge per thrall that Revenant passes through, up to the full charge count.
- While Mesmer Skin is active, allies such as Warframes and Companions that contact Reave's current will gain 1 Mesmer Skin charge.

Augment

- Main article: Mesmer Shield

Mesmer Shield is a Warframe Augment Mod for Revenant's Mesmer Skin that increases its own Ability Strength and grant charges to allies within Affinity Range.

Rank | Mesmer Shield's Ability Strength Bonus | Ally Maximum Charges | Cost
0 | +12% | 2 | 6
1 | +25% | 3 | 7
2 | +37% | 4 | 8
3 | +50% | 5 | 9

Tips & Tricks

- It is probably more beneficial to focus on Ability Strength, Ability Duration and Ability Range, rather than equipping Health and Shield mods on Revenant as Mesmer Skin provides high survivability.
- Casting while in air allows Revenant to maintain forward momentum while activating Mesmer Skin.
- When receiving the Ability Strength and Ability Range buff from Void Fissure missions, activate Mesmer Skin right before the buff ends. Avoid Nullifier Crewmen and other enemies with an ability nullifying field to take full advantage of the buffed Mesmer Skin. Additionally, if Mesmer Skin is activated and the buff is no longer active, the un-buffed Mesmer Skin value will replace the buffed Mesmer Skin value, even if the buffed value was greater.

Maximization

Mesmer Shield?

Mesmer Skin

Bugs

- Damage dealt by Nullifier Crewman with its null sphere intact does not use up Mesmer Skin charges. Damage is still mitigated completely.
- The remaining charge counter on the ability icon can sometimes disappear while the ability is still active, most prominently observed after performing Transference back into the Warframe.
- Charges can be modified into decimals, but the ability icon counter only displays whole numbers, including 0 which can be misleading.
- When using Rage or Hunter Adrenaline, even though damage is fully nullified, if the damage exceeds Revenant's shield value, energy will still be granted.

 | 3 | Scarab Shell Activate to form Armor by draining Inaros' Health. Activate again to stop the formation early. The protective layer reduces incoming Damage and absorbs Status Effects. Introduced in Update 35.5 (2024-03-27) | Strength:175 / 250 / 300 / 350 (armor bonus)
Duration:N/A
Range:N/A
Misc: 5% (status protection cost) ? m (charging damage radius) ? (damage per tick) Stagger on hit 2,500 HP (total health cost) 2 HP (min. health threshold) ∞ (armor bonus duration) 25 HP (health drain per percent charge) 4.67s (time to full armor bonus)

Info

- Inaros summons the desert sands and sacred scarabs, offering his Health as a sacrifice to gain Scarab Shell, gaining up to 350 bonus Armor and immunity to Status Effects. While charging Scarab Shell, enemies within 7m of Inaros are Staggered and take 500 Slash damage every half second, as Inaros loses 25 Health for every 1% of generated bonus armor, for a total of 2500 health lost to fully charge the armor.
  - The armor buildup will end once the bonus armor is fully filled, Inaros only has 2 health left, or the ability is manually deactivated.
  - Upon negating a status effect, the shell loses 5% of its maximum armor value. Afterwards Inaros will remain immune to all status effects for 3s, statuses negated during this time will not consume shell charge.
    - A full charge will therefore make Inaros immune to status effects for a minimum of 60 seconds.
    - Knockdowns will consume charge even when negated by Primed Sure Footed, and statuses will consume charge even when negated by sources like Arcane Ice.
  - Scarab Shell is not dispelled from falling Out of Bounds or entering an ability nullification zone such as Nullifier Crewman bubbles.
  - The shell can last indefinitely until Inaros suffers a lethal hit.
  - While the armor bonus is active, a stylized armor bonus counter appears above the ability icons.
  - Scarab Shell status immunity does not prevent Negation Armor's Slash proc.
- Charging Scarab Shell takes 4.67s in total, not affected by Casting Speed.
- Inaros can move but cannot cast other abilities, use weapons, or perform parkour Maneuvers or general interactions while channeling this ability.

Augment

- Main article: Negation Armor

Negation Armor is a Warframe Augment Mod for Inaros that sacrifices an active Scarab Shell to prevent Inaros from entering Bleedout, but receives a Slash status effect once its Invulnerability period expires.

Rank | Cooldown | Cost
0 | 60 s | 6
1 | 48 s | 7
2 | 38 s | 8
3 | 30 s | 9

Tips & Tricks

- Bonus armor can trigger effects that need high amounts of armor (e.g. Arcane Battery, Arcane Persistence).
- Status Immunity and bonus armor will keep Arcane Persistence always active, and will re-activate it as soon as Inaros leaves a Nullifier Crewman bubble.

Maximization

Current maximum Health:
Negation Armor?

Scarab Shell

Bugs

- The charging animation will not stop if Inaros has 2Health left.
- Inaros can zoom and crouch during the charge, it will reduce his movement speed and provide no benefit.

This section is transcluded from Lavos/Abilities/Passive. To change it, please edit the transcluded page.

Valence Block

Purifying himself from all ailments, Lavos cleanses all active negative Status Effects and gains status immunity for 10 seconds upon collecting an Energy or Universal Orb. Picking up an Energy or Universal Orb has a cooldown of 5 seconds.

- Buff duration is renewed to full upon collecting a new orb.
- Valence Block buff icon and timer are shown beside Lavos' shield and health indicators.
- While activated, three serpent-like energy particle effects encircle Lavos' body.
- If Lavos is injured with missing health, Universal Orbs are collectible to heal him with no cooldown period in between.
- When Lavos' Companion is equipped with Synth Fiber, all nearby Health and Universal Orbs will be collected, bypassing Lavos' innate orb pickup cooldown entirely.

Special Casting

## Stats and Modding

Lavos has no energy capacity and his abilities do not use any resource to activate. Instead, each of his abilities are free to cast with a cooldown in between uses. The Ability Efficiency stat will instead affect the cooldown reduction effect from Transmutation Probe and Swift Bite.

- Mods which convert energy spent on abilities to shields, such as Brief Respite or the Augur Mod Set, do not replenish shields.
- Because Lavos can still pick up energy orbs, mods or arcanes that benefit from picking up energy, such as Equilibrium, Energy Conversion, and Arcane Energize, still function.
- While piloting a Railjack, all Battle Mods will have a 10 second cooldown.
- Subsumed abilities injected into Lavos via the Helminth system will cost 0 energy, but instead incur a 10 second cooldown after cast and disable the elemental imbuement hold-function (see below) associated with the ability button.
  - On non-recastable abilities (e.g. Roar), the cooldown begins after the ability's duration expires, unless modded with an augment that allows it to be recastable (e.g. Piercing Roar).
  - On channeled abilities (e.g. Gloom), they instead have a 12 second base duration.

The Ability Duration stat will also affect the Status Duration stat uniquely innate to Lavos, which extends or shortens the duration of all status effects created by Lavos using his weapons and abilities.

- Bonus is additive with other sources of Status Duration.

## Elemental Imbuement

Experiment and unleash volatile mixtures of the deadly elements. Hold down one of the four ability buttons (default 1 ,2 ,3 ,4 ) to imbue a Primary Elemental damage type ( Toxin, Cold, Electricity, and Heat respectively) into the mixing vial displayed above Lavos' ability icons. Imbuement has no cost nor cooldown between uses.

- Elemental imbuement is available by default to Lavos at Warframe Rank 0 without requiring his abilities to be fully unlocked.
- Primary Elements are shown in the four smaller diamond-shaped icons below the mixing vial. When an ability button is held down, its diamond icon is briefly highlighted until the element is mixed in.
- Combine with a different element to produce a Secondary Elemental damage type: Blast (2 +4 ), Corrosive (1 +3 ), Gas (1 +4 ), Magnetic (2 +3 ), Radiation (3 +4 ), and Viral (1 +2 ).
  - Inputs can be in any order, or the hotkeys can be held down together to instantly produce a Secondary Elemental damage type.
- The Imbued Primary or Secondary Element is shown in the vial with a colorcoded emblem and plays a unique sound effect upon mixing.
- With an element in the mixing vial, Lavos' next ability cast drains the vial to add the Primary or Secondary Elemental damage type, onto the chosen ability dealing an extra instance of damage and status proc.
  - The same Primary Elemental damage type can be imbued onto an ability that already inflicts that damage type (e.g. Ophidian Bite imbued with Toxin, Vial Rush imbued with Cold, etc) to double the damage and status proc.
  - Imbued Primary Elemental damage types do not merge with the ability's innate damage type.
  - Non-damaging status effects inflicted by all of Lavos' abilities (Cold, Corrosive, Magnetic, Radiation, and Viral) will proc 3 stacks in a single application of elemental status.
    - Blast, despite being damaging, still exhibits this behavior as well.
  - Lavos' mixing vial is only cleared of its elemental contents upon imbuing an ability.
  - Elements can be imbued even if Lavos cannot use the ability.
- Because imbuement is only available from Lavos' original abilities, a subsumed ability replacement from the Helminth system will disable the associated element.
  - For example, applying a subsumed ability over top of Lavos's first ability will disable imbuement of Toxin.
  - Imbued elements also cannot be applied to subsumed abilities.

Rank Bonuses

When Lavos ranks up, he receives a special set of rank bonuses which are indicated at the top-left of the Warframe Upgrade screen:

- +20 Base Health every three ranks, starting at rank 1.
- +10 Base Shield every three ranks, starting at rank 2.
- +10 Base Armor every three ranks, starting at rank 3.

At rank 30, this results in a total of:

- +200 Base Health
- +100 Base Shield
- +100 Base Armor

- Main article: Valence Formation

Valence Formation is a Warframe Augment Mod for Lavos that allows weapons to gain the corresponding element of an ability whenever it is cast, with a guaranteed status effect.

Rank | Elemental Damage | Duration | Cost
0 | 50% | 20s | 6
1 | 100% | 20s | 7
2 | 150% | 20s | 8
3 | 200% | 20s | 9

 | 1 25 | Fire Walker Blaze a trail of flames, scorching enemies and cleansing allies. Teleporting blasts the landing area with a ring of fire. Introduced in Update 18.1 (2015-12-16) | Strength:50 / 100 / 150 / 200 ( Heat damage per second) 500 / 750 / 1000 / 1250 ( Heat explosion damage)
Duration:15 / 20 / 25 / 30 s (buff duration) 5 / 6 / 7.5 / 10 s (flame duration)
Range:3 / 4 / 5 / 6 m (explosion radius)
Misc: 15 / 15 / 20 / 25 % (movement speed bonus) 0.5 s (damage interval) 10 / 25 / 50 / 75 % ( Heat status chance) 100 % (flame trail status cleanse) ? s (flame ring duration)
Subsumable to Helminth

Info

- Nezha expends 25 energy to ignite his Wind Fire Wheels to gain 15% / 15% / 20% / 25% bonus Movement Speed for 15 / 20 / 25 / 30 seconds, while leaving behind a trail of fire beneath his feet that lasts for 5 / 6 / 7.5 / 10 seconds. Enemies that walk over the flames are dealt 25 / 50 / 75 / 100 Heat damage per 0.5 seconds, with each instance of damage having a 10% / 25% / 50% / 75% Heat status chance. While Nezha and his allies stand on the flames, they are immune and continually cleansed of all Status Effects.
  - Cast animation of ~0.5 seconds, affected by Casting Speed.
  - Flames can be formed in mid-air but only while Bullet Jumping. Falling will not leave behind any flames.
- Damage does not bypass obstacles in the environment and diminishes with distance.
- Fire Walker can be cast while moving but will interrupt all other actions.
- Can be recast while active to refresh its duration.

Kit Interactions

- If Fire Walker is active when using Blazing Chakram's teleportation, Fire Walker will overheat at the destination and deal 500 / 750 / 1000 / 1250 Heat damage with a 10% / 25% / 50% / ? Heat status chance within a radius of 3 / 4 / 5 / 6 meters, as well as leaving a lingering ring of Fire Walker's flames for ? seconds.

Helminth

- Subsuming Nezha to the Helminth will offer Fire Walker and its augments to be used by other Warframes.
  - This does not allow other Warframes to use Fire Walker's explosion on teleport. This is exclusively a synergy with Blazing Chakram.

Augment

- Main article: Pyroclastic Flow

Pyroclastic Flow is a Warframe Augment Mod for Nezha and Nezha Prime that accumulates the damage Fire Walker deals and unleashes it in a trail of fire upon reactivating the ability.

Rank | Damage Accumulation | Trail Duration | Cost
0 | 100% | 6s | 6
1 | 150% | 7s | 7
2 | 200% | 8s | 8
3 | 250% | 10s | 9

Tips & Tricks

- The 75% chance of the Heat status effect makes this an effective form of control for narrow hallways or choke points while also temporarily stripping the enemies armor.
- Quickly sliding into groups of enemies can reliably disable them.
- The amount of ground that can be covered in flames can be improved using Sprint Speed mods.
- Also works as an escape tool to prevent enemies from following you.
- Can be used to cut off melee units from defense objectives.
- Briefly tapping slide key allows for additional control over Nezha's momentum while maintaining the additional speed.
- Choosing a dark energy color makes the visual effect less intrusive.

Maximization

Pyroclastic Flow?

Fire Walker

 | 3 75 | Warding Halo Create a protective ring of fire, that also stuns and damages enemies who get too close. Introduced in Update 18.1 (2015-12-16) | Strength:500 / 650 / 800 / 1000 (base health) 50 / 75 / 100 / 125 ( Slash damage per second) 1.15x / 1.25x / 1.75x / 2.50x (armor multiplier) 2.5x (absorption multiplier)
Duration:N/A
Range:1.25 / 1.5 / 1.75 / 2 m
Misc: 3 s (invulnerability duration on cast) 90% (damage redirection) 2 s (invulnerability duration on break)

Info

- Nezha expends 75 energy to summon a fiery ring that encircles him, granting immunity to Status Effects and 90% Damage Redirection towards the ring's health pool. The ring starts with 500 / 650 / 800 / 1000 base health, to which 115% / 125% / 175% / 250% of Nezha's total armor is added as bonus health. Upon activation, the ring is invulnerable for 3 seconds, during this time all incoming damage it takes is multiplied by 250% and added to its total health. Enemies that wander within 1.25 / 1.5 / 1.75 / 2 meters of Nezha are continuously Staggered and dealt 50 / 75 / 100 / 125 Slash damage every second. Warding Halo cannot be refreshed while it is active, and only expires when its health is depleted or when it is dispelled.
  - Warding Halo's health uses the following expression: Modified Health = (Base Health + Armor Multiplier × (Health Conversion Armor + Nezha's Base Armor × (1 + Armor Bonus)) + Absorbed Damage × Absorption Multiplier) × (1 + Ability Strength)
    - As an example, with a maxed Steel Fiber and Intensify, and one stack on Health Conversion, a rank-3 Warding Halo will have an initial health of (1000 + (2.5 × (450 + 200 × (1 + 1.1)))) × (1 + 0.3) = 4,127.5 before absorbing damage.
  - While active, a health counter is displayed on the lower-right of the HUD, above the ability icons, indicating how much damage absorption is left.
  - Slash damage instances immediately affect enemies as they enter the stun radius.
  - Cast animation of ~1 second, affected by Casting Speed.
    - Casting this ability makes Nezha stop all other actions, including movement. However, players can perform a running slide and hold it before casting in order to maintain momentum during the animation.
- Upon expiring, Warding Halo releases a wave of heat, inflicting all surrounding enemies with a guaranteed Heat status effect, and making Nezha invulnerable for 2 seconds.
  - Warding Halo cannot be cast while active, but can be recast during this expiry invulnerability period.
  - Damage taken from a hit which exceeds the health of Warding Halo will transfer over in full to Nezha's health, but that damage cannot lower his health below 2.
  - The invulnerability period will not occur, if Nezha loses his own health before Warding Halo does.

Augment

- Main article: Safeguard

Safeguard is a Warframe Augment Mod for Nezha that allows him to cast Warding Halo on allies, albeit with reduced durability.

Rank | Durability | Cost
0 | 20% | 6
1 | 30% | 7
2 | 40% | 8
3 | 50% | 9

Tips & Tricks

- Using Health Conversion to gain armor stacks before casting Warding Halo, greatly increases its base health without requiring as much Power Strength.

Maximization

Current Armor:
Casting Safeguard?

Warding Halo

 | 2 50 | Hallowed Ground Sanctifies the ground around Oberon, inflicting Radiation Damage to all enemies within the radius. Also grants protection against Status Effects for Oberon and his allies. Introduced in Update 11.5 (2013-12-19) | Strength:25 / 50 / 75 / 100 ( Radiation damage)
Duration:10 / 15 / 17 / 20 s
Range:8 / 10 / 12 / 15 m (radius)
Misc: 100% ( Radiation Status Chance) 0.5 s (damage tick interval) 3 (Hallowed Ground cap)

Info

- Oberon expends 50 energy to consecrate the ground around him up to 8 / 10 / 12 / 15 meters, for 10 / 15 / 17 / 20 seconds. Enemies standing on the area of effect are dealt 25 / 50 / 75 / 100 Radiation damage with 100% Radiation status chance every 0.5 seconds. Allies are cleansed and granted full Status Immunity for as long as they are standing in the area.
  - Up to a maximum of 3 Hallowed Grounds can exist at a time.
  - Area of effect extends ~2m above and below the casting surface.
  - If cast in midair, Oberon will instantly drop to the ground to perform this ability.
  - Nullifier Crewman will not destroy Hallowed Ground, but instead render enemies immune to its effects while inside the bubble.
- Hallowed Ground spawns foliage inside its area of effect as visual representation. Oberon creates a field of grass, while Oberon Prime creates a field of ferns. Grass and ferns are affected by Oberon's chosen Warframe Accent color.
  - The shimmering energy field encompassing the ground is affected by Oberon's chosen Warframe energy color.

Kit Interactions

- Renewal's Health restore per second is increased by 2x when standing on Hallowed Ground.
- Hallowed Ground rapidly applies Radiation statuses to boost Reckoning's damage.

Augment

- Main article: Hallowed Eruption

Hallowed Eruption is a Warframe Augment Mod for Oberon's Hallowed Ground that causes recasts to detonate the ground for all its remaining damage with a chance to inflict a Radiation status. It also passively increases the duration of Hallowed Ground.

Rank | Bonus Duration | Cost
0 | 50% | 6
1 | 100% | 7
2 | 150% | 8
3 | 200% | 9

Tips & Tricks

- Enemies will traverse and fight through Hallowed Ground without any special attempts to evade its area of effect.
- Narrow pathways such as doorways and halls are effective at forcing groups of enemies to cluster into Hallowed Ground.
- Summoning multiple, overlapping layers of Hallowed Ground will deal the full combined damage over time to enemies.
- Hallowed Ground is most efficiently used in areas where constant enemy and ally activity is expected over an extended period of time.
- Hallowed Ground's status effect immunity can be used to pass through environmental traps unhindered, such as Grineer Magnetic Sensor Bars and Corpus Laser Barriers.
  - Note however that activating these traps in spy missions will still trigger vault alarms.
- Hallowed Ground will make players immune to to Radiation and Magnetic singularities in Sorties.

Maximization

Hallowed Eruption?

Hallowed Ground

 | 4 25 +5/s | Silken Stride Unfurl Oraxia's spider legs and go on the prowl. Oraxia is immune to Status Effects and has increased Maximum Health. Ranged Weapons are imbued with Toxin Damage. Killing enemies causes them to burst with Toxin. Silken Thread: Tap Dodge to leap to a targeted surface. Introduced in Update 39.0 (2025-06-25) | Strength:1.25x / 1.5x / 1.75x / 2x Health Bonus 10% / 20% / 30% / 40% Toxin Weapon Damage 20% / 40% / 60% / 80% Wall Latch Toxin Weapon Damage 200 / 300 / 400 / 500 Toxin Explosion Damage
Duration:N/A
Range:5 m Explosion Radius 75 m Dodge Range
Misc: Status Effect and Hard Landing immunity +30% movement speed +25% parkour velocity +100% jump height Toxin status on weapon hits and explosion Stagger on explosion 10 m explosion max radius Auto Wall Latch 70 m/s Silken Thread travel speed ∞ Wall Latch duration

Info

- Oraxia expends 25 Energy to unfurl her spider legs and go on the prowl. In this form, Oraxia becomes immune to Status Effects and hard landings, increases her maximum Health by 1.25x / 1.5x / 1.75x / 2x, and gains +30% Movement Speed, +25% Parkour Velocity, and +100% Jump Height.
  - The health bonus is coded as a multiplier on max health, following the formula:
    - Silken Health =(Base Health at Rank×(1 + Health Mods) + Health Bonuses)×(1+Ability Strength)
      - For example, (675 × (1 + 100%) + 1200) × (1 + (100% + 30%)) = 5,865
    - Ability Strength is snapshotted on ability cast
    - Silken Stride's effects are multiplied against max health from all sources, including abilities, shards, and arcanes.
    - Oraxia is healed to her new maximum health points when Silken Stride is cast.
  - She is able to perform most parkour Maneuvers, except rolling, side strafe, and backflipping. Wall latching happens automatically when Oraxia jumps against a vertical surface.
  - The player camera is positioned further back, to expand one's field of view.
  - Oraxia's spider legs visually disappear when aiming down sights with ranged weapons.
  - Oraxia's character model is the center of her foothold on horizontal surfaces, even though her spider legs appear to stretch out.
  - In spider form, Oraxia's upper body continues to play her chosen Idle Animations set, while her legs dangle in mid-air.
- While active, Oraxia laces her primary and secondary weapons' magazine ammo with potent venom, causing each weapon hit to inflict an Extra Hit of 10% / 20% / 30% / 40% Toxin damage (20% / 40% / 60% / 80% while Wall Latching) with 100% status chance; however, Oraxia is unable to equip her melee weapon. Enemies killed by Oraxia's guns and abilities (and assisted kills by allies) explode, dealing 200 / 300 / 400 / 500 Toxin damage with 100% Status Chance and Stagger to enemies within a 5 meter radius.
  - Damage bonus is calculated on ability cast, and doesn't change with Ability Strength changes, like Arcane Bellicose.
  - Toxin ranged weapon damage bonus is shown as a buff icon beside Oraxia's hitpoints indicator, and beside the primary or secondary firearm magazine counter, similar to Cyte-09's Resupply buff.
    - The buff will override the elemental damage bonus of Cyte-09's Resupply, and the Heat damage bonus of the Reconifex and Uriel's Demonium.
  - Explosion radius is capped at 10 meters, achievable with 200% Ability Range.
- Silken Stride consumes 5 energy per second while active, and will remain active until Oraxia's energy is depleted or the ability is deactivated manually.
  - Silken Stride's energy drain is not converted into shields by Augur Mods.
  - Oraxia cannot replenish energy using Energy Vampire, Rally Point, Rift Plane's innate energy regeneration, Squad Energy Restores, Energy Siphon, Energy Nexus, Dreamer's Bond, Archon Stretch, or Wellspring while Silken Stride is active.
  - Energy Orbs, Orokin Void Death Orb's energy restores, Rage, Hunter Adrenaline, Spellbound Harvest, Arcane Energize, and Emergence Dissipate's Energy Motes can still replenish Oraxia's energy while Silken Stride is active.
  - Silken Stride counts as a "Channeled Ability" for certain Incarnon evolutions.
    - Though be aware that the toxin damage bonus will not apply while a weapon is in Incarnon Form, since Incarnon Forms do not have a magazine to buff.
  - Oraxia's melee weapon will still be equipped, just not accessible. This means that passive effects (like Amalgam Furax Body Count) will function as normal, as will effects that involve checking and updating the melee weapon's state (like Secondary Outburst and Ceramic Dagger's Gun and Blade perk).
- Rolling (default Shift ) causes Oraxia to shoot from her hand a Silken Thread, up to 75 meters long toward the surface the reticle is pointing at, which then immediately pulls her at a speed of 70 meters per second to her destination. When cast on a vertical surface or the ceiling, Oraxia wall-latches onto it upon arrival for an infinite duration.
  - Silken Thread can be canceled mid-sling by pressing the jump key (default Spacebar ), allowing Oraxia to carry the forward momentum and perform other actions.
    - The speed of the Silken Thread pull is not affected by mods to parkour velocity, dodge speed, or sprint speed.
  - While wall-latched after using Silken Thread, Oraxia is considered constantly airborne, which will trigger aerial prerequisite Mods and Arcanes.
  - When wall-latched, Oraxia's spider legs visually animate to cling to the surrounding surfaces. Her main body rotates and orients with the reticle direction and movement keys (default W A S D ).
  - Riven challenges that require wall-latching will not be counted during Silken Stride, but Arcane Arachne and Proton Set mods will still trigger their effects as normal.
  - While the wall-latch duration is infinite, the duration of Predator's Lurk remains capped at 8 seconds.
  - Wall-latching is permitted even when an Archgun is equipped.

Kit Interactions

- Silken Thread can quickly wall latch to activate Predator's Lurk.
- Oraxia may cast her other abilities during Silken Stride and while wall-latched.
- Performing a melee attack (default E ) during Silken Stride will instead perform Mercy's Kiss on an enemy in range, which is able to trigger Silken Stride's Toxin damage explosion on kill.
  - If Mercy's Kiss is subsumed over with another ability, casting Mercy's Kiss this way is impossible, and melee weapons are still inaccessible in this form.
- Webbed Embrace's Damage Vulnerability increases Silken Stride's explosion damage.
- Widow's Brood's Scuttlers are able to trigger Silken Stride's Toxin damage explosion on kill.

Tips & Tricks

- Unlike normal wall latching, Silken Stride enables airborne damage reduction via mods such as Aerodynamic, Aviator, and Boreal's Set while latched onto a wall or ceiling.
- While melee weapons are unusable during Silken Stride, their passive effects still apply, such as set bonuses from equipped mods or passive Incarnon evolutions.
- Only the on-kill explosions will apply Archon Continuity.
- Casting Silken Stride will instantly heal Oraxia to the modified max health. By flicking the ability on and off you can heal indefinitely as long as you can afford the initial energy cost.
- Rage and Hunter Adrenaline can be used alongside her Mercy's Kiss orbs to provide Oraxia a consistent way to regenerate energy. Combined with Arcane Persistence and at least 700 armor from other sources, the only danger to Oraxia is not restoring enough health during her 4, as the two mods will provide 200/225 energy respectively per each 500 health damage taken.

Maximization

Wall Latching?

Silken Stride

Bugs

- Weapons in Incarnon Form do not receive the toxin damage bonus from Silken Stride, presumably because the bonus is applied to Oraxia's magazines, and Incarnon Forms don't have magazines. The Toxin explosion on kill still triggers, though.

 | 3 25 | Parasitic Link Bind to a target with parasitic link. When cast on an ally, both the host and Nidus have their Ability Strength and Weapon Damage increased. Linked enemies take some of the damage inflicted on Nidus. Introduced in Update 19.5 (2016-12-22) | Strength:10% / 15% / 20% / 25% (strength bonus) 10% / 15% / 20% / 25% (damage bonus) 20% / 30% / 40% / 50% (damage redirection)
Duration:30 / 35 / 45 / 60 s
Range:24 / 28 / 34 / 40 m (ally link) 10 / 13 / 16 / 20 m (enemy link)
Misc: 4 s (link break grace period) = 6 s ( post link brake effect grace period)

Info

- Nidus expends 25 energy to perform symbiosis with a targeted ally Warframe or Companion (excluding Sentinels) within 24 / 28 / 34 / 40 meters or parasitically link with a targeted enemy within 10 / 13 / 16 / 20 meters. The link persists as long as Nidus and his target remain in range of each other, lasting for 30 / 35 / 45 / 60 seconds or when manually deactivated by holding the ability key.
- Holding the ability key 3 will make Parasitic Link target the nearest ally from Nidus (Targeting in priority ally that is the closest from Nidus' crosshair while using a relaxed line of sight check ignoring obstacles and allowing tether to targets outside field of view).
  - When linked with an ally Warframe or Companion, Nidus and his target both receive a 10% / 15% / 20% / 25% Ability Strength bonus and a 10% / 15% / 20% / 25% Weapon Damage bonus.
    - Parasitic Link's Ability Strength bonus affects Ability Strength multiplicatively using the following expressions:
    - Modified Strength Bonus = Strength Bonus × (1 + Ability Strength)
      - With a maxed Intensify and the 15% Ability Strength rank bonus, Nidus will have 145% Ability Strength, resulting in 0.25 × (1 + 0.3 + 0.15) = 36.25% Modified Strength Bonus displayed on the UI.
      - Modified Ability Strength = (1 + Ability Strength) × (1 + Modified Strength Bonus)
      - Modified Strength Bonus then increases Ability Strength multiplicatively, granting 1.45 × (1 + 0.3625) = 197.5625% Modified Ability Strength that affects Nidus' other abilities while a rank-3 Parasitic Link is active.
      - The Modified Strength Bonus is the same percentage for the linked ally. However, Modified Ability Strength's calculation will depend on the linked ally's own Ability Strength.
    - The damage bonus is multiplicative to other damage bonus sources such as Serration and is a Universal Weapon Bonus.
      - Damage bonus does not affect the damage gained from additive Condition Overload sources.
        - For example at 200% ability strength, Parasitic Link will increase weapon damage by 50%. Using a melee weapon with 100 base damage and Condition Overload, attacking an enemy affected by 1 status will cause them to take (100 * 1.5) + (100 * 0.8) = 230 damage. If Parasitic Link's damage bonus affected the CO damage bonus, they would instead take 100 * 1.5 * 1.8 = 270 damage.
  - When linked with an enemy, the target is incapacitated for the duration while Nidus gains 20% / 30% / 40% / 50% Damage Redirection toward the linked target.
    - All negative Status Effects, including Knockdown and Stagger, are also redirected.
    - Damage Redirection is capped at 90%, achievable with 180% Ability Strength.
    - The enemy target is invulnerable to outside sources of damage and immune to external crowd control effects while linked, but is not immune to damage and crowd control effects transferred from Nidus. All damage prevented by the external invulnerability is stored and dealt in full when the ability ends.
    - While Parasitic Link can be used on enemies with Overguard, the target will only be incapacitated and made invulnerable after Overguard is removed.
  - Parasitic Link does not require Line of Sight to maintain connection between Nidus and his target.
  - Casting Parasitic Link is a One-Handed Action and can be done while in midair.
  - Can be recast to move the link to the new target.
    - Recasting on the same target will refresh Parasitic Link's duration.
  - If an enemy target dies during cast before the link is attached, the energy used for Parasitic Link will be refunded.
  - If the target moves out of range, dies or is nullified, there is a 3 second grace period before the link breaks.
    - If the target moved back into range or leaves the nullification field before the grace period ends, the link will not be broken.
    - If Nidus is the one nullified, the link will be broken immediately.
  - When Parasitic Link ends, there is a 6 second grace period before previously-affected players lose any bonuses gained, including Health granted by Parasitic Vitality.
- Nidus and the target are visibly covered in infestation and connected via a tether of biochemical energy, which is affected by the chosen Warframe energy color.
- Cannot link to a target already affected by Parasitic Link. Multiple Nidus players cannot link to the same target, nor to each other while their own Parasitic Link ability is active.
- When connected to another Nidus player, both players will use the Ability Strength bonus from the casting player; the link will break if the partner activates Parasitic Link on a different target.
- Cannot link to enemies affected by Mind Control.

Kit Interactions

- While linked to a target, using Virulence will spawn a second instance from the linked target that grows towards the targeted location, converging with the first instance from Nidus.
  - The second instance grants Mutation stacks independently of the first, allowing for multiple Mutation stacks to be gained from the same enemies.
- Ability Strength increase from linking with an ally or Companion will affect all of Nidus's abilities.

Augment

- Main article: Parasitic Vitality

Parasitic Vitality is a Warframe Augment Mod for Nidus that allows Parasitic Link to grant both Nidus and his linked ally bonus Health based on their Base Health, scaling with each Mutation stack.

Rank | Health Bonus | Cost
0 | 1% | 6
1 | 2% | 7
2 | 3% | 8
3 | 4% | 9

Tips & Tricks

- Link with a nearby teammate/companion or enemy for Virulence to create two lines from Nidus and the linked target. This effectively extends Virulence's reach, doubles its damage output, staggers enemies in its paths, can hit more enemies for mutation stacks, and earns extra energy for the cost of one cast.
  - Virulence's range indicator, activated by holding 1 before releasing to cast the ability, will show the directions both Nidus and his linked target will cast towards.
- Bringing a free moving Companion is strongly advised, as it allows Nidus to use Parasitic Link to gain additional Ability Strength and Weapon Damage.

  - Panzer Vulpaphyla synergize well with Nidus. Using Viral Quills and Hunter Adrenaline offer a consistent source of healing. Be mindful that Panzer Vulpaphyla can feel very vulnerable on high level content. Nidus is unable to apply Parasitic Link to any Vulpaphyla while they are in their larval states, as they are considered sentinels rather than free moving companions in this state.

  - Hound may be preferred for such content, with the precept mod Reflex Denial and Null Audit the hound will offer Nidus a strong and reliable anchor point for Parasitic Link while granting him and his teammates all sorts of beneficial effects depending on the copied Eximus power.

- Link Fiber and Link Vitality can greatly increase your Companion's survivability, especially when using Parasitic Vitality. Pack Leader/Primed Pack Leader can additionally help sustain its health.

- Using Arcane Bellicose and Parasitic Vitality will let you gain additional Ability Strength, increasing Parasitic Vitality's effectiveness.

- Enemies with high health and armor values such as Heavy Gunners can absorb a large amount of damage when linked to.
- Linked enemies with Shield will see their Shield restored overtime after some time passes without taking damage.
- As long as Nidus and his target are in range of each other, Parasitic Link's biochemical tether will help you visually track your positions.
- Before reviving a downed teammate, link with a nearby enemy to protect yourself from taking too much damage.
- A linked enemy, despite being immune to damage, will still count as being hit for effects that require doing so, such as gaining melee combo, charging Incarnon gauge, and triggering relevant Arcane effects.
  - Coda Hema can let player heal from headshots on the linked target.
  - Sancti Magistar will partially proc its Lifesteal effect, attackers will not be granted any Health Regen BUT nearby allies and objective will be healed.
  - Coda Hirudo will not proc its Lifesteal effects on enemies affected by Parasitic Link.
- Maggots from Ravenous will ignore your linked enemy target. However, Maggot's explosions will still count as hits for the Mutation gauge even when they cannot damage the target. When you cast Parasitic Link on an enemy with maggots attached, the maggots will detach once the link is established.
  - They are also not valid targets for parasitic link.
- Parasitic Link can be cast on Juggernauts, and though it will not immobilize the Juggernaut it will still transfer damage to it, bypassing the Juggernaut's normally-impenetrable armor.
  - This also applies to other Boss enemies such as Acolytes, Kuva Lich, and Sisters of Parvos.
- Can be used to immobilize Synthesis targets, instead of deploying Kinetic Siphon Trap. This also prevents the target from being killed, provided Nidus himself is not under heavy fire.
- Parasitic Link can transfer negative Conduit Effects given in Disruption. For example, Energy Drain will drop from 5 energy per second to 1. This reduces, but does not negate, the threat of negative effects from conduits, should one fail.
- Teammates with Warframes that possess high ability damage and Ability Strength-based effects are prime candidates for Parasitic Link.
  - Allies such as Wisp,Dante or Revenant before they cast Reservoirs, Light Verse or Mesmer Skin can provide tremendously improved squad wide effects.
- Linking to the last enemies of a Defense mission wave allows you to stall the wave, which lets Ravenous heal the Defense Objective without risking the health of the defense objective.
- If a linked enemy does not die, it may be targeted again when the buff timer expires.
- Hacked Ambulas will be treated as allies and buffed accordingly.
- Redirected Knockdown and Ragdoll can potentially knock enemies outside of the range of Virulence.
- Melee Vortex can move the tethered enemy towards Nidus.
- If Gloom is subsumed on Nidus the redirected damage will participate to the lifesteal effect , possibly out healing the incoming damage passively .
- Scyotid can displace enemy affected by parasitic link .

Maximization

Parasitic Vitality?

Parasitic Link

Bugs

- Linking to an enemy with Overguard and then removing said Overguard will cause enemies from other factions to begin attacking the linked enemy despite being invulnerable.
- Companion falling or teleporting can break the link instantly
- Parasitic Link no longer prevents enemies with overguard from taking damage from outside sources once their overguard is depleted.
- Parasitic Vitality + Link Vitality will damage your companion each time you gain a mutation , up to 2 hp remaining
- Linking with crewmate is inconsistent as most of the time they simply cannot be tied with

 | 3 75 | Disometric Guard Guard yourself and nearby allies against Status Effects. Each time Qorvex kills or assists in killing an enemy affected by Radiation Status, the number of Status Effects Disometric Guard can prevent increases. Introduced in Update 35.0 (2023-12-13) | Strength:200 / 300 / 400 / 500 Radiation damage on cast 2 / 3 / 4 / 5 initial status immunity stacks 5 / 7 / 8 / 10 max status immunity stacks
Duration:N/A
Range:N/A
Misc: 6 m damage radius Radiation status and Knockdown on cast 50 m Affinity Range Status cleanse on cast ∞ stack duration +10% stack chance per active Radiation status on enemy from kills and assists 100% stack chance cap

Info

- Qorvex expends 75 Energy to explosively fragment out several protective concrete plates. On cast, Qorvex reels back then leaps in the air, detonating an explosion that inflicts 200 / 300 / 400 / 500 Radiation damage with a guaranteed Status Effect and Knockdown to enemies in a radius of 6 meters.
- After the explosion, Qorvex's concrete plates encircle himself and allied Warframes inside his Affinity Range. All negative status effects on Qorvex and his allied Warframes are first cleansed, then an initial number of 2 / 3 / 4 / 5 stacks of concrete plates surround them. Each stack lasts indefinitely until consumed by negating an incoming status effect, including Knockdown and self or enemy-inflicted Stagger.
  - Status cleanse on cast is a separate function and does not consume an initial stack.
  - Each guarded Warframe consumes stacks individually and do not reduce the stacks on other guarded Warframes.
  - Allied Warframes retain their Disometric Guard stacks when leaving Qorvex's Affinity Range, and even when Qorvex himself has zero stacks.
  - When a status effect is negated, the player's screen borders flash in a fading radioactive visual effect, while an orbiting concrete plate dissolves away.
  - Concrete plates orbiting a player visually disappear when aiming down sights with ranged weapons, and when the camera is positioned close to Qorvex's character model.
- While Qorvex has at least 1 stack of Disometric Guard remaining, when Qorvex himself kills or assists in killing an enemy with an active Radiation status effect, there is a 10% chance to add 1 stack to Qorvex and allied Warframes in his Affinity Range; for each active Radiation status effect on the enemy, the stack chance increases up to a cap of 100% at 10 Radiation statuses. Disometric Guard can only sustain max 5 / 7 / 8 / 10 stacks per player.
  - When gaining or losing stacks, concrete plates visually materialize or dissolve away, shuffling the entire orbit to occupy equal distances between plates.
  - Amount of remaining stacks are shown on the ability icon and as a buff icon beside Qorvex's hitpoints indicator.
- Can be recast while active. If Qorvex and allied Warframes are below max stacks, recast adds initial stacks to their current stack count up to the max.

Kit Interactions

  - Radiation status effects from Chyrinka Pillar's pulses, Containment Wall's radioactive waves and smash, Disometric Guard's explosion, and Crucible Blast's beam increase the stack chance on kills and assists.

Maximization

Disometric Guard

Bugs

- In the Simulacrum, stacks visually do not disappear once the modding changed via Arsenal, but the ability is deactivated as expected. Qorvex is unable to prevent status effects properly due to the lingering stacks.
- Using transference, or being forced into operator form, may show 0 stacks when returning to the warframe. This is purely visual.

 | 1 25 | Spellbind Enemies fumble their weapons as they are whisked into the air. Nearby allies become immune to Status Effects. Hold the ability to cast the immunity onto Titania. Introduced in Update: The Silver Grove (2016-08-19) | Strength:N/A
Duration:10 / 12 / 14 / 16 s
Range:1 / 3 / 3 / 5 m (area radius) 20 / 30 / 40 / 50 m (cast range)
Misc: 100 % (status cleanse and immunity)
Subsumable to Helminth

Info

- Titania expends 25 energy to scatter enchanted dust in a 1 / 3 / 3 / 5 meter radius around the location she aims at, up to 20 / 30 / 40 / 50 meters away. Enemies within this area are Disarmed and Ragdolled as they weightlessly float in mid-air for 10 / 12 / 14 / 16 seconds. Titania and her allies caught within the dust cloud are cleansed from Status Effects and gain immunity to them for the duration of the ability. Holding down the ability key (default 1 ) casts the ability centered on Titania.
  - Cast animation of 1 second is affected by Casting Speed.
    - Can be cast while moving, but will interrupt other actions such as reloading, charging or shooting.
  - Status immunity also protects from crowd control effects such as Knockdown and Stagger, including the lock-out animation of Archwing and Razorwing when impacting a surface.
- After Spellbind expires, enemies previously armed with weapons cannot attack until they retrieve their weapons on the ground. Those that do not use weapons (such as the Infested) will recover quickly.
- Spellbound allies and enemies emit unique particle effects:
  - Enemies visually emit energy butterflies fluttering about and an upward stream of energy stripes, both affected by Titania's energy colors.
  - Allies visually emit energy butterflies fluttering about, affected by their own energy colors.
- Spellbind can be aimed at any surface, but will only allow you to use it if an enemy is within the predicted area of effect.
- Subsuming Titania to the Helminth will offer Spellbind and its augments to be used by other Warframes.

Augment

- Main article: Spellbound Harvest

Spellbound Harvest is a Warframe Augment Mod for Titania which lets her regain Energy and increases the Ability Range of the next cast of Spellbind after hitting at least 4 enemies with Spellbind.

Rank | Energy Granted | Next Spellbound Cast Range | Cost
0 | 20 | +10% | 6
1 | 30 | +20% | 7
2 | 40 | +30% | 8
3 | 50 | +40% | 9

Tips & Tricks

- The status immunity granted by Spellbind also prevents Titania from being staggered when hitting surfaces in Razorwing. Holding the button down to activate Spellbind on yourself can be really helpful when flying through tight spaces.

Maximization

Spellbound Harvest equipped and active?

Spellbind

 | 1 25 | Well of Life Create a well of life on an enemy who will absorb Status Effect damage intended for nearby allies. Allies gain additional Health when they attack the target. If allies die, enemies in the well of life die in their stead. Introduced in Update 4 (2012-11-02) | Strength:+ 25 / 50 / 75 / 100 HP/s (health per second) 0.25 / 0.5 / 0.75 / 1 % (lifesteal on hit)
Duration:13 / 15 / 17 / 20 s
Range:100 m (cast range) 20 m (healing radius)
Misc: Invulnerable target 3 (max target limit) 100% (stored damage) ∞ (lifesteal range) Status effect negation 10% / 5% (status negation damage on normal or boss targets) Immortality bleedout prevention 5 s (invulnerability duration) 60 s (revive cooldown)
Subsumable to Helminth

Info

- Trinity expends 25 energy to imbue a single enemy target within 100 meters with life energy and suspends it in midair. The enemy is Invulnerable and incapacitated, lifted airborne, and emits an 20 meter aura for 13 / 15 / 17 / 20 seconds. A maximum of 3 targets can be turned into a Well of Life. 100% of damage suffered by the invulnerable enemy target is stored and dealt in full when the ability ends; while active, aim at the target and press the ability key again (default 1 ) to release the target early.
  - Affects the target immediately upon cast.
  - Casting time of 2 seconds is affected by Casting Speed.
  - Well of Life targets are not removed from mission progression objectives (i.e. Defense waves) while affected.
  - Casting beyond the max number of targets will release the oldest Well of Life target.
- Well of Life imparts multiple effects on Trinity and her allies within its aura:
  - Healing per second and Lifesteal: Trinity and her allies are healed 25 / 50 / 75 / 100 Health points per second inside the aura. Damaging the well instantly heals the attacking ally for 0.25% / 0.5% / 0.75% / 1% of the damage dealt over infinite range, as well as applying the damage-converted healing to all allies inside the aura.
    - Allies affected by the radial healing include all Warframes, Companions, Eidolon Lures, summoned allied units such as Specters, allied Invasion units, Hostages, Kavor Defectors, Sortie and Arbitration Defense Operatives, and Defense Objects.
    - Defense Object healing is uncapped, making this ability one of the only abilities in the game not subjected to this healing cap.
  - Status Effect negation and Well percentage health damage: each status effect received by allies inside the aura are negated, spawning a wisp from the ally to seek the Well target, damaging it for 10% of its maximum health (5% on boss enemies). Wisps are restricted to spawning at a rate of once per second.
    - Wisps do not deal any inherent damage type, bypassing any normal damage calculation steps.
    - Wisps can NOT be triggered by self-stagger.
    - Will negate Toxin procs but not damage (e.g. Mutalist Osprey, Toxic Ancient).
  - Death Gating: if Trinity herself, fellow Warframe or Companion takes fatal damage inside the aura, the Well of Life target is killed in their place to negate Bleedout, while fully healing the revived ally and granting them 5 seconds of Invulnerability. The revived ally experiences a 60 second cooldown before they can revived by a Well of Life again.
    - Cannot save the Operators/Drifters.
    - Cannot revive an ally already in bleedout state by casting a Well of Life nearby afterward.
    - Immortality cooldown per ally is shown beside the ally's hitpoints indicator and tracked by Trinity in her squad list.
    - If the Well of Life target is a VIP (e.g Demolyst) or Boss enemy, they will receive up to 20,000 damage instead of being instantly killed.
- Well of Life is a one-handed action. As such, it can be used while performing various maneuvers and actions without interruption.
- If the target dies before Trinity finishes her casting animation, the energy cost is refunded.

Kit Interactions

- Link can tether to a Well of Life target, applying lifesteal during Link's Damage Redirection.

Helminth

- Subsuming Trinity to the Helminth will offer Well of Life and its augments to be used by other Warframes.
  - However, Subsumed Well of Life's revive cooldown is increased to 120 seconds.

Augment

- Main article: Pool of Life

Pool Of Life is a Warframe Augment Mod that makes enemies marked by Trinity's Well of Life drop Health Orbs, with a chance to drop an additional Energy Orb.

Rank | Health Orbs dropped | Energy Orb chance | Cost
0 | 1 | 100% | 6
1 | 2 | 100% | 7
2 | 3 | 100% | 8
3 | 4 | 100% | 9

Tips & Tricks

- Well of Life can effectively lock down a Synthesis Target for scanning.
  - Additionally, the invulnerability offers the target temporary protection from accidental death, but stored damage will be dealt in full when the ability ends.

Maximization

Pool of Life?

Well of Life

Bugs

- If Well of Life is cast on a Shockwave MOA readying to stomp the ground, it will still produce a shockwave, but it also will be suspended in midair for the duration of the skill.
- In Corpus levels, if the player targets something outside of the above-mentioned range [clarification needed], the nearest turret (and possibly cameras) will be targeted.

 | 3 75 | Link Any damage taken while Link is active will be channeled to a nearby enemy. Introduced in Update 4 (2012-11-02) | Strength:1 / 2 / 2 / 3 (affected enemies)
Duration:14 / 16 / 18 / 20 s
Range:12 / 14 / 17 / 20 m
Misc: 50% / 60% / 70% / 75% (damage redirection) 100% (damage and status transfer)

Info

- Trinity expends 75 energy to link herself with up to 1 / 2 / 2 / 3 enemies within a radius of 12 / 14 / 17 / 20 meters for 14 / 16 / 18 / 20 seconds. While linked, she receives 50% / 60% / 70% / 75% Damage Redirection, which reduces her damage taken by the same amount, while 100% of the pre-mitigation damage she would've received is transferred to all linked enemies. She also becomes status immune, with any Status Effects she would've received being transferred to the linked enemies.
  - Max number of linked enemies is affected by Ability Strength, requiring an additional 33.3% strength per max target. In other words, Max Target Count = Floor(3 * Strength)
  - Casting time of 0.6 seconds is affected by Casting Speed.
  - Trinity must be linked to at least one enemy at any given moment to gain the ability's defensive benefits.
  - All linked enemies receive the full 100% of the damage she would've taken; the damage is not split between each linked enemies.
- Status redirection from Link has the following special behaviors:
  - Status redirection applies to Stagger and Knockdown.
    - Includes knockdown from environmental traps such as Corpus Laser Barriers. Note that tripping these barriers in Spy missions will still trigger vault alarms.
    - Self-stagger from explosive weapon fire is prevented, but is not redirected to enemies affected by Link.
  - Status effects applied before casting Link are not transferred to linked enemies.
    - Damage from damage over time effects, such as Heat, is redirected by Link's Damage Redirection when active.
  - When Trinity is hit by an enemy attack that has status chance, the damage redirected to her linked targets will inherit that status chance, meaning the status chance is calculated separately for each enemy.
    - Due to this, it is possible that only some enemies receive transferred status effects, except when status is guaranteed.
    - Status Effects applied this way deal the full effect, duration, and damage of one which would have applied to Trinity.
- If Trinity is bleeding out while this ability is active, she will remain linked with nearby enemies.
- Trinity cannot link with Stalker.
- Trinity and linked enemies will shine the color of her energy.
- Can be recast while active.
- Link is a one-handed action. As such, it can be used while performing various maneuvers and actions without interruption.

Kit Interactions

- Link can tether to a Well of Life target, applying lifesteal during Link's Damage Redirection.

Augment

- Main article: Abating Link

Abating Link is a Warframe Augment Mod for Trinity's Link that reduces the Armor of all connected enemies.

Rank | Armor Reduction | Cost
0 | 30% | 6
1 | 40% | 7
2 | 50% | 8
3 | 60% | 9

Tips & Tricks

- Keeping this ability active when surrounded by high-level enemies will dramatically increase Trinity's survivability.
- Use Trinity's Energy Vampire to fuel Link's high energy cost.
- Link connects to enemies through walls and other obstacles, which serves as an early-warning system indicating if enemies are nearby.
  - Similarly, Link can connect to and track the position of cloaked enemies such as Capture targets and Manics.
- Be wary of mods and effects which reduce Ability Range as they make it harder to maintain an active link, and with that, Link's defensive benefits.
- On cast, Link will target the closest enemies to Trinity within range.
  - If another enemy enters this range and Link has already reached maximum number of enemies, Link will not re-target the new enemy, even if this enemy is closer to Trinity.
- Transferred Status Effect activates additional effects like Archon Stretch

Maximization

Abating Link?

Link

 | 4 25 +5/s | Hysteria Valkyr bares her deadly claws, unleashing devastating attacks that also heal her. Valkyr becomes immune to Status Effects and her Armor bonus from Warcry is multiplied while using the claws. Introduced in Update 11.0 (2013-11-20) | Strength:100 / 125 / 200 / 250 damage 70 / 80 / 90 / 100 health restore per hit
Duration:N/A
Range:N/A

Info

- Overcome with rage, Valkyr expends 25 energy to unleash a pair of energy talons, the Valkyr Talons, as her melee Exalted Weapon, while also becoming immune to Status Effects. Normal attacks deal 100 / 125 / 200 / 250 damage within 2.15 meters and all of Valkyr's attacks restore 70 / 80 / 90 / 100 Health per hit.
  - Enemies that are immune to damage but can take hits (e.g. Arbitration Shield Drone) will also restore Valkyr's health.
  - Exclusively uses the Hysteria Stance.
  - Damage is distributed between 25% Puncture and 75% Slash.
  - Wall attacks and slide attacks inflict 300 / 375 / 600 / 750 damage for each strike.
  - Aerial attacks inflict 200 / 250 / 400 / 500 damage.
  - Slam attacks inflict 300 damage within 5 meters.
  - Attacks have a 2x critical multiplier, 50% critical chance, and 10% status chance.
  - Valkyr Talons can be equipped with melee mods and Arcane Enhancements.
    - Riven Mods are not generated for Valkyr Talons.
  - Because attacks with Valkyr Talons are counted as melee strikes, it is affected by mods and Warframe Arcanes such as Steel Charge and Arcane Fury.
  - Hysteria consumes 5 energy per second while active and will remain active until either Valkyr's energy is depleted or the ability is deactivated by pressing the ability key again.
    - Valkyr cannot replenish energy using Energy Vampire, Rally Point, Rift Plane's innate energy regeneration, Squad Energy Restores, Energy Siphon, Energy Nexus, Dreamer's Bond, and/or Wellspring while Hysteria is active.
    - Energy Orbs, Orokin Void Death Orb's energy restores, Spellbound Harvest, Arcane Energize, and Emergence Dissipate's Energy Motes can still replenish Valkyr's energy during Hysteria.
    - Hysteria's energy drain is not converted into shields by Augur Mods.
- While Hysteria is active, Valkyr can cast other abilities and use primary and secondary weapons. However, switching weapons will disable Hysteria's effects, including the status immunity, health restore, and Warcry's tripled armor, while continuing to drain energy over time.
- Cast time of 1 second is affected by Casting Speed.
- Hysteria's attacks can damage enemies across the Rift Plane.
- Movement-boosting passives from Incarnon melee weapons typically continue to function while Hysteria is active. A few examples include:
  - Drifting Grace (+20% Sprint Speed, +20% Slide)
  - Evolved Ascension (+30% Parkour Velocity)
  - Striking Swiftness (+30% Sprint Speed)
  - Swordsman's Celerity (+30% Movement Speed)
- Mods that boost Wind Up Speed equipped on your regular melee weapon benefit heavy attacks done with Valkyr Talons.
  - This stacks with Wind Up Speed mods on Valkyr Talons itself.

Weapon

- Main article: Valkyr Talons

Valkyr Talons are Valkyr and Valkyr Prime's signature Exalted Weapon, summoned by activating the ability Hysteria. The weapon exclusively uses the Hysteria stance.

- This weapon deals primarily Slash damage.
- Innate and two polarities.

Advantages:

- Highest critical chance of all melee weapons.
- Innate 100 lifesteal on every hit.
- Very high attack speed.

Disadvantages:

- Low status chance.
- Short range.
- Requires energy to activate and keep active.

Stance

- Main article: Hysteria (Stance)

Hysteria is a unique Stance exclusive to Valkyr Talons that can only be acquired and used by activating Valkyr's fourth ability, Hysteria. This Stance overrides the Stance on any currently equipped melee weapon for as long as Hysteria remains active.

## Combos

Combo/Attack | Name | Attack Multipliers and Forced Procs | Avg Dmg Multi/s | Length @ 1.0 Attack Speed | Animation
Neutral (While Not Moving) | Fervor | 100% | 100% | 2x 200% | 2x 200% | 300% | 2x 300% | 666.7%/s | 2.9s | 
Forward (While Moving) | Rage | 100% | 200% | 200% | 300% |  |  | 470.6%/s | 1.7s | 
Forward Block (While Blocking & Moving) | Madness | 100% | 2x 150% | 3x 150% | 2x 200% | 3x 250% | 300% 300% 300% | 805.6%/s | 3.6s | 
Block (While Blocking) | Delirium | 300% | 2x 300% | 3x 250% | 300% 300% 300% |  |  | 1062.5%/s | 2.4s | 
Heavy (Heavy Attack) | Rise From Ashes | 500% | 300% 300% 300% 300% 300% |  |  |  |  | 750.0%/s | 2.0s | 
Slide (While Sliding) | Launching Spring | 6x 300% |  |  |  |  |  | 2250.0%/s | 0.8s | 
Aerial (While In Air) | One Point | 200% | 2x 200% | 300% |  |  |  | 620.7%/s | 1.4s | 
Wall (While Wall Latching) | Through Strike | 300% |  |  |  |  |  | 176.5%/s | 1.7s | 
Finisher (On Knocked Down Enemy) | Roaring Drums | 5x 250% |  |  |  |  |  | 961.5%/s | 1.3s | 
Slam (Looking At Ground While In Air) | Slam Attack | 200% |  |  |  |  |  | 0.0%/s | 0.7s | 
Default "Sweep" Attack • 360°/Spin Attack • Direct and Radial Slam Attack • Ranged Attack • "Thrust" Attack View Full Legend Key Inputs Basic Melee (PC default LMB or E; Xbox, PlayStation, and Nintendo Switch default right button) Heavy Attack (PC default MMB; Xbox, PlayStation, and Nintendo Switch default left trigger) Block (PC default RMB; Xbox, PlayStation, and Nintendo Switch default right trigger) Forward Movement (PC default W; Xbox, PlayStation, and Nintendo Switch default tilt up right thumbstick) Multipliers and Hits 200% Attack does double damage 2x 100% Attack hits twice Forced Procs Knockback Weakened Bleed Detonate Knockdown Lifted Stagger Big Stagger Ragdoll Finisher (front, back, or ground) Impair (PvP only) Melee Attack Explanations "Sweep attack" is an arcing melee strike that hits an enemy with the edge of the blade (the length of obround melee hitbox). "Thrust attack" is a melee strike that hits an enemy with the tip of the blade (the rounded edge of obround melee hitbox). "360/spin attack" is a sliding sweep attack that hits targets around the player (not always in a 360° arc, but is usually above 180°). "Direct slam attack" is a melee strike that hits a single target at the epicenter of a slam attack. Affected by the Seismic Wave mod. "Radial slam attack" is the area-of-effect component of the melee slam attack. Affected by the Seismic Wave mod. "Ranged attack" is any melee attack that launches a ranged projectile or can hit targets beyond melee range. View Full Legend Average Damage Multiplier per second only applies to single-target DPS calculations. Hits marked as "Radial Slam Attack" will not apply at the epicenter of a single target hit so these will not be accounted for in Avg Dmg Multi/s calculations. Combo animation lengths are approximate and are only accurate within a few tenths of a second. Each tile marking in stance preview gifs are 2m apart. Combos labeled with an asterisk (*) are shared between weapons within the same weapon type.
Basic Melee (PC default LMB or E; Xbox, PlayStation, and Nintendo Switch default right button)
Heavy Attack (PC default MMB; Xbox, PlayStation, and Nintendo Switch default left trigger)
Block (PC default RMB; Xbox, PlayStation, and Nintendo Switch default right trigger)
Forward Movement (PC default W; Xbox, PlayStation, and Nintendo Switch default tilt up right thumbstick)
200% Attack does double damage
2x 100% Attack hits twice
Knockback
Weakened
Bleed
Detonate
Knockdown
Lifted
Stagger
Big Stagger
Ragdoll
Finisher (front, back, or ground)
Impair (PvP only)
"Sweep attack" is an arcing melee strike that hits an enemy with the edge of the blade (the length of obround melee hitbox). "Thrust attack" is a melee strike that hits an enemy with the tip of the blade (the rounded edge of obround melee hitbox). "360/spin attack" is a sliding sweep attack that hits targets around the player (not always in a 360° arc, but is usually above 180°). "Direct slam attack" is a melee strike that hits a single target at the epicenter of a slam attack. Affected by the Seismic Wave mod. "Radial slam attack" is the area-of-effect component of the melee slam attack. Affected by the Seismic Wave mod. "Ranged attack" is any melee attack that launches a ranged projectile or can hit targets beyond melee range.

Kit Interactions

- While channeling Hysteria, Warcry grants 3x additional Armor.
- Hysteria's Slide attack does 6 hits, rapidly gaining Rage, which increases the damage of Valkyr Talons.

Augment

- Main article: Enraged

Enraged is a Warframe Augment Mod for Valkyr's Hysteria that increases its damage and critical chance but fixes its duration to 15 seconds and adds a matching cooldown. The base Energy cost is also increased to 50, while the Energy drain over time is removed.

Rank | Damage & Critical Chance Bonus | Maximum Hysteria Duration | Maximum Hysteria Cooldown | Cost
0 | +200% | 15s | 15s | 6
1 | +250% | 15s | 15s | 7
2 | +300% | 15s | 15s | 8
3 | +350% | 15s | 15s | 9

- Main article: Hysterical Assault

Hysterical Assault is a Warframe Augment/Exilus mod for Valkyr that allows her to pounce onto enemies while in Hysteria by meleeing while aiming, dealing damage on contact, then provides a boost to Parkour Velocity and Sprint Speed. It also provides brief Invulnerability when switching off her Valkyr Talons while in Hysteria.

Rank | Leap distance | Parkour Velocity/Sprint Speed Buff | Buff Duration | Invulnerability duration | Cost
0 | 25m | 20% | 5s | 0.5s | 6
1 | 30m | 30% | 5s | 0.5s | 7
2 | 40m | 40% | 5s | 0.5s | 8
3 | 50m | 50% | 5s | 0.5s | 9

Tips & Tricks

- The health generation and high armor stat synergize greatly with Arcane Persistence, you just need to add max health.
- There may be a dark red hue for the duration of Hysteria, making it difficult to see enemies. This is especially problematic if Infested Parasites are nearby.
  - Turning 'Color Correction' off in Options > Display can alleviate this issue.
- Considered alone, Steel Charge adds more damage to Hysteria than Growing Power, but this changes when using Condition Overload.
  - Having enough status effects on the target causes CO's damage boost to vastly reduce Steel Charge's overall benefit, since they stack additively, while Growing Power's boost stacks with CO multiplicatively.
  - Steel Charge does grant an extra 4 mod capacity to Valkyr herself, though.
  - Even with Steel Charge equipped, using Power Drift will still add more damage than Coaction Drift.
- Heavy Attacks in Hysteria open enemies to Finishers, allowing you to reliably use the damage boost without spending energy on her Paralysis ability.
  - This finisher also knocks enemies down, allowing for a successive ground finisher for a quick burst of high damage.
- The opening heavy attack in Hysteria's two-attack heavy combo is considered a slam, and thus benefits from Seismic Wave.

Maximization

Melee damage modifier:
Elemental damage modifier:
Faction damage modifier:
Rage percentage:
Enraged?
Hysterical Assault?

Hysteria

Bugs

- Using Hysteria the moment you are downed by enemies will trigger a bug. Sometimes, you'll only be able to use your actual melee weapon, but it will swing as though it's your claws. In other instances, you may be able to use your other weapons, while also being invincible. You must wait until the effect ends for the bug to clear.
- If only a melee weapon is equipped in the player's loadout, casting Hysteria while holding either a Codex or Synthesis Scanner will cause Hysteria's attacks to instead use the equipped melee weapon's quick-attacks, while also making it impossible to use combos or to block.

This section is transcluded from Voruna/Abilities/Passive. To change it, please edit the transcluded page.

Like a blood moon striding across the starlit night, Voruna never hunts alone. Safeguarded by her four loyal wolves, she may freely invoke their protective passives anytime during a mission.

Hold down the ability button (default 1 , 2 , 3 , 4 ) to invoke 1 passive into the UI indicator above the ability icons. Wolf passives persist indefinitely until switched, undergoing a cooldown (Ulfrun's Descent), or revoked by holding down the ability key again; while a passive is selected, the corresponding wolf skull on Voruna's body glows with energy, as a flying wolf skull orbits around her.

- Shroud of Dynar increases Parkour Velocity by 50%.
  - Bonus is additive with other sources of Parkour Velocity.
- Fangs of Raksh grants complete resistance to new Status Effects.
- Lycath's Hunt imbues Voruna's melee weapon with an additive 100% Heavy Attack Efficiency.
  - Since heavy attack efficiency is hard-capped to 90%, the extra 10% is only visible and viable when equipped with a Riven Mod that penalizes it.
- Ulfrun's Descent has Ulfrun die in Voruna's place when she receives lethal damage, preventing bleedout, rendering her invulnerable for 3 seconds and restoring 100% of her shields and health. Ulfrun's passive undergoes a 60 second cooldown after his sacrifice or when swapped out.
- Passives are only available from Voruna's original abilities. Therefore, a subsumed ability replacement from the Helminth system will disable the associated passive.
- Passives are not disabled nor revoked when Voruna enters an ability-nullifying field such as from Nullifier Crewmen, or if she falls into an Out of Bounds zone.

 | 3 25 +10/s | Warding Grace Renders the Warframe and nearby allies immune to Status Effects, while slowing nearby enemies. Introduced in Update: Specters of the Rail 0.0 (2016-07-08) | Strength:20 / 30 / 40 / 50% (Slow)
Duration:N/A
Range:160 / 240 / 320 / 400 m

Info

- Amesha expends 25 energy to create an invisible field with a 160 / 240 / 320 / 400 meter radius which renders it and all nearby allies immune to Status Effects, as well as removing any existing negative status procs. Any enemies caught within the field are Slowed by 20% / 30% / 40% / 50%.
  - In Landscape missions, the range of Warding Grace is reduced down to 16 / 24 / 32 / 40 meters.
  - Slow is capped at 80%.
  - Warding Grace consumes 10 energy per second while active and will remain active until Amesha's energy is depleted or the ability is deactivated by pressing the ability key again.
    - Amesha can still receive energy from Energy Orbs and Vengeful Rush while Warding Grace is active.

Tips & Tricks

- Warding Grace can be helpful navigating tight corridors, as it will prevent stagger from collisions with the environment for the caster and any ally within range.

Maximization

Show Landscape ranges?

Warding Grace

Mods

- Carnis Carapace
- Carnis Mandible
- Carnis Stinger
- Empowered Quiver
- Hearty Nourishment
- Negate
- Purifying Flames
- Shield of Shadows
- Tidal Impunity

Miscellaneous

- Ancient Healer Specter

### Sources of Status Effect Cleansing

Status effect cleansing removes active status effects on the player.

Abilities

 | 3 | Bloodletting Garuda sacrifices her health to generate energy and clear Status Effects. Introduced in Update 24.0 (2018-11-08) | Strength:N/A
Duration:N/A
Range:N/A
Efficiency: 18 / 22 / 30 / 40 % (energy gain)
Misc: -50% (health deducted) 100% (status cleanse) 2 HP (minimum health threshold)

Info

- Garuda slashes herself with her talons as she spins into the air, sacrificing up to 50% of her maximum Health to cleanse all status effects and restore up to 18% / 22% / 30% / 40% of her maximum Energy capacity. Garuda cannot reduce her health below 2 health points using Bloodletting.
  - Health cost is 50% of Garuda's maximum HP, including mods.
  - Energy gain is the listed % of her maximum energy, including mods, Helminth invigorations and slotted Azure Archon Shards.
  - Energy gain follows the formula: Total Energy Gain = Base Energy Gain ÷ (2 - Ability Efficiency).
  - Bloodletting can be cast if Garuda has less than 50% of her maximum HP remaining, but will only restore energy proportionate to the amount of HP sacrificed. For example, if she has 25% of her health left (or 50% of 50%) when Bloodletting, the energy gain will be halved.
- Cannot be cast if Garuda has 2 or less health points.
- This ability does not trigger health damage into energy conversion mods like Rage or Hunter Adrenaline.

Augment

- Main article: Blood Forge

Blood Forge is a Warframe Augment Mod for Garuda's Bloodletting to reload her equipped weapon up to a percentage.

Rank | Reloaded Up To | Cost
0 | 25% | 6
1 | 50% | 7
2 | 75% | 8
3 | 100% | 9

Tips & Tricks

- This ability gains no benefits from increasing health. Having lower max health allows flat HP regeneration such as health orbs or Oberon's Renewal to generate more energy more quickly.
- Synergizes with Blood Altar's continuous healing to give Garuda a near infinite supply of energy.
- Despite sacrificing HP, Bloodletting is an effective way of shedding off any harmful status effects (especially slowing effects and DoT procs from Slash and Toxin damage), possibly improving her survivability better than not removing the procs.
- Bloodletting is a powerful ability to combine with Helminth-infused toggled abilities that constantly drain energy, the most notable being Sevagoth's Gloom as it provides Garuda with another self-healing ability besides Blood Altar to constantly regenerate her energy reserves.
  - The Gloom and Bloodletting combo makes Garuda viable at completing Steel Path missions alone, including missions not normally frequented by players such as the Rathuum nodes and the Zealoid Prelate battle in Deimos.
  - Seeking Talons also synergize extremely well with this build as the damage-over-time of her quills also triggers Gloom healing and, subsequently, powers Bloodletting. The quills' homing ability also offers little chance for enemies to escape and can even track and hit hiding enemies, ensuring Garuda can be healed by Gloom as long as they stay within the aura.
  - Molt Reconstruct can work as a stand-in for Gloom's regeneration by allowing any energy spent to heal a large portion of Garuda's health. Often healing her to full in a single cast.
    - Bloodletting itself will not restore health however, as it does not expend any Energy.
- Equipping Blood Forge and using Bloodletting allows Garuda to quickly reload otherwise slow-reloading weapons (such as the Strun, Nagantaka, Tenet Envoy and Kuva Zarr) and increase their overall DPS potential. It comes at the risk of getting struck while already losing her Health to reload, thus she should consider safeguards such as a nearby Blood Altar or equipping Quick Thinking and/or Gladiator Finesse, the mods accounting for her replenished Energy while using Bloodletting.
  - Slotting Azure Archon Shards for extra Energy while also equipping Quick Thinking will make Garuda deceptively durable due to the resulting increased efficiency of regaining Energy via Bloodletting.
  - Slotting Azure Archon Shards for extra Armor instead of extra Energy grants Garuda more effective hitpoints since Quick Thinking benefits from Armor.
- If a Garuda player wishes to take advantage of the reworked passive to further amplify damage output, Helminth can replace Bloodletting with another damage-related self buff ability, such as Xaku's Xata's Whisper or Mirage's Eclipse, as these abilities synergize well with the damage buff and Garuda's own Seeking Talons, while still maintaining self-survival options with Dread Mirror and Blood Altar.
  - In exchange for losing this ability to generate Energy, Garuda can equip Rage or Hunter Adrenaline so she gains Energy while taking damage - which will be offset by a nearby Blood Altar.

Maximization

Current Health percentage:

Bloodletting

 | 2 150 | Pillage Pillage a percentage of Shields and Armor of nearby enemies to replenish Hildryn's own Shields and Overshields. Also removes Status Effects from Hildryn and her allies. Introduced in Update 24.4 (2019-03-08) | Strength:10% / 15% / 20% / 25% (shield/armor drain per enemy)
Duration:2 s (expansion duration)
Range:5 m / 6 m / 7 m / 8 m (pulse initial radius)
Misc: ? / ? / 6 / 20 m/s (expansion distance per sec) 100% (status cleanse on cast)
Subsumable to Helminth

Info

- Hildryn expends 150 shields or overshields to emit a radial pulse with an initial radius of 5 / 6 / 7 / 8 meters, which follows her as an aura and rapidly expands outward by ? / ? / 6 / 20 meters per second over a duration of 2 seconds. Hildryn and allies touched by the expanding pulse are instantly cleansed of all negative Status Effects. Enemies in direct line of sight of Hildryn and within range of her aura are marked for pillage, reducing their current Shields or total Armor by 10% / 15% / 20% / 25%. When Pillage expires or when the ability key (default 2 ) is pressed again while the ability is active, the pulse instantly retracts to Hildryn to restore her missing shields and produce Overshields based on the amount of shields and/or armor stolen from all pillaged enemies.
  - Enemy armor and shields are fully removed at 400% Ability Strength.
    - With one Corrosive Projection, armor will be fully stripped at 328% Ability Strength.
    - Enemy shields can still regenerate with natural shield regeneration (such as Armis Ulta, Kuva Liches, or Sisters of Parvos) or while affected by regeneration buffs (such as Shield Ospreys).
  - Does not steal from enemies without shields or armor stats.
    - Enemy Overguard will not be stolen, converted, or damaged in any way.
  - Magnetic has no effect on the shield damage done to enemies.
  - Enemies that possess both shields and armor will need to have their shields broken before armor can be pillaged.
  - Pillaged enemies leaving Pillage's pulse and/or Hildryn's line of sight will still return shields to her.
- From Activating the ability, it takes 0.2 seconds of cast time (can be reduced) for the aura to spawn and start expanding at its given rate for the modded duration. After Which it takes 0.5 seconds for the drained defenses to return to Hildryn as shields (cannot be reduced).
- Casting Pillage is a full body animation that stops Hildryn's movement and melee (but not weapon firing) for 0.75 seconds of cast time (can be reduced).
- Hildryn's shoulder-mounted shield pads briefly become visible when Pillage is cast.
- Enemies affected by Pillage glow in an upward stream of energy particles. Pillaged shields return to Hildryn as energy missiles once the ability expires or is recast while active.
- Pulse, energy stream, and energy missiles are affected by Hildryn's chosen Warframe energy color.
- The total shields restored equal the total amount of armor and shields redued from affected enemies by the pulse and the excess above maximum shields is converted into Overshields.

Helminth

- Subsuming Hildryn to the Helminth will offer Pillage and its augments to be used by other Warframes.
  - Subsumed Pillage uses 50 energy instead of shields.
  - Does not generate shields for Inaros, Nidus, or Kullervo.
  - Other Warframes cannot make use of the Blazing Pillage augment, due to their inability to cast Haven.

Augment

- Main article: Blazing Pillage

Blazing Pillage is a Warframe Augment Mod for Hildryn that makes enemies affected by Haven receive Heat damage with a guaranteed proc and restore Shields to Hildryn when hit by Pillage.

Rank | Heat Damage | Shields restored | Cost
0 | 50 | 20 | 6
1 | 100 | 30 | 7
2 | 150 | 40 | 8
3 | 200 | 50 | 9

Tips & Tricks

- Similar to Molecular Prime, ability duration is far more effective at increasing this ability's range than ability range itself. Increasing duration also provides more time for Hildryn to move around and tag enemies with the aura.
- Using Corrosive Projection is useful , as the armor strip is additive with Pillage. For example, the 18% reduced armor from Corrosive Projection equates to 72% power strength that is no longer needed, bringing down the power strength requirement for a full armor strip from 400% to 328%.

Maximization

Infused?
Blazing Pillage?

Pillage
Additional Shield restoration: | / Haven target

Bugs Visually, the ability only expands at 17-17.5 meters/second, but actually expands at 20 meters/second

 | 1 25 | Fire Walker Blaze a trail of flames, scorching enemies and cleansing allies. Teleporting blasts the landing area with a ring of fire. Introduced in Update 18.1 (2015-12-16) | Strength:50 / 100 / 150 / 200 ( Heat damage per second) 500 / 750 / 1000 / 1250 ( Heat explosion damage)
Duration:15 / 20 / 25 / 30 s (buff duration) 5 / 6 / 7.5 / 10 s (flame duration)
Range:3 / 4 / 5 / 6 m (explosion radius)
Misc: 15 / 15 / 20 / 25 % (movement speed bonus) 0.5 s (damage interval) 10 / 25 / 50 / 75 % ( Heat status chance) 100 % (flame trail status cleanse) ? s (flame ring duration)
Subsumable to Helminth

Info

- Nezha expends 25 energy to ignite his Wind Fire Wheels to gain 15% / 15% / 20% / 25% bonus Movement Speed for 15 / 20 / 25 / 30 seconds, while leaving behind a trail of fire beneath his feet that lasts for 5 / 6 / 7.5 / 10 seconds. Enemies that walk over the flames are dealt 25 / 50 / 75 / 100 Heat damage per 0.5 seconds, with each instance of damage having a 10% / 25% / 50% / 75% Heat status chance. While Nezha and his allies stand on the flames, they are immune and continually cleansed of all Status Effects.
  - Cast animation of ~0.5 seconds, affected by Casting Speed.
  - Flames can be formed in mid-air but only while Bullet Jumping. Falling will not leave behind any flames.
- Damage does not bypass obstacles in the environment and diminishes with distance.
- Fire Walker can be cast while moving but will interrupt all other actions.
- Can be recast while active to refresh its duration.

Kit Interactions

- If Fire Walker is active when using Blazing Chakram's teleportation, Fire Walker will overheat at the destination and deal 500 / 750 / 1000 / 1250 Heat damage with a 10% / 25% / 50% / ? Heat status chance within a radius of 3 / 4 / 5 / 6 meters, as well as leaving a lingering ring of Fire Walker's flames for ? seconds.

Helminth

- Subsuming Nezha to the Helminth will offer Fire Walker and its augments to be used by other Warframes.
  - This does not allow other Warframes to use Fire Walker's explosion on teleport. This is exclusively a synergy with Blazing Chakram.

Augment

- Main article: Pyroclastic Flow

Pyroclastic Flow is a Warframe Augment Mod for Nezha and Nezha Prime that accumulates the damage Fire Walker deals and unleashes it in a trail of fire upon reactivating the ability.

Rank | Damage Accumulation | Trail Duration | Cost
0 | 100% | 6s | 6
1 | 150% | 7s | 7
2 | 200% | 8s | 8
3 | 250% | 10s | 9

Tips & Tricks

- The 75% chance of the Heat status effect makes this an effective form of control for narrow hallways or choke points while also temporarily stripping the enemies armor.
- Quickly sliding into groups of enemies can reliably disable them.
- The amount of ground that can be covered in flames can be improved using Sprint Speed mods.
- Also works as an escape tool to prevent enemies from following you.
- Can be used to cut off melee units from defense objectives.
- Briefly tapping slide key allows for additional control over Nezha's momentum while maintaining the additional speed.
- Choosing a dark energy color makes the visual effect less intrusive.

Maximization

Pyroclastic Flow?

Fire Walker

 | 2 50 | Hallowed Ground Sanctifies the ground around Oberon, inflicting Radiation Damage to all enemies within the radius. Also grants protection against Status Effects for Oberon and his allies. Introduced in Update 11.5 (2013-12-19) | Strength:25 / 50 / 75 / 100 ( Radiation damage)
Duration:10 / 15 / 17 / 20 s
Range:8 / 10 / 12 / 15 m (radius)
Misc: 100% ( Radiation Status Chance) 0.5 s (damage tick interval) 3 (Hallowed Ground cap)

Info

- Oberon expends 50 energy to consecrate the ground around him up to 8 / 10 / 12 / 15 meters, for 10 / 15 / 17 / 20 seconds. Enemies standing on the area of effect are dealt 25 / 50 / 75 / 100 Radiation damage with 100% Radiation status chance every 0.5 seconds. Allies are cleansed and granted full Status Immunity for as long as they are standing in the area.
  - Up to a maximum of 3 Hallowed Grounds can exist at a time.
  - Area of effect extends ~2m above and below the casting surface.
  - If cast in midair, Oberon will instantly drop to the ground to perform this ability.
  - Nullifier Crewman will not destroy Hallowed Ground, but instead render enemies immune to its effects while inside the bubble.
- Hallowed Ground spawns foliage inside its area of effect as visual representation. Oberon creates a field of grass, while Oberon Prime creates a field of ferns. Grass and ferns are affected by Oberon's chosen Warframe Accent color.
  - The shimmering energy field encompassing the ground is affected by Oberon's chosen Warframe energy color.

Kit Interactions

- Renewal's Health restore per second is increased by 2x when standing on Hallowed Ground.
- Hallowed Ground rapidly applies Radiation statuses to boost Reckoning's damage.

Augment

- Main article: Hallowed Eruption

Hallowed Eruption is a Warframe Augment Mod for Oberon's Hallowed Ground that causes recasts to detonate the ground for all its remaining damage with a chance to inflict a Radiation status. It also passively increases the duration of Hallowed Ground.

Rank | Bonus Duration | Cost
0 | 50% | 6
1 | 100% | 7
2 | 150% | 8
3 | 200% | 9

Tips & Tricks

- Enemies will traverse and fight through Hallowed Ground without any special attempts to evade its area of effect.
- Narrow pathways such as doorways and halls are effective at forcing groups of enemies to cluster into Hallowed Ground.
- Summoning multiple, overlapping layers of Hallowed Ground will deal the full combined damage over time to enemies.
- Hallowed Ground is most efficiently used in areas where constant enemy and ally activity is expected over an extended period of time.
- Hallowed Ground's status effect immunity can be used to pass through environmental traps unhindered, such as Grineer Magnetic Sensor Bars and Corpus Laser Barriers.
  - Note however that activating these traps in spy missions will still trigger vault alarms.
- Hallowed Ground will make players immune to to Radiation and Magnetic singularities in Sorties.

Maximization

Hallowed Eruption?

Hallowed Ground

 | 3 75 | Disometric Guard Guard yourself and nearby allies against Status Effects. Each time Qorvex kills or assists in killing an enemy affected by Radiation Status, the number of Status Effects Disometric Guard can prevent increases. Introduced in Update 35.0 (2023-12-13) | Strength:200 / 300 / 400 / 500 Radiation damage on cast 2 / 3 / 4 / 5 initial status immunity stacks 5 / 7 / 8 / 10 max status immunity stacks
Duration:N/A
Range:N/A
Misc: 6 m damage radius Radiation status and Knockdown on cast 50 m Affinity Range Status cleanse on cast ∞ stack duration +10% stack chance per active Radiation status on enemy from kills and assists 100% stack chance cap

Info

- Qorvex expends 75 Energy to explosively fragment out several protective concrete plates. On cast, Qorvex reels back then leaps in the air, detonating an explosion that inflicts 200 / 300 / 400 / 500 Radiation damage with a guaranteed Status Effect and Knockdown to enemies in a radius of 6 meters.
- After the explosion, Qorvex's concrete plates encircle himself and allied Warframes inside his Affinity Range. All negative status effects on Qorvex and his allied Warframes are first cleansed, then an initial number of 2 / 3 / 4 / 5 stacks of concrete plates surround them. Each stack lasts indefinitely until consumed by negating an incoming status effect, including Knockdown and self or enemy-inflicted Stagger.
  - Status cleanse on cast is a separate function and does not consume an initial stack.
  - Each guarded Warframe consumes stacks individually and do not reduce the stacks on other guarded Warframes.
  - Allied Warframes retain their Disometric Guard stacks when leaving Qorvex's Affinity Range, and even when Qorvex himself has zero stacks.
  - When a status effect is negated, the player's screen borders flash in a fading radioactive visual effect, while an orbiting concrete plate dissolves away.
  - Concrete plates orbiting a player visually disappear when aiming down sights with ranged weapons, and when the camera is positioned close to Qorvex's character model.
- While Qorvex has at least 1 stack of Disometric Guard remaining, when Qorvex himself kills or assists in killing an enemy with an active Radiation status effect, there is a 10% chance to add 1 stack to Qorvex and allied Warframes in his Affinity Range; for each active Radiation status effect on the enemy, the stack chance increases up to a cap of 100% at 10 Radiation statuses. Disometric Guard can only sustain max 5 / 7 / 8 / 10 stacks per player.
  - When gaining or losing stacks, concrete plates visually materialize or dissolve away, shuffling the entire orbit to occupy equal distances between plates.
  - Amount of remaining stacks are shown on the ability icon and as a buff icon beside Qorvex's hitpoints indicator.
- Can be recast while active. If Qorvex and allied Warframes are below max stacks, recast adds initial stacks to their current stack count up to the max.

Kit Interactions

  - Radiation status effects from Chyrinka Pillar's pulses, Containment Wall's radioactive waves and smash, Disometric Guard's explosion, and Crucible Blast's beam increase the stack chance on kills and assists.

Maximization

Disometric Guard

Bugs

- In the Simulacrum, stacks visually do not disappear once the modding changed via Arsenal, but the ability is deactivated as expected. Qorvex is unable to prevent status effects properly due to the lingering stacks.
- Using transference, or being forced into operator form, may show 0 stacks when returning to the warframe. This is purely visual.

 | 3 50 | Reave Dash through enemies as a wall of sentient energy, leeching shields and health from any encountered, enhanced for thralls. Introduced in Update 23.5 (2018-08-24) | Strength:2 / 4 / 6 / 8 % (hitpoints drain/restore) 10 / 20 / 30 / 40 % (thrall hitpoints drain/restore)
Duration:0.25 / 0.5 / 0.75 / 1 s (duration)
Range:3 / 4 / 5 / 6 m (current width)
Misc: 25 m/s (travel speed) 100 % (status effects transfer) 1 (Mesmer Skin ally buff charge)
Subsumable to Helminth

Info

- Revenant expends 50 energy to transform into a torrent of Sentient mist-like energy that surges forward toward the aiming reticle, at a speed of 25 meters per second for 0.25 / 0.5 / 0.75 / 1 second. While traveling in energy form, Revenant is intangible, Invulnerable to damage and protected against new Status Effects, as he pushes an energy current with a width of 3 / 4 / 5 / 6 meters. Reave can be manually cancelled by pressing the ability key again (default 3 ) or jumping during the dash.
  - Casting speed is affected by Casting Speed.
  - Travel speed and distance are affected by Sprint Speed.
- Enemies passing through the energy current are drained 2% / 4% / 6% / 8% of their maximum Shields and Health, while Revenant restores 2% / 4% / 6% / 8% of his maximum shields and health from each enemy leeched; all active status effects on Revenant are also transferred to enemies he passes through.
  - Does not restore shield points to Revenant if enemies do not possess shields.
  - Hitpoints from enemies can be drained and restored to Revenant multiple times, if enemies pass through the same instance of Reave.
  - Revenant still removes all status effects if doesn't pass through any enemy.
- During Reave, Revenant continuously dashes toward the direction of the aiming reticle.
  - While grounded, Revenant can freely change his dash direction.
  - While airborne, Revenant cannot change directions until he makes contact with a horizontal surface.
- Can be cancelled by jumping, which preserves forward momentum.
  - While airborne, can only be canceled by pressing slide and jump buttons simultaneously.
- It is possible to slide during Reave, which allows going under obstacles as with normal slide.
- Casting Reave is an upper body animation that interrupts only upper body actions such as melee attacks or reloading and can be cast while airborne.
- Revenant visually becomes translucent and enveloped in Sentient energy during the dash.
- Sentient energy cloak, energy current, and particle trails are affected by Revenant's chosen Warframe energy color.

Kit Interactions

- Reave steals 10% / 20% / 30% / 40% Health and Shields from enemies affected by Enthrall (5x more than base).
  - The drain percentage displayed in Abilities and the Upgrade screen display the Thrall-empowered drain.
- While Mesmer Skin is active, Reave restores 1 charge per enthralled enemy that Revenant passes through, up to the full charge count.
  - While Mesmer Skin is active, allies such as Warframes and Companions that contact Reave's current will gain 1 Mesmer Skin charge.
  - Reave costs halved energy during Danse Macabre, with instantaneous casting speed and Danse Macabre's stopping animation can be skipped if deactivated during Reave.

Helminth

- Subsuming Revenant to the Helminth will offer Reave and its augments to be used by other Warframes. Note that the UI's listed 40% damage is not applicable for non-Revenant frames and instead deals 8% damage.

Augment

- Main article: Blinding Reave

Blinding Reave is a Warframe Augment Mod for Revenant's Reave that blinds enemies caught in its fog, while also passively increasing its range.

Rank | Ability Range | Duration | Cost
0 | +40% | 6s | 6
1 | +40% | 7s | 7
2 | +40% | 8s | 8
3 | +40% | 10s | 9

Tips & Tricks

- Since Reave deals a set percent damage to enemies' health, it can scale indefinitely.
  - Without mods, at 100% Ability Strength, it would take 13 Reave casts to kill any enemy, only 3 if that enemy is enthralled.
  - The percent damage is always significantly reduced against Nox, even with enthralled one. Thus, it is quite ineffective and inefficient to kill them with Reave.
- Use Aim Glide during Reave to descend slowly.
- Move the aiming reticle during Reave to change your dash direction.
- Dash in a circle around enemies to drain from them multiple times.
- Consoles can be activated and terminals can be hacked while Reave is active.
- When falling from a sufficient height that would induce a hard landing, activate Reave before or immediately after the hard landing to cancel it.
- Jump right before Reave ends to take full advantage of its speed and to conserve its momentum. This is especially handy on larger tilesets or the open world maps.
- If a turret on the Plains of Eidolon is hit with Reave, it is instantly destroyed, regardless of level.

Maximization

Target is Enthralled ?
Blinding Reave?

Reave

 | 2 50 | Molt Shedding her skin like a snake, Saryn leaves a decoy behind to draw fire from enemies. Introduced in Update 7.0 (2013-03-18) | Strength:150 / 300 / 400 / 500 (health) 240 / 300 / 350 / 400 ( Toxin explosion damage) 30% / 35% / 40% / 50% (movement speed buff)
Duration:14 / 24 / 32 / 40 s (decoy) 3.5 / 4 / 4.5 / 5 s (movement speed buff)
Range:5 / 6 / 7 / 10 m
Misc: 100 % (status cleanse on cast) 1.5 / 2 / 3 / 3 s (decoy invuln. time) 400 (decoy shields) 100 % ( Toxin status chance) 1 (limit of molts)
Subsumable to Helminth

Info

- Saryn expends 50 energy to shed her skin, removing all existing status effects and increasing her Movement Speed by 30% / 35% / 40% / 50% for 3.5 / 4 / 4.5 / 5 seconds, while leaving behind a decoy with 400 shields and 150 / 300 / 400 / 500 health that draws enemy fire for 14 / 24 / 32 / 40 seconds. When deployed, the decoy is Invulnerable for 1.5 / 2 / 3 / 3 seconds, during which all incoming damage absorbed by it is converted and added to its health. The decoy will explode if it loses all of its hitpoints, if its duration expires or if the ability is cast again, inflicting 240 / 300 / 350 / 400 Toxin damage with 100% Toxin status chance to all enemies within 5 / 6 / 7 / 10 meters from it. A maximum of 1 Molt can exist.
  - Explosion damage does not bypass obstacles in the environment and diminishes with distance.
  - Recasting while active will detonate the Molt and spawn a new one.
  - Does not have a cast time or animation.
- Molt's decoy is placed at Saryn's current position, mirroring her pose and elevation.
  - Molt's shields regenerate over time and can be buffed with the use of allied Shield Ospreys, whether in Specter or Mind Controlled forms.
  - Elemental augment mods, such as Ember's Fireball Frenzy, can be applied to Molt. The damage augment will not affect the explosion damage or damage type upon Molt's expiration.
  - Molt cannot be knocked down or moved, and acts as a physical object, unlike Loki's Decoy.
  - Molt will slowly vaporize and dissipate for its duration, eventually exploding once it nearly vanishes.
- Casting Molt can be done while performing any action without interrupting it, including reloading, charging, shooting, maneuvering, and while on a zipline.
  - Can be cast in all states (except while upside down in a flip jump or while dodging) and can be reused instantly.

Helminth

- Subsuming Saryn to the Helminth will offer Molt and its augments to be used by other Warframes.

Augment

- Main article: Regenerative Molt

Regenerative Molt is a Warframe Augment Mod for Saryn that allows her to regenerate health over a span of time after casting Molt.

Rank | Health Regeneration | Duration | Cost
0 | 20/s | 10s | 6
1 | 30/s | 10s | 7
2 | 40/s | 10s | 8
3 | 50/s | 10s | 9

Tips & Tricks

- Using during a well timed jump can result it being low enough for enemies to target, such as Infested or Melee units, but be more protected from most melee attacks. (Ancients will still be able to reach, as well as the knockback damage from Leapers).
- Place Molt in locations which can protect it from enemy attacks to maximize its survival.
- Limbo can utilize this ability by casting Banish on the decoy, granting it immunity to all attacks that do not affect targets in the Rift Plane.
- If Molt is closer to the enemy than the player, enemies will (normally) focus it. Applies to the caster as well as other players, unless they're using aggro-increasing abilities such as Nyx's Absorb or Rhino's Iron Skin.
- It can be used as protection from enemy fire, when you revive an downed teammate.

Maximization

Regenerative Molt?

Molt
Health restoration: | /10s

Bugs

- When knocked back by an Ancient, the physical target of the decoy will move, but the model remains in place. This can be seen while having Enemy Sense and Enemy Radar equipped while seeing the decoy (as a friendly blip) against a group of infested.
- For clients, Molt will sometimes be in a default standing position when deployed.

 | 1 25 | Spellbind Enemies fumble their weapons as they are whisked into the air. Nearby allies become immune to Status Effects. Hold the ability to cast the immunity onto Titania. Introduced in Update: The Silver Grove (2016-08-19) | Strength:N/A
Duration:10 / 12 / 14 / 16 s
Range:1 / 3 / 3 / 5 m (area radius) 20 / 30 / 40 / 50 m (cast range)
Misc: 100 % (status cleanse and immunity)
Subsumable to Helminth

Info

- Titania expends 25 energy to scatter enchanted dust in a 1 / 3 / 3 / 5 meter radius around the location she aims at, up to 20 / 30 / 40 / 50 meters away. Enemies within this area are Disarmed and Ragdolled as they weightlessly float in mid-air for 10 / 12 / 14 / 16 seconds. Titania and her allies caught within the dust cloud are cleansed from Status Effects and gain immunity to them for the duration of the ability. Holding down the ability key (default 1 ) casts the ability centered on Titania.
  - Cast animation of 1 second is affected by Casting Speed.
    - Can be cast while moving, but will interrupt other actions such as reloading, charging or shooting.
  - Status immunity also protects from crowd control effects such as Knockdown and Stagger, including the lock-out animation of Archwing and Razorwing when impacting a surface.
- After Spellbind expires, enemies previously armed with weapons cannot attack until they retrieve their weapons on the ground. Those that do not use weapons (such as the Infested) will recover quickly.
- Spellbound allies and enemies emit unique particle effects:
  - Enemies visually emit energy butterflies fluttering about and an upward stream of energy stripes, both affected by Titania's energy colors.
  - Allies visually emit energy butterflies fluttering about, affected by their own energy colors.
- Spellbind can be aimed at any surface, but will only allow you to use it if an enemy is within the predicted area of effect.
- Subsuming Titania to the Helminth will offer Spellbind and its augments to be used by other Warframes.

Augment

- Main article: Spellbound Harvest

Spellbound Harvest is a Warframe Augment Mod for Titania which lets her regain Energy and increases the Ability Range of the next cast of Spellbind after hitting at least 4 enemies with Spellbind.

Rank | Energy Granted | Next Spellbound Cast Range | Cost
0 | 20 | +10% | 6
1 | 30 | +20% | 7
2 | 40 | +30% | 8
3 | 50 | +40% | 9

Tips & Tricks

- The status immunity granted by Spellbind also prevents Titania from being staggered when hitting surfaces in Razorwing. Holding the button down to activate Spellbind on yourself can be really helpful when flying through tight spaces.

Maximization

Spellbound Harvest equipped and active?

Spellbind

 | 2 25 | Cloud Walker Evaporate into a cloud of mist and float through the battlefield, dazing any enemies encountered, while healing Wukong and his twin. Introduced in Update 17.12 (2015-11-25) | Strength:0.5% / 0.6% / 0.8% / 1% (health / meter)
Duration:2 s (cloud duration)
Range:5 / 6 / 7 / 8 m (stun radius)
Misc: +300% (movement speed bonus) 100% (status cleanse on cast) 2 s (stun duration)

Info

- Wukong expends 25 energy to disappear into a cloud, turning Invisible for 2 seconds. In this form, Wukong gains +300% Movement Speed, along with vertical and horizontal flight capabilities using the movement (W A S D ), crouch (Ctrl ), and jump (Spacebar ) hotkeys, similar to Archwing Maneuvers. While traveling in the cloud, Wukong is Invulnerable to damage, cleanses all Status Effects, and restores 0.5% / 0.6% / 0.8% / 1% health per meter travelled. Enemies that come within the cloud's radius of 5 / 6 / 7 / 8 meters are temporarily Stunned for 2 seconds and opened to Melee Finishers (default X ). Cloud Walker can be manually cancelled by pressing the ability key again (default 2 ) or by attacking.
  - Movement Speed buff is additive to other sources of movement speed such as using Dispatch Overdrive, infusing Saryn's Molt onto Wukong, or equipping Okina Incarnon Genesis with the Swordsman's Celerity evolution.
    - Buff is not affected by Sprint Speed, such as from Rush or parkour speed buffs such as Lightning Dash.
  - Unalerted enemies staggered by Cloud Walker remain unalerted during the stagger animation, and thus can engage Stealth Kill Affinity Bonuses when killed.
- Cloud Walker does not trigger Sensor Bars, Laser Barriers, and Security Cameras, and can pass through Spy defenses without triggering alarms.
- Wukong cannot cast other abilities, perform parkour Maneuvers or general interactions while Cloud Walker is active.

Kit Interactions

- When activating Cloud Walker with an active Celestial Twin, the twin becomes invulnerable to damage and receives the health restore per meter traveled bonus. After Cloud Walker ends, Wukong's twin is teleported to his side instantly.

Augment

- Main article: Enveloping Cloud

Enveloping Cloud is a Warframe Augment Mod for Wukong's Cloud Walker that gives allies near the cloud temporary invisibility.

Rank | Range | Duration | Cost
0 | 2.5m | 8s | 6
1 | 3m | 10s | 7
2 | 3.5m | 12s | 8
3 | 4m | 14s | 9

Tips & Tricks

- An equipped Robotic companion with Vacuum or Beast companion with Fetch will still collect nearby items and hold onto them for you to collect when Cloud Walker ends.

Maximization

Enveloping Cloud?

Cloud Walker

 | 3 50 | Defy Wukong and his twin become invulnerable and defy enemies to attack. All damage is captured, stored, and dealt back in a single furious strike of Wukong's staff. Bonus Armor is then granted relative to the damage captured. Introduced in Update 17.12 (2015-11-25) | Strength:4 / 5 / 6 / 7.5 x (damage multiplier) 0.8 / 1 / 1.2 / 1.5 x (armor multiplier)
Duration:2 s (invulnerability duration) 15 / 18 / 20 / 25 s (armor duration)
Range:7 / 8 / 10 / 12 m (staff swing radius)
Misc: 500 (minimum damage) -50 % (move speed penalty) 100 % (status cleanse on spin) 100 AP (min. armor bonus) 1,500 AP (armor bonus cap)
Subsumable to Helminth

Info

- Wukong expends 50 energy to engage a defiant stance while priming his Iron Staff, becoming Invulnerable to damage and new Status Effects, increasing his Threat Level to taunt enemies into attacking him, and reducing his Movement Speed by 50% for 2 seconds. Any damage Wukong takes while in this stance is absorbed and multiplied by 4 / 5 / 6 / 7.5, then stored. After the invulnerability period expires, Wukong cleanses himself of any negative Status Effects, spins in place while elongating his staff and deals 500 Impact damage plus the stored damage and Ragdoll to all enemies within a radius of 7 / 8 / 10 / 12 meters. The spin can be executed earlier by pressing the ability key again (default 3 ) or using melee attack.
  - Spin does not require line of sight to hit enemies.
    - The attack does have very little vertical range however, which can make it difficult to hit enemies in some environments.
- After executing his spin, Wukong gains a variable Armor bonus lasting for 15 / 18 / 20 / 25 seconds or until Defy is recast; Defy armor bonus value depends on the damage absorbed during the taunt, with the stored amount multiplied by 0.8 / 1 / 1.2 / 1.5 times to grant a minimum of 100 armor points, up to a maximum of 1,500 armor points.
  - Armor bonus is removed if Defy is recast before it expires.
  - While the armor bonus is active, a stylized armor bonus counter appears above the ability icons.
- Wukong cannot cast other abilities, perform parkour Maneuvers or general interactions during the taunt portion of Defy.

Kit Interactions

- When activating Defy with an active Celestial Twin, the twin engages in Defy, gaining the same increased Threat Level, invulnerability, damage absorption attack, and armor bonus.

Helminth

- Subsuming Wukong to the Helminth will offer Defy and its augments to be used by other Warframes.
  - However, Subsumed Defy's armor bonus is capped at 750.

Maximization

Infused?

Defy

Mods

- Hearty Nourishment
- Purging Slash
- Rolling Guard
- Safeguard Switch
- Tidal Impunity

### Status Resistance

Unlike sources of status immunity, these provide a percent chance to ignore an incoming proc on the player.

- Arcane Deflection
- Arcane Healing
- Arcane Ice
- Arcane Nullifier
- Arcane Resistance
- Arcane Warmth
- Empowered Quiver (chance affected by ability strength and mod rank)
- Fortitude
- Motus Impact
- Motus Setup
- Motus Signal
- Power Drift
- Primed Sure Footed
- Resolute Focus
- Holding Sancti Magistar, 20% to resist any incoming procs
- Sure Footed

## Status Immune Enemies

It's taking longer than I calculated.

This page is actively being worked on and may not be completely correct. Please assist in making this page accurate by adding more info. For guidance on performing research, see WARFRAME Wiki:Research.

### Full Immunity

- Arbitration Shield Drone
- Desert Skate
- Exploiter Orb
- Profit-Taker Orb
- Regulator
- Ropalolyst
- Eidolons, including Vomvalysts
- Tusk Thumper
- Tusk Thumper Bull
- Tusk Thumper Doma

### Partial Immunity

To Viral procs

- Ambulas
- Basal Diploid
- Deimos Carnis
- Deimos Genetrix
- Deimos Jugulus
- Deimos Leaping Thrasher
- Deimos Saxum
- Deimos Therid
- Demolisher Boiler
- Demolisher Charger
- Demolisher Juggernaut
- Demolisher Leaping Thrasher
- Feral Diploid
- Juggernaut
- Leaping Thrasher
- Mitosid
- Undying Flyer

## Trivia

- Prior to Update 25.7 (2019-08-29), a status effect's duration could be increased or decreased, along with the total number of ticks in the case of damage-over-time procs, if the target's speed was altered by a Warframe power (such as Molecular Prime or Rest & Rage) according to the following formulas:
  - For slowing effects: Effective status duration = (base status duration) ÷ (1 − slow % in decimals)
  - For speeding effects: Effective status duration = (base status duration) ÷ (1 + speed up % in decimals)

- Prior to Update 27.2 (2020-03-05), physical procs were weighted four times more than elemental ones.
- Prior to Update 27.2 (2020-03-05), shotguns' status chance per pellet were calculated differently, instead of being the exact status chance shown in the Arsenal: Chance per Pellet = 1 − (1 − Status Chance)(1 ÷ Pellet Count)
  - In other words, the status chance shown in the Arsenal represented the calculated probability that at least one of the weapon's pellets would proc.
  - This meant that shotguns that could reach 100% status chance in the Arsenal (before Multishot mods) benefited significantly more from a status build since each pellet would proc as a result of the above equation.
  - However, a shotgun that only reaches shy of 100% status chance when modded would see significantly diminished results.
    - For example, a 99% status chance on a 10 pellet weapon would result in a 36.9% status chance per pellet.

▾View Old Status Chance Calculation Table List ▾

A table with example values to display the relation of status chance and multishot.

 | Arsenal Status Chance
 | 100% | 99% | 80% | 100% | 99% | 80%
Pellets | Chance per Pellet | Average Amount per Shot
3 | 100% | 78.5% | 41.5% | 3 | 2.4 | 1.25
5 | 100% | 60.2% | 27.5% | 5 | 3.0 | 1.38
10 | 100% | 36.9% | 14.9% | 10 | 3.7 | 1.5
20 | 100% | 20.6% | 7.7% | 20 | 4.1 | 1.6

## Media

## Patch History

Update 42.0 (2026-03-25)

- Increased the number of Status Effects per line on Boss Health Bars.
- Fixed status effects being unclear by showing them on their own line under enemy names.

Update 40.0 (2025-10-15)

- Fixed Status Effect icons being hidden under large enemies (e.g., Scaldra Dedicant) models.

Update 38.5 (2025-03-19)

- Players will now parry enemy Status Effects when parrying an enemy Melee Attack.
  - This fixes Scaldra Flayers Gas Status Effect damaging players through Melee parries, turning a bug into a feature. Woo!

Update 37.0 (2024-10-02) Introducing a new Status Effect: Tau Damage

Being of half-Sentient origin, Caliban brings a new element to the fight. He’ll inflict Tau Damage and Tau Status Effects upon the battlefield with many of his abilities (specifics listed below for affected abilities).

Tau’s Status Effect inflicts Status Chance Vulnerability* to enemies affected by it, with a max of 10 Stacks culminating in 100% Status Chance Vulnerability (10% per Stack), with each stack individually lasting 8 seconds!

*This effect was originally introduced by Dante and his Pageflight Paragrimms, which applies Status Chance Vulnerability to enemies. This mechanic increases the likelihood an enemy receives a Status Effect when being hit.

UI QOL Changes

- Added an on-hover tip for the Status Damage stat to explain its mechanics (notably on Elementalist Mods).

FIXES

- Fixed an issue where rag-dolled enemies received more Electrical Status Effects than they should.
- Fixed Abilities or sources that could cleanse Status Effects unintentionally triggering Blast Detonate damage.

Update 36.0 (2024-06-18)

Status Effect Reworks

Blast

Our goal with Blast is to invoke an immediate and on-death effect to emphasize explosions.

Now, instead of enemy inaccuracy, you detonate your enemies! When dealing a Blast Status Effect to an enemy, the following will happen:

Blast Changes:

- Upon inflicting a Blast Status Effect, individual stacks will cause a mini-explosion, and a max stack count of 10 will inflict combined damage in a 5m radius
  - After 1.5 seconds, an individually incurred Blast Status Effect deals a percentage of base-inflicted damage per stack-explosion and over 100% of base-inflicted damage for a full (10 stack) explosion.
- Status Duration will increase the delay before the Status Effect applies and depletes.
- Removed the previous Status Effect of inaccuracy.

Cold

With Cold, we want to fully realize the fantasy of slowing, freezing and shattering your enemies. The existing Cold Status mechanic of slowing enemies is unchanged, but now has a new mechanic upon applying Max Stacks - freezing your foes!

Cold Changes:

- Cold now has a maximum cap of 10 stacks (was 9).
  - Applying 10 Cold stacks to a foe will make them Frozen for 3 seconds. Frozen enemies cannot move, will not recharge Shields, and receive double Critical Damage. After the Frozen effect wears off, 3 Cold stacks will remain.
    - Bosses, such as Alad V or Kela De Thaym, will be unable to be Frozen since they cannot accumulate 10 Cold stacks.

Gas

Gas often lacked effective readability, making it difficult to distinguish its presence from the enemy or yourself. We’ve introduced enhanced visuals so that when the Gas Status Effect is active, you’ll be able to recognize it more clearly.

Gas Changes:

- Added VFX on top of the target affected by a Gas Cloud to clearly show an effect is active.
  - In addition to current and new VFX, Gas VFX now also more clearly shows the radius of the Gas Damage-over-Time (DoT) effect around a given target to better understand its impact on surrounding enemies.
    - If a player is inside the radius of the Gas DoT, the visuals are reduced for them to maintain visibility, similar to Frost’s Snow Globe.
- Gas VFX now has billowy volume to better present presence.
- Gas VFX now has additional floating particles around the smoke.

Magnetic

Magnetic has received a few buffs to increase its effectiveness against Shields and to hammer home the power fantasy of overloading enemy Shields.

Magnetic Changes:

- Damage to Nullifier Bubbles has been increased
  - Minimum Damage raised to 300 Damage per shot.
  - Maximum Damage raised to 1200 Damage per shot.
  - Additionally, we now show the minimum and maximum damage numbers against Nullifier Bubbles, with Magnetic attacks displaying the buffed damage shown above, while non-Magnetic sources will display the original, unbuffed damage.
    - Known issue: Clients see the incorrectly unbuffed damage from Magnetic sources, which is strictly a UI/visual bug. Magnetic sources will continue to deal increased damage towards Nullifier Bubbles despite the incorrect numbers displayed. We will look to resolve this in a future Hotfix/Update.
- Reduced Shield Regeneration by a percentage per Magnetic stack against affected targets.
- Upon Shield/Overguard Breaking a target, the enemy will now be dealt Electric Status damage for a percentage of Max Shields/Overguard per Magnetic stack while also forcing an Electric Status Effect.
- Magnetic stacks on an enemy with Overguard now allow for bonus damage to Overguard, similar to how Magnetic affects Shields.

Update 35.0 (2023-12-13)

- Fixed icons of currently inflicted Status Effects not appearing over enemy heads with the “Show Enemy Names” setting toggled off.

Update 34.0 (2023-10-18)

- Fixed Status Proc icons appearing under squadmate username when aiming over their player avatar. Now these icons will appear beside their name to improve legibility.

Update 33.6 (2023-07-27)

Status Changes

With the variety of Status effects in Warframe, there are certain types that may be seen as less favorable than others. Cold, Puncture, and Impact tend to have a lesser impact on the battlefield, so we felt it was time to revisit the value they added to player kits:

Puncture Changes: Weakened Status Effect Buffs:

- Increased the debuff to enemy attacks from 30% to 40% on the first stack.
- Reduced the maximum amount of stacks from 10 to 5.
- Increased per-stack debuff from 5% to 10%.
- Increased the total debuff at Max Stacks from 75% to 80%.

Weakened Status Effect Additions:

- Increases Critical Chance threshold on enemy by 5% per Stack, to a maximum of 25% at 5 Stacks. This is additive after mods, not before. Does not apply to Abilities or AOE damage.

Impact Changes: Stagger Status Effect Changes:

- Reduced the maximum amount of stacks from 10 to 5.
- Increased the Mercy Threshold from 4% to 8% per stack.

Functionally, this allows for players to trigger early Mercy kills with less stacks required!

NOTE: These changes should not affect the functionality of Impact Stacks for Mods such as Internal Bleeding or Hemorrhage.

Cold Changes: Freeze Status Effect Changes:

- Increased the maximum amount of stacks from 8 to 9.
- Increased the additional per-stack Slow from 3.5% to 5%.
- Increased the maximum Slow effect from 75% to 90%.
- While we previously mentioned buffing Cold Slow Effect to 85% in our Citrine’s Last Wish update, we mistakenly only increased it to 75% instead.

Freeze Status Effect Additions:

- Increased the Critical Damage taken by an enemy by 10% on initial Status Effect Subsequent Stacks increase this debuff by 5%, up to a maximum of 50%. This is additive after mods, not before.

Update 33.0 (2023-04-26)

- Fixed issues with enemies affected by Status Effects not behaving as intended when the game is paused.

Update 32.3 (2023-02-15)

Cold Status Effect Changes:

Cold Damage has traditionally been one of the lesser-used and valued Status Effects within the community, as its effect on foes may not be as noticeable compared to its peers. As a result, we’ve decided to to make the following changes:

- Increased base Slow from 25% to 50%.
- Max stacks reduced from from 10 to 8.

Final result of the above is an overall increase in the Max Slow from 70% to 85%.

Update 31.5 (2022-04-27)

- Removed potential rare specific scenarios where Status Effects could potentially do unintended critical damage.

Update 27.2 (2020-03-05)

Damage-Type Changes:

- Slash Status now does not bypass Shields and instead deals damage over time to Shields. Slash Status still bypasses Armor.
- Toxin Damage used to apply to Armor with a 25% bonus. Now it is neutral. For role distinction, Toxin bypasses Shields (but not Armor) where as Slash Status bypasses Armor but not Shields.

Greater than 100% Status having meaning

Years ago we added Orange and Red Critical Damage numbers when you land a Critical with greater than 100%. For years, Status being greater than 100% has done nothing except guarantee Status - which is good, just not an added incentive to go over 100%. We are changing that this update.

When you hit a Status Chance greater than 100%, a single damage instance will be able to create two Status Effects. This means if you have a Shot with 200% Status Chance modded with both Blast and Toxin Damage, that single shot will result in both Status Effects!

It is worth noting we are fixing a UI inconsistency that is ‘Display Only’. Right now the Arsenal shows Status Chance affected by Multishot, which makes reading the new >100% value confusing. For example, the Arsenal might say 120% but really the Status Chance is 80%. We don’t have Multishot affect any Critical Stats (Chance or Multiplier), so we are fixing this display inconsistency. Multishot now has its own Stat.

Shotguns have a unique Role here based on a very patch-work history with how they interact with Status Chance. A Shotgun that shoots 99% Status Chance would give you 35% (roughly) status per pellet. 100% Status Gives you 100% Status per pellet. This huge jump in performance happens with just a 1% gain - why? Well, to answer that we have to look at our choice to make what the UI conveys reality. It would feel broken to shoot a Shotgun with 100% Status and not see a perfect spread of Effects. In reality, to make Status consistent we have to treat Shotguns as a special case.

Shotguns as a special case means we have buffed the Status Chance of all Shotguns by x3 or greater. The UI now behaves to show the reality that you are determining Status Chance per pellet.

Stacking Status Effects

But wait - THERE’S MORE! In addition to being able to achieve two Status Effects on a single shot with >100% Status, we are also adding new meaning if you get a duplicate Status Effect on an enemy overall.

This section will outline exactly what this means for each Status type, including information on how multiple Status Effects behaved with stacking prior to this Hotfix:

- Impact: Repeat single-target Impact Status Effects will escalate the efficacy of the Impact Status (removed previous change of adding Ragdoll as maximum Stagger consequence).
- Puncture: The first Puncture Status Effect has an enemy deal 30% less Damage. Subsequent Puncture Status add +5% weakening, leading to up to 75% (capped). Each Puncture Status has a duration of 6 Seconds.
- Slash: Each Slash Status has its own duration, but now we only show a maximum of 10 damage numbers in the HUD, damage is unaffected, but reducing how many damage events we show helps with performance
- Cold: The first Cold Status Effect deals 25% slow. Subsequent Cold Status Effects deal +5% slow for a total of 70% slow at 10 procs. Each Cold Status has a duration of 6 seconds.
- Heat: No Change.
- Toxin: See Slash, plus the base duration of a Toxin Status Effect now matches Slash for 6 seconds.
- Electricity: AoE Electric Damage that is part of the Status Effect can now reoccur while the target is still under the stun animation of another Electric Status Effect.
- Blast: Grants the Blast Status Effect a single target. Blast Status reduces enemy accuracy by 30% base. Subsequent Blast Status Effects add +5% inaccuracy for for 75% total at 10 stacks. Each Blast Status has a 6 second Duration.
- Corrosive: The first Corrosive Status Effect strips 26% Armor. Subsequent Corrosive Status Effects strip 6% more Armor, leading up to 80% Armor removal. Each Corrosive Status Effect lasts 8 seconds. Note: Corrosive was the only Status with infinite Duration and 100% Efficacy toward a defensive stat. This was necessary to some based on how Armor Scaled. We feel our rebalancing efforts need a differently behaving Corrosive to balance out all Status overall.
- Radiation: The first Radiation Status Effect has an enemy deal 100% Damage to allies. Subsequent Radiation Status adds +50% damage, leading to up to 550% (capped). Each Radiation Status Effect has a duration of 12 seconds.
- Magnetic: New Status Effect entirely: enhanced Damage! First Magnetic Status Effect deals 100% additional Shield damage, subsequent Magnetic Status add +25% for a total of 325% (capped). Enemies under a Magnetic Status Effect cannot regenerate Shields. Magnetic Status Duration is now 6 seconds.
- Viral: New Status Effect entirely: enhanced Damage! First Viral Status Effect deals 100% additional Health damage, subsequent Viral Status add +25% for a total of 325% (capped).
  - Note: Before Viral would halve a target’s health pool and simply refresh the duration. Now it deals 2x Damage to Health, and can scale up to 4.5x Damage on repeat Status Effects.
- Gas: The base duration of a Gas Status Effect now matches Slash for 6 seconds. No longer does AoE with forced Poison Status Effect (resulting in Poison DoT for enemies in radius), instead it does AoE DoT Gas damage around the target.

Players - aka Tenno - can only have a Maximum of 1 Stack on them - you cannot receive Stacked Status Effects as a player from enemies, fear not!

Why: The inclusion of enhanced or different stacking of Duplicate Status Effects is one to refresh the appeal of Status.

In addition, we’ve removed 0.25x Multiplier for Elemental Status Effects, meaning all Elemental Status Effects are 4x more likely.

Why: Critical has long been king - and while we are leaving Critical as is, our goal is to bring Status into the Arsenals in a new light for all Primary, Secondary, and Melee weapons. Our long-term goal with this change is to build upon this series of changes to eventually allow Status to impact bigger threats like Liches and Eidolons.

Update 27.1 (2020-02-04)

- Fixed projectile explosion & embed damage not properly using Status Chance upgrades.

Update 25.7 (2019-08-29)

- Reduced Status Effect light FX intensity further to compensate for stacking procs (Gas multiprocs, etc.)
- If you freeze enemies with things like Frost, Atlas, or Gara’s abilities, you can now immediately apply other Status Effects! Before these powers would prevent Status Effects from being added. Read more on that here: https://forums.warframe.com/topic/1119134-cold-status-effects-how-they-block-new-status-effects-coming-changes/
- Fixed Status FX not applying to ragdolled enemies.
- Fixed sometimes seeing duplicate corpses if the enemy died from a Slash Status Effect.

Update 11.7 (2014-01-15)

- Continued Changes to proc/status logic with Continuous Fire weapons:
  - Their proc/status is now determined per second – the Arsenal will display the “Status per second” value. Continuous fire weapons that had a weaker proc chance before should be yielding reasonable proc/status per second with this calculation.

Hotfix 11.0.2 (2013-11-21)

- Added more visibilty to Proc/status on enemies when dealing damage. Proc/status icons added to damage numbers.

Update 11.0 (2013-11-20)

- New Damage Model 2.0! More information here: https://forums.warframe.com/index.php?/topic/132366-information-on-damage-20/
- Stun Chance mods (Pistol, Rifle, Shotgun, Melee) are now Status Effect mods in accordance with new damage system
