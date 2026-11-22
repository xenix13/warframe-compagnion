# Damage Reduction (wiki)
Source : https://wiki.warframe.com/w/Damage_Reduction

It's taking longer than I calculated.

Unclear if new or old Damage Attenuation stats, unclear how long it lasts. The whole page needs a check and rewrite.

Very well. Keep your secrets.

This article/section contains unofficial information, concepts, or terminology derived from or based on community discussion, invention, or knowledge. It may be subjective and contain information or terminology that is not used by Digital Extremes or in official WARFRAME communications, and may not be an officially recognized concept.

When a player or enemy deals damage to their targets' health or shields, that damage may be mitigated by sources of damage reduction (also called damage resistance relative to receiving damage). In other words, players may deal less damage than the listed Arsenal value due to armor; damage type modifiers from different health, armor, and shield classes; and/or other sources of damage reduction.

Note that in-game and on the wiki, sometimes Abilities and Mod descriptions mention damage reduction when they really mean negative damage type modifier and vice versa. This distinction is needed to differentiate between multiplicative and additive stacking of different forms of damage reduction.

## How Damage Reduction Affects Damage

- Main article: Damage/Calculation

### Basic

When a player is dealt damage, it is reduced by a scalar calculated from the amount of damage reduction (DR) active (from Mods, Warframe abilities, etc.). The general calculation takes a form of:

- { Damage Received =Damage Dealt×(1−DR_1)×(1−DR_2)×⋯ ; =Damage Dealt×Total Damage Multiplier }

For example, if a Grineer Lancer normally deals 100 IPS damage (50 Impact, 25 Puncture, and 25 Slash) against a player, and that damage is dealt to the player's shields, which have an innate 50% DR, the amount of damage the player receives will be:

- ( 50 + 25 + 25) × (1 - 50%) = 50

### With Armor

In the case of armored targets (players and enemies), the modified damage dealt is calculated as:

- { Damage Received =Damage Dealt×(1−DR_1)×(1−DR_2)×⋯×(300)/(300+Armor) ; =Damage Dealt×Total Damage Multiplier from Pure Damage Reduction×Total Damage Multiplier from Armor }

To calculate the damage reduction percentage from any amount of armor (for informative purposes), use the following: (Armor)/(Armor+300)×100

For example, if 100 pure Impact damage is dealt to a player with 500 armor, the amount of damage they receive will be:

- 100 × 300/(300 + 500) = 37.5

### With Damage Type Modifiers and Physical/Elemental Damage

Damage Type Modifiers (DM, not to be confused with damage reduction, DR) play a role in damage calculations. Although the Tenno are neutral to all damage types as of Update 27.2 (2020-03-05), mods such as Toxin Resistance or ability effects like Kinetic Plating add damage modifiers to a player's health and shields against either one type of damage:

- Toxin for Toxin Resistance
- or multiple (Impact, Puncture, Slash, Heat, Cold, and Blast for Kinetic Plating.

The generalized formula from above can be modified to account for these as such:

- { Damage Type Received =Damage Type Dealt×(1−DR_1)×(1−DR_2)×⋯×(300)/(300+Armor)×(1+DM_1)×(1+DM_2)×⋯ ; =Damage Type Dealt×Total Damage Multiplier from Pure Damage Reduction×Total Damage Multiplier from Armor×Total Damage Multiplier from Damage Type Modifiers }

For example, if 50 Impact, 25 Puncture, and 25 Slash damage is dealt to Corpus health, with 100 armor, and Guardian Eximus aura active (90% DR), the amount of damage the enemy receives will be:

- 50 × (1 - 90%) × (1 - 100/(100 + 300)) × (1 + 0%) = 3.75
- 25 × (1 - 90%) × (1 - 100/(100 + 300)) × (1 + 50%) = 2.8125
- 25 × (1 - 90%) × (1 - 100/(100 + 300)) × (1 + 0%) = 1.875

### Against Non-Health/Shield Types

Damage Reduction has no affect on effects that absorb damage, Overguard, or Object health such as:

- Frost's Snow Globe and Icy Avalanche
- Nezha's Warding Halo (during 3-second invulnerability period; DR to health after 3-second period works normally)
- Rhino's Iron Skin
- Saryn's Molt

Some of these may benefit from increased Armor (e.g. damage absorption scales with Armor values), but Damage Reduction will not be applied to these to reduce incoming damage received.

## Types of Damage Reduction

Type | Applies to | Stacking behavior & source
Armor | Health only | Damage Reduction=(Net Armor)/(Net Armor+300) DR from armor is multiplicative with other types Armor bonuses stack additively (e.g. Steel Fiber and Gladiator Aegis)
Pure Damage Reduction | Shields and Health | DR is multiplicative with all forms of damage reduction Typically obtained from using Warframe abilities
Damage Redirection | Overguard, Shields, and Health | DR is multiplicative with all forms of damage reduction Typically obtained from using Warframe abilities
Damage Type Modifier | Where Applicable* | DR from damage type modifier is multiplicative within the same type DR is multiplicative with other types
Energy as Health | Energy at 2 Health | Damage Reduction=1−(100)/(Net Efficiency) DR is multiplicative with other types From equipping Quick Thinking and/or Gladiator Finesse, efficiency bonuses stack additively
Damage Attenuation | Enemy Health | Damage reduction adapts to player DPS DR is multiplicative with other types

*Modifiers granted by mods or effects (e.g. Toxin Resistance) are applied to both health and shields, while modifiers that are innate to a shield or health type only apply to the damage dealt to shields or health. E.g. Slash damage dealt to the neutral shields of an enemy that has a +25% modifier to slash on its health will not take increased damage to its shields. The exception to this are damage modifiers on armor, which do apply to health as well, but not to shields.

## Armor

- Main article: Armor

Armor is an attribute that reduces damage taken to health but not to shields or overguard. Not all enemies possess armor; Warframes, some Murmur, most bosses, and all Grineer do, but normal Corpus and Infested enemies do not have any. For a given Warframe, its armor value can be found in the Arsenal. Armored enemies have their base armor values listed in the Codex but this value increases when they spawn with higher levels due to Enemy Level Scaling.

In combat, enemies with more than one point of armor have their health bars displayed yellow instead of red. It is possible to strip away armor value through certain abilities or damage Status Effects, turning those enemies' health bars back to red.

## Pure Damage Reduction

Any source of damage reduction, aside from armor, will decrease damage done to health and shields. Sources of damage reduction (including armor) stack multiplicatively with each other.

This form of damage reduction is usually temporary or conditional, unlike armor, so it must be reapplied to receive less damage to health and shields.

### Sources of Pure Damage Reduction

Abilities

Baruuk's tolerance for violence wanes as his hand is forced by his foes. Restraint is a resource unique to Baruuk that provides up to 50% Damage Reduction when the meter is completely depleted.

- Restraint meter is displayed in the lower-right on the HUD, above the ability icons.
- Restraint meter starts fully filled, and is depleted using Baruuk's abilities:
  - Each attack evaded through Elude erodes 1.2% from the meter.
  - Each enemy affected by Lull erodes 0.8% from the meter.
  - Each enemy disarmed by Desolate Hands erodes 1.6% from the meter.
- Baruuk's fourth ability Serene Storm utilizes Restraint instead of Energy to cast and maintain. Using this ability refills Restraint meter by 4% on activation and by 0.8% per second until the ability is deactivated.
  - Restraint can still erode from using Baruuk's other abilities during this ability.

 | 3 75 | Desolate Hands Summon a bevy of orbiting daggers to seek out enemy guns, destroying them with a small explosion. Combine with Elude to double the range. Introduced in Update 24.2 (2018-12-18) | Strength:100 / 150 / 200 / 250 ( Blast damage) 3 / 4 / 6 / 8 (number of charges)
Duration:N/A
Range:6 m (seek range) 3 m (explosion radius)
Misc: 1.6% (Restraint erosion per enemy disarmed) 10% (damage reduction per dagger) 90% (damage reduction cap) 50% (dagger cap per ally)

Info

- Baruuk expends 75 energy to summon a protective ring of 3 / 4 / 6 / 8 levitating energy daggers around him that passively provide him with 10% Damage Reduction per dagger orbiting in the ring. The daggers will seek enemies in sight and within 6 meters, launching one by one every 1 second to Disarm their targets on impact, then explode dealing 100 / 150 / 200 / 250 Blast damage to all enemies within a 3 meter radius.
  - Arsenal lists the damage reduction with maximum daggers.
    - Damage reduction can not exceed 90% under any circumstance, capping out at 9 daggers.
  - Enemies that have already been disarmed will not be targeted by the daggers.
- While active, Desolate Hands shares its effects with allies by launching 1 dagger per second to the nearest ally within Baruuk's dagger seek range and in direct line of sight. Shared daggers also provide damage reduction, disarm charges, and erodes Baruuk's Restraint on enemy disarm for the affected allies; each ally can carry up to 50% of the modded number of daggers.
  - Affected allies includes all Warframes, Companions, Eidolon Lures, summoned allied units such as Specters, allied Invasion units, Hostages, Kavor Defectors, Sortie and Arbitrations Defense Operatives, and Defense Objects.
    - On Defense Objects, the damage reduction is capped at 50%, but the object may still carry more than 5 daggers.
  - Baruuk does not lose his own dagger charges when shared with allies, instead his allies receive new daggers.
  - Once the maximum number of shared daggers is reached on an ally, Baruuk's Desolate Hands will not share new daggers with that ally.
  - Both sharing a dagger and launching one at an enemy share same one second interval and cannot happen at the same time.
  - Only Baruuk's own Desolate Hands will share new daggers to allies.
- Can be recast while active to restore the number of daggers to full.
  - New instance of Desolate Hands will cause daggers to retarget previously disarmed enemies and allies with shared daggers if within range.
- Casting Desolate Hands is a full-body animation that stops Baruuk's grounded movement and other actions.

Kit Interactions

- Baruuk's Passive erodes by 1.6% per enemy disarmed by his own daggers and shared daggers on allies.
- While Elude is active, the daggers' seeking range is doubled.
- Damage dealt by Desolate Hands' dagger explosion will not awaken sleeping enemies under Lull's influence.

Tips & Tricks

- Low range values can help prevent the daggers from seeking out enemies, making it easier to keep them for damage reduction.

Maximization

Elude active?

Desolate Hands

 | 4 | Serene Storm With his Restraint eroded, Baruuk commands the Desert Wind to deliver powerful radial strikes with his fists and feet. Each moment commanding the storm restores his Restraint. Introduced in Update 24.2 (2018-12-18) | Strength:100 / 125 / 200 / 250 ( Impact damage) 10% / 15% / 20% / 25% (damage reduction)
Duration:N/A
Range:N/A
Misc: 40% (damage reduction cap) ? % (disarm chance on hit) 100 % (wind wave projectile deflection)

Info

- Baruuk foregoes his restraints to empower his fists with volatile energies, commanding the Desert Wind and wielding it as his melee Exalted Weapon. While Serene Storm is active, Baruuk also receives 10% / 15% / 20% / 25% Damage Reduction against enemy attacks, and slows enemies within a 3 meter radius by 50%.
  - Exclusively uses the Serene Storm Stance.
  - Damage reduction is capped at 40%.
  - Damage reduction only applies when Desert Wind is the active weapon.
  - Slow amount and radius are not affected by mods.
- Rather than using energy, Baruuk regenerates his Restraint, recovering 4% Restraint on activation and then restores 0.80% Restraint per second.
  - Baruuk can still erode his Restraint while Serene Storm is active by using his other abilities.
  - Baruuk does not need to have completely eroded his Restraint meter to use Serene Storm. He is free to activate it as long as he has 96% Restraint, and can deactivate it at any time to stop restoring his Restraint if he wishes.

- Normal attacks deal 100 / 125 / 200 / 250 damage within 1.2 meters.
  - Damage is purely Impact.
  - Wall attacks and slide attacks inflict 300 / 375 / 600 / 750 damage for each strike.
  - Aerial attacks inflict 200 / 250 / 400 / 500 damage.
  - Slam attacks inflict 250 damage within 8 meters.
  - Attacks and wind waves have a 35% critical chance, 2.0x critical multiplier, and 15% status chance.
  - Desert Wind can be equipped with melee mods and Arcane Enhancements.
    - Riven Mods are not generated for Desert Wind.
  - Because Serene Storm is counted as a melee strike, it is affected by mods and Warframe Arcanes such as Steel Charge and Arcane Fury.
  - Radial damage from slam attacks diminishes with distance, does not have a critical chance, is not affected by the Melee Combo Counter, and will cause enemies within range to suffer a knockdown.
  - Ground finishers inflict 1600% of the total modified damage from normal attacks. Prompted finishers inflict 6400% of the total modified damage from normal attacks as True Damage.
    - The damage composition of a ground finisher is the same as a modified normal attack; however, Impact damage from ground finishers is multiplied by 125%.
    - The finisher multipliers for both attacks are affected by Finishing Touch.
  - Each attack adds to the Melee Combo Counter; however, radial damage from slam attacks does not.

- Normal attacks will emit a wind wave in the direction of aim that travel 20 meters. Wind waves have the same base damage as the melee attacks that release them.
  - The wind waves and Serene Storm itself are considered separate entities and will both deal damage separately.
  - Wind waves will Punch Through and hit enemies and terrain up to their maximum range, but requires enemies to be in Line of Sight to deal damage.
  - Wave damage does not fall off with distance.
  - Wave range and flight speed are not affected by mods.
  - Wave hits can increase Melee Combo Counter and trigger Tennokai.
  - Enemies hit by the waves will suffer a stagger.
  - Enemy projectiles hit by the waves have a 100% chance to be redirected toward their originating direction.
- Serene Storm comes installed with its own unique stance. Additional combos will be unlocked as Serene Storm increases in rank.
  - Forward melee combo thrusts Baruuk's fists toward his enemies to generate a powerful push that inflicts damage, stagger, and ragdoll effects.
  - Hold melee combo creates an upward draft that drifts forward and gradually lifts enemies high into the air.
  - Block melee combo creates a suctioning pull to drag enemies toward Baruuk.
  - Slide melee combo bends gravity around Baruuk to radially lift all nearby enemies into the air.
  - Slam melee combo creates a radial blast that knocks back all enemies in range.
  - Slam melee combo while blocking creates a radial vortex that pulls in all enemies in range.
- Any hits made directly by the impact of Baruuk's fist or the waves of energy caused by Desert Wind, will permanently Disarm the enemy only if applying any of the following status effects:
  - Knockdown
  - Lifted
  - Ragdoll
  - Stagger

Weapon

- Main article: Desert Wind

Baruuk

Baruuk Prime

Serene Storm

Serene Storm

- This weapon deals pure Impact damage.
  - Reactive Storm augment changes the damage from Impact to adapt to the enemy's damage-type weaknesses.
- Innate two and one polarities.

Advantages:

- Very high critical chance.
- Good base status chance.
  - Can reach over 100% status chance with Reactive Storm.
- Attacks release waves that travel 20 meters with unlimited punch through.
  - Enemies must be within Line of Sight for the wave to deal damage.
  - Waves can increase Melee Combo Counter and trigger Tennokai.
- Melee and wave damage can be increased by the combo counter.
- Waves can Ragdoll enemies and reflect projectiles.
- Fist attacks will Disarm enemies, unless the enemy has Overguard or is resistant to Disarm (i.e. Acolytes, Gokstad Officer, Bursa, Ambulas).

Disadvantages:

- Requires Restraint to activate and keep active.

Stance

- Main article: Serene Storm (Stance)

Serene Storm is a unique Stance exclusive to Desert Wind that can only be acquired and used by activating Baruuk's fourth ability, Serene Storm. This Stance overrides the Stance on any currently equipped melee weapon for as long as Serene Storm remains active.

## Combos

Combo/Attack | Name | Attack Multipliers and Forced Procs | Avg Dmg Multi/s | Length @ 1.0 Attack Speed | Animation
Neutral (While Not Moving) | Trespass Denied | 100% 100% | 2x 100% 100% | 2x 100% 100% | 100% 100% | 285.7%/s | 3.5s | 
Forward (While Moving) | Father's Lesson | 100% 100% | 100% 100% | 100% 100% |  | 240.0%/s | 2.5s | 
Forward Block (While Blocking & Moving) | Final Sunrise | 2x 100% 100% | 2x 100% 100% | 2x 100% 100% |  | 285.7%/s | 3.1s | 
Block (While Blocking) | Patience Shattered | 3x 100% 100% | 100% 100% | 4x 100% 100% | 100% 100% | 317.1%/s | 4.1s | 
Heavy (Heavy Attack) | Rise From Ashes | * 500% 400% | 4x 300% 300% |  |  | N/A | N/A | 
Slide (While Sliding) | Rolling Blast | 5x 300% 300% 300% |  |  |  | N/A | N/A | 
Aerial (While In Air) | One Point | 200% | 2x 200% | 300% |  | N/A | N/A | 
Wall (While Wall Latching) | Through Strike | 300% |  |  |  | N/A | N/A | 
Finisher (On Knocked Down Enemy) | Roaring Drums | 6x 500% |  |  |  | N/A | N/A | 
Slam (Looking At Ground While In Air) | Slam Attack | 200% |  |  |  | N/A | N/A | 
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

Augment

- Main article: Reactive Storm

Reactive Storm is a Warframe Augment Mod for Baruuk's Serene Storm to increase Desert Wind's status chance and alters its damage type to match enemy weaknesses.

Rank | Status Chance | Cost
0 | 100% | 6
1 | 150% | 7
2 | 200% | 8
3 | 250% | 9

Maximization

Melee damage modifier:
Elemental damage modifier:
Faction damage modifier:
Reactive Storm?

Serene Storm

 | 2 50 | Preserving Shell Citrine guards herself and nearby allies with a crystalline shell that gradually decays. Kills and assists increase the defensive power of the shell. Introduced in Update 32.3 (2023-02-15) | Strength:10 / 20 / 30 / 40 % initial damage reduction +3% damage reduction per kill +1% damage reduction per assist
Duration:18 / 20 / 22 / 25 s
Range:N/A
Misc: 50 m Affinity Range 8 m Stagger radius 2 m Knockback distance 1 s initial decay delay 10 / 20 / 25 / 25 % minimum damage reduction -1%/s decay rate at 25%-75% -3%/s decay rate at 75%-90% 2 s kill/assist decay delay 90% max damage reduction

Info

- Citrine expends 50 Energy to align a protective pentagonal array of five orbitting crystals that reduces incoming enemy damage, surrounding herself, all allied Warframes within her Affinity Range, and Companions with personal arrays. On cast, Citrine also inflicts Stagger on enemies within a radius of 8 meters and Knockback by 2 meters.
  - Allies gain or lose Preserving Shell whenever they enter or leave Citrine's Affinity Range.
    - Affinity Range is not affected by Ability Range but is affected by Fosfor and Vazarin's Mending Unity.
- Preserving Shell lasts for 18 / 20 / 22 / 25 seconds, during which Damage Reduction begins at 10% / 20% / 30% / 40%, then after a 1 second delay it continuously decays per second until pausing at 10% / 20% / 25% / 25% minimum damage reduction and resuming decay when above the threshold. Decay rate changes when total damage reduction reaches its thresholds, alternating from -1% per second when between 25% to 75% damage reduction, to -3% per second when between 75% to 90% damage reduction.
  - Modded initial damage reduction percentage is rounded down to the nearest whole number.
  - While active, the lower half of the diamond-shaped UI indicator above the ability icons appears, tracking the current damage reduction value and this ability's remaining duration via a countdown curve.
  - Damage reduction value is displayed in real-time as a buff icon beside Citrine and her squadmates' hitpoints indicators.
  - Multiple Citrines in the squad can stack Preserving Shell's damage reduction multiplicatively.
- While active, kills and assists made by Citrine will pause the decay for 2 seconds and increase total damage reduction by 3% per kill and 1% per assist. Damage reduction is capped at a maximum value of 90%, whether earned via kills and assists, or modded with at least 225% Ability Strength at ability rank 3.
  - Modded damage reduction per kill percentage in decimals is rounded down to the nearest whole number, whereas per assist is rounded up.
- Can be recast while active to preserve the current damage reduction value if above the minimum threshold, or return to initial damage reduction if the current value is lower, while also refreshing to full duration.
- Casting Preserving Shell is a full-body animation that displaces Citrine into the air and allows slowed directional movement, but interrupts other actions.

Kit Interactions

- Damage, status effects, and crowd control inflicted by Fractured Blast, Prismatic Gem, and Crystallize can contribute as kills and assists to increase Preserving Shell's damage reduction.

Maximization

Preserving Shell

 | 2 50 +when at max heat: +1t/s-2 t = time at max heat in seconds | Immolation Protect Ember with flame armor that burns stronger over time, consuming energy once its meter is at full strength. Cast again to extinguish the flame. Introduced in Update 26.0 (2019-10-31) | Strength:10-50 / 20-65 / 30-75 / 40-85 % (damage reduction)
Duration:N/A
Range:N/A
Misc: 50-90% (damage reduction cap) 0.5%/s (minimum heat generation) +1%/s ( Fireball heat rate per cast) -2%/s ( Fire Blast heat rate per cast) -50% ( Fire Blast heat per cast) +3%/s ( Inferno heat rate per cast)

Info

- Ember expends 50 Energy to surround herself in a swirling torrent of protective flame that burns stronger with each moment. While immolated, a thermometer appears above the ability icons, gradually rising in temperature. Ember gains 10% / 20% / 30% / 40% Damage Reduction on cast displayed as a percent (%) next to the thermometer, which scales up to 50% / 65% / 75% / 85% damage reduction at maximum heat. Press the ability key (default 2 ) again to deactivate this ability, expending all stored heat instantly.
  - Damage reduction is capped 50% - 90%, achievable with 125% Ability Strength. 0.75 × Min(0.90,0.85 × (1 + 0.3)) + (1 - 0.75) × Min(0.50,0.40 × (1 + 0.3)) = 0.75 × Min(0.90,1.105) + (0.25) × Min(0.50,0.52) = 0.75 × 0.9 + (0.25) × 0.5 = 0.8 (80% damage reduction)
    - Damage reduction (DR) is related to the current percent heat (H) by the following formula: DR = H × Min(0.90,0.85 × (1 + Ability Strength)) + (1 - H) × Min(0.50,0.40 × (1 + Ability Strength))
    - E.g., with a max rank Intensify and 75% heat Ember's damage reduction would be:
  - Once Immolation reaches maximum heat, Ember drains energy at an increasing rate of 0.4 energy per second to sustain Immolation. The energy drain growth is uncapped.
    - Example: After 10 seconds at max heat, Immolation will drain 4 energy per second: After 30 seconds at max heat, Immolation will drain 12 energy per second.
    - While at maximum heat Ember cannot replenish energy using Energy Vampire, Rally Point, Rift Plane's innate energy regeneration, Squad Energy Restores, Energy Siphon, Energy Nexus, Dreamer's Bond and/or Wellspring.
    - Energy Orbs, Orokin Void Death Orb's energy restores, Rage, Hunter Adrenaline, Spellbound Harvest, Arcane Energize, and Emergence Dissipate's Energy Motes can still replenish Ember's energy at max heat.
    - Immolation is treated as a channeled ability by Incarnon Genesis perks only while at maximum heat.

Kit Interactions

- Immolation's heat generation is affected by Ember's abilities. The following values refer to how full the heat bar is, i.e. 0% means the bar is empty and 100% means it is full; these values are not referring to the damage reduction displayed to the left of the bar.
  - The bar passively fills at a rate of 0.5% per second.
  - Each cast of Fireball increases the rate of heat generation by 1% per second.
  - Each cast of Fire Blast decreases the rate of heat generation by 2% per second, while also removing 50% heat.
  - Each cast of Inferno increases the rate of heat generation by 3% per second.
  - E.g. after casting Fireball three times, Fire Blast once, and Inferno once, Ember would be gaining 0.5% + (1% × 3) - 2% + 3% = 4.5% heat per second, and the heat bar would take 22.2 seconds to completely fill.
- Fireball:
  - Immolation adds up to 4x (based on Heat level) to Fireball's combo multiplier.
    - At max Heat, this increases Fireball's minimum damage from 800 to 2400 on direct hit and 300 to 900 on AOE.
    - At max Heat and 3+ consecutive casts, this increases Fireball's maximum damage from 3600 to 5200 on direct hit and 1350 to 1950 on AOE.
- Fire Blast:
  - Enemy armor reduction scales linearly with Immolation's heat level, with 0 percent heat resulting in the minimum value being removed and 100 percent heat resulting in the maximum.
  - Energy cost decreases with Immolation's heat down to 25 energy cost at maximum heat.
- Inferno:
  - Rings of Fire from Inferno gain up to 100% bonus damage, scaling linearly with Immolation's heat level at the time of cast.
    - Initial hit damage of the meteor is unaffected.

Augment

- Main article: Immolated Radiance

Immolated Radiance is a Warframe Augment Mod for Ember that allows Immolation to affect friendly players within affinity range, reducing incoming damage.

Rank | Shared Damage Reduction | Cost
0 | 20% | 6
1 | 30% | 7
2 | 40% | 8
3 | 50% | 9

Tips & Tricks

- When at max heat quickly cast Fire Blast in order to negate the energy drain for being at full heat.
- In order to quickly build up Ember's heat (and the damage reduction that comes along with it) cast Inferno while there are no enemies in rage, increasing heat generation for zero energy cost.
- Only 105.8% Strength is needed to reach 90% damage reduction. This is nearly met by having a single enemy affected by a Heat proc within Immolation's range, providing +5% Strength.

Maximization

Immolation level:
Seconds spent at maximum Immolation:
Immolated Radiance?

Immolation

 | 3 10 +0.5/s/enemy +3/ability | Pacify & Provoke In Night-Form, reduces damage inflicted by nearby enemies. In Day-Form, increases Ability Strength of nearby allies. Introduced in Update 17.0 (2015-07-31) | Strength: 20% / 33% / 43% / 50% (damage reduction) Duration: N/A Range: 10 / 12 / 14 / 16 m Strength: 5% / 10% / 15% / 20% (Ability Strength bonus) Duration: N/A Range: 10 / 12 / 14 / 16 m
Strength: 20% / 33% / 43% / 50% (damage reduction)
Duration: N/A
Range: 10 / 12 / 14 / 16 m
Strength: 5% / 10% / 15% / 20% (Ability Strength bonus)
Duration: N/A
Range: 10 / 12 / 14 / 16 m

Info

- Equinox emits a crippling or empowering aura with a radius of 10 / 12 / 14 / 16 meters. Pacify & Provoke will remain active indefinitely until deactivated by casting Metamorphosis, by running out of Energy, or by pressing the ability key again (default 3 ).
  - Despite being a channeled ability, this does not interrupt energy regeneration from Energy Siphon, Energy Nexus, Dreamer's Bond, Wellspring and is not affected by Ability Duration.
  - Neither Pacify nor Provoke can activate channeling-based Incarnon Genesis perk bonuses.
  - Aura radius is visibly determined by wave-like strings of energy orbiting Equinox.
  - Equinox utilizes different versions of the ability depending on her current form:

- Night Equinox emits a crippling aura that reduces enemy damage by 20% / 33% / 43% / 50% the closer they are to Equinox.
  - Does not affect enemies with Overguard, and Anarch Gladius (bug).
  - Does protect allied Overguard, because this ability reduces damage output of enemies instead of reducing damage taken by allies.
    - Also protects any imaginable Defense Objects, allied players, allied NPCs, Operators, etc.
  - While Pacify is active, 1.5 / 1.25 / 1 / 0.5 Energy is drained per second for each enemy within the aura.
    - The number of enemies that can affect the energy cost is not capped, unlike Gloom.
  - Damage reduction falls-off with distance. The aura is divided into 4 subsequent "rings", each with 1/4 of the total radius of the ability:
    1. The first (inner) ring grants 100% of the listed damage reduction,
    2. The second ring grants 83.33%,
    3. The third ring grants 66.67%,
    4. The fourth (outer) ring grants 50%.
  - The maximum value of damage reduction is calculated with the following formula: Modified Damage Reduction = 1 − [Base Damage Reduction ÷ Ability Strength].
    - For example: With a rank 3 Pacify, and with a maxed Intensify, Equinox reduces enemy damage by 1 − [0.5 ÷ (1 + 0.3)] = 61.5385%.
      1. The first (inner) ring will reduce enemy damage by 61.5385% × 100% = 61.5385%,
      2. The second ring by 61.5385% × 83.33% = 51.28%,
      3. The third ring by 61.5385% × 66.67% = 41.0277%,
      4. The fourth (outer) ring by 61.5385% × 50% = 30.7693%.
- Enemies in range are highlighted in Equinox's energy color. Color intensity scales with distance from Equinox, with the nearest enemies glowing the brightest.

- Day Equinox emits an empowering aura that grants Equinox and all ally Warframes within range an additional 5% / 10% / 15% / 20% Ability Strength.
  - While Provoke is active, 5 / 4.33 / 3.66 / 3 Energy is drained for each Warframe ability cast within the aura.
  - Unlike Pacify, the Ability Strength bonus does not fall-off with distance.
  - Ability Strength bonus cannot exceed 50%, unless Peaceful Provocation is equipped. Different instances of Provoke auras do not stack, only the strongest bonus will be applied.
  - Provoke, after being affected by equipped Ability Strength Mods, stacks additively with Ability Strength bonuses when applied to other abilities.
    - For example: with a maxed Intensify, Equinox's abilities will gain 0.3 + 0.2 × 1.3 = 56% Ability Strength when cast while a rank 3 Provoke is active.
  - In order to acquire the Ability Strength bonus from Provoke, allies only have to cast their abilities while inside the aura.
  - The additional energy cost is only applied when abilities are activated within the aura, including Equinox's abilities. The energy cost is not applied for energy drains.

- Ability Synergy:
  - Ability Strength bonus fom Provoke applies to all her other abilities.
  - Metamorphosis can switch between Pacify and Provoke.
    - If that ability was removed, Pacify or Provoke is chosen based on emissive color of the warframe.

Augment

- Main article: Peaceful Provocation

Peaceful Provocation is a Warframe Augment Mod for Equinox that increases the effectiveness of Pacify & Provoke. Pacify converts damage done to Equinox and her allies into an aura that slows enemies by up to 40%. Provoke converts damage done to enemies within the aura into up to 15% bonus Ability Strength.

Rank | Pacify Slow Effect | Provoke Ability Strength | Cost
0 | 20% | +6% | 6
1 | 30% | +9% | 7
2 | 35% | +12% | 8
3 | 40% | +15% | 9

Tips & Tricks

- Provoke will reach a maximum bonus of 50%Ability Strength at 250%Ability Strength.
- Pacify will reach 95% damage reduction at 800%Ability Strength. (did not test higher)
  - 500%Ability Strength is achievable solo, for 90% damage reduction.
- Use Arcane Circumvent, Secondary Fortifier, or Magnetic damage to quickly remove enemy Overguard and apply Pacify's debuff.
  - At the same time Pacify will reduce damage dealt to stolen Overguard.

Maximization

Peaceful Provocation?

Pacify & Provoke

Bugs

- Does not affect Anarch Gladius.

 | 3 50 | Self Portrait Draw an ink effigy to absorb the damage dealt to Follie and allies. Below, a pool of ink spreads Inkblot. Kill enemies inside the pool to grow Follie's effigy and its ink puddle. Introduced in Update 42.0 (2026-03-25) | Strength:250 / 350 / 450 / 550 ( Corrosive damage) 35% / 40% / 45% / 50% (maximum damage reduction)
Duration:20 / 24 / 26 / 30 s 40 / 48 / 52 / 60 s (maximum duration) 3 s (bonus duration per kill)
Range:6 - 15m / 7 - 17.5m / 7 - 17.5m / 8 - 20m (Radius)
Misc: 10% (starting damage reduction) 90% (maximum damage reduction cap) 50 m (maximum spawn range)
Subsumable to Helminth

Info

- Follie expends 50 Energy to congeal an inky effigy of herself, centered around the location on the aiming reticle up to 50 meters away. The ink effigy lasts 20 / 24 / 26 / 30 seconds, sustaining an ink pool with a starting radius of 6 / 7 / 7 / 8 meters; each enemy killed inside the ink pool increases its duration and range, up to a maximum of 40 / 48 / 52 / 60 seconds and 15 / 17.5 / 17.5 / 20 meters. On cast and on ability expiration, the effigy deals 250 / 350 / 450 / 550 Corrosive damage to enemies within its starting radius and applies Inkblot to them, then continuously applies Inkblot to all enemies that enter the ink pool for the entire duration. While Follie and allies are in the Self Portrait's ink pool, they are granted 10% Damage Reduction, with each enemy killed inside the ink pool increasing the Damage Reduction up to 35% / 40% / 45% / 50%.
  - Damage Reduction applies to Warframes, Companions, summoned allied units such as Specters, allied Invasion units, Hostages, Kavor Defectors, Sortie and Arbitration Defense Operatives etc.
  - Killing an enemy inside the ink pool does the following:
    - Increases its duration by 3 seconds.
    - Increases the Damage Reduction by (Max Damage Reduction − Min Damage Reduction)/(15) .
    - Increases its radius by 0.6 / 0.7 / 0.7 / 0.8 meters.
  - Maximum Damage Reduction is capped at 90%, achievable with 180% Ability Strength.
  - Damaging effect requires Line of Sight to the target, while inking does not.
  - On cast damage instance has 100% damage falloff over its radius, while the ability expiration damage instance has 0% falloff.
  - Follie can recast Self Portrait at any time to move it a new location, while maintaining its current Damage Reduction, range, and duration.
    - If the remaining duration is lower than the starting duration, recasting Self Portrait will increase its duration back to the starting duration.

Helminth

- Subsuming Follie to the Helminth will offer Self Portrait and its augments to be used by other Warframes.
  - However, Subsumed Self Portrait's maximum Damage Reduction caps at 75% and does not apply Inkblot.

Maximization

Infused?

Self Portrait

Bugs

- Does not apply Inkblot on Overguarded enemies on cast or during its lifetime, but does apply Inkblot on Overguarded enemies when Self Portrait expires.

 | 2 50 | Splinter Storm Gara's armor splinters into a maelstrom of shattered glass. Allies who contact the cloud are fortified against damage. Introduced in Update 22.0 (2017-10-12) | Strength:100 / 150 / 200 / 250 (damage per second) 25% / 30% / 50% / 70% (damage reduction) 15% / 20% / 25% / 35% (damage vulnerability)
Duration:10 / 14 / 18 / 22 s
Range:15 / 20 / 25 / 30 m (cast) 1 / 1.5 / 2 / 2.5 m (radius)
Misc: 50% (absorbed damage)

Info

- Gara expends 50 Energy to shatter her glass armor into a storm of razor-sharp fragments that encircles herself, an ally, or an enemy target on the aiming reticle within 15 / 20 / 25 / 30 meters, lasting for 10 / 14 / 18 / 22 seconds. The shard storm has a radius of 1 / 1.5 / 2 / 2.5 meters, within which enemies and Objects are dealt 100 / 150 / 200 / 250 damage per second and constantly pushed away from the center. When surrounded by the Splinter Storm, Gara and her allies also receive 25% / 30% / 50% / 70% Damage Reduction, while targeted enemies receive 15% / 20% / 25% / 35% Damage Vulnerability.
  - Damage per second is distributed between 20% Impact, 40% Puncture, and 40% Slash.
  - Damage reduction is capped at 90%, achievable with 129% Ability Strength.
  - Damage vulnerability affects Splinter Storm's damage per second, causing the affected enemy target to receive increased damage from the Splinter Storm around it.
  - Eligible ally targets include all Warframes, Companions, Eidolon Lures, summoned allied units such as Specters, allied Invasion units, Hostages, Kavor Defectors, Sortie and Arbitrations Defense Operatives, Excavators and Defense Objects.
    - On Defense Objects, the damage reduction is capped at 50%.
  - Despite being a Warframe power, Splinter Storm seems to be considered as an object and cannot damage enemies across the Rift Plane.
    - Splinter Storm cast in the material plane will not be able to harm enemies in the Rift, even when the affected target later crosses into the Rift, and vice versa.
  - Enemies debuffed with Splinter Storm become immune to pushback and pull effects, including those of Splinter Storm, Ferrox and Tether Grenades.
- Casting Splinter Storm stops Gara's movement and actions.
- Can be cast on self when not aiming at an ally or enemy target.
- Can be cast on multiple targets while active.
- Cannot be cast on a target already affected by Splinter Storm.
- The newest active instance of Splinter Storm is tracked by the ability icon timer, including the instance on Gara herself.
- Splinter Storm buff on ally players appears as an icon with the timer below and percentage of damage reduction at the top-right, displayed beside the Shield and Health indicators on the affected players' HUD.
- Glass fragments are affected by Gara's chosen Warframe energy color.

Kit Interactions

- Gara's Passive allows casting abilities to have a 15% chance to Blind enemies within 12 meters for 10 seconds, exposing them to Melee Finisher attacks. Blind chance increases by 20% until the blind triggers.
- If a Spectrorage mirror shatters inside Splinter Storm's radius, 50% of the mirror's damage is permanently added to Splinter Storm's damage per second until its duration expires.
  - Absorbed damage can stack from multiple mirrors breaking inside Splinter Storm's radius.
  - Splinter Storms on any target can receive added damage from Spectrorage mirrors.
  - Splinter Storm does not receive added damage from Spectrorage's collapse explosion.
- Casting Mass Vitrify will also refresh the duration of Splinter Storm on Gara, as well as any affected allies that contact the molten glass during its expansion.
  - If Mass Vitrify's barrier is destroyed by Shattered Lash and Splinter Storm is within the explosion radius of the barrier, 50% of the explosions damage is permanently added to Splinter Storm's damage per second until its duration expires.
  - Added damage can stack from repeated Mass Vitrify explosions inside Splinter Storm's radius.
  - Splinter Storms on Gara herself and allies can receive added damage from Mass Vitrify's explosion, while storms on affected enemies do not.

Augment

- Main article: Mending Splinters

Mending Splinters is a Warframe Augment Mod for Gara's Splinter Storm that causes it to heal friendly targets it's applied to, with the healing being increased for every target (friendly or not) affected by Splinter Storm for a short time.

Rank | Health Regeneration | Cost
0 | 10/s | 6
1 | 11/s | 7
2 | 12.5/s | 8
3 | 15/s | 9

Tips & Tricks

- Aim away from allies and enemies then press 2 to cast Splinter Storm on yourself. If aiming at a target, pressing the ability key will lock onto the target and apply Splinter Storm on it after the casting animation.
- Buff your team and the objective with Splinter Storm to drastically increase their durability. Apply on Companions when able to protect them and grant them a pushback aura to defend against melee enemies.
- Use Splinter Storm's damage resistance and pushback effect to enhance your team's melee combat effectiveness, allowing any ally to clear paths through crowded hallways and chokepoints blocked by enemies.
- Damage resistance applies to Overshields, Shields and Health, making rapid regeneration of these stats ideal for endurance. Arcane Aegis, Arcane Barrier, Arcane Grace, Sentinel's Guardian mod, Raksa Kubrow's Protect mod, and Taxon's Molecular Conversion mod are great options to consider.
- Cast on an enemy to increase all damage against that target.
  - The pushback effect helps single out the enemy among a crowd for a direct line of gunfire.
  - Because of the pushback effect, melee weapons with short reach such as daggers and most melee ground finisher attacks can miss the intended target as it is moved away from Splinter Storm during the animation. Debuff a desired enemy with Splinter Storm to stop it from being pushed away, as well as enhancing damage against it.
- Splinter Storm also damages and breaks Objects in the environment, allowing for easy resource collection such as Iradite on the Plains of Eidolon. However, Explosive Barrels can also detonate if destroyed by the glass shards, therefore care should be taken when such objects are nearby.
  - Coincidentally, Splinter Storm offers great protection against enemy thrown grenades, causing them to detonate harmlessly against Tenno and applying its explosion damage against nearby enemies.
- Cast Mass Vitrify to simultaneously refresh your Splinter Storm to full duration. Any allies that touch the expanding molten glass will also have their Splinter Storms' timers refreshed, reducing overall energy costs for reapplying Splinter Storm on you and your allies and avoiding the prolonged casting animation locks.
- Stand next to Spectrorage's mirrors as enemies break them to stack additional damage onto Splinter Storm's damage per second.
  - This extra damage applies to you, your allies, and any enemies debuffed with Splinter Storm inside Spectrorage's carousel; extra damage remains as long as Splinter Storms remain active on the individual targets.
- Destroy Mass Vitrify's glass barrier using Shattered Lash, allowing you and your allies' Splinter Storms in range of the glass explosion to stack additional damage onto Splinter Storm's damage per second.
  - This extra damage applies to you and your allies only, and benefits from melee mods that apply to Shattered Lash, granting high damage amounts per explosion; extra damage remains as long as Splinter Storms remain active on the individual targets.
- When the Splinter Storm damage counter above the ability icons disappear, it signals that no more Splinter Storms are active from you. Keep close attention to avoid accidentally exposing you and your team to more incoming enemy damage than potentially able to be resisted.
- Splinter Storm will not be dispelled by Violence's Silence, so players can take advantage of it for The Steel Path missions.

Maximization

Mending Splinters?
Number of targets:

Splinter Storm

 | 2 50 | Kinetic Plating Generate armor plating that converts a portion of absorbed Kinetic Damage (Physical, Heat, Cold, and Blast) into Energy. Also protects Gauss from being staggered or knocked down. Damage Resistance is relative to the battery level. Introduced in Update 25.7 (2019-08-29) | Strength:14 - 70% / 16 - 80% / 18 - 90% / 20 - 100% (damage reduction)
Duration:15 / 20 / 25 / 30 s (duration)
Range:N/A
Misc: 0.1% (battery drain per hit) 1% (battery drain per second) 0.25% (battery charge per melee attack) 2 / 3 / 4 / 5 % (energy restore per hit) 50% (damage reduction cap at empty battery) 100% (damage reduction cap at full battery) 100% ( Slash status chance for Mach Rush) 100% (melee damage bonus, follow through, and stagger chance from Redline)

Info

- Gauss expends 50 energy to shield himself in a barrier of kinetic energy with one swift motion, protecting himself against incoming Impact, Puncture, Slash, Cold, Heat, and Blast damage types, while also becoming immune to Heat, Cold, Blast, Stagger, and Knockdown statuses for 15 / 20 / 25 / 30 seconds. While active, Kinetic Plating drains 1% battery power per second and 0.1%⋅sqrt(Hit Damage) battery power per hit received, to reduce affected damage by a minimum of 14% / 16% / 18% / 20% at empty battery, up to a maximum of 70% / 80% / 90% / 100% at full battery. 2% / 3% / 4% / 5% of incoming damage is converted into extra Energy for Gauss. Melee attacks while Kinetic Plating is active will restore 0.25% battery. Kinetic Plating deactivates on duration end or by manually pressing the ability key again (default 2 ).
  - Maximum damage reduction cannot exceed 100%. Minimum damage reduction cannot exceed 50%.
    - Damage reduction is calculated as: Min Damage Reduction + (Max Damage Reduction - Min Damage Reduction) × Current Battery Level
    - For example, with Kinetic Plating at rank 3, 100% Ability Strength, and battery level at 80%, the damage reduction will be: 20% + (100% - 20%) × 80% = 84%
  - Battery drain per second, battery drain per hit, energy restore per hit, and battery charge per melee attack are not affected by Mods.
  - Both damage reduction and energy restoration still function even when the battery is empty.
    - Energy restoration is calculated before all damage mitigation.

Kit Interactions

- While Kinetic Plating is active, it adds 100% Slash damage to Mach Rush's shockwave, and makes it inflict a Slash proc on enemies caught in the explosion radius.
- While above 80% battery during Redline, Kinetic Plating also grants Gauss a 100% Melee Damage bonus, sets Follow Through to 100%, and gives melee attacks 100% chance to stagger enemies on hit.
  - Melee Damage bonus is additive with other source of Melee Damage such as Pressure Point

Tips & Tricks

- Kinetic Plating stacks and synergizes well with Adaptation.
  - Kinetic Plating provides initial protection while Adaptation builds up damage resistance from 0% to 90%.
  - Though Kinetic Plating's damage resistance can reach 100% at full battery, it cannot cover all damage types, making it possible to get instantly killed by high level toxin damage.
    - Adaptation's damage reduction can alleviate this downside.
- Kinetic Plating stacks with Hunter Adrenaline and, when combined, can quickly restore energy while under heavy fire.
- Kinetic Plating synergizes well with Quick Thinking as it reduces energy drain upon fatal hit, and also compensates with its energy restoration.
- Kinetic Plating does not require high Ability Strength to be viable as its damage reduction is primarily scaled with battery level.
  - Damage reduction will be 84% with 100% Ability Strength at 80% battery level.
  - This can be scaled up to 90%, which requires 250% Ability Strength.
  - However, at full battery, damage reduction will reach 100% if Ability Strength is 100% or more.

Maximization

Battery level:

Kinetic Plating

 | 4 25 +5/s +25/alt fire | Glory on High Soar with destructive power. Use alternate-fire to detonate Judgments, causing an explosion of Jade Light. Enemies inside the Light's Judgment radius empower the explosion. Introduced in Update 36.0 (2024-06-18) | Strength:75 / 100 / 125 / 150 Heat damage 750 / 1000 / 1,250 / 1,500 Alternate Fire Heat damage 20 / 25 / 30 / 35 % damage reduction
Duration:N/A
Range:2 m primary fire explosion 4 m alternate fire explosion
Misc: 50% damage reduction cap 10% Judgment chance on Glory primary fire 1.5x Light's Judgment empowered range multiplier 7.2 ms (base movement speed) 100% (innate movement speed bonus).

Info

- Ascending the stairway to heaven, Jade expends 25 energy to soar into the sky with her seraphic wings unfurled. In this form, Jade permanently remains in mid-air, moving at 7.2 m/s with an innate +100% Movement Speed along with gaining vertical and horizontal flight capabilities using the movement (W A S D ), descend (Ctrl ), ascend (Spacebar ), and dodge (Shift ) hotkeys, similar to Archwing Maneuvers. Additionally, Jade gains 20% / 25% / 30% / 35% Damage Reduction while in flight and sheathes her weapons to equip her Exalted Weapon secondary orbitars Glory.
  - Damage Reduction is capped at 50%, achievable with 143% Ability Strength.
  - Movement speed bonus is additive with other sources of movement speed.
  - Jade cannot sprint during Glory on High.
  - Jade counts as being airborne in regards to the effects of Aerodynamic, Agility Drift and Aviator.
- Glory has its own unique statistics:
  - Primary fire shoots light orb projectiles.
    - Base damage is 75 / 100 / 125 / 150 pure Heat.
    - Shots explode in a 2 meter radius on impact with a surface or enemy.
      - Affected by Fulmination (Primed).
        - Bonus only scales with the base explosion radius, stacking additively with the bonus from ability range.
      - Has 100% damage falloff over its radius.
      - Requires Line of Sight to deal damage.
        - Line of Sight is affected by Punch Through; Sufficient amounts of Punch Through allows the explosion to deal damage to enemies not within line of sight.
  - Alternate Fire detonates all enemies affected by Judgments, consuming their marks in the process.
    - Base damage is 750 / 1,000 / 1,250 / 1,500 pure Heat.
      - The detonated enemy receives the damage before the Judgments mark is removed, increasing its damage taken by 50%. Nearby enemies will only receive the increased damage if they themselves are currently marked by Judgments.
        - Multiple marked enemies will all be detonated on the same game tick, but internally they are detonated one at a time. If multiple detonated enemies are within each others' explosion radii, some of those enemies will take fewer hits boosted by Judgments than others. The damage they take depends on how early into the detonation chain their Judgments mark was removed.
    - Detonated enemies explode in a 4 meter radius.
      - Not affected by Fulmination (Primed).
    - Consumes 25 energy.
    - Requires Line of Sight to at least 1 enemy afflicted by a Judgment to be triggered, however all enemies marked with Judgments will be detonated, regardless of distance or if they can be seen.
    - Has a fixed casting cooldown of 1.5 seconds, unaffected by fire rate, reload speed, or casting speed.
    - Glory's Alternate Fire is not affected by:
      - Base Damage (Hornet Strike, Secondary Merciless, Deathbringer's weapon damage bonus)
      - Multishot (Barrel Diffusion)
  - Shots have a 15% critical chance, 2x critical multiplier, 20% status chance, 1.67 fire rate, infinite ammunition, and does not need to reload.
  - Glory can be equipped with secondary mods and Arcane Enhancements.
    - Galvanized Shot's damage per status type has no effect on Glory's primary or alternate fire.
    - Riven Mods are not generated for the Glory.
  - Because Glory is counted as a secondary, it is affected by mods and Warframe Arcanes such as Pistol Amp and Arcane Precision.
    - Headshot effects only trigger if it procs a status effect that can headshot, like Electricity or Gas, or must be activated beforehand.
  - Glory on High consumes 5 energy per second while active and will remain active until Jade's energy is depleted, or the ability is deactivated by pressing the ability key again.
    - Jade cannot replenish energy using Energy Vampire, Rally Point, Rift Plane's innate energy regeneration, Squad Energy Restores, Energy Siphon, Energy Nexus, Dreamer's Bond, and/or Wellspring while Glory on High is active.
    - Energy Orbs, Orokin Void Death Orb's energy restores, Rage, Hunter Adrenaline, Spellbound Harvest, Arcane Energize, and Emergence Dissipate's Energy Motes can still replenish Jade's energy while in Glory on High.
    - Glory on High's energy drain is not converted into shields by Augur Mods.
- Jade is unable to accomplish any action that requires the Use key (default X ) while Glory on High is active, thus cannot interact with consoles, pick up carriables such as datamasses, or directly revive allies from bleedout.
  - Jade can pick up carriables before activating Glory on High, but is not able to use them until she deactivates the ability.
  - The Operator can still be used while in Glory on High, and be able to do these actions without deactivating the ability. However, energy drain will still continue while in Operator mode.
- Subsumed abilities injected into Jade via the Helminth system can be cast while in Glory on High.

Weapon

- Main article: Glory

Glory is Jade's Exalted Orbitars, summoned by activating the ability Glory on High. Primary fire shoots explosive Heat beams, while its Alternate Fire detonates Judgments in a disintegration blast.

- This weapon deals pure Heat damage.
- Innate two polarities.
- Primary fire shoots explosive projectiles.
  - Shots explode in a 2 meter radius on impact with a surface or enemy, with 100% damage falloff from the center.
    - Affected by Fulmination (Primed).
      - Bonus only scales with the base explosion radius, stacking additively with the bonus from ability range.
    - Requires Line of Sight to deal damage.
      - Line of Sight is affected by Punch Through; Sufficient amounts of Punch Through allows the explosion to deal damage to enemies not within line of sight.
  - Shots have a 10% chance to debuff enemies with Judgments, applying 50% Damage Vulnerability for 10 seconds.
    - Debuff chance is unaffected by Status Chance, or any Ability Stats.
- Alternate Fire detonates Judgments.
  - Enemies explode in a 4 meter radius.
    - Not affected by Fulmination (Primed).
    - Enemies standing within Light's Judgment have their explosion radius increased by 1.5x.
    - Is affected by:
      - Critical Chance and Critical Damage
      - Elemental Damage
      - Faction Damage
      - Status Chance, Status Damage, and Status Duration
      - Secondary Enervate, Secondary Encumber, Secondary Fortifier, and Secondary Outburst
    - Is not affected by:
      - Base Damage (Hornet Strike, Secondary Merciless, Deathbringer's weapon damage bonus)
      - Multishot
      - Fire Rate
      - Reload Speed
      - Cascadia Empowered, Secondary Irradiate, Secondary Shiver, and Secondary Surge

Advantages:

- Has infinite ammo and does not need to reload.

Disadvantages:

- Primary fire has 100% damage falloff, dealing 0 damage at the edge of its explosion radius.
- Requires energy to activate and keep active. Alternate Fire uses additional energy to activate.
- Galvanized Shot's damage per status type has no effect on the explosion.

Kit Interactions

- Primary fire shots have a 10% chance to inflict Judgments, inflicting 50% Damage Vulnerability for 10 seconds.
  - Debuff chance is unaffected by Status Chance, or any Ability Stats.
- Light's Judgment can apply Judgments. Alternate Fire gains an increased 1.5x explosion radius against enemies inside Light's Judgment.
- Enemies killed while debuffed by Judgments extends Symphony of Mercy's duration by 2 seconds.
- Symphony of Mercy's Power of The Seven Ability Strength bonus and Deathbringer weapon damage bonus enhance Glory on High and its Glory exalted secondary weapon.
- Ophanim Eyes can revive allies during Glory on High.

Maximization

Weapon Damage modifier:
Elemental damage modifier:
Faction damage modifier:
Blast Radius modifier:
Enemy has Judgment?

Glory on High

 | 3 75 | Shatter Shield Envelops Mesa in a barrier of energy, reflecting back incoming bullet damage. Introduced in Update 15.5 (2014-11-27) | Strength:50% / 60% / 70% / 80% (damage reduction)
Duration:10 / 15 / 20 / 25 s
Range:5 / 7 / 9 / 11 m
Misc: 95% (damage reduction cap) 45° (deflect angle for non-hitscan) 90° (divert angle for hitscan) ∞ (hitscan reflect range)

Info

- Mesa expends 75 energy to envelop herself in an energy shield for 10 / 15 / 20 / 25 seconds, which reduces incoming damage from enemy gunfire by 50% / 60% / 70% / 80%. The shield reflects hitscan bullets back to the attacker over unrestricted range, but deflects non-hitscan projectiles randomly up to 45° from the point of impact. Affected gunfire will instead divert towards a random enemy, if any, within an 5 / 7 / 9 / 11 meter radius and up to 90° from the point of impact.
  - Damage reduction is capped at 95%, achievable with 119% Ability Strength.
  - Diverted gunfire is physically redirected. As such, obstacles in the environment can prevent it from hitting enemies.
    - Damage is equivalent to what enemies would receive if they were to damage themselves.
    - With Secondary Fortifier equipped, damage reflected to overguarded units will grant Mesa Overguard
    - Status Effects can proc normally, on both Mesa and enemy targets.
- Projectile-based Knockdown is resisted, such as the grappling hooks from Scorpions and Infested Ancients. However, knockdown caused by radial blasts from units such as Shockwave MOAs and Heavy Gunners will bypass Shatter Shield.
- Will also decrease damage from Combat Discipline
- Shatter Shield does not protect Mesa from area damage or melee attacks, thus damage will be dealt as normal.
- Cannot be recast while active.

Augment

- Main article: Staggering Shield

Staggering Shield is a Warframe Augment Mod for Mesa that gives shots reflected by Shatter Shield a chance to stagger enemies.

Rank | Stagger Chance | Cost
0 | 30% | 6
1 | 35% | 7
2 | 40% | 8
3 | 50% | 9

Tips & Tricks

- As damage reduction is capped to 95%, any Ability Strength beyond 119% will not have further effect to Shatter Shield. Maximum damage reduction can be achieved with just a rank 3 Intensify, or a rank 4 Augur Secrets for 3 less drain.
- Players should take caution, as while damage reduction will apply to Projectile/Hitscan weaponry, it does not apply to explosions.
- Bombard rockets will be deflected and often will ricochet back into enemies with a good chance of proccing radial knock-down.

Maximization

Staggering Shield?

Shatter Shield

Bugs

- Reflected damage from non-hitscan weapons is not calculated properly. The reflected damage enemies receive from non-hitscan weapons does not appear to factor in the enemy's level, causing the same damage to be reflected regardless of enemy difficulty.
- When shot by an Embolist with Shatter Shield active Mesa will receive the poison proc even if the damage source was friendly.
- Some types of projectiles stop when hitting Shatter Shield and disappear at the time their damage is being dealt to a target within range, instead of being visually redirected towards them. No damage loss, though.

 | 3 25 | Eclipse (TAP) Temporarily reduce the damage Mirage takes from enemies. (HOLD) Temporarily increase Mirage's weapon damage. Introduced in Update 14.0 (2014-07-18) | Strength:25 / 40 / 60 / 75 % (damage reduction) 50 / 100 / 150 / 200 % (weapon and melee damage bonus)
Duration:10 / 15 / 20 / 25 s
Range:N/A
Misc: 90 % (damage reduction cap)
Subsumable to Helminth

Info

- Mirage expends 25 Energy to adapt to lighting conditions for 10 / 15 / 20 / 25 seconds.
  - Tap down the ability key to receive Lunar Eclipse, bathing Mirage in shadows to gain 25% / 40% / 60% / 75% Damage Reduction and reducing enemy accuracy.
    - Damage reduction is capped at 90%.
  - Hold the ability key to receive Solar Eclipse, bathing Mirage in light to gain 50% / 100% / 150% / 200% weapon and melee damage.
    - This buff is multiplicative with almost all other flat damage buffs. For example, a weapon with 250 base damage, Serration, and Solar Eclipse with a maxed Intensify will increase the weapon's damage to 250 × ( 1 + 1.65) × (1 + 2.0 × [1 + 0.3]) = 2,385.
      - The one flat damage buff that is additive with Eclipse comes from condition overload effects on weapons that have additive CO. Base damage is multiplied separately and then added together.
- Has a casting delay of 1 second, affected by Casting Speed.
- Can be recast while active to refresh the duration.
- Companions and holograms from Hall of Mirrors do not normally gain Eclipse's damage bonus, but will gain that bonus with the Total Eclipse augment equipped.
- Applies twice on Exodia Contagion and glaive explosions.
- As Eclipse applies universally, it can affect certain abilities.

Kit Interactions

- Eclipse provides benefits to Prism:
  - Lunar Eclipse (tap cast) halves Prism's base energy cost to 25 energy and base energy drain to 5 energy per second.
  - Solar Eclipse (hold cast) doubles Prism's damage bonus per hit to +50%.

Helminth

- Subsuming Mirage to the Helminth will offer Eclipse and its augments to be used by other Warframes.
  - However, Subsumed Eclipse's damage reduction caps at 75%, and damage bonus is reduced to 2% / 9% / 15% / 30%.
  - When placed on Chroma, Cyte-09, Octavia, Oraxia, Rhino, Temple, Xaku, or Uriel, Subsumed Eclipse can only replace Vex Armor, Resupply, Amp, Silken Stride, Roar, Ripper's Wail, Xata's Whisper, or Demonium respectively.

Augment

- Main article: Total Eclipse

Total Eclipse is a Mirage Warframe Augment Mod for Eclipse that allows it to grant its bonuses to nearby allies.

Rank | Effect | Radius | Cost
0 | 100% | 8m | 6
1 | 100% | 10m | 7
2 | 100% | 12m | 8
3 | 100% | 15m | 9

Maximization

Total Eclipse?
Infused?

Eclipse

 | 1 25 | Null Star Creates antimatter particles that orbit Nova and attack nearby targets. Each active particle reduces damage to Nova's Health and Shields. Introduced in Update 9.0 (2013-07-13) | Strength:150 / 200 / 250 / 300 ( Blast damage) 5% (damage reduction per particle)
Duration:12 (particles)
Range:10 m (attack radius)
Misc: 1 s (attack interval) ∞ (particle duration) 100% ( Blast status chance) 90% (damage reduction cap)
Subsumable to Helminth

Info

- Nova expends 25 energy to create 12 antimatter particles that orbit her and automatically launch themselves one by one every 1 second at enemies within 10 meters inflicting 150 / 200 / 250 / 300 Blast damage with 100% status chance. Each particle persists on Nova indefinitely until launched, granting her 5% Damage Reduction as they orbit her.
  - Damage reduction is capped at 90%.
- While active, a counter becomes visible on the ability icon that displays the number of available particles.
- Null Star has a 2.5 second cooldown between casts
- Nova cannot be knocked down while casting Null Star.
- The particles benefit from generic increases to weapon base damage, such as from Arcane Arachne, Holster Amp, and Vigorous Swap, but not from weapon class specific increases like Steel Charge or Rifle Amp.
  - The particles can also benefit from flat critical chance, such as from Covenant or Arcane Avenger. However, they have a critical multiplier of 1x, so sources of critical damage like Tenacious Bond are required for any effect on the damage.
  - Most elemental damage boosts, such as Shock Trooper, have no effect.
  - Valence Formation does apply both its effects.
  - Nourish applies both damage and Viral elemental weight that will compete with the innate Blast of the particles.

Kit Interactions

- With Molecular Fission, Null Stars will slow or speed up enemies based on the most recent type of hold or tap Molecular Prime cast.
  - Molecular Fission will cause enemies hit by Null Stars upon death to recharge Null Stars.

Helminth

- Subsuming Nova to the Helminth will offer Null Star and its augments to be used by other Warframes.
  - Damage reduction caps at 75% instead of 90%.
- If Garuda subsumes Null Star or Nova subsumes Blood Altar, then the particles will not target enemies currently impaled by Blood Altar.
- If Chroma subsumes Null Star, Vex Armor's damage boost will apply to Null Stars.
- If Limbo subsumes Null Star, Rift Torrent's damage boost will apply to Null Stars.

Augment

- Main article: Neutron Star

Neutron Star is a Warframe Augment Mod for Nova's Null Star that allows it to inflict Heat damage with guaranteed status effect in a radius and recasting the ability will disperse currently active particles to seek out enemies before being replenished. Neutron Star's seek radius is doubled than that of Null Star's.

Rank | Heat Damage | Radius | Cost
0 | 120 | 4m | 6
1 | 160 | 5m | 7
2 | 200 | 6m | 8
3 | 240 | 8m | 9

Tips & Tricks

- 90% damage reduction can be achieved with 150% strength or duration, as long as the other stat is not below 100%. Going beyond this is still useful, as it provides a buffer when particles are used up.
- When you are full on energy and come across extra energy spheres laying on the floor, you can cast a "free" Null Star and instantly go back to full energy. This allows you to easily keep stars active for each encounter.
- Stars will launch themselves at unaware enemies, alerting them if they survive. This makes this ability sub-optimal for stealth oriented missions.
- Each particle will stun on hit, allowing you to continually stagger a target while you attack them.
  - although multiple Null Star's hitting the same target will sadly not yield more Null Star's than normal when using Molecular Fission think of it as a "Yes or No" state, not a stacking buff/effect on the enemy.
- Defensively, it is wise to use it before reviving an ally or accessing a terminal, as you are very vulnerable when doing either. Activating Null Star beforehand can stun or kill any enemies nearby that decide to attack you, preventing you from taking a lot of unnecessary damage.
- On higher enemy ranks Nova may wish to use the skill in the same manner as Rhino's Iron Skin and recast it every time her damage reduction dips significantly below 90%, as this will prevent her from being blindsided by enemies that are stuck in corners or behind obstacles. This is particularly important in Grineer tilesets because infantry will often jam themselves into corners on either side of the round doorways and open fire as soon as the player passes by.
- To focus on keeping Null Star particles for damage reduction, it can be beneficial to have Ability Range lower than 100%. Lower range will prevent particles from seeking enemies at a distance. This will however hinder her other abilities, particularly Antimatter Drop.
- Null Star particles will seek deactivated Bursa in range. It is advisable to stay away to prevent wasting the particles.
- The Molecular Fission augment will allow Molecular Prime and even Null Star's themselves to restore up to two charges of Null Star per enemy killed while under its effects.

Maximization

Neutron Star?
Infused?

Null Star
Targeting radius | m

Bugs

- The base damage of null star is currently 200, not the 300 stated in the patch notes

 | 3 50 | Light's Sanctuary Sirius creates a well of light that heals and revives allies, while reducing incoming damage. The well slowly grows in size and power. (HOLD) Swap to Orion and use Event Horizon. Introduced in Update 43.0 (2026-06-17) | Strength:10 - 40 / 15 - 45 / 20 - 50 / 25 - 55 (heal rate) 15% - 45% (damage reduction)
Duration:25 / 26 / 28 / 30 s
Range:5 - 10 m (radius)
Misc: 10 s (expansion time) 60 s (revive cooldown per ally) 1 (sanctuary limit) 75% (maximum damage reduction cap)

Info

- Sirius expends 50 Energy to create a celestial sanctum of Jade Light that lasts for 25 / 26 / 28 / 30 seconds. The sanctum's radius and effect expands over 10 seconds, spanning a range of 5 - 10 meters, restores 10 / 15 / 20 / 25 - 40 / 45 / 50 / 55 Health per second, and provides 15% - 45% Damage Reduction. Allied Warframes and Companions that enter bleedout while within the sanctum are gradually revived, incurring a 60 second cooldown on the downed ally. Only 1 Light's Sanctuary can be active at once.
  - Maximum Ramp-Up Damage Reduction is capped at 75%, achievable with 167% Ability Strength.
  - Initial Damage Reduction ignores the Ramp-Up Damage Reduction cap, allowing 100% Damage Resistance, achievable at 667% Ability Strength
  - Damage Reduction always takes 10 seconds to reach maximum effect, even with strength above 167% which narrows the gap between minimum and maximum effect. The rate of increase slows down to match the new difference.
  - If controlled Sirius is downed, Light's Sanctuary can revive him.
  - If allies are downed while inside this ability during Arbitrations, they can be revived gradually.
  - Affected entities are visually surrounded by a constellation ring floating near their torso.
  - Light's Sanctuary's effect radius is spherical, matching the expanding dome of light. The constellation circle visual effect below the sanctum always appears on the ground below the dome of light, but do not indicate the ability's radius.
- Can be recast while active.
  - Recasting elsewhere relocates the sanctum, resetting it to base radius and effect.
  - Recasting inside an active Light's Sanctuary refreshes its duration to full, while keeping its location and current radius and effect.

Kit Interactions

- Holding this ability changes control to Orion who executes Event Horizon instead.

Maximization

Switching passive?

Light's Sanctuary

Localization

Language | Official Translation
(PT) Brazilian Portuguese | Sirius criará um poço de luz que cura e revive aliados, além de reduzir o dano recebido. O poço crescerá lentamente em tamanho e poder. (SEGURAR) Alternará para o Órion e conjurará o Horizonte de Eventos.

 | 2 25 | Tribute Cycle through and extract one of the four Buffs when cast on an enemy. Thorns reduces incoming damage. Dust degrades enemy accuracy. Full Moon increases companion damage. Entangle slows enemies within range. Introduced in Update: The Silver Grove (2016-08-19) | Strength:200 / 300 / 400 / 500 ( Impact damage)
Duration:6 / 8 / 10 / 12 s (debuff duration)
Range:10 / 15 / 20 / 25 m (cast range)
Misc: -25% (damage debuff) 15 s (offering duration) 120 s (aura buff duration) 35 m (aura range) 50% (Thorns damage reflection and reduction) -50% (enemy hit chance) 75% (Full Moon damage bonus) 50% (Full Moon health and armor bonus) 25% (Entangle move speed debuff)

Info

- Titania selectively enchants her spell by tapping the ability key (default 2 ) to freely cycle between the Thorns, Dust, Full Moon, and Entangle buffs. Hold down the ability key to expend 25 energy while aiming at an enemy up to 10 / 15 / 20 / 25 meters away will deal 200 / 300 / 400 / 500 Impact damage and Knockdown while reducing their damage by 25% for 6 / 8 / 10 / 12 seconds. The target also leaves behind an offering for 15 seconds to be collected by Titania.
  - Cast animation of 1 second is affected by Casting Speed.
- A special cyclic display located above Titania's weapon stats in the HUD will show the currently selected buff and shows timers for each buff's active duration.
- The offering extracted is left in place near the location where the target got hit by Tribute and appears as a shadow replica of the enemy. If Titania picks it up by touching it, she is granted the respective buff chosen before cast. These buffs are auras that last for 120 seconds and have a radius of 35 meters around Titania. Picking up an offering of an already active buff will refresh its duration. All four buffs can be active at once. The following buffs are available:

- The Thorns buff aura grants 50% damage reduction and reflects 50% of the damage taken back to the attacker.
  - Allies affected visually emit energy butterflies, affected by Titania's energy colors.
  - Defense Objects do not benefit from Thorns.

- The Dust buff aura reduces the Accuracy of enemies within range by 50%.
  - Enemies affected visually emit energy butterflies, affected by Titania's energy colors.

- The Full Moon buff aura increases the damage dealt by Companions and Razorwing's Razorflies by 75%, as well as their Health and Armor 50%.
  - Companions affected visually emit energy butterflies, affected by Titania's energy colors.

- The Entangle buff aura inflicts 25% Slow to enemies within range.
  - Enemies affected visually emit energy butterflies, affected by Titania's energy colors.

- Ability Synergy:
  - Razorwing spawns an extra Razorfly for each Tribute buff picked up, up to 4 extra Razorflies to a maximum of 10.
    - While Titania remains in Razorwing, these extra Razorflies are permanent and do not expire when the corresponding buff does.
  - Razorflies will fly to and pick up Tribute offerings for Titania.
- Offerings created by Tribute display a symbol above them that denotes the aura they bestow.
  - The color of the offerings and their symbols are affected by Titania's energy colors.

Tips & Tricks

- Since offerings sometimes tend to drift upwards, it is more convenient to use the ability while close to the target.

Maximization

Tribute

Bugs

- The offering pickup will often fly off into the skybox, becoming unreachable. This generally bypasses any roofs/overhangs when it happens, although not always.
  - Holding "move backwards" while activating the ability seems to minimize the chances of this bug occurring.
- The damage bonus from Full Moon is currently only 50%.
  - It will overwrite Summoner's Wrath if the summon is created while under the effect of the buff. (otherwise they stack multiplicatively)

 | 4 100 | Blessing Restore the health and shields of allies within Affinity Range while reducing the damage they take from enemies. Introduced in Update 4 (2012-11-02) | Strength:40% / 50% / 75% / 80% (shield/health restoration) 25% / 30% / 40% / 50% (damage reduction)
Duration:8 / 10 / 12 / 15 s (buff duration)
Range:N/A
Misc: 50 m (affinity range) 75% (damage reduction cap)

Info

- Trinity expends 100 energy to invokes potent restorative and defensive power from within for herself and all allies within Affinity Range, restoring 40% / 50% / 75% / 80% of her and her allies' maximum Shields and Health and granting them 25% / 30% / 40% / 50% Damage Reduction for 8 / 10 / 12 / 15 seconds.
  - Cast time of 0.5 seconds is affected by Casting Speed.
  - Affinity Range is affected by Mending Unity and Fosfor flares.
    - Affinity Range increase for Archwing and Landscape missions also apply to the range of Blessing.
    - Range is not affected by Ability Range.
  - Damage reduction is capped at 75%, achievable with 150% Ability Strength.
  - Affected allies include all Warframes, Companions, Eidolon Lures, summoned allied units such as Specters, allied Invasion units, Hostages, Kavor Defectors, Sortie and Arbitration Defense Operatives, and Defense Objects.
    - On Defense Objects, Blessing restores up to 500 health over 5 seconds which does not stack with similar restoration effects. The damage reduction is also capped at 50%.
- Blessing is uninterruptable. Even if Trinity enters bleedout while casting, the healing and damage resistance will still be granted.
- After life support has completely drained in Survival, losing all shields will prevent Blessing from restoring them similar to No Shields Nightmare mode.
- Does not restore or create overshields.
- While active, electricity-like energy waves will appear on all affected characters and companions; the color is affected by Trinity's energy color.
- Can be recast while active.
  - Blessing's damage reduction will not disappear while recasting the ability.

Augment

- Main article: Champion's Blessing

Champion's Blessing is a Warframe Augment Mod for Trinity's Blessing that increases their own primary and secondary Critical Chance based on the total percentage health healed, up to a +350% bonus.

Rank | Duration | Max Critical Chance Bonus | Cost
0 | 12s | +350% | 6
1 | 18s | +350% | 7
2 | 24s | +350% | 8
3 | 30s | +350% | 9

Tips & Tricks

- Blessing's damage reduction increases the effectiveness of her Vampire Leech augment's overshields.
- Fosfor flares greatly increase affinity range and Blessing range by 200m. Try them in open world Landscapes.
- Narrow Minded does not decrease the range of Blessing, but does impact Trinity's other abilities.
- 125% Ability Strength or higher allows Blessing to completely restore shields from 0% and reliably reset shield gate invulnerability.

Maximization

Champion's Blessing?

Blessing

Bugs

- Casting Blessing after a Nova casts Molecular Prime will cause the explosions to have your energy color.
- Blessing's healing doesn't consistently heal Kavor Defectors within affinity range. This bug seems to be more prominent when the Defectors are buffed by mote(s) from Wisp's Reservoirs

Mods

- Firewall (75% damage reduction)
- Guardian Armor (75% damage reduction for allies)
- Immolated Radiance (up to 50% damage reduction for allies)
- Ironclad Flight (40% damage reduction)
- Proton Jet Proton Set Bonus (16.67% damage reduction)
- Proton Pulse Proton Mod Set Bonus (16.67% damage reduction)
- Proton Snap Proton Mod Set Bonus (16.67% damage reduction)
- Reverse Rotorswell (35% damage reduction)
- Warding Thurible (50% damage reduction for allies)
- Armored Acrobatics (20% damage reduction. Only useable in Conclave)
- Armored Evade (40% damage reduction. Only useable in Conclave)
- Armored Recovery (50% damage reduction. Only useable in Conclave)
- Agility Drift (12% damage reduction)
- Aerodynamic (24% damage reduction)
- Aviator (40% damage reduction)
- Boreal's Anguish Boreal's Set Bonus (20% damage reduction)
- Boreal's Contempt Boreal's Set Bonus (20% damage reduction)
- Boreal's Hatred Boreal's Set Bonus (20% damage reduction)
- Necramech Aviator (40% damage reduction)

Arcanes

- Arcane Double Back (25% damage reduction on maneuver, stacks 3 times)
- Magus Firewall (12.5% damage reduction per second in Void Mode, stacks 6 times)

Others

- Tenno Shield (50% damage reduction)
- Marauder's Nerve Decree (Up to 75% damage reduction)
- Innodem's Incarnon Resilience buff on finishers (10% damage reduction, stacks 4 times)
- Blocking with melee (100% damage reduction)
- Rolling (75% damage reduction)

Enemies

- Guardian Eximus aura (90% damage reduction)
- Ancient Disruptor (90% damage reduction from damage done by abilities)
- Grustrag Bolt (50% damage reduction against Grineer)

### Notes

- Reverse Rotorswell: Despite claiming in its description that this mod offers Damage Redirection, the mod actually offers Damage Reduction, which does not affect Overguard, nor provides Status Effect immunity, alongside the damaging effect.

## Damage Redirection

- Main article: Damage Redirection

Damage Redirection is different from Pure Damage Reduction in that it also applies to Overguard.

### Sources of Damage Redirection

This section is transcluded from Damage Redirection § Sources of Damage Redirection. To change it, please edit the transcluded page.

Abilities

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

 | 2 25 | Merulina Summon Merulina, a rideable creature of the waves, and the inspiration for K-Driving. Merulina protects Yareli by absorbing a large portion of incoming damage. Introduced in Update 30.5 (2021-07-06) | Strength: N/A Duration: N/A Range: N/A Misc:4 s initial invuln. time Secondary only restriction Ragdoll immunity Stagger & knockdown resistance 1.5 s dismount invuln. time Strength: 3,000 / 4,500 / 6,000 / 7,500 HP health pool Duration: N/A Range: N/A Misc:90% damage redirection ∞ duration 18 m/s move speed 21 m/s boost speed 3 m jump height 12 m double jump height 1.25 s jump charge time 17 m charged jump height 10 m dash distance 1,000 Impact damage on landing 5 Impact damage on slam shockwave 2 m slam shockwave radius
Strength: N/A
Duration: N/A
Range: N/A
Misc:4 s initial invuln. time Secondary only restriction Ragdoll immunity Stagger & knockdown resistance 1.5 s dismount invuln. time
Strength: 3,000 / 4,500 / 6,000 / 7,500 HP health pool
Duration: N/A
Range: N/A
Misc:90% damage redirection ∞ duration 18 m/s move speed 21 m/s boost speed 3 m jump height 12 m double jump height 1.25 s jump charge time 17 m charged jump height 10 m dash distance 1,000 Impact damage on landing 5 Impact damage on slam shockwave 2 m slam shockwave radius

Info

- Yareli expends 25 energy to summon her faithful aquatic creature from the watery depths and rides aboard Merulina after it emerges. Upon activation, the board is Invulnerable for 4 seconds, during this time all incoming damage it takes is added to its total health. While riding Merulina, Yareli switches her combat and movement controls to K-Drive controls; aboard her transport, Yareli unholsters and only wields her equipped secondary weapon, becomes immune to Ragdoll and resists Stagger and Knockdown from most sources. Yareli may manually dismount from Merulina for 0 energy cost by pressing the ability key again (default 2 ), press or hold and release the quick melee attack key (default E ), or hold and release the interact key (default X ) to despawn it and switch back to normal Warframe controls.
  - Yareli is Invulnerable for 4 seconds after summoning Merulina, and 1.5 seconds when dismounting manually or on Merulina's destruction.
  - She is immune to K-Drive ragdoll effects from dismounting Merulina, does not eject off from failing K-Drive board grabs and flips, nor from strong impact collisions with the environment and obstacles.
  - She will resist self-stagger effects inflicted by her equipped area-of-effect secondary weapons, as well as knockdown effects from enemies such as Grineer Heavy Gunner, Shield Lancer, Scorpion, Corpus Shockwave MOA, Laser Barrier, Infested Ancients, and Arson Eximus units.
  - Merulina is immune to the slowing effect of a Hobbled Dragon Key.
  - She is able to collect Pickups such as orbs and ammo.
  - She is able to use selective Gear items such as equipping the Codex Scanner or deploying Team Bonus Consumables.
  - She can also initiate interaction (default X ) with some entities and Objects such as opening doors and lockers, using elevators, picking up/inserting a datamass, picking up Ayatan Star/Sculptures and Granum Crown, Hacking consoles, activating Survival Life Support Capsules, etc.
    - Attempting to revive an ally in Bleedout forces Yareli to dismount when the interact key is pressed.
    - Interacting with objects requires Reload with Context Action Input enabled otherwise the player will dismount.
  - She is able to perform Transference while aboard Merulina. This will not cause her to dismount.
- Merulina is Yareli's personal deployable vehicle that possesses unique attributes and K-Drive maneuvers:

Attributes

- Merulina has a base Health pool of 3,000 / 4,500 / 6,000 / 7,500 health and 50 armor that protects Yareli by redirecting 90% of all incoming damage from Yareli to Merulina's health. The ability lasts indefinitely until its health pool fully depletes, or Yareli dismounts or falls Out of Bounds. Upon destruction, Merulina prevents the damage from the last lethal hit from spilling over to Yareli's hitpoints.
  - Merulina's health pool is not affected by Damage Reduction from abilities and mods such as Total Eclipse and Adaptation.
    - However, Adaptation stacks can still be accumulated while riding Merulina and will reduce the damage Yareli herself takes as normal.
    - Merulina benefits from armor from Azure Archon Shard and Helminth Armor Invigorations, but not other sources.
  - Merulina cannot be healed by conventional means, such as picking up Health Orbs and triggering Arcane Enhancement effects.
    - While riding Merulina, using subsumed Gloom will cause Yareli's damage to be converted into healing for Merulina rather than herself.
  - While active, Merulina's health indicator is displayed above Yareli's ability icons. The UI element consists of Merulina's animated portrait on the left, the current numeric total of remaining health points on the right, and a health bar at the bottom that drains from left to right.
- Merulina's hidden K-Drive stats include:
  - Move Speed of 18 meters per second and Boost Speed of 21 meters per second
  - Jump Height of 3 meters and Double Jump Height of 12 meters.
  - Jump Charge Time of 1.25 seconds and Charged Jump Height of 17 meters.
- Despite being functionally a K-Drive, Merulina cannot be modded, and is unaffected by mods equipped on a custom-built K-Drive in Yareli's Vehicle tab in the Arsenal screen.
- Merulina gradually loses a percentage of health per second when Yareli is within an ability nullifying sphere created by special enemies, such as the Nullifier Crewman.
- Merulina's colors can be customized via its own Appearance tab in the Arsenal screen, once the ability is unlocked on Yareli at Warframe Rank 3.
  - Energy colors on Merulina will instead match the chosen selections in Yareli's Appearance tab.
- Merulina visually appears as an Infested aquatic creature with physical characteristics commonly found in real world stingrays (flat body with flaps and tail), Portuguese man o' war (translucent membranes, multiple stingers), and crustaceans (spiked chitinous carapace). The creature's frontal beak, fin flaps, and tails use cloth and jiggle physics, allowing them to sway along to Yareli's movement. The bioluminescent central cavity holds flowing liquid in motion that glistens and shimmers to the light.
  - Merulina produces liquid splashes and bubbles beneath its belly as it moves and lands on surfaces.
  - Merulina audibly makes chirping and gurgling creature sounds while Yareli is riding on it and performing K-Drive tricks.

Tricks

- K-Drive trick scores earned with Merulina yield Ventkids Standing in any mission.
- While riding Merulina, Yareli can holster away her secondary weapon by pressing the switch weapon key (default F ) to enable her to perform more K-Drive tricks such as board grabs (default LMB ) and flips (default RMB ).
- Yareli and Merulina will dash toward the input direction for a distance of 10 meters when performing a dodge maneuver:
  - Merulina's dash can be used on the ground, while in midair, and during casting animations to quickly reposition and break free from falling.
  - Each dash triggers a short cooldown before another can be performed.

Action | PC | PlayStation | Xbox | Nintendo Switch | iOS
Dash | Tap LShift | Tap L1 /LB | Tap LB | Tap L | ??

- When moving at cruising or boosted speed (default hold LShift ) with enough momentum, Yareli aboard Merulina can slide through some environmental barriers such as small railings, and surf on top of Defense Objects such as the Warframe Cryopod and Excavator.
- Merulina can ollie and double jump (default Spacebar x2) to reach greater heights than Warframes' jumping.
  - Double jump can be performed after a charged jump (default hold and release Spacebar ).
- Landing directly on top of an enemy from any height with Merulina inflicts 1,000 Impact damage and knockdown.
- Performing a K-Drive slam shockwave (default while in midair, tap + tap and hold down LCtrl ) causes Yareli to dive toward the ground, emitting a 2 meter expanding shockwave on landing that inflicts 5 Impact damage with a status chance to all enemies inside, causing guaranteed heavy knockdown and knockback away from the impact point.
- Merulina is able to surf on some allied summoned objects, such as Frost's Snow Globe.

- Cannot be cast if spacing around Yareli is obstructed. Merulina will self-destruct if Yareli attempts to mount it while she is standing in an out-of-bounds zone, usually below the playable area of a mission such as the pillar protrusions in the Simulacrum.
- Mounting and dismounting from Merulina are full-body animations that carry forth Yareli's momentum while stopping other actions.
- Yareli visually leaps gleefully into the air as she spins counterclockwise, summoning Merulina beneath her as they land onto the ground with a splash.
  - When performing a moving dismount from Merulina, Yareli hops off spinning clockwise and lands several meters away, while creating a splashing wave for Merulina to dive forward back into the abyss.
- When dashing with Merulina, various animations play for Yareli depending on the input direction:
  - Without moving, she twirls clockwise as she lands back onto Merulina's back.
  - While moving, she holds onto Merulina as they launch forward, flipping upside down and returning upright similar to a Bullet Jump.
  - While moving backward, she recoils raising both her hands up with open palms.

Kit Interactions

- Merulina's innate K-Drive drifting momentum helps activate and sustain Yareli's Critical Flow passive.
- Yareli performs her other abilities' casting animations without stopping her movement while aboard Merulina.
- Sea Snares' casting animation is faster while aboard Merulina.
- Surging Blades costs 0 energy to cast while aboard Merulina.

Helminth

- Subsumed abilities injected into Yareli via the Helminth system cannot be cast while aboard Merulina.
  - Developers noted that due to the amount of new custom animations required for this to function properly, this interaction will remain unchanged for the foreseeable future.

Augment

- Main article: Loyal Merulina

Loyal Merulina is a Warframe Augment Mod for Yareli that disables riding Merulina in exchange for it shooting Sea Snares at enemies as it follows her.

Rank | Cooldown | Cost
0 | 5s | 6
1 | 4s | 7
2 | 3s | 8
3 | 2s | 9

- Main article: Merulina Guardian

Merulina Guardian is a Warframe Augment Mod for Yareli's Merulina that causes enemies killed while affected by Sea Snares to heal Merulina and grant increased Reload Speed and Fire Rate to secondaries for a duration.

Rank | Healing | Reload Speed/Fire Rate | Duration | Cost
0 | 5% | +50% | 8s | 6
1 | 10% | +100% | 12s | 7
2 | 15% | +150% | 16s | 8
3 | 25% | +200% | 20s | 9

Tips & Tricks

- General
  - Riding Merulina counts in Nightwave challenges involving K-Drives.

- Build Options
  - While Yareli herself is rather fragile, Merulina vastly improves her survivability. Deploying her during a fight, even when standing still, makes Yareli deceptively durable.
    - Since Yareli cannot attack with primaries or melees while on Merulina, weapons of these categories that grant active buffs or passive bonuses are very beneficial to run.
      - Amalgam Furax Body Count will passively increase the fire rate of Yareli's secondary by +45%.
      - Primary Kitguns with Pax Bolt installed can give a temporary +30% Ability Strength and Efficiency, which can both increase Merulina's health pool and make her cheaper to cast.
      - Killing an enemy while standing in Afentis's alt-fire radius will trigger the Ballistarii Might buff, providing reload speed, fire rate, recoil, and reserve ammo bonuses that will persist for 40 seconds.
  - Unlike most sources of healing, Blood Altar will work with Merulina, providing healing even over the initial total health, unless the augment Loyal Merulina is equipped.
  - Since Merulina's roll covers significantly more distance than a regular roll, Yareli is able to effectively extend the hitbox of arcanes that proc on roll.
    - Arcane Circumvents 4m radius is active during Merulina's entire roll animation.
      - Since Merulina grants Yareli 90% damage redirection, the 10,000 Overguard cap from this arcane acts as effectively 100,000 Overguard. In addition to bolstering Yareli's effective HP, this also grants her status immunity.
      - This arcane can also allow for quickly armor stripping multiple enemies grouped with Riptide.
    - Melee Careen equipped on a melee weapon will freeze enemies around Merulina's roll, providing valuable crowd control.
      - The +1.0 final critical damage bonus granted by the 10 cold procs has synergy with Yareli's passive +200% critical chance for secondaries.
      - With Shivering Contagion equipped on a primary or sentinel, the cold procs are spread to additional enemies within 6m of the initially affected enemies.
        - Frozen enemies are easier to headshot, which makes arcanes such as Arcane Pistoleer and Secondary Deadhead easy to trigger. These headshots also benefit from the additional 2x Critical Headshot multiplier, augmented by Yareli's passive and cold proc bonuses.

- Movement
  - On mouse and keyboard, steering on Merulina with mouse is much more precise than using movement keys.
    - The left and right movement keys are best used only for strafing.
  - Double-tapping the crouch key initiates a slam and increases Merulina's fall speed.
    - Merulina has significantly higher acceleration on the ground compared to in the air, so this maneuver can be used to maintain or build speed quickly.
  - Rail grinding instantly brings Merulina up to its maximum non-sprint speed.

Maximization

Loyal Merulina?
Merulina Guardian?

Merulina

For Loyal Merulina's Sea Snares, use the Sea Snares calculator.

Bugs

- Gameplay
  - Cannot replenish the magazine or gain stacks while using Ocucor with the Sentient Surge augment. However, tendrils still function.
  - Cannot trigger Arcane Pulse while aboard Merulina.
  - Magus Drive does not increase Merulina's speed.
  - Subsumed Fire Walker's fire trail will not make Yareli immune to status procs while aboard Merulina.
  - Yareli can fall through a moving elevator while riding on Merulina.
  - Yareli on Merulina can be slowed down by bumping her head on doorframes in older Tile Sets such as Corpus Outpost and Grineer Galleon as she moves through them at any speed.
  - Yareli's Critical Flow passive does not activate when falling from heights aboard Merulina, while it works when Yareli is on foot.
  - Yareli aboard Merulina is incapable of picking up Resurgence Tokens in Arbitrations without crouching.
  - In rare instances on the Corpus Ship tileset, dismounting Merulina close enough to the ceiling of some hallways can cause Yareli to be placed out of bounds.
  - Yareli aboard Merulina counts as separate unit.
    - Any affinity gained while on Merulina is shared to yourself as if an ally killed the enemy.
    - Damage numbers from procs or other delayed attacks that would have been dealt while on Merulina disappear after dismounting.
  - During an Abyssal Zone mission, picking up a Defixio and gaining the Hunter Curse while aboard Merulina will result in the curse failing to behave correctly. Neither Yareli nor Merulina will take damage from the curse while moving.
  - During an Infested Salvage mission, Yareli aboard Merulina is always considered to be outside of Vaporizor bubbles regardless of if she is inside of one or not.
  - Falling into a Transference-disrupting field such as one created by the Kuva Trokar while aboard Merulina can sometimes cause the player to become softlocked. All inputs are disabled including camera movement, the pause menu, and even opening the chat window. If enemies are present, the players' Operator/Drifter can be killed by them which will fix the bug. (More testing needed)

- Menus
  - When customizing Merulina's Appearance via the Arsenal, it does not appear properly on screen when Yareli is in Captura or Relay hubs, including Cetus, Fortuna and Necralisk.
  - Merulina can sometimes be seen leveling up and accumulating Affinity at the end of mission summary screen.

- Visuals
  - Playing as client, Yareli does not play an animation when picking up an object such as datamass or excavator power core.
    - Activating Life Support Capsules and hacking a console will trigger the latest ability cast's animation.
  - Yareli on Merulina inside Limbo's Rift Plane does not show the Rift overlay effect on the player's screen.

Mods

- Deceptive Bond
- Electromagnetic Shielding (50% damage redirection for allies)
- Shield of Shadows

Others

- Ancient Protector Specter aura (90% damage redirection)

## Damage Type Modifiers

- Main article: Damage Type Modifier

Damage Type Modifiers are a unique classification of damage reduction that is usually specific to only one type of damage. Damage modifiers stack multiplicatively with each other and other sources of damage reduction.

### Sources of Damage Type Modifiers

This section is transcluded from Damage Type Modifier § Sources of Damage Type Resistance. To change it, please edit the transcluded page.

Abilities

This section is transcluded from Caliban/Abilities/Passive. To change it, please edit the transcluded page.

Versatile and resilient, Caliban and allies within his Affinity Range gain Adaptive Armor that builds damage resistance against the highest damage type received from enemy attacks, stacking 5% per hit up to a cap of 50%. If Caliban or his allies do not receive damage for 5 seconds, their Adaptive Armor loses 2% per second until fully removed.

- Passive bonus value is displayed as a Buff icon beside Caliban's hitpoint indicators.
  - Impact, Puncture, Slash, Cold, Electricity, Heat, Toxin, Blast, Corrosive, Magnetic, Radiation, Viral, and Tau damage types stack their respective resistances separately, and will have different icons in the status bar.
- Damage over time from procs (such as Slash or Toxin for example) will not contribute nor maintain damage resistance.
- Adaptive Armor does not stack with Adaptation. The damage reduction provided to Caliban (or his allies) equipped with Adaptation will be the higher of the two values.
- Works in Archwing missions.

Mods

- Adaptation (up to -90% modifier for taken damage)
- Antitoxin (-45% damage type modifier for Toxin damage)
- Diamond Skin (-45% modifier for Radiation damage)
- Flame Repellent (-60% damage type modifier for Heat damage)
- Insulation (-60% damage type modifier for Cold damage)
- Lightning Rod (-60% damage type modifier for Electricity damage)
- Shock Absorbers (-20% damage type modifier for Impact, Puncture, and Slash damage)
- Toxin Resistance (-15% damage type modifier for Toxin damage)
- Umbral Fiber (-11% damage type modifier for Tau damage)
- Umbral Intensify (-11% damage type modifier for Tau damage)
- Umbral Vitality (-11% damage type modifier for Tau damage)
- Orgone Tuning Matrix (-15% damage type modifier for Cold, Electricity, Heat, and Toxin damage)
- Anti-Flak Plating (-20% damage type modifier for Blast damage. Only usable in Conclave)

Enemies

- Grineer Prosecutor aura (Sets damage type modifier for physical and primary elemental damage types to -100%. -85% damage type modifier for combined elemental damage types)
- Toxic Ancient (-80% damage type modifier for Toxin damage)

## Quick Thinking and Gladiator Finesse

Quick Thinking and Gladiator Finesse are mods that convert a percentage of lethal damage taken into energy drain when the player reaches 2 health. At above 100% efficiency, additional lethal damage taken will be reduced. With both mods at maxed rank equipped, your Warframe's energy pool will be 300% efficient in absorbing damage, reducing incoming damage by 66.67%.

To calculate the multiplier on incoming damage: Multiplier on incoming damage=(100)/(Net efficiency percentage)

To calculate damage reduction provided by these mods: Damage reduction percentage=(1−Multiplier on incoming damage)×100

Rank | Efficiency | Additional damage reduction | Multiplier on incoming damage
0 | 40% | -150% | 2.5x
1 | 80% | -25% | 1.25x
2 | 120% | 16.667% | 0.833x
3 | 160% | 37.5% | 0.625x
4 | 200% | 50% | 0.5x
5 | 240% | 58.333% | 0.41667x

Rank | Efficiency | Additional damage reduction | Multiplier on incoming damage
0 | 10% | -900% | 10x
1 | 20% | -400% | 5x
2 | 30% | -233.33% | 3.33x
3 | 40% | -150% | 2.5x
4 | 50% | -100% | 2x
5 | 60% | -66.67% | 1.667x

## Special Enemies and Damage Attenuation

It's taking longer than I calculated.

Need details on exact numbers and add more enemies that have some unique DR on their shields or health (separate from armor)

Certain enemies possess unique damage reduction calculations separate from armor or sources of pure damage reduction. Usually, this unique damage reduction scales based on the weapon's average damage per second (DPS) (more specifically burst DPS), sometimes excluding Critical Hits. Officially, this is referred to as adaptive damage scaling, scaling damage reduction, or damage attenuation. The game calculates DPS typically as:

- { Burst DPS =(total damage) ; ⋅(total critical multiplier if damage instance crits) ; ⋅(total fire rate or attack speed) ; ⋅(total multishot) ; ⋅(body part multipliers) }

Where damage, critical multiplier, fire rate/attack speed, and multishot is calculated after mods and buffs are applied (e.g. Octavia's Amp or Volt's Shock Trooper for damage, Sharpened Bullets for critical multiplier, Valkyr's Warcry or Gauss' Redline for fire rate/attack speed, and Split Flights for multishot).

Note that weapons with the auto-spool trigger type, like the Gorgon or Kohm, will noticeably deal less damage per damage instance as their fire rate ramps up to their maximum value.

In most cases, this scaling DR stacks multiplicatively with DR provided by the enemy's armor.

To calculate damage reduction based on DPS:

- Damage reduction percentage=(1−Damage multiplier or modifier)×100

### Archon

This section is transcluded from Archon § Damage Resistance. To change it, please edit the transcluded page.

Archons fought during Archon Hunts possess a dynamic Damage Reduction that limits damage per second to 935,000. Additionally, they possess a flat 20% reduction to all damage and a 50% reduction to status effect damage.

Currently, the enemy's damage reduction values with this "dynamic damage reduction" feature are as follows：

Enemy name | MDPT value | MDPS value
The Fragmented Suzerain | 175,000 | 300,000
The Fragmented One | 175,000 | 300,000
Archon Amar | 460,000 | 935,000
Archon Nira | 460,000 | 935,000
Archon Boreal | 460,000 | 935,000

### Damage Resistance Parameters

- Max Damage Per Trigger=MDPT=460000 ,
- Max Damage Per Second=MDPS=935000 ,
- Exponential Decay Constant=λ=2/3 ,
- ShotgunCompensation={{ 0.7, if base multishot>0 ; 1, otherwise }

### Condrix

This section is transcluded from Condrix § Damage Resistance. To change it, please edit the transcluded page.

Condrix possess DR that scales depending on your weapon's DPS excluding Critical Hits. DPS is calculated by:

- (total damage)⋅(total fire rate)⋅(total multishot)⋅(body part multipliers)

Critical Hits are applied after DR is calculated. Additionally, the average DPS is calculated using Health Modifiers and is quantized.

### Eidolons

This section is transcluded from Eidolon Teralyst § Damage Reduction. To change it, please edit the transcluded page.

Eidolons' shields and health possess Damage Attenuation based on the Eidolon's maximum health. They have a Max Damage Per Hit attenuation based on 200% of their maximum health, and a Max Damage Per Second attenuation based on 100% of their maximum health.

Eidolons possess a body part multiplier of 2x, and a critical damage bonus of 2x. The Eidolon's head possesses a 3x headshot multiplier and also benefits from the 2x critical damage bonus. However, when damaging the Eidolon's head, AOE weapons will not benefit from the 3x headshot multiplier, providing no bonus damage, and will not benefit from the 2x critical damage bonus. Body hits with AOE weapons will still benefit from the 2x body part multiplier and 2x critical damage bonus.

### Guardian Eximus

- Main article: Eximus#Guardian

Corpus Guardian Eximus enemies project an aura that have increased damage type resistance to all damage types by 90% for themselves and their allies.

### Hyekkas and Hyekka Masters

- Main article: Hyekka
- Main article: Hyekka Master

Hyekkas and Hyekka Masters resist 80% of all Heat damage.

### Juggernaut (Behemoth)

This section is transcluded from Juggernaut § Damage Reduction. To change it, please edit the transcluded page.

- The Juggernaut has an innate 90% damage reduction, and cannot have status effects applied to it. However, it has two weakpoints:
  - The first weak point is the glowing stomach located on its underside, which the Juggernaut will expose before performing its ground stomp attack. This weakpoint has a 10x damage multiplier, a 4x Critical Damage multiplier, and allows players to apply Status Effects.
  - The second weak point is the maw on its back from which the Juggernaut launches its ranged attacks. This weakpoint has a 10x damage multiplier and a 4x Critical Damage multiplier, even when closed. When open, it also allows players to apply Status Effects.
    - The Juggernaut opens this weakpoint when firing its barbs, using Charge, or during Poison Rain.
    - Vertical melee attacks (e.g. Shattering Storm's or Galeforce Dawn's Neutral combo) can hit this weakpoint.
- The Juggernaut has an additional 50% damage reduction against Area of Affect and melee attacks.
- Every other part of the Juggernaut aside from its weakpoints has a 2x Critical Damage multiplier.
- The Demolisher version of the Juggernaut possess 20% damage reduction instead of the 90% of its regular counterpart.
  - The Demolisher Juggernaut possess two boils on either side of its body. These boils have a 0.5x damage multiplier, and lack the 2x Critical Damage multiplier the other non-weakpoint body parts possess, but allows players to apply status effects to the Demolisher Juggernaut.
- The Jack O'Naut version (exclusive to the Hallowed Nightmares Tactical Alert) is immune to all damage from weapons and abilities. It can only be damaged by the Fire rings created by the explosive jack o'lantern towers that spawn in its arena.

### Kuva Thralls

A Kuva Lich's Kuva Thralls have an innate 25% damage reduction on top of their armor.

### Lephantis / Hemocyte

This section is transcluded from Lephantis § Damage Reduction. To change it, please edit the transcluded page.

Lephantis possesses Damage Attenuation that is based on 5% of its maximum health. Lephantis will spawn at lvl 30 in normal mode and lvl 125 in Steel Path. Lephantis takes 2x damage from critical hits. The Grineer head's chest weakpoint also has a 2x damage multiplier.

Calculate DPS after per-hit attenuation (MaxPeakDamageHealthPercent)
Fire Rate:
Multishot:
Critical Chance (%):
Critical Damage:
Damage:
Infested Faction Damage:
On Steel Path?

Lephantis health:88 033
Single hit:100
Average DPS:100

Heat

Lephantis

This section is transcluded from Hemocyte § Damage Reduction. To change it, please edit the transcluded page.

The Hemocyte possesses per hit Damage Attenuation that is based on 5% of the Hemocyte's maximum health.

- Incoming Damage=Damage⋅Body Part Multipliers⋅Critical Damage (if triggered)⋅any other damage multipliers
- Max Damage Per Hit=0.05⋅Maximum Health
- Attenuated Damage=(Incoming Damage⋅Max Damage Per Hit)/(Incoming Damage⋅Multishot+Max Damage Per Hit)

Additionally, the Hemocyte takes 2x damage from critical hits. The Grineer Head's chest weakspot has a 2x damage multiplier.

For example, a single critical hit from weapon with 1,000 damage, 3x critical damage, and 2 multishot would do the following damage to a level 117 Hemocyte's Grineer Head's chest weakspot:

- Incoming Damage=1,000⋅(3⋅2)⋅2=12,000
- Max Damage Per Hit=0.05⋅2,472,207=123,610
- Attenuated Damage=(12,000⋅123,610)/(12,000⋅2+123,610)=10,049 damage

Calculate DPS after per-hit attenuation (MaxPeakDamageHealthPercent)
Fire Rate:
Multishot:
Critical Chance (%):
Critical Damage:
Damage:
Infested Faction Damage:
Hemocyte has Armor?
On Steel Path?
Stage:

Hemocyte health:2 472 177
Hemocyte armor:2 649 (89.83% damage reduction)
Single hit:100
Average DPS:100

Heat

Hemocyte

The Hemocyte possesses DPS Damage Attenuation that is based on 20% of the Hemocyte's maximum health.

### Orphix

This section is transcluded from Orphix § Damage Resistance. To change it, please edit the transcluded page.

Orphix possess DR that scales depending on your weapon's DPS excluding Critical Hits. DPS is calculated by:

- (total damage)⋅(total fire rate)⋅(total multishot)⋅(body part multipliers)

Critical Hits are applied after DR is calculated. Additionally, the average DPS is calculated using Health Modifiers and is quantized.

Damage Modifier={{ 1, DPS_(Average)≤1000 ; 0.7+(300)/(DPS_(Average)), 1000<DPS_(Average)≤2500 ; 0.5+(800)/(DPS_(Average)), 2500<DPS_(Average)≤5000 ; 0.2+(2300)/(DPS_(Average)), 5000<DPS_(Average)≤10000 ; 0.02+(4100)/(DPS_(Average)), 10000<DPS_(Average) }

### Prosecutors

This section is transcluded from Guardsman § Prosecutor Variant. To change it, please edit the transcluded page.

Prosecutors are elite Guardsmen hand-picked by Councilor Vay Hek. They have a 100% chance to drop Javlok Capacitors on death.

- Prosecutors are distinguished by their elemental shield auras. There are four variants, each corresponding to one of the base elemental damage types: Heat, Cold, Electricity, and Toxin. They project an aura that grants allies a -100% Damage Type Modifier against physical and non-combined elemental damage, and a -85% modifier against combined elemental damage. Conversely, the aura grants allies a +100% Damage Type Modifier against the specific non-combined element corresponding to the Prosecutor's type.
  - All increases or decreases are multiplicative to health and shield damage type modifiers.
  - Multiple Prosecutor auras stack.
  - Void damage can also deal damage to Prosecutors of any type.
- Prosecutors are likely to spawn after alarms have been triggered.
- Prosecutors can share their immunity buff with Tenno should they be allied with the Tenno, such as when summoned through Nekros's Shadows of the Dead or during an Invasion when the player has sided with the Grineer.
- Prosecutors are considered Eximus units for all purposes (for example, dropping Carbides on the Grineer Shipyard tileset).
- Prosecutors are most commonly found in the Rescue mission Nuovo on Ceres. The Lotus will warn the Tenno of the Prosecutor's appearance. They will then be found patrolling the area near the prisoner.

### Sentients / Shadow Stalker

- Main article: Sentient#Damage Adaptation

Most Sentient enemies (and Shadow Stalker) have a damage adaptation mechanic that allows them to have damage type modifiers as well as damage reductions toward particular damage types.

### Raknoids

- Aurax Atloc Raknoids possess 80% damage reduction.
- Kyta Raknoids possess 25% damage reduction, but only on their shields.
- Scyto Raknoids possess 50% damage reduction.

### Treasurer

This section is transcluded from Treasurer § Damage Resistance. To change it, please edit the transcluded page.

Treasurers have a unique shield that possesses 99% innate Damage Reduction, as well as being impenetrable by methods that would normally bypass shields (such as Toxin damage), making them very resilient to most weapons and abilities. Unlike most shields, their shields will not recharge after being damaged. They can, however, be recharged by Shield Ospreys, even when fully depleted. Toxin procs have no effect (dealing 0 damage) while their shields are up.

Their health has an innate 98% damage reduction, despite having no armor.

## References

## Patch History

Hotfix 40.0.3 (2025-10-21)

Damage Attenuation & EHP Changes:

- Increased the MDPI (Max Damage Per Instance) on Kuva Lich, Sisters of Parvos and Technocyte Coda, so that weapons like Snipers are more effective against these foes.
- Removed Damage Attenuation from Skittergirl.
  - She now has 90% Damage Reduction, and her Base Health* has been increased from 50 to 600.
- Greatly increased the MDPI (Max Damage Per Instance) for Eidolons.
  - As stated in our Dev Workshop, our intention was to keep this fight as close to the original iteration as possible. The Time-to-Kill was a little longer than it was before, so these changes should bring this fight back to pre-The Vallis Undermind speeds.
- Increased the Techrot Babau's Base Health* from 1,500 to 10,000, and increased the Temporal Archimedea base health bonus from 1,000 to 9,000.
  - Since Damage Attenuation was removed from these enemies in 40.0.2, their time-to-kill was significantly reduced. Now, they should be a little more challenging to reflect their rare enemy status.

*As a refresher, Base Health refers to the Health Value at Level 1.

Hotfix 40.0.2 (2025-10-16)

Damage Attenuation Changes:

With our Damage Attenuation changes in The Vallis Undermind, our intention was to normalize the difficulty of boss-type enemies between groups of players. After gauging the community’s response, we recognize that our broad application of that term inadvertently made “objective-type” enemies (ex: Demolishers) harder to kill. We’re redefining our standardization of Damage Attenuation to only apply to True Bosses / HUD Health Bar enemies with our upcoming hotfix, thanks to player feedback.

- Damage Attenuation changes have been removed from regular objective enemies. As a result of this, these regular objective enemies can be one-shotted again.
- Damage Attenuation is now solely reserved for true Bosses and enemies with the HUD health bars.
- For certain enemies retaining Damage Attenuation, we have adjusted the values to allow for one-shot kills, if a player’s build is powerful enough.

Enemies that no longer have Damage Attenuation:

- Scaldra Dedicants
- Demolishers (including Necramechs)
- Deimos Jugulus
- Deimos Saxum (and Saxum Rex)
- Rogue Necramechs (Voidrig and Bonewidow)
- Amalgams
- Empyrean Units (Corpus Proxima):
  - Aurax Actinic
  - Aurax Baculus
  - Aurax Vertec
  - Numon (all variants)
  - Vambac (all variants)
  - Zerca (all variants)
- Errant Specters
- Gruzzling
- Necramite
- Sister of Parvos Hounds
- Techrot Babau
- Treasurer
- Tusk Thumpers (all variants, including Narmer)

Boss Enemies with Damage Attenuation that can be One-Shot:

- Acolytes
- Infested Oni

Our goal was to make powerful builds feel more impactful against Damage Attenuated foes, and with your continued feedback, we can ensure we achieve that together.

The team is continuing to look into other reports of bugs and feedback. Please keep it coming!

Update 40.0 (2025-10-15)

DAMAGE ATTENUATION CHANGES

Damage Attenuation is one of the tools we use to normalize the difficulty of boss-type enemies between groups of players, and its implementation has been a hot topic in the community for a while now. While meant to balance out high-powered builds, Attenuation could sometimes lead to paltry damage numbers — great to make an enemy hard to kill, but not necessarily fun for the player.

With community feedback in mind, we have some sweeping changes planned, which we have outlined below! The core of our goals is as follows: a) address outlier cases of Bosses having a very long time-to-kill as a result of of Damage Attenuation (notably in high level content), b) making player builds feel impactful against Damage Attenuated foes, and c) standardizing how Damage Attenuation applies to the majority of Boss-type enemies in Warframe. There are a few moving pieces here, so we’ll first break down the wider Attenuation changes, and then go over how we’ll be standardizing this for various enemies.

A few key terms to familiarize yourself with as we move forward:

- Damage Attenuation: a mechanic that caps the amount of damage an enemy can take. Warframe uses caps for damage per second and per instance.
- Damage Reduction: a modifier that directly reduces the damage taken by a flat amount. (ex, 50% damage reduction multiplies the final damage taken by 0.5)
  - Damage Reduction is not directly relevant to these changes, but we want to show how it works differently from Damage Attenuation.
- Max Damage Per Second (MDPS): a target cap of the amount of damage an enemy can receive per second. Sustained damage over time is reduced to avoid exceeding that target cap. Instead of explicitly applying “per second”, this mechanic works to moderate sustained damage output.
- Max Damage Per Instance (MDPI): a cap applied to the amount of damage applied in one damage instance. (ex, a sniper bullet or melee hit)
- Time-to-Kill: How long it takes a player to kill an enemy using the expected gear they’d have access to when they first encounter them.
  - This term is a simplified way for us to represent the complex layers of modifiers, damage reduction, damage attenuation, etc., that are applied to enemies, which results in the overall level of difficulty to kill them.

1 - Damage Attenuation Scaling

If you hop into a Legacyte Harvest mission in Höllvania on the live build, a few things will change depending on whether you’re on the Normal Path or Steel Path: enemies have different modifiers, squad consumables have cooldowns, and so on. One thing that stays the same is the current Max Damage Per Second (MDPS) and Max Damage Per Instance (MDPI) that the Legacyte will take.

This is because Damage Attenuation applied to the Legacyte is a flat value, regardless of its health pool. At Normal Path levels, these values can feel reasonable, but once Steel Path or even Temporal Archimedea modifiers apply, that’s where the “bullet sponge” allegations begin. At certain points, Damage Attenuation became less of a tool to balance out powerful player builds, and more so acted as a time gate to kill high-health enemies.

A careful touch is needed to embrace the power fantasy of Warframe while also ensuring high level content is not completely trivialized. In the current iteration of Damage Attenuation, we have not accomplished that goal to our satisfaction — simply put, it has created gameplay interactions that are unfun. So, the following changes are being made to address it:

- Firstly, Damage Attenuation values are now proportional to Max Health.
- Secondly, Damage Attenuation’s MDPS now applies independently between players.

Damage Attenuation in Proportion to Max Health

If we go back to the Legacyte example from earlier, players should notice a distinct difference in how Damage Attenuation applies to this enemy in both Steel Path and Temporal Archimedea missions. Instead of the MDPS and MDPI using the same values of Normal Path Legacytes, the amount of damage players can deal per second and per instance now scales based on the enemy’s Max Health*. As Max Health increases with enemy level and mission modifiers, so will the maximum damage caps from Damage Attenuation.

The result is a higher damage output from players, and a more reasonable time-to-kill! Players who invested much time and effort into their builds should feel more rewarded for their work, especially against high-level enemies with Damage Attenuation.

Our focus with this sweeping change is to establish the overall Time-To-Kill for enemies within a reasonable range, considering the equipment available to players when they are first encountered.

Since this is a significant change to how Damage Attenuation is calculated, we have increased the Health of various Bosses to balance with this new scaling mechanic. The goal is to reward players with powerful builds but still avoid one-shotting Archons. We’ll cover the Health changes in the “Standardizing Damage Attenuation” section below!

* Max Health for this calculation only uses the Health value. Overguard, Shield, and Armor values are not considered.

Independent Maximum Damage Per Second per Player

Previously, the Maximum Damage per Second (MDPS) cap in Damage Attenuation would apply squad-wide. If you have a teammate blasting their 6-forma Incarnon Form Laetum at an Archon, there’s a good chance they consistently hit those pillows before you have an opportunity to aim your gun.

With that in mind, the MDPS in Damage Attenuation will now be applied on a per-player basis. The damage output of your squadmates no longer has an impact on the efficacy of your attacks! Max Damage Per Instance has always applied per-player (due to the nature of this mechanic), so it is unchanged.

To recap our Damage Attenuation changes, a) the damage caps now scale proportionately to the enemy’s max health, and b) no longer apply squad-wide. Now, let’s move on to how we are standardizing it.

2 - Standardizing Damage Attenuation

Damage Attenuation is just one method that we use to balance player power against Boss-type enemies. Depending on whether you fight an Eidolon, a Kuva Lich, or an Archon, your damage output will be affected in different ways. These differences are often the legacy of the many hands that have worked to make Warframe over the years — decisions for new content in 2018 can eventually result in gameplay quirks that players learn to adapt to in 2025.

There is so much to learn in Warframe, and that list only grows with every update; part of maintaining a decade-long game is reducing the scope of what players need to know. With that in mind, we are replacing existing Damage Attenuation on various Boss-type enemies and standardizing them to use the same system.

Actual MDPI and MDPS values will be balanced around the content type, but enemies from Liches to Void Angels to Legacytes now all share the same attenuation mechanic. For those familiar with Archon Hunts, our new standard model is based around the Damage Attenuation in those missions.

As mentioned earlier, we are increasing Base Health* values to balance the time-to-kill for these foes. While larger health pools may increase difficulty, they also increase the Damage Attenuation caps since they now scale with max health. Our hope is that players will hit harder and their weapons will feel more satisfying, while also ensuring enemies have a reasonable time-to-kill (on both ends: avoiding one-shots, but also avoiding time-gated slogs).

Enemies using Standardized Damage Attenuation: *For simplicity’s sake, we are representing Health changes by comparing their difference in Health at Level 1, referred to as “Base Health” moving forward.

- Acolytes
  - Base Health: 5,500 (was 550)
  - Base Shields: 2,500 (was: 1,000)
- Adversaries (Kuva Lich, Sisters of Parvos, and Techocyte Coda, including Railjack Crew)
  - Since Liches and Sisters have increasing health scaling as they rank up, we have not increased their Base Health, but rather increased the health multipliers per level and per rank.
- Amalgams
- Archons (Boreal, Amar, and Nira)
- Deimos Jugulus
- Deimos Saxum (and Saxum Rex)
  - Base Health: 750 (was 550)
- Demolishers (including Necramechs)
  - Necramech Demolisher Base Health: 4,500 (was 3,000)
  - Juggernaut Demolisher Base Health: 1,000 (was 3,000)
    - Steel Path base health bonus: 2,000
- Eidolons (Teralyst, Gantulyst, and Hydrolyst)
  - Teralyst:
    - Body Base Health: 50,000 (was 9,000)
    - Radiator Base Health: 25,000 (was 2,200)
    - Base Shields: 50,000 (was 1,500)
  - Gantulyst:
    - Body Base Health: 55,000 (was 10,000)
    - Radiator Base Health: 25,000 (was 2,200)
    - Base Shields: 60,000 (was 1,800)
  - Hydrolyst:
    - Body Base Health: 65,000 (was 12,000)
    - Radiator Base Health: 25,000 (was 2,200)
    - Base Shields: 70,000 (was 2,000)
  - NOTE: This is a dramatic change from the existing damage reduction mechanics applied to Eidolons. We are taking care to ensure their time-to-kill is not disrupted, but players may see a change in the meta when killing them. Eidolon hunters, please let us know your feedback once you’ve played around with the changes.
- Empyrean Units (Corpus Proxima):
  - Aurax Actinic
    - Base Health: 1,500 (was 1,000)
    - Base Shields: 750 (was 500)
  - Aurax Baculus
    - Base Health: 300 (was 150)
    - Base Shields: 750 (was 500)
  - Aurax Vertec
    - Base Health: 1,500 (was 1,000)
    - Base Shields: 750 (was 500)
  - Numon (all variants)
    - Base Health: 750 (was 500)
    - Base Shields: 450 (was 300)
  - Vambac (all variants)
    - Base Health: 750 (was 500)
    - Base Shields: 450 (was 300)
  - Zerca (all variants)
    - Base Health: 750 (was 500)
    - Base Shields: 450 (was 300)
- Errant Specters
- Gruzzling
- Infested Oni
- Juggernaut (all variants)
  - Juggernaut:
    - Base Health: 900 (was 2,700)
    - Steel Path base health bonus: 1,800
  - Juggernaut Behemoth:
    - Base Health: 1,500 (was 4,500)
    - Steel Path base health bonus: 3,000
- Kuva Lich Thralls
- Legacyte
  - Base Health: Unchanged
  - Steel Path / Temporal Archimedea base health bonus: 7,500
- Lephantis (and Hemocyte)
  - Hemocyte Base Health: 5,000 (was 3,300)
  - Lephantis:
    - Head Base Health: 900 (was 1,200)
    - Body Base Health: 3,000 (was 1,200)
- Mocking Whispers
- Necramite
- Oraxia (Isleweaver stage)
- Protea (The Deadlock Protocol quest)
- Rogue Necramechs (Voidrig and Bonewidow)
  - Base Health: 7,500 (was 3,800)
  - Limb Base Health: 600 (was 300)
- Scaldra Dedicant
  - Base Health: 2,000 (was 1,550)
- Sister of Parvos Hounds
- Technocyte Coda Duets
- Techrot Babao
  - Base Health: 1,500 (was 1,000)
- The Fragmented (all variants)
  - Base Health: Unchanged
    - Steel Path / Deep Archimedea base health bonus: 150,000
- Treasurer
  - Base Health: 2,500 (was 100)
- Tusk Thumpers (all variants, including Narmer)
  - Tusk Thumper:
    - Base Health: 9,000 (was 3,000)
  - Tusk Thumper Bull:
    - Base Health: 12,000 (was 4,000)
  - Tusk Thumper Doma:
    - Base Health: 15,000 (was 5,000)
  - Thumper Plate Base Health: 500 (was 50)
- Void Angel (and Archimedia Revival variant)
  - Archimedia Revival Angel Base Health: 25,000 (was 12,000)
- Zealoid Prelate
  - Base Health: 9,000 (was 7,500)

Other Enemy Health Changes:

Stalker has also received some health changes as part of our enemy review, but rest assured Stalker (and his variants) do not use the new Damage Attenuation.

- Stalker:
  - Base Health: 750 (was 550)
- Shadow Stalker:
  - Base Health: 950 (was 750)
- Protector Stalker:
  - Base Health: 1,100 (was 750)
  - Base Shields: 500 (was 200), plus 2,000 Overshields

Damage Attenuation Fixes:

- Fixed Steel Path health modifiers not applying to Lephantis and the Hemocyte.

Update 35.5 (2024-03-27)

- Fixed low framerate (below 30 FPS) affecting the efficacy of Damage Attenuation.
  - A combination of low frame rate and high fire rate/damage weapons was allowing enemies with Damage Attenuation (Archons, Kuva Liches, etc.) to be quickly one-shotted. Basically, low frame rates would extend the time it took for Damage Attenuation to kick-in and ramp up in relation to the damage per second being dealt. We found that this issue was present before the changes we made to Damage Attenuation in the Abyss of Dagath update, but it only really became apparent afterwards due to the increase in maximum damage per damage instance and damage per second. So we’ve fixed this unintended interaction by ensuring frame rate has no impact on Damage Attenuation. For reassurance, this fix has not changed anything about the current intended functions of Damage Attenuation.

Update 34.0 (2023-10-18)

Archon Hunt Damage Attenuation Changes

Speaking of earning Archon Shards, Damage Attenuation (or “damage pillows”) may be a familiar mechanic for those who frequent Archon Hunts each week.

This was a hot topic, especially near the end of 2022. Since then, we’ve taken our time to assess player feedback and devise a plan to address it -- and we’re finally at a place where we can execute it.

Damage Attenuation is one tool of many to increase enemy difficulty by limiting how much damage they take from player weapons, etc. Our current form of Damage Attenuation has resulted in many weapons feeling lackluster due to the high attenuation values, and damage output was reduced significantly to balance out the post-attenuation modifiers -- meaning that Archon fights felt like a slog if players did not use a limited set of optimal builds.

This is not a favorable outcome, so we have made the following changes:

1 - Maximum Damage Caps have increased

- Maximum Damage per Damage Instance has been increased
- Maximum Damage Per Second has been increased

Our goal is to make big hits still feel like big hits, especially for low-rate-of-fire weapons. We’re able to reduce the damage cap significantly because of the next change:

2 - Modifiers now apply before Damage Attenuation

Critical Multipliers (and other modifiers) applying post-damage-cap allowed for many of the One Shot builds to function, and for full transparency, we want to prevent One Shot Archon builds as much as possible. By changing where these modifiers apply, we can increase the Damage Caps to a much less punishing level for players.

Our goals with these changes are to:

- Increase player damage output, thereby reducing the overall time to kill for Archons
- Make “big hits” feel impactful by no longer throttling them to such an extreme degree
- Encourage overall build diversity for Archon Hunts
- Reduce the ability to use one-shot builds

We’re excited to see what Archon Hunts look like for players with these changes in the live build! Now that these changes have been released, we'll be keeping a close eye on player feedback and the resulting time-to-kill for Archons to see if further iteration is needed.

Update 30.5 (2021-07-06)

Adaptive Damage Scaling Changes for Liches:

Throughout our boss design history, we have added things like diminishing returns and damage mitigation techniques like armor or damage attenuation. In the time since we’ve launched the Kuva Liches, we’ve made adjustments to how we handle player damage vs. Liches. We’ve done things like add allowing Status Effects and attenuate damage to try and create a balanced combat experience. Like many bosses in Warframe, Liches have some damage modifiers applied to them.

We found a bug in the damage attenuation code, and have fixed it and polished the attenuation for Kuva Liches.

This system generally targets the scenario of very high damage things like the Void Rig’s Arquebex vs. a Kuva Lich, a scenario that is now possible due to the final showdown being based in Railjack. When we were testing this Voidrig Vs Lichout, our Liches barely lasted a second and we realized the damage attenuation code could use some review! We found bugs to fix and things to tweak to account for these new scenarios. Our only intention is to give you a fight that lasts more than mere seconds - happy hunting and may your teamwork and gear lead you to victory! We will be closely reviewing this to ensure we strike the right balance of a fight that requires teamwork and consistent offensive gameplay to beat, but also doesn’t feel impossible. Feedback is welcome!

Damage Resistance Mod Math Changes:

The following changes occurred due to the following scenario being shared:

A player reported that combining Umbral Mods + Adaptation + Lightning Rod on any Warframe made them fully immune to all damage from the Hydrolyst Eidolon.

Prior to this discovery, we already made sure we couldn’t reach 100% Damage Resistance because that would just be excessive in all cases. You can see this in action when we capped the ‘In Air’ Damage Resistance Mods. Even though the Mods theoretically could reach 100% Damage Resistance, there is a hard cap at 90%.

In response and to avoid future oversights, we have changed the way Damage Resistance works. It now works on ‘Damage Remaining’ instead of having all the Modifiers combined and operating at once.

Example: Consider the case of: 4x 25% Damage Resistance Mods

WAS: (25% + 25% + 25% + 25%) = 100% Damage Reduction

NEW: Take 25% Less Damage = Only take 75% Damage

0.75 x 0.75 x 0.75 x 0.75 = 31.5% damage taken AKA 68.5% damage reduction

Update 29.5 (2020-11-19)

- Fixed Warframe not being vulnerable with 90% Damage Reduction after directly Transferring into your Necramech.

Hotfix 25.7.8 (2019-09-26)

- Airborne resistance from Mods is now capped at 90% to prevent stacking past 100% in some cases.
