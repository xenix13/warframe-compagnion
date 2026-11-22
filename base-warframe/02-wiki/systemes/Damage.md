# Damage (wiki)
Source : https://wiki.warframe.com/w/Damage

Damage

Calculation

Overview Table

Preceded by
Damage 2.0 since Update 36.0 (2024-06-18)

Damage

Damage (version 3.0) is a system that determines the damage done to a certain target by a given attacker. Damage results are modified by several mechanics – damage type modifiers (main content of this article), armor, critical hit bonuses, stealth bonuses, Warframe ability debuffs, body part modifiers, faction modifiers, and other sources of damage reduction – which are discussed below and on their respective pages.

All damage dealt by any weapon or ability belongs to a certain damage type, and every target has specific resistances and vulnerabilities to different damage types. In-game, enemy resistances and vulnerabilities can be seen in the player's Codex after scanning at least one enemy of a particular type or by aiming at an enemy using the Synthesis Scanner with the Data-Parse Widget. Exploiting enemy vulnerabilities and avoiding resistances by means of weapon selection and mod installation may significantly improve players' damage output.

Since its predecessor Damage 2.0, all different Health, Armor, and Shield types have been simplified into one type for each (e.g. Grineer's Cloned Flesh and Machinery is now just "Health", Ferrite Armor and Alloy Armor is now just "Armor", and Shield and Proto Shield is now just "Shield"). Vulnerabilities and resistances have also been decoupled from health types and are now solely based on the enemy Faction (e.g. all Grineer are now exclusively vulnerable to Impact and Corrosive at all times, regardless of the presence of armor or shields, and no longer have any resistances).

## Overview Table

This section is transcluded from Damage/Overview Table. To change it, please edit the transcluded page.

- As of Update 36.0 (2024-06-18), Vulnerable + = x1.5 and Resistant - = x0.5 incoming damage multiplier.

Damage Type | Tenno | Grineer | Kuva Grineer | Corpus | Corpus Amalgam | Infested | Infested Deimos | Orokin | Sentient | Narmer | The Murmur | Zariman | Scaldra | Techrot | Anarchs | Status Effects
Physical | Impact |  | + | + |  |  |  |  |  |  |  |  |  | + |  | + | Stagger Increase Parazon Mercy threshold
Puncture |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  | Enemy Damage Reduced Amplified Crit Chance
Slash |  |  |  |  |  | + |  |  |  | + |  |  |  |  |  | Bleed (DoT) Ignores Armor
Primary Elemental | Cold |  |  |  |  |  |  |  |  | + |  |  |  |  | - |  | Slow/Freeze Amplified Crit Damage
Electricity |  |  |  |  | + |  |  |  |  |  | + |  |  |  | + | Tesla Chain (DoT) Stun
Heat |  |  | - |  |  | + |  |  |  |  |  |  |  |  |  | Burn (DoT) Panic Reduce Armor
Toxin |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  | Poison (DoT) Ignores Shields
Secondary Elemental | Blast ( Heat + Cold ) |  |  |  |  | - |  | + |  |  |  |  |  |  |  |  | Multiple Explosions
Corrosive ( Electricity + Toxin ) |  | + | + |  |  |  |  |  | - |  |  |  | + |  |  | Reduce Armor
Gas ( Heat + Toxin ) |  |  |  |  |  |  | + |  |  |  |  |  | - | + |  | Gas Cloud (AOE DoT)
Magnetic ( Cold + Electricity ) |  |  |  | + | + |  |  |  |  | - |  |  |  | + |  | Amplified Damage to Shields, Overguard, and Nullifier Bubbles Negates Shield Regeneration
Radiation ( Heat + Electricity ) |  |  |  |  |  |  |  | - | + |  | + |  |  |  | - | Friendly Fire
Viral ( Cold + Toxin ) |  |  |  |  |  |  | - | + |  |  | - |  |  |  |  | Amplified Damage to Health
Special | Void |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  | Bullet Attract
Tau |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Status Vulnerability
True |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Finisher |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

## Damage Display

- Main article: Damage Numbers

Damage dealt from players to enemies is displayed on the HUD as numbers near the point of impact on an enemy. Damage dealt from enemies to players is displayed on the HUD both as a bent strip to indicate its direction of origin and as a reduction in shield or health Hit Points to indicate its quantity.

Each individual projectile or melee attack will display a single damage instance whose value is rounded to the nearest integer. Weapons with multiple projectiles like shotguns or rifles with Multishot will display a damage instance for each individual projectile. Weapons that fire continuously will display a damage instance at a constant rate depending on the fire rate of the weapon.

Damage indicators are color-coded using the following system (default UI colors):

- Damage appears by default in white (◼).
- Ability damage appears by default in purple (◼).
- Critical hits, also called 'Base Critical Hits', and stealth attacks are in yellow (◼).
- Orange crits, also called 'Big Critical Hits', appear in orange (◼). These are stronger than yellow crits.
- Red crits, also called 'Super Critical Hits', as their name suggests, appear in red (◼). These are stronger than orange crits.
- Damage against shields and overshields appears in blue (◼), regardless of other factors such as critical hits.
- Attempts to damage an invulnerable enemy appear in grey (◼).

## Damage Types

Every weapon, ability or method of dealing damage is classified as one or more types of damage. Through mods or abilities, further types of damage can be added to attacks.

When multiple damage types are present on an attack, all of them will deal their respective amounts independent of each other, but only one damage number calculated from the combined value of the damage types will show.

With each shown damage value, there is also a chance of a Status Effect occurring; the likelihood of which type of damage this Status Effect is based on depends on the percent distribution of the damage types on the weapon.

### Physical Damage

Most weapons' base damage is made up of a combination of three physical damage types: Impact, Puncture, and Slash. The overall physical damage of any given weapon is the sum of Impact, Puncture, and Slash damage. This is sometimes referred to as IPS.

Damage Type | Damage Type Internal Name | Status Effect Internal Name | Status Effects
Impact | DT_IMPACT | PT_KNOCKBACK | Knockback Universal: Causes target to flinch and staggers movement for 1 second with higher stacks causing longer stagger duration. For 6 seconds, increases the health threshold for a Parazon finisher by 8% per stack, up to 5 stacks for 80% (100% on Corpus with all their shields removed) of their total health. Each stack has its own duration.
Puncture | DT_PUNCTURE | PT_FRAILTY | Weakened Universal: Reduces damage dealt by the target by 40% and increases received Critical Chance by 5% for 6 seconds. Subsequent Puncture Status effects add +10% weakening, leading to up to 80% reduced damage and 25% critical chance at 5 stacks. Each stack has its own duration.
Slash | DT_SLASH | PT_BLEEDING | Bleed Universal: Deals 35% of the base damage as Cinematic damage per second for 6 seconds after a 1 second delay. Stacks are not limited. Each stack has its own duration.

Although most weapons have varying proportions of Impact, Puncture, and Slash, some weapons (such as the Glaxion or Phage) can have no physical damage at all. Other weapons (like the Plinx or Tysis) can deal a combination of physical and elemental, or combo elemental damage.

Unlike elemental, or combo elemental damage types which can be added via mods, physical damage cannot be added to weapons already lacking them.

Adding a physical damage mod to a weapon (such as Razor Shot or Heavy Trauma) specifies a physical damage type, and only increases damage matching that type. The effect of a mod can be calculated by taking the weapon's base damage, multiplying the percent distribution of the matching damage type, and multiplying again with the mod's value. The more a weapon's damage distribution is concentrated around one physical damage type, the more effective physical mods of that type become.

Take for example, Piercing Hit, which adds 90% Puncture damage:

- Applied to the Reconifex, which deals 40 base damage (60% Puncture), it adds 21.6 Puncture damage.
- Applied to the Supra Vandal, which deals 40 base damage (75% Puncture), it adds 27 Puncture damage.
- Applied to the AX-52, which deals 40 base damage (100% Puncture), it adds 36 Puncture damage, and is at maximum effectiveness.

This is in contrast with elemental mods, which are always applied at 100% value, even if the element is completely new to the weapon. This makes elemental mods the more flexible option for increasing weapon damage.

If a weapon has >75% damage from one physical type, like Desert Wind, then rare mods like Collision Force with 120% physical damage offer greater damage than typical 90% elemental damage mods. However, this edge is lost once Primed versions are factored in, both because Primed elemental and physical mods have the same numerical values, and because more elemental mods have been Primed.

General damage increasing mods such as Serration affect all the damage types of a weapon. Additionally, Faction Damage Mods such as Expel Grineer also affect damage as a total damage multiplier against the faction in question.

### Elemental Damage

Elemental Damage can be applied on top of a weapon's base damage depending on what Elemental Mods are applied. Elemental Damage is applied in addition to a weapon's physical damage types.

Weapon Damage = ( Impact + Puncture + Slash) + (Elemental Damage Types)

Note that a primary elemental damage type that has been combined into a secondary type will no longer be dealt to the weapon's targets, nor its status effect will be applied to the targets either. For example, a weapon dealing Blast damage that is created by combining Cold + Heat will no longer deal Cold damage or cause its Freeze effect, nor Heat damage or its Ignite effect to this weapon's targets.

#### Primary Elemental Damage

There are four primary Elemental Damage types: Heat, Cold, Electricity, and Toxin. A single primary Elemental Damage type can be applied alone, but if a second primary Elemental Damage type is introduced they will combine into a secondary Elemental Damage type.

Damage Type | Damage Type Internal Name | Status Effect Internal Name | Status Effects
Heat | DT_FIRE | PT_IMMOLATION | Ignite On Enemy: Deals 50% of the base damage as Heat damage per second over 6 seconds after a 1 second delay (can be refreshed) while causing the target to panic for 4 seconds and stripping up to 50% Armor over 2 seconds. Stacks are not limited. On Player: Deals 50% base Heat damage over 6 seconds and strips up to 50% Armor over 2 seconds.
Cold | DT_FREEZE | PT_CHILLED | Freeze On Enemy: Reduces Movement Speed, Fire Rate, and Attack Speed by 50%, and increases Critical Multiplier received by +0.1, for 6 seconds. Stacks up to 10 times, with subsequent procs increasing slow by 5% to a total of 90%, and critical multiplier by +0.05 to a total of +0.5. Each stack has its own duration. On the 10th stack, the enemy becomes Frozen for 3 seconds, completely freezing them in place, negating Shield recharge, and increases critical multiplier by +1.0; upon thawing, 3 Cold stacks will remain. On Player: Reduces Movement Speed, Fire Rate, and Attack Speed by 25% for 6 seconds.
Electricity | DT_ELECTRICITY | PT_ELECTROCUTION | Tesla Chain On Enemy: Deals 50% of the base damage as Electricity damage per second over 6 seconds to enemies within 3 meters of the target and stuns the affected target for 3 seconds. Each stack has its own duration. On Player: Deals 50% base Electricity damage to allies within 3 meters of the target.
Toxin | DT_POISON | PT_POISONED | Poison Universal: Deals 50% of the base damage as Toxin damage over 6 seconds after a 1 second delay (bypasses Shield). Stacks are not limited. Each stack has its own duration.

#### Secondary Elemental Damage

Creating these secondary elements requires mixing two primary elements together.

Combined Damage Type | Elemental Damage Types | Damage Type Internal Name | Status Effect Internal Name | Status Effects
Blast | Cold + Heat | DT_EXPLOSION | PT_FLASHBANG | Detonate It causes a miniature explosion inflicting 30% of base damage after 1.5 seconds. If the effect is forced to end early, either by reaching the maximum 10 stacks or when the target dies, all stacks are dealt simultaneously and enemies within 5 meters are dealt 300% of base damage. The radius is unaffected by Firestorm or Fulmination.
Radiation | Electricity + Heat | DT_RADIATION | PT_RAD_TOX | Confusion On Enemy: Attacks any closest enemy with +100% bonus damage to allies and will be attacked in return for 12 seconds. Also applies +100% damage dealt to allied units. Stacks for a maximum of 10 stacks and +550% damage against allied units. Each stack has its own duration. Bosses: Increases damage received from other units. Stacks for a maximum of 4 stacks and +250% damage received. Does not make the Boss attack allied units. On Player: Reduces firing Accuracy, able to damage and be damaged by allies for 4 seconds.
Gas | Heat + Toxin | DT_GAS | PT_ASPHYXIATION | Gas Cloud Universal: Creates a 3 meter radius effect which deals 50% of base damage as Gas damage per second for 6 seconds to targets inside. Stacks for a maximum of 10 stacks and a 6 meter radius. Each stack has its own duration. The effect stays for its duration even if the affected enemy dies.
Magnetic | Cold + Electricity | DT_MAGNETIC | PT_MAGNETIZED | Disrupt On Enemy: Any instance of damage dealt to target's Shields and Overguard will deal +100% additional damage for 6 seconds. Stacks for a maximum of 10 stacks and +325% additional damage. Each stack has its own duration. Enemies under this effect also cannot regenerate shields naturally. When Shields/Overguard break, the target receives Electricity damage and status equal to 3% of the target's maximum Shields/Overguard per Magnetic stack up to 30%. On Player: Amplifies damage dealt to shields by 100%, nullifies shield regeneration, and deals 20 Energy Drain damage per second and scrambles the interface for 4 seconds.
Viral | Cold + Toxin | DT_VIRAL | PT_INFECTED | Virus On Enemy: Any instance of damage dealt to target's Health will deal +100% additional damage for 6 seconds. Stacks for a maximum of 10 stacks and +325% additional damage. Each stack has its own duration. On Player: Amplifies damage dealt to health by 100% for 6 seconds.
Corrosive | Electricity + Toxin | DT_CORROSIVE | PT_CAUSTIC_BURN | Corrosion On Enemy: Reduces current Armor by 26% for 8 seconds. Stacks for a maximum of 10 stacks and 80% reduced armor. Each stack has its own duration. On Player: Reduces armor by 26% for 8 seconds.

#### Modding

Elemental Damage Combinations are made by following a mod placement hierarchy. This hierarchy is from closest to top left (first to be considered) to the bottom right (last to be considered) on the mod layout. Innate weapon elemental damages are considered the very last in any hierarchy, with one exception: some Kuva and Tenet weapons from Kuva Liches or Sisters of Parvos are capable of having two base elemental damages (one from the weapon, one from the Valence damage of the Progenitor Warframe that made the Lich/Sister). In these cases, whichever of the two primary elements comes first in this element order - Heat > Cold > Electricity > Toxin, or "HCET" for short - will be placed second to last in the element combine order, while the other primary element will be placed last in the combine order.

However, a weapon's innate elemental damage can be forced into a different position in the hierarchy (and thus be combined into a secondary element earlier) if the player has equipped a mod of the same element as the innate element. As well, when using multiple mods with the same element, the first position that element is placed in establishes its hierarchy and where it's combined.

For example, putting Stormbringer on the top left slot of an Amprex will change the position of its innate Electricity damage from last in hierarchy to first in hierarchy. Similarly, placing Thermite Rounds earlier in the hierarchy before placing Hellfire will still count the Heat damage where it was first placed.

A weapon's innate elemental damage will contribute to elemental combinations, as long as the combination has been established earlier in the hierarchy. It can also combine with the last uncombined elemental mod in the hierarchy to form a secondary element.

For example: when modding a weapon with Electricity such as the Prova or the Lecta, then adding Cold, Toxin, and Heat in 1, 2 and 3 respectively get: Viral ( Cold + Toxin) and Radiation ( Heat + Electricity).

In the case of Riven Mods where there is more than one elemental stat present, the hierarchy priority will be given to the last elemental stat listed on the Riven mod. For example, a Riven mod with a bonus of +100% Electricity damage first and +90% Toxin damage last, will enable the Toxin damage to combine with an elemental mod higher up in the hierarchy, and the Electricity damage will combine with an elemental damage type lower in the hierarchy. If no other elemental damage mods are present, the elements on the Riven mod will combine with itself.

Weapons with innate secondary elements such as Ogris ( Blast), Penta ( Blast), Stug ( Corrosive), Nukor ( Radiation) and Detron ( Radiation) will always have that damage type, regardless of mods used. On weapons like these, basic elemental damage mods will combine and function independently of the innate secondary elements, as basic elements cannot combine with a weapon's already combined innate damage type. Kuva Weapons and Tenet Weapons will follow this behavior too. For example, a Tenet Detron ( Radiation) can come with an additional Electricity Progenitor damage bonus that will not add onto the innate Radiation damage.

#### Possible Combinations

Except by using weapons with innate secondary elemental damage, or mods which give a secondary element such as Magnetic Might, it is impossible to add more than two elemental damage types on a single weapon. There are only four types of primary elemental damage and every two types of primary elemental damage will be automatically combined into a secondary type. Because of this mechanic, the following combinations of added elemental damage are possible on a single weapon using primary elemental mods (read as Cold is only possible with either Corrosive, Gas or Radiation ):

### Unique Damage

Orokin secrets cannot remain secret forever! Start talking!

The following article or section is conjecture. Conjecture contains unverified gameplay anecdotes or unofficial interpretations of the game's lore. Please do not use this as a primary source of critical information.

It's taking longer than I calculated.

More research on unique damage types needed

These damage types are unique as they are not available as base damage types for any typical weapons nor can they be added through mods.

Damage Type | Damage Type Internal Name | Description | Status Effect Internal Name | Status Effects
Finisher | DT_FINISHER | A damage type that can be applied through finishers and some warframe abilities (notably Ash). Damages Health, Shield, and Overguard, bypasses Armor damage reduction. | N/A | N/A
Void | DT_RADIANT | A damage type that can be used by the Operator after completing The War Within or by players controlling the Warframe Xaku. It deals increased damage to Zariman but is neutral towards all other factions. It also possesses special properties and effects against certain Sentient enemies. | PT_RADIANT | Bullet Attractor: A 2.5 meter radius field will be centered around where target is shot at for 3 seconds, redirecting all bullets and projectiles to its center.
Tau | DT_SENTIENT | A damage type unique to the energy attacks of Sentients, the warframe Caliban and the weapon Haalvu. | N/A | Status Vulnerability: Those inflicted by Tau are 10% more likely to receive a status effect. Tau can stack up to 10 times, capping the status chance multiplier at 100%.
Cinematic | DT_CINEMATIC | A damage type that can be applied through Slash procs. Damages Health, Shield, and Overguard, bypasses Armor damage reduction. | PT_BLEEDING | N/A
Shield Drain | DT_SHIELD_DRAIN | A damage type that can be applied through certain Warframe abilities. | N/A | N/A
True | DT_HEALTH_DRAIN | A damage type that can be applied through certain Warframe abilities and some weapons. Damages Health and Overguard, bypasses Armor damage reduction and Shield. Has no faction modifiers. | N/A | N/A
Energy Drain | DT_ENERGY_DRAIN | Applied by Magnetic procs and Ancient Disruptor's aura. Drains energy equal to the damage dealt. Unaffected by most sources of Damage Reduction. | N/A | N/A
Suicide | DT_SUICIDE | Special damage type applied by typing /suicide, requires admin privileges. | N/A | N/A
Physical | DT_PHYSICAL | Possibly a generic wrapper class for physical damage. | N/A | N/A
Base Elemental | DT_BASE_ELEMENTAL | Possibly a generic wrapper class for primary elemental damage. | N/A | N/A
Compound Elemental | DT_COMPOUND_ELEMENTAL | Possibly a generic wrapper class for secondary elemental damage. | N/A | N/A
Any | DT_ANY | Unknown | N/A | N/A
Invalid | DT_INVALID | Unknown | N/A | N/A

### Empyrean

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

### Conclave-Specific (PvP)

- Main article: Conclave#Damage Mechanics

## Status Effect

- Main article: Status Effect

A Status Effect, also known as a proc, is an additional effect that may be triggered at random by a hit from a weapon, while Status Chance is the probability that a hit will inflict a Status Effect. Each damage type has a unique Status Effect associated with it.

It is a common misconception that status effects determine the damage type dealt to the enemy when in fact a weapon will always (with every shot) deal any elemental and physical damage installed, regardless of the corresponding status triggering or not. In other words, status chance/effects are independent from the actual damage types dealt.

## Damage Over Time

- Main article: Damage over Time

Damage over time, or "DoT," is a type of damage dealt to targets periodically over a duration of time. These instances of damage, or "ticks," typically occur once every second i.e. for Status Damage and some abilities e.g. Spores and Elemental Ward.

This section is transcluded from Damage over Time § DoT Damage Scaling. To change it, please edit the transcluded page.

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

## Enemy Damage Scaling

- Main article: Enemy Level Scaling

The formula enemy damage scales at is as follows:

- Damage Multiplier=1+0.015×(Current Level−Base Level)^(1.55)

## Base Damage

### Increasing Base Damage

- Amalgam Serration
- Blaze
- Heavy Caliber
- Semi-Rifle Cannonade
- Serration
- Spectral Serration
- Point Blank
- Primed Point Blank
- Semi-Shotgun Cannonade
- Vicious Spread
- Arcane Rise
- Arcane Primary Charger
- Arcane Rage
- Primary Bulwark
- Primary Deadhead
- Primary Dexterity
- Primary Merciless
- Primary Plated Round

- Augur Pact
- Eximus Advantage
- Hornet Strike
- Magnum Force
- Semi-Pistol Cannonade
- Arcane Awakening
- Arcane Precision
- Cascadia Flare
- Secondary Deadhead
- Secondary Dexterity
- Secondary Merciless

- Amar's Contempt
- Boreal's Contempt
- Nira's Contempt
- Pressure Point
- Primed Pressure Point
- Sacrificial Pressure
- Spoiled Strike
- Arcane Blade Charger
- Arcane Fury

- Deadly Efficiency
- Primed Deadly Efficiency
- Primed Rubedo-Lined Barrel
- Rubedo-Lined Barrel
- Sabot Rounds

- Cutting Edge

- Financial Stress debuff
- Arcane Arachne
- Theorem Demulcent

### Decreasing Base Damage

- Having equipped an Extinguished Dragon Key reduces damage by 75%.
- Frail Momentum
- Hollow Point
- Being affected by Puncture proc
- Shrapnel Rounds
- Vile Acceleration
- Anemic Agility

## Media

### Visual Effects

## References

## See Also

- Category:User_Research_(Damage)

## Patch History

Update 43.0 (2026-06-17)

Damage Over Time Preview

Damage Over Time (DOT) Status Effects are now reflected by a new “Damage Over Time Preview” indicator on healthbars, showcasing the exact amount of damage they will deal over their duration.

- This new indicator will display the damage that will be dealt across Health, Shields, and/or Overguard.
- Damage Over Time that applies lethal damage will result in a black outline around the health bar.
- This indicator only applies to DOT from Status Effects, not Abilities that deal damage over time.
  - Ex: Damage from Saryn’s Spores will not be reflected in this new indicator, but damage from the Status Effects dealt by Koumei’s Bunraku will.
- Players can change the color of this indicator via the Customize Hud Colors screen in the Accessibility settings.

Update 40.0 (2025-10-15)

- (Undocumented) Damage Quantization changed from 1/16 to 1/32.

Update 37.0 (2024-10-02)

- Damage stat tool tips will no longer show unknown Factions as “???” if the player has yet to encounter them.
  - For example, if you haven’t yet unlocked Albrecht’s Laboratories instead of the Murmur Faction appearing as “???” in the tool tip, it will now just not appear.

Hotfix 36.0.3 (2024-06-20)

- Updated Damage type icons in Status Damage tooltips to their colored version.

Update 36.0 (2024-06-18)

RESISTANCES AND STATUS REWORK

As discussed over the last two months, across both Devstreams 179 and 180, we’ve overhauled Warframe’s Health Types and Resistances alongside a select few Status Effects!

To help players revisit their builds following these changes, an inbox containing 3x Forma will be sent to all players today (June 18th) at 12pm ET today.

New Health Types

Previously, enemy resistances and vulnerabilities were split between 13 Health Types:

Each of these Health Types had unique interactions with the various Status Types:

Optimizing builds to make use of this system required players to memorize health types per enemy (not just per Faction) and their resistances/vulnerabilities. Our goal is to reduce the friction necessary to engage in optimal play, so we’ve:

a) Simplified the number of Health Types

b) Redesigned how Faction Resistances work

c) Increased the visibility of the new vulnerabilities in normal gameplay flow

Instead of having 13 Health Types, we have simplified them into 4:

- Health
- Armor
- Shields
- Overguard

Now, these Health Types only serve to differentiate between Status Effects and Abilities that affect them, such as Magnetic hindering Shields, Corrosive stripping Armor, or Viral amplifying Health damage.

We’ve changed the system so that Resistances and Vulnerabilities are no longer tied to the previous Health Types. Resistances and Vulnerabilities are now based upon the Faction a player is engaging with.

Star Chart “Suggested Damage”

Vulnerabilities are now listed in The Star Chart mission nodes! Here, we aim to recommend the appropriate per-Faction Resistances, which will then universally affect that specific group.

The Star Chart now shows Faction Resistances per node. Aligned with the present Faction, Vulnerabilities and Resistances will be listed to communicate the “Suggested Damage” options best used against any specific Faction or location.

Sub-Factions will also have different Vulnerabilities and Resistances from their primary counterpart. The three main Sub-Factions are:

- Kuva Grineer
- Corpus Amalgam
- Deimos Infested

Viewing Faction Vulnerabilities and Resistances now also depends on where the player is within Warframe’s Story. The Factions (and Sub-Factions) will be unlocked via:

Factions:

- Grineer: Unlocked by default.
- Corpus: Unlocked by default.
- Infested: Unlocked by default.
- Orokin: Unlocked after Phobos Junction.
- Sentient: Unlocked after The Second Dream Quest completion.
- Narmer: Unlocked after The New War Quest completion.
- Zariman: Unlocked after Angels of the Zariman Quest completion.
- Murmur: Unlocked after Whispers in the Walls Quest completion.

Sub-Factions: Kuva Grineer: Unlocked after The War Within Quest completion. Corpus Amalgam: Unlocked after Jupiter Junction. Deimos Infested: Unlocked after Heart of Deimos Quest completion.

Simplified Faction Resistances

With the removal of Resistances/Vulnerabilities being tied to Health Type, they will now be Faction-specific.

Default Faction Vulnerabilities and Resistances:

- Grineer: Vulnerable to Impact and Corrosive
- Corpus: Vulnerable to Puncture and Magnetic
- Infested: Vulnerable to Slash and Heat

Factions by Quest Vulnerabilities and Resistances:

- Orokin:
  - Vulnerable to Puncture and Viral
  - Resistant to Radiation
- Sentient:
  - Vulnerable to Cold and Radiation
  - Resistant to Corrosive
- Narmer:
  - Vulnerable to Slash and Toxin
  - Resistant to Magnetic.
- Zariman: Vulnerable to Void
- The Murmur:
  - Vulnerable to Electric and Radiation
  - Resistant to Viral
    - Rogue Necramechs also fall under these Vulnerabilities and Resistances.

With these Resistance and Vulnerability changes, we’ve made a notable decision to make Impact deadlier towards the Grineer, while making Puncture deadlier towards the Corpus. This is a departure from the previous system, however, we believe that these two Statuses are more suited for these specific Factions.

Since Impact Status Effects enables Mercy actions, we found that it wasn’t all too effective against Corpus due to their lower Health counts compared to their Shields, while Mercy killing Grineer is more accessible due to their innate tankiness. The Corpus can deliver incredibly high amounts of raw damage, allowing for Puncture to naturally play effectively into limiting their damage potential.

General UI Changes & Fixes

- Damage Numbers have received an overhaul to make it easier to see while damaging an enemy. Damage number “flyoffs” (the way the numbers appear and move off of damaged enemies) will now “fly” further based on distance from target, to ensure you can aim to hit the target easily without numbers blocking your view
  - The last “Cloud” iteration of damage numbers (bunched around the reticle) is still available to use if preferred in the Interface Options > Show Damage Numbers.

Hotfix 33.6.1 (2023-07-31)

- Fixed Enhanced Damage Numbers missing their outline.

Missed Notes:

- With the new Ability Damage qualifier with the Enhanced Damage Numbers system, some players may think that certain Warframe abilities have had their Critical Chance nerfed. In truth, some Warframe abilities had a Critical Chance multiplier simply to add “oomph” to their damage numbers, without having an actual impact on Damage output. With this new Enhanced Damage System, that extra oomph is no longer needed, so those non-functional Critical Change values were removed, but the overall damage of these abilities are unchanged.

Update 33.6 (2023-07-27)

Enhanced Damage Numbers

Warframe is a numbers game, whether you’re Modding your Warframe or your Weapons to do as much damage as possible. With that in mind, we have introduced a new Enhanced Damage Number setting with the goal of properly communicating the impact of your attacks and increasing the overall legibility of damage numbers in-game.

This new setting can be found in the Interface: HUD Category of your Settings Menu under “Show Damage Numbers.” You can cycle between the new Enhanced system and the familiar Legacy system or turn off damage numbers altogether!

Overall Damage Number Changes: Whether you are using Legacy or Enhanced Damage Numbers, these new settings will be available with Echoes of Duviri:

Damage Number Scale Custom scaling of your damage number text size, from 50 to 300!

Additionally, Damage numbers will no longer scale with HUD scale setting as they used to. So you can customize the HUD and the numbers separately.

Compact Damage Numbers This Toggle will shorten large numbers for legibility (i.e. 100,357 would be shortened to 100k)

Enhanced Damage Numbers Setting With this new setting toggled on, players can expect to see the following:

Refreshed Damage Number Appearance A punchier presentation of damage numbers, with an updated font treatment to improve legibility. For reference of what this looks like in action, refer to Pablo’s video above.

Prioritized Critical Hits Player damage output varies wildly from damage over time (DOT) from Status Effects to powerful Critical Hits. Previously all types of Damage were treated the same in the Damage Number cycle: meaning, Critical Hit Damage Numbers often disappeared quickly if there were a lot of small DOT procs happening concurrently. From a gameplay side, this had no impact on the actual damage done to your enemies, but it meant the true impact of your Critical Hits was not always communicated to you as clearly as we would like.

Now, your Critical Hits will be prioritized over smaller damage numbers. Those smaller numbers will still appear but now disappear sooner if higher-priority damage is done. Additionally, this prioritization system applies to Critical Hit Tiers as well, meaning Super Critical Hit Damage Numbers will linger longer than regular Critical Hits.

Custom Ability Damage Treatment Since your Abilities traditionally cannot Crit, these attacks tend to have less oomph. Now Ability Damage has its own Damage Color so that it will stand out amongst the rest!

Like all other Damage Numbers, you can customize Ability Damage colors in the “Customize Hud Colors” menu (found in the Interface category of your Accessibility Settings).

Melee Damage Numbers With Legacy settings, Damage Numbers appear at the point of contact, often off-screen or otherwise obstructed by Melee attacks.

With Enhanced settings, Melee Damage numbers will now travel with you to improve visibility and will travel with the attack movement as well. Again, this is best illustrated in Pablo’s video for those who want to see this in action!

Hotfix 32.2.1 (2022-11-30)

- Added a new backer to the new enemy damage resistance icons to improve visibility.

Update 32.2 (2022-11-30) HUD Improvements: The following changes have been made to better communicate an enemy’s state to players via HUD improvements.

- Elemental Damage Resistance Icons (Soft Launch): These new icons help indicate when Elemental Damage resistances are active on enemies. For each active resistance, the corresponding icon will now appear to the right of the enemy’s Health bar.
  - Since this new feature is still in its infancy stages, the following enemies are the only ones that currently use these new icons: Infested Alad V, Hyekka Masters, Hyena Pack, and Sentients.
  - Resistance from armor/health types (e.g. Ferrite Armor) are not included as it would clutter the UI too much.

Update 27.2 (2020-03-05)

Armor and Damage Changes (Enemy):

This section will go over before and after scenarios with our enemy Armor, Health, and Shield changes. Reading this section should give you a conceptual and on-paper understanding of what we’re changing and why, but practical experiences will tell the full story here. You may need to refresh some aspects of your Builds to truly optimize your power against your enemies.

Before: Armor, Shields and Health on an Exponential Curve After: Armor Shields and Health on an S curve

Damage Changes:

Enemy Damage output should still be close to what is currently on the Live version of the game, but we have made a few changes that will affect how players take Damage in-game.

Damage-Type Changes:

- Slash Status now does not bypass Shields and instead deals damage over time to Shields. Slash Status still bypasses Armor.
- Toxin Damage used to apply to Armor with a 25% bonus. Now it is neutral. For role distinction, Toxin bypasses Shields (but not Armor) where as Slash Status bypasses Armor but not Shields.

Player Changes:

Player Shields, Health, and Armor used to be shared with all AI, so they had all the weaknesses and resistances that their AI counterparts did.

Now Players have their own unique Shield, Health, and Armor type classified as TENNO! These have all weaknesses and resistances neutralized (for now). Player Shields now reduce 25% of incoming damage. Player Shields now recharge with custom player-only logic. Shield recharge delays are based on depleted or partial depleted shields. Partially depleted shields (any amount) is a 1 second recharge delay. Full depletion is a 4 second recharge delay.

These changes to Player shields are in addition to coming Shield Gating changes, which you can read about in our Shield Gating section!

Why: Armor Scaling and enemy Damage Reduction was the nucleus for this change. For years Tenno have had the tools to deal with these things, but the tools were uniform: Use Corrosive Projection, or else. While this is a simplification, it removed the feeling of choice. With these changes, we hope players experience a feeling of variety and choice when taking on enemies. By changing the scaling for Armor, we could consistently change the scaling for all!

Stacking Status Effects:

But wait - THERE’S MORE! In addition to being able to achieve two Status Effects on a single shot with >100% Status, we are also adding new meaning if you get a duplicate Status Effect on an enemy overall.

This section will outline exactly what this means for each Status type, including information on how multiple Status Effects behaved with stacking prior to this Hotfix:

- Impact: Repeat single-target Impact Status Effects will escalate the efficacy of the Impact Status (removed previous change of adding Ragdoll as maximum Stagger consequence).
- Puncture: The first Puncture Status Effect has an enemy deal 30% less Damage. Subsequent Puncture Status add +5% weakening, leading to up to 75% (capped). Each Puncture Status has a duration of 6 Seconds.
- Slash: Each Slash Status has its own duration, but now we only show a maximum of 10 damage numbers in the HUD, damage is unaffected, but reducing how many damage events we show helps with performance
- Cold: The first Cold Status Effect deals 25% slow. Subsequent Cold Status Effects deal +5% slow for a total of 70% slow at 10 procs. Each Cold Status has a duration of 6 seconds.
- Heat: No Change.
- Toxin: See Slash, plus the base duration of a Toxin Status Effect now matches Slash for 6 seconds.
- Electricity: AoE Electricity Damage that is part of the Status Effect can now reoccur while the target is still under the stun animation of another Electricity Status Effect.
- Blast: Grants the Blast Status Effect a single target. Blast Status reduces enemy accuracy by 30% base. Subsequent Blast Status Effects add +5% inaccuracy for for 75% total at 10 stacks. Each Blast Status has a 6 second Duration.
- Corrosive: The first Corrosive Status Effect strips 26% Armor. Subsequent Corrosive Status Effects strip 6% more Armor, leading up to 80% Armor removal. Each Corrosive Status Effect lasts 8 seconds.
  - Note: Corrosive was the only Status with infinite Duration and 100% Efficacy toward a defensive stat. This was necessary to some based on how Armor Scaled. We feel our rebalancing efforts need a differently behaving Corrosive to balance out all Status overall.
- Radiation: The first Radiation Status Effect has an enemy deal 100% Damage to allies. Subsequent Radiation Status adds +50% damage, leading to up to 550% (capped). Each Radiation Status Effect has a duration of 12 seconds.
- Magnetic: New Status Effect entirely: enhanced Damage! First Magnetic Status Effect deals 100% additional Shield damage, subsequent Magnetic Status add +25% for a total of 325% (capped). Enemies under a Magnetic Status Effect cannot regenerate Shields. Magnetic Status Duration is now 6 seconds.
- Viral: New Status Effect entirely: enhanced Damage! First Viral Status Effect deals 100% additional Health damage, subsequent Viral Status add +25% for a total of 325% (capped).
  - Note: Before Viral would halve a target’s health pool and simply refresh the duration. Now it deals 2x Damage to Health, and can scale up to 4.5x Damage on repeat Status Effects.
- Gas: The base duration of a Gas Status Effect now matches Slash for 6 seconds. No longer does AoE with forced Poison Status Effect (resulting in Poison DoT for enemies in radius), instead it does AoE DoT Gas damage around the target.

Hotfix 27.0.9 (2020-01-09)

Weapon & Proc Adjustments

The idea of ‘one damage type to rule them all’ is one we want to avoid in Railjack’s early days. We are rebalancing aspects of certain Damage types to ensure there’s balanced choices. The Armor changes in conjunction with this means this is a combined effort of finding the right place for all damage types, not just one leader. Please bear with us as we navigate this particular space - with your help, hopefully everyone will get to put their favourites from their Arsenal to use!

- Decreased the effectiveness of the Particle proc but increased its Duration
  - Reduced to 7.5% damage bonus per hit, still stacks, and lasts 20 seconds. The exponential growth and short duration meant this was far more beneficial to rapid-fire guns than anything else.
- Increased the effectiveness of the Incendiary proc but decreased its Duration
  - Double the damage per tick but half the duration; same total damage but in less time to feel more relevant.
- Fixed Ballistic and Particle damage icons being swapped in-game.

Hotfix 25.7.5 (2019-09-09)

- Updated terminology for Damage Types in Portuguese.

Update 11.2 (2013-12-04)

- Tweaked Radiation Proc to not last as long on players and is more obvious when active.

Update 11.0 (2013-11-20)

Damage 2.0 Introduced

Source: https://forums.warframe.com/topic/132366-information-on-damage-20/

This new damage system introduces a number of new terms. This post will take you through introducing and explaining these terms, then elaborating on what they mean for combat. Keep in mind that things are subject to change, that some terms may be placeholder.

Physical Damage:

- Impact
- Puncture
- Slash

Every weapon in the game is made up of a combination of these three damage types. The overall damage of any given weapon is the sum of Impact, Puncture, and Slash damage. Weapons will exhibit a variety of combinations on the Impact, Puncture, and Slash damage spectrum. Mods will affect damage types as decided by the player by their loadout.

In short, Weapon Damage = (Impact + Puncture + Slash)

Real-life Firearm Metaphor: Impact = Slug; Puncture = Armor Piercing; Slash = Hollow-point. When assigning physical damage aspects to weapons we avoid making them 'pure' (100% in one direction). This ensures you can damage all enemies in the game.

Elemental Damage:

In addition to the 3 base damage types, Elemental Damage can be applied on top of a weapon’s base damage depending on what Elemental Mods are applied. For some rare weapons, elemental damage is all they have.

There are four primary Elemental Damage types:

- Heat
- Cold
- Electric
- Toxin

Elemental Damage can be applied alone but if you combine primary elements they create new combined elemental damage types! This opens up new possibilities, reduces 'rainbow build' problems and reduces some of the confusing effects like 'frozen guy is on fire'.

Combined Elemental Types:

To create these combined elements requires mixing two primary elements together:

- Blast (Fire + Cold)
- Gas (Fire + Toxin)
- Radiation (Fire + Electricity)
- Magnetic (Cold + Electricity)
- Viral (Cold + Toxin)
- Corrosive (Electricity + Toxin)

Elemental Damage is applied in addition to a weapon’s physical damage types.

Weapon Damage = (Impact + Puncture + Slash) + (Elemental).

Elemental Damage Hierarchy & Combining Elementals

Elemental damage combinations are made by following a strict order.

Fire, Cold, Electric, Toxin.

As an example: If you want Fire damage + Magnetic damage (Cold + Electricity), you will need to split it between weapons because when a Fire Mod enters the mod loadout any other elementals will combine with it as it is first in the hierarchy.

Elemental Damage & Combining Elements: CHANGES!

After reviewing this thread and working things out with combinations, we have changes to report to Elemental Combinations. Elemental combinations will no longer be based on a predetermined elemental hierarchy, but instead a MOD PLACEMENT hierarchy.

This hierarchy is from closest to top left (first to be considered) to closest to bottom right (last to be considered) on the Mod Layout.

If you place Cold, Toxin, Fire, and, Electric, in that order from top left to bottom right, you will get:

(Cold + Toxin) and (Electric + Fire).

Status Effects ('Procs')

All damage types have a chance to inflict a status on the target – including you!

Impact: Knockback Puncture: Weakened (reduced damage output) Slash: Bleed (health reduced over time, healing blocked)

Fire: Ignited (fire damage over time) Cold: Slowed Electric: Chain Electricity Damage Toxin: Poison Damage over time to health.

Blast: Stun Gas: Poison in area Radiation: Confusion (difficulties targeting) Magnetic: Shield reduction Viral: Sickened Corrosive: Armor Damage

Enemy Levels

Enemy levels now fall in a more compressed scale. Level 1 enemies are still the easiest, but the difficulty of a Level 40 enemy in Damage 2.0 will be comparable to a Level 100 enemy in Damage 1.0. Infinite mission types will still feature ever increasing enemy levels. Enemies will be wielding weapons that can inflict different types of damage and Procs on the Tenno, meaning the difficulty will come from a combination of their loadouts and their level.

Know your enemy.

Enemies will react to damage types differently. Begin hunting your enemies to discover the best way to approach different faction and enemies. With your Primary, Secondary, and Melee weapon, you will be able to take on the fiercest foes with many different combinations.

Significance of Change

Damage 2.0 is a very significant change to Warframe. We are standing by to receive feedback and experiences on this new Damage system when it is released.

Thank you for reading, everyone!
