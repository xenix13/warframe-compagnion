# Armor (wiki)
Source : https://wiki.warframe.com/w/Armor

Armor

Calculator

Armor

An example of an armored health bar

- For the Warframe Cosmetic, see Armor (Cosmetic).

Reduces damage to Health by |AMOUNT|%. Shields are not affected by Armor.—In-game Description

Armor is an attribute that reduces damage taken to health but not to shields or overguard. Not all enemies possess armor; Warframes, some Murmur, most bosses, and all Grineer do, but normal Corpus and Infested enemies do not have any. For a given Warframe, its armor value can be found in the Arsenal. Armored enemies have their base armor values listed in the Codex but this value increases when they spawn with higher levels due to Enemy Level Scaling.

In combat, enemies with more than one point of armor have their health bars displayed yellow instead of red. It is possible to strip away armor value through certain abilities or damage Status Effects, turning those enemies' health bars back to red.

## Effects

When damage is inflicted to an armored target, incoming damage is reduced by armor value according to a damage reduction formula.

- See also: Damage Calculation

### Tenno Damage Reduction Formula

The damage reduction from armor is as follows:

Tenno Damage Reduction=(Net Armor)/(Net Armor+300)

A net armor value of 300 will reduce incoming damage by 300 ÷ 600 = 50%, so only half of the weapon's damage is inflicted in total. At 600, you receive only 33% (reduction is 600 ÷ 900 = 66.6667%) of a weapon's outgoing damage. At 900 armor, inflicted damage is only 25% (reduction 900 ÷ 1200 = 75%), and so on.

### Enemy Damage Reduction Formula

For enemies using the standard NPC armor calculation, damage reduction is calculated as follows when Net Armor is no greater than 2,700:

Enemy Damage Reduction=90%⋅sqrt((Net Armor)/(2700))

Enemy level scaling normally clamps an enemy's initial armor to between 200 and 2,700. Armor removal can still reduce current armor below 200. If an enemy's Net Armor exceeds 2,700 under an exceptional condition, damage reduction instead uses:

Enemy Damage Reduction=(Net Armor)/(Net Armor+300)

When damage is reduced from armor, each damage type has a minimum damage of 1. E.g. a Braton will always do a minimum of 3 damage against an armored target regardless of how high their armor value is, as it has 3 different damage types. Non-Armor sources of damage reduction do not have such a behavior.

## Effective Health

- Main article: Health#Effective Health

Effective health is the concept that each single point of health you have actually absorbs more than one point of damage, so you effectively have more hit points than indicated. Therefore, there are two ways that armor functionality can be imagined: either as a reduction to damage, or as an increase of effective health and incoming heals.

An alternative way to think of armor transforms the above equation to the following:

Effective Health=(Nominal Health)/(1−Damage Reduction)

- Nominal Health means "health in name", referring to the Health points in your screen's upper right corner.
- Effective Health is your "health in effect", reflecting a "truer" measurement of survivability.

Or in terms of armor:

Effective Health=Nominal Health×(Net Armor+300)/(300)

Example 1: If you have 1000 Nominal Health and 100 armor, your Effective Health would be:

Damage Reduction=(Net Armor)/(Net Armor+300)=(100)/(100+300)=0.25=25%

Effective Health=(Nominal Health)/(1−Damage Reduction)=(1000)/(1−0.25)≈1,333

Or

Effective Health=Nominal Health×(Net Armor+300)/(300)=1000×(100+300)/(300)≈1,333

Example 2: If you have 1000 Nominal Health and 600 armor, your Effective Health would be:

Damage Reduction=(Net Armor)/(Net Armor+300)=(600)/(600+300)≈0.67=67%

Effective Health=(Nominal Health)/(1−Damage Reduction)=(1000)/(1−0.67)≈3,000

Or

Effective Health=Nominal Health×(Net Armor+300)/(300)=1000×(600+300)/(300)≈3,000

In-Depth Analysis
The relative increase in effective health is exactly proportional to the armor increase. Let us call E the effective health, H nominal health, A armor, and R effective health multiplier, and use ΔX to denote the discrete increase in some variable X , then: E =H/(1−Damage Reduction)=HR Now we first find the change in E as a result of a change in H , and then the change in E as a result of the change in A . The total change in E is the sum of these two changes: { ΔE =RΔH+HΔR ; =((300+A)/(300))ΔH+H(ΔA)/(300) ; =((300+A)/(300))ΔH+H/(300)ΔA } Now ignoring any increases in the nominal health (i.e. ΔH=0 ): ΔE =H/(300)ΔA Since H is a constant we end up with effective health being proportional to armor: ΔE∝ΔA Where most algebraic simplification was omitted and to make the notation cleaner, we have set: R =1/(1−Damage Reduction)=(300+A)/(300) It is also worth noting that this is only including individual, independent variations in H and A . If we were to vary them at the same time, a different and much more involved analysis has to be carried out: Let us begin by redefining our variation in the arbitrary variable X as δX . This is purely due to convention and is just a "relabeling". Given E as a function of H and A (written more compactly as E(H,A) ) we need to find δE(δH,δA) . Therefore, we carry on by considering the sum of E and its variation in terms of H and A with their respective variations and then isolating the variations { E =H(300+A)/(300) (Initial equation) ; E+δE =(H+δH)(300+(A+δA))/(300) (Substituting in the variations) ; E+δE =(H+δH)((300+A)/(300)+(δA)/(300)) (Expanding out the fraction) ; E+δE =H(300+A)/(300)+δH(300+A)/(300)+H(δA)/(300)+(δHδA)/(300) (Simplifying) ; E+δE =E+δH(300+A)/(300)+H(δA)/(300)+(δHδA)/(300) (By definition of E) ; δE =δH(300+A)/(300)+H(δA)/(300)+(δHδA)/(300) (Subtracting E from both sides) } This equation is the variation equation we wanted; it is the same as the one obtained in the first analysis but with the extra correction term (δHδA)/300 . When varying the terms independently, this term will evaluate to zero (since one of the variations would be zero) and we recover the equation from the previous analysis, and all the results that follow from it. It is good to note that at the moment, this equation is currently unnecessary for most of the applications it has in-game since the preceding equation is pretty much always sufficient. At the moment, the game has no circumstances where the nominal health is a function of its armor and vice versa, this is more for mathematical rigor.

## Increasing Armor

### Mods

- Stand United
- Armored Agility
- Steel Fiber
- Umbral Fiber
- Carnis Carapace
- Amar's Hatred
- Gladiator Aegis
- Jugulus Carapace
- Mecha Pulse
- Saxum Carapace
- Health Conversion
- Hallowed Reckoning
- Ironclad Charge
- Shepherd (Companion only)
- Link Fiber (Companion only)
- Metal Fiber (Companion only)
- Synth Fiber (Companion only)

Steel Fiber and Armored Agility increase armor value when equipped. As a percentage modifier, Warframes with higher base armor values have a higher benefit from it. Like with most other stats, armor gains from mods stack additively together before being multiplied with the Warframe's base armor:

Total Armor=Base Armor(1+Mod Multiplier)

- Mod Multiplier refers to the value on the mods equipped. It is 1.0 at max rank Steel Fiber, 0.40 at max rank Armored Agility, and 1.40 with both equipped.

### Abilities

Edit

### Atlas's Passive

This section is transcluded from Atlas/Abilities/Passive. To change it, please edit the transcluded page.

Wielding explosive power and incredible stamina, Atlas strengthens his insurmountable durability through battle. Atlas possesses various passive mechanics highlighted in the tabs below:

Strong as the mountain, Atlas is immune to Knockdown while in contact with the ground.

- Knockdown immunity does not apply while in the air.
- Does not apply to pushback effects.
- Does not prevent the recoiling effect from firing powerful Archguns such as Corvas, Velocitus, and Larkspur in non-Archwing missions.
- Works in Archwing missions.

Rubble is a pickup item unique to Atlas that drops from petrified enemies and Rumblers on death. Rubble restores Health to Atlas if he is injured; if Atlas is at full health, Rubble instead grants additional Armor that decays over time.

- Each petrified enemy and each Rumbler will drop 1 piece of Rubble that restores 50 health or provides 50 armor. Rubble will remain on the ground for 30 seconds before crumbling away if left untouched.
  - Enemies petrified by Path of Statues' rock trail, Petrify's flash, and the summoning of Rumblers are eligible to drop Rubble.
  - Petrified enemies killed by Landslide grant 75 health or armor from their dropped Rubble.
  - Rumblers that sustain damage to their health will grant less health points or bonus armor from their dropped Rubble.
  - Rubble will not grant armor if at least 1 health point is missing from Atlas' maximum health pool. Excess health points gained will not overflow into bonus armor points.
- Rubble armor is displayed in a circular gauge on the HUD above the ability icons.
  - The current number of bonus armor is shown below the gauge and will visibly subtract as bonus armor decays or add as Atlas picks up new Rubble.
  - Armor bonus is capped at 1,500 points.
  - Bonus armor decays at a rate of 5 armor points per second.
    - Decay rate is doubled when Atlas is inside a Nullifier Crewman's bubble or inside a Fog or Nul Comba and Scrambus's nullification field.
  - Upon picking up Rubble to gain bonus armor, bonus armor decay is paused for 2 seconds. Picking up Rubble to restore health points will not pause armor decay.
  - Bonus armor will not be lost if the player falls Out of Bounds, but will be lost in the event of a host migration.
  - The stone icon in the center of the gauge will enlarge or shrink depending on the amount of bonus armor stored. At 0 bonus armor, it remains a pebble; at 1,500 bonus armor, it becomes a large boulder.
  - Rock formations will appear on Atlas' body as he accumulates bonus armor.
- Rubble pickup can be vacuumed by Sentinels or the Warframe's innate vacuum radius, or fetched by Companions.
- Rubble pickups resemble a piece of stone encased in a translucent layer of reflective rock-shaped metal, which is tinted in Atlas' chosen Warframe energy color.
- Rubble pickups spawned when a petrified enemy or Rumbler dies while airborne will fall to the ground.
- The additional armor Atlas gains from Rubble affects Arcane Battery.

- Main article: Rubble Heap

Rubble Heap is a Warframe Augment Mod for Atlas' passive that makes Landslide cost no energy, increases its damage, and increases its speed when his Rubble count is above a threshold of 1400.

Rank | Damage & speed multiplier | Cost
0 | 1.25x | 6
1 | 1.5x | 7
2 | 1.75x | 8
3 | 2x | 9

This section is transcluded from Elemental Ward. To change it, please edit the transcluded page.

 | 2 50 | Elemental Ward Depending on Chroma's elemental alignment, an offensive area-of-effect is created. Chroma and its nearby allies are imbued with defensive energy. Introduced in Update 16.0 (2015-03-19) | Strength: 25 / 50 / 75 / 100 ( Heat damage per second) 15 / 20 / 30 / 55 % ( Health bonus) Duration: 10 / 15 / 20 / 25 s Range: 6 / 8 / 10 / 12 m (aura range) Misc:2 / 5 / 7 / 10 % ( Heat status chance) 5 m (burn radius) Strength: 2.5 / 3 / 5 / 10 x (damage reflection multiplier) 10 / 15 / 20 / 30 % (Shield bonus) 10 / 15 / 20 / 25 % ( Electricity status chance) 50 / 60 / 100 / 200 (minimum Electricity damage) Duration: 10 / 15 / 20 / 25 s Range: 6 / 8 / 10 / 12 m (aura range) 5 / 6 / 8 / 10 m (discharge range) Strength: 25 / 35 / 40 / 50 % ( Toxin damage chance per second) 15 / 25 / 30 / 35 % (Holster damage) Duration: 10 / 15 / 20 / 25 s 3 s (Holster damage duration) 15 / 25 / 30 / 35 % (Reload Speed bonus) Range: 6 / 8 / 10 / 12 m (aura range) Misc:5 m (poison radius) 5 % (enemy health to Toxin damage) 100 % ( Toxin status chance) Strength: 1.5 / 2 / 2.5 / 3 x (damage reflection multiplier) 25 / 70 / 90 / 145 % ( Armor bonus) 10 / 15 / 20 / 25 % ( Cold status chance) Duration: 10 / 15 / 20 / 25 s Range: 6 / 8 / 10 / 12 m (aura range)
Strength: 25 / 50 / 75 / 100 ( Heat damage per second) 15 / 20 / 30 / 55 % ( Health bonus)
Duration: 10 / 15 / 20 / 25 s
Range: 6 / 8 / 10 / 12 m (aura range)
Misc:2 / 5 / 7 / 10 % ( Heat status chance) 5 m (burn radius)
Strength: 2.5 / 3 / 5 / 10 x (damage reflection multiplier) 10 / 15 / 20 / 30 % (Shield bonus) 10 / 15 / 20 / 25 % ( Electricity status chance) 50 / 60 / 100 / 200 (minimum Electricity damage)
Duration: 10 / 15 / 20 / 25 s
Range: 6 / 8 / 10 / 12 m (aura range) 5 / 6 / 8 / 10 m (discharge range)
Strength: 25 / 35 / 40 / 50 % ( Toxin damage chance per second) 15 / 25 / 30 / 35 % (Holster damage)
Duration: 10 / 15 / 20 / 25 s 3 s (Holster damage duration) 15 / 25 / 30 / 35 % (Reload Speed bonus)
Range: 6 / 8 / 10 / 12 m (aura range)
Misc:5 m (poison radius) 5 % (enemy health to Toxin damage) 100 % ( Toxin status chance)
Strength: 1.5 / 2 / 2.5 / 3 x (damage reflection multiplier) 25 / 70 / 90 / 145 % ( Armor bonus) 10 / 15 / 20 / 25 % ( Cold status chance)
Duration: 10 / 15 / 20 / 25 s
Range: 6 / 8 / 10 / 12 m (aura range)
Subsumable to Helminth

Info

- Chroma expends 50 Energy to emit an aura of elemental energy, empowering himself and nearby allies within 6 / 8 / 10 / 12 meters for 10 / 15 / 20 / 25 seconds, providing both offensive and defensive buffs.
- Elemental Ward exhibits different effects depending on Chroma's current elemental alignment, determined by Chroma's primary emissive color or the selected element of Spectral Scream.

Heat

- Generates a flame aura around Chroma and affected allies that increases Health by 15% / 20% / 30% / 55% and inflicts 25 / 50 / 75 / 100 Heat damage per second within a radius of 5 meters with a 2% / 5% / 7% / 10% status chance. The radius of this damage effect is not increased with ability range.
  - The Health bonus stacks additively with Health modifiers such as Vitality.
    - A rank-3 Elemental Ward with Intensify and a maxed Vitality will increase Chroma's Health to ⌊370 × (1 + 1 + 0.55 × 1.3)⌋ = 1,004.
  - Damage bypasses obstacles in the environment and decreases with distance.

Electricity

- Infuses Chroma and affected allies with an electric current that increases Shields by 10% / 15% / 20% / 30% and converts incoming damage into arc discharges. An arc discharge inflicts 250% / 300% / 500% / 1,000% incoming damage as Electricity damage to a single target within 5 / 6 / 8 / 10 meters with a 10% / 15% / 20% / 25% status chance.
  - The Shield bonus stacks additively with Shield modifiers such as Redirection.
    - A rank-3 Elemental Ward with Intensify and a maxed Redirection will increase Chroma's shield capacity to ⌊370 × (1 + 1 + 0.3 × 1.3)⌋ = 884.
  - Arc damage bypasses obstacles in the environment.
  - The final damage of an arc discharge is determined by the amount of shields and/or health lost by incoming damage. For example with a maxed Intensify, losing 100 shields from a single instance of damage will produce an arc that inflicts 100 × 10 × 1.3 = 1,300 Electricity damage at rank 3 to a single target as long as it's within range.
  - No arc will be created if an incoming attack deals less than 20 damage. However, the total damage taken since the last arc creation will be tracked behind the scenes. Once a hit has been taken that pushes the total tracked damage past 20, the total tracked damage will be multiplied by the 250% / 300% / 500% / 1,000% multiplier and emitted as an arc. This means arcs will inflict a minimum of 50 / 60 / 100 / 200 Electricity damage.
  - Arcs can be triggered by certain forms of self-damage and health drain, such as Scarab Shell's health cost or Hildryn's shield costs on all of her abilities.
    - Constant health drains like Scarab Shell can rapidly discharge arcs, with the rate of discharges limited only by the minimum threshold of 20 damage taken to trigger an arc.
  - Damage from environmental hazards can also be converted into arc discharges.
  - The same enemy may be targeted multiple times in a row by successive arcs, and arcs can be produced in quick succession should Chroma and allies receive multiple instances of damage that exceed the minimum threshold.

Toxin

- Emits an aura of noxious fumes around Chroma and affected allies that increases Reload Speed by 15% / 25% / 30% / 35%, as well as weapon damage when Holstering by 15% / 25% / 30% / 35% for 3 seconds. Every 2 seconds, each enemy within 5 meters has a 25% / 35% / 40% / 50% (capped at 100%) chance to be dealt 5% of their maximum health as Toxin damage with a guaranteed Toxin status proc.
  - The Toxin damage will only be applied to an enemy if it is not already affected by a Toxin proc, but can occur as soon as an existing Toxin proc expires. As such, its effect cannot stack with itself but can refresh itself every 8 seconds.
  - Damage bypasses obstacles in the environment and does not decrease with distance.
  - Holster bonus damage is additive with Vex Armor's Fury and mods like Serration.

Cold

- Encases Chroma and affected allies in a layer of frost that increases Armor by 25% / 70% / 90% / 145% and creates an ice shield that reflects incoming attacks back to their source. Reflected damage is converted to Cold damage and multiplied by 150% / 200% / 250% / 300% and has a 10% / 15% / 20% / 25% status chance.
  - The Armor bonus stacks additively with Armor modifiers such as Steel Fiber.
    - A rank-3 Elemental Ward with Intensify and a maxed Steel Fiber will increase Chroma's Armor to ⌊370 × (1 + 1 + 1.45 × (1 + 0.3))⌋ = 1,437.
  - Incoming hitscan and non-hitscan projectiles are physically redirected after hitting Chroma. As such, obstacles in the environment can prevent reflected damage from hitting enemies.
  - Hitscan projectiles are reflected directly to the source enemy regardless of distance from Chroma.
  - Non-hitscan projectiles are reflected in the direction of the source enemy.
  - Does not prevent damage to Chroma aside from the additional Armor bonus and other damage reduction rules; Chroma will be hit normally before reflecting weapons fire.
  - Reflected projectiles count as Unattributed Damage for the sake of proccing select weapon passives.
    - This means that on-kill effects like Dual Ichor's Incarnon Clouds & Kitgun's effects will work when enemies are killed by Melee Influence and Pax Seeker respectively.

- Elemental Auras of any type from two or more Chromas do not stack and only the first aura will apply its benefits as long as the player is within buff range. For example, two Heat auras do not increase damage nor health values, and possessing a Heat aura will negate receiving a Cold aura.
- Has a casting delay of 1 second. The animation interrupts movement and other actions.
- Elemental Ward cannot be recast while active.
- Elemental Ward does not work on Nekros's Shadows or Arbitration Operative.

Helminth

- Subsuming Chroma to the Helminth will offer Elemental Ward and its augments to be used by other Warframes. The Ward's effects are determined by the Warframe's primary emission color.

Augment

- Main article: Everlasting Ward

Everlasting Ward is a Warframe Augment Mod for Chroma that allows allies to retain Elemental Ward's effects upon moving out of its range, lasting for a percentage of Elemental Ward's remaining duration.

Rank | Duration | Cost
0 | 50% | 6
1 | 65% | 7
2 | 80% | 8
3 | 100% | 9

Tips & Tricks

Heat

- In a pinch, the bonus Health provided by the Ward can be used as a quick heal, as the Health granted is automatically added to your remaining health and is not reduced from your remaining health when Elemental Ward wears off.
- The Ward is capable of damaging containers and hazards, albeit fairly slowly. Combining Elemental Ward with Spectral Scream and range mods will make for a useful farming tool so long as you have the energy to maintain it.

Electricity

- Can be used to great effect on Survival and Exterminate missions where enemies approach you from all directions and are often difficult to locate or target. At maximum Ability Strength, the damage reflected can easily finish off weaker enemies and potentially stun any survivors.

Toxin

- Works very well with weapons that require you to reload frequently or have long reload times.
- Its damage increase is considered as a Universal damage increase, same as Vex Armor and Arcane Arachne
- Can reduce recharge delay for Cycron or a Kitgun equipped with Pax Charge, however, it does not affect recharge rate.
- The Toxin proc can by replicated by Sickening Pulse and Melee Afflictions. When the initial Toxin proc expires, any additional Toxin procs created by Sickening Pulse will deal 1 Toxin damage per tick.

Cold

- Properly modded, a Cold-oriented Ward can provide an armor bonus high enough that can counteract the armor penalty generated when casting Effigy.
- The damage reflection is calculated using the damage before any damage reduction.

Maximization

Elemental Ward

Bugs

- Allies who enter, leave, then re-enter the radius of Heat-oriented Ward will not regain the buff on the same cast of Elemental Ward. This results in an empty space where the bonus health should have been, even if they took no damage at all.
  - This causes Medi-Ray and other healing abilities to attempt to heal the player, but if the player gets out of Elemental Ward's range, their health will return to normal again, wasting the health restored in the process.
- The in-game UI shows the armor bonus from the Cold aura as a flat bonus rather than a percentage.

This section is transcluded from Vex Armor. To change it, please edit the transcluded page.

 | 3 75 | Vex Armor Chroma fortifies squad Armor when his Shields are damaged or he kills an enemy with a melee weapon. He increases squad Weapon Damage when he loses Health or he kills an enemy with a ranged weapon, double the effect on weak point kills. Introduced in Update 16.0 (2015-03-19) | Strength:0.5 / 0.625 / 0.75 / 0.875 %/SP (Scorn armor bonus per shield point lost) 7 / 10 / 12 / 15% (Scorn armor bonus per melee weapon kill) 200 / 250 / 300 / 350 % (Scorn max armor bonus) 2 / 2.25 / 2.5 / 2.75 %/HP (Fury damage bonus per health point lost) 7 / 10 / 12 / 15% (Fury damage bonus per ranged weapon kill) 200 / 225 / 250 / 275 % (Fury max damage bonus)
Duration:10 / 15 / 20 / 25 s
Range:8 / 10 / 15 / 18 m

Info

- Chroma expends 75 Energy and enters a state of primal rage, sustaining an Armor and damage buffing aura with a radius of 8 / 10 / 15 / 18 meters for 10 / 15 / 20 / 25 seconds. While active, Chroma and his allies within aura range gain the Scorn armor buff once Chroma's Shields are hit or performs a melee kill, and the Fury damage buff once his Health is damaged or performs a ranged weapon kill.
  - Scorn increases Warframe Armor by 0.5% / 0.625% / 0.75% / 0.875% for every point of shields lost or 7% / 10% / 12% / 15% per melee kill, up to a maximum of 200% / 250% / 300% / 350%.
  - Fury increases weapon and Chroma's abilities' base damage by 2% / 2.25% / 2.5% / 2.75% for every point of health lost or 7% / 10% / 12% / 15% per ranged weapon kill (doubled for weakspot kills), up to a maximum of 200% / 225% / 250% / 275%.
  - Scorn, Fury, and conversion percentages are linearly affected by Ability Strength.
    - E.g., with Intensify, Steel Fiber and maximum Scorn at rank 3, Chroma's armor will be at: Base Armor × (1 + Armor Mods + Scorn Modifier × (1 + Strength Mods)) = 370 × (1 + 1 + 3.5 × (1 + 0.3)) = 2,423.5.
    - E.g., with Intensify, Serration and maximum Fury at rank 3, a weapon with 100 base damage will be at: Base Damage × (1 + Damage Mods + Fury Modifier × (1 + Strength Mods)) = 100 × (1 + 1.65 + 2.75 × (1 + 0.3)) = 622.5.
    - Both Scorn and Fury are additive multipliers that function the same as (and add together with) mods like Steel Fiber and base-damage-increasing mods like Serration. If these mods are present, all the multipliers are added together before any further calculations such as elemental damage mods, critical hit mods, or multishot mods.
  - Scorn and Fury are tracked from 0% to their maximum increase in the HUD next to Chroma's shield and health indicators.
    - Scorn and Fury will gradually increase each time shields or health are hit, and each time Chroma gets a melee or ranged weapon kill, until they reach their maximum percentages. 400 shield points must be lost to maximize Scorn, and 100 health points must be lost to maximize Fury.
    - Alternatively, 24 Enemies must be killed with Melee to maximize Scorn, and 19 Enemies must be killed with Ranged Weapons to maximize Fury.
  - Hits on overshields count towards Scorn accumulation.
  - Shield drain from a Hijack payload counts towards Scorn accumulation.
  - Multiple Chromas' Scorn and Fury buffs will stack together.
- Applies once additively with Pressure Point effects and once multiplicitively on Exodia Contagion and glaive explosions.
- Casting Vex Armor is a One-Handed Action. As such, it can be used while performing various maneuvers and actions without interruption.
- Vex Armor can be recast while active, retaining the existing buffs.
  - When recast with a higher power strength than the current active buff, the max Scorn and Fury limits will only be increased if Chroma has not already reached their respective limits.
  - E.g., If Vex Armor is casted with 100% power strength, then recast while it's still active with the Energy Conversion buff, the Scorn and Fury buffs max limit will be increased to 525% (350 * 1.5) and 412% (275 * 1.5) only if the buffs weren't at the existing limit of 350% and 275% respectively. If Scorn has reached the limit but Fury has not when recast with a higher power strength, then only Fury will benefit from the increased power strength, and vice versa.

Kit Interactions

- Spectral Scream and other abilities will increase the Scorn buff on kills. The Fury aspect of Vex Armor boosts the damage output of Spectral Scream, Effigy, and other abilities that scale from weapon damage increases.
- Effigy will only maintain the damage increase from Fury so long as Chroma's Effigy is within range of Vex Armor.

Augment

- Main article: Guardian Armor

Guardian Armor is a Warframe Augment Mod for Chroma's Vex Armor that provides Damage Reduction to allies within Affinity Range while causing their kills to heal Chroma.

Rank | Damage Reduction | Health Regeneration Over 3s | Added Duration | Cost
0 | 75% | 2% | 1s | 6
1 | 75% | 3% | 1s | 7
2 | 75% | 4% | 1s | 8
3 | 75% | 5% | 1s | 9

- Main article: Vexing Retaliation

Vexing Retaliation is a PvE Warframe Augment for Chroma that makes Vex Armor detonate an area-of-effect attack upon receiving 150 incoming damage, dealing procs on enemies.

Rank | Range | Cost
0 | 4m | 6
1 | 5m | 7
2 | 7m | 8
3 | 9m | 9

Tips & Tricks

- Equipping a rank 4 or higher Vigor mod will allow you to maximize Scorn armor bonus without requiring shields to recharge, as well as provide additional health.
- Using an electric element Elemental Ward will allow you to maximize the Scorn armor bonus without having to equip any mods increasing your shields.
- Equipping a Decaying Dragon Key to lower your shields can increase the likelihood of health damage at the loss of some of the Scorn Armor bonus due to the reduction of your shields.
- Using Energy to Shield conversion mods, like Brief Respite and Augur mod set effect, to generate shields/overshields when casting Vex Armor will help you maximize the Scorn armor bonus without having to equip any mods increasing your shields.
- Armor increase applies to defense objectives.
- To take full advantage of bonuses to Ability Strength that you gain after stacking Fury and Scorn to their respective maximums (e.g. Molt Augmented) while using the Guardian Armor augment (which can make it impossible for Vex Armor to end naturally), try jumping into a pit, entering a Nullifier Crewman bubble, or intentionally dying and reviving. This will remove all of your buffs, allowing you to recast Vex Armor with the higher maximum values provided by your increased Ability Strength.

Maximization

Guardian Armor?
Vexing Retaliation?

Vex Armor
Scorn gained from damage: | %/ Shield
Scorn gained from kills: | %/melee kill
Fury gained from damage: | %/ Health
Fury gained from kills: | %/gun kill
Fury gained from Weak Point kills: | %/gun Weak Point kill
Health restoration: | %/3s

Edit

### Frost's Passive

This section is transcluded from Frost/Abilities/Passive. To change it, please edit the transcluded page.

Frost's abilities have their Cold status effect duration increased by 100%. Frost's Fortifying Freeze passive increases his Armor by 50 per enemy afflicted by a Cold status effect within Affinity Range.

- The armor buff works in Archwing missions.

- Main article: Biting Frost

Biting Frost is a Warframe Augment Mod for Frost's passive, gaining increased Critical Chance and Critical Damage on enemies frozen by 10 Cold status effects.

Rank | Crit Chance | Crit Damage | Cost
0 | +130% | +130% | 6
1 | +150% | +150% | 7
2 | +175% | +175% | 8
3 | +200% | +200% | 9

Edit

### Grendel's Passive

This section is transcluded from Grendel/Abilities/Passive. To change it, please edit the transcluded page.

Devouring his prey whole, Grendel slowly digests the enemies he swallows via Feast. Each enemy still alive in Grendel's belly passively grants him 250 Armor, to a maximum of 1,250 bonus armor at the 5 enemy cap.

- Passive bonus value is displayed above Grendel's ability icons.
- Gourmand provides an additional 150 armor bonus per enemy at max rank to Grendel's passive, increasing the armor bonus to 400 per enemy and the total armor bonus to 2,000 at enemy cap.
- Armor bonus is added after armor mods such as Steel Fiber. For example, Grendel with a rank 10 Steel Fiber and one enemy alive in his belly will have Total armor = (350 × (1 + 1.1)) + 250 = 985
- Armor bonus adds or subtracts depending on the number of enemies currently residing in Grendel's stomach.

- Main article: Gastroparesis

Gastroparesis is a Warframe Augment Mod for Grendel's passive that grants an Extra Hit of Gas damage to Primary and Secondary Weapons for each consumed enemy.

Rank | Gas Damage Per Enemy | Cost
0 | 6% | 6
1 | 9% | 7
2 | 12% | 8
3 | 15% | 9

This section is transcluded from Parasitic Armor. To change it, please edit the transcluded page.

 | N/A 50 | Parasitic Armor Sacrifice Shields to reinforce Armor for a period of time. Introduced in Update 30.5 (2021-07-06) | Strength:25 / 50 / 75 / 100 % (Shields to Armor conversion)
Duration:10 s / 15 s / 20 s / 25 s
Range:N/A
Subsumable to Helminth

Info

- Expend 50Energy to sacrifice Shield to increase Armor value by 25% / 50% / 75% / 100% of maximum Shield capacity for 10 / 15 / 20 / 25 seconds.
  - Armor gain is only based on the maximum Shield capacity upon cast. Current Shield value is irrelevant, casting at 0 Shields or full Shields will yield the same result.
    - For example, a Warframe with 300 Max Shields and 200% Ability Strength will gain 600 armor from casting the ability.
    - Shield Capacity increases from any source (e.g. Shield Charger, Haven, and Elemental Ward) can increase the Armor gain.
    - Overshields do not contribute to Armor gain.
- Completely disables Shields for the duration of the ability, leaving Health exposed and removing the ability to use Shield Gating.
  - Also changes Hijack's Shield drain to Health drain.
- Can be recast to cancel early.
  - Because of the recast mechanic, can be used to selectively allow conversion through Hunter Adrenaline and Rage. This allows it to work with ally-provided Overguard like it would with Shield-less Warframes like Nidus, Inaros, and Kullervo.
- The gained Armor is not increased by mods such as Steel Fiber, and acts as a flat increase to your total Armor.
  - For example: Excalibur has 240 base Armor and 370 base Shields at rank 30. If they have Steel Fiber equipped with no increase to maximum shields or ability strength, they will have (240 * 2) + 370 = 850 Armor.

Tips & Tricks

- Arcane Expertise strongly synergizes with Parasitic Armor, giving the ability quadratic scaling with Ability Strength, as strength will now increase both max Shields and the Armor multiplier from those shields.

Maximization

Parasitic Armor

This section is transcluded from Plunder. To change it, please edit the transcluded page.

 | 3 75 | Plunder Plunder Armor from nearby enemies and increase Corrosive Damage on your Abilities and weapons. Enemies affected by Corrosive Status offer a greater increase. Introduced in Update 34.0 (2023-10-18) | Strength:20 / 25 / 30 / 40 (armor per enemy) 20 / 25 / 30 / 40 (armor per Corrosive status) 750 (armor cap) 5% / 6% / 7.5% / 10% ( Corrosive bonus damage per enemy) 5% / 6% / 7.5% / 10% ( Corrosive bonus damage per enemy per Corrosive status) 200% ( Corrosive bonus damage cap)
Duration:10 / 15 / 20 / 25 s (duration)
Range:25 m (range)

Info

- Hydroid expends 75 energy to siphon the armor from all on-screen enemies within 25 meters, Staggering them and consuming any active Corrosive status to permanently remove their armor. For 10 / 15 / 20 / 25 seconds, Hydroid gains a 20 / 25 / 30 / 40 bonus armor per enemy and per consumed Corrosive status effect to a cap of 750 bonus armor, and a Corrosive damage bonus to all abilities and weapons by 5% / 6% / 7.5% / 10% per enemy and per consumed Corrosive status effect to a cap of 200% Corrosive damage bonus.
  - Does not require Line of Sight from Hydroid; enemies only need to be within view of the camera to be affected.
    - An enemy that has line of sight but is off-screen will not be hit.
  - While the bonus is active, a stylized armor and damage bonus counter appears above the ability icons.
  - If Plunder affects enemies on recast, the bonus values are replaced by the new values. If no enemies are affected, the bonus values will not change but the duration will not be refreshed.
  - Damage increase does not apply to Helminth infused abilities.

Kit Interactions

- Passive allows 10 Corrosive stacks to fully and permanently remove all enemy armor.
- Tempest Barrage, Tidal Surge, and Tentacle Swarm all inflict Corrosive status for Plunder to apply its effects.
- Plunder's Corrosive damage buff increases the damage of Hydroid's other abilities.

Augment

- Main article: Rousing Plunder

Rousing Plunder is a Warframe Augment Mod for Hydroid that allows Plunder to heal Hydroid and his allies within Affinity Range, and increases the Corrosive damage and armor bonus from Plunder.

Rank | Health Restore | Corrosive Damage and Armor Increase | Cost
0 | 20 | 20% | 6
1 | 30 | 30% | 7
2 | 40 | 40% | 8
3 | 50 | 50% | 9

Maximization

Rousing Plunder?

Plunder

This section is transcluded from Scarab Shell. To change it, please edit the transcluded page.

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

This section is transcluded from Renewal. To change it, please edit the transcluded page.

 | 3 25 +3.5/s | Renewal Generates a protective aura that grants bonus Armor to Oberon and his allies and restores allies' Health over time. Healing is doubled while within the radius of Hallowed Ground. Introduced in Update 11.5 (2013-12-19) | Strength:20% / 30% / 40% / 50% (armor buff) 50 / 75 / 100 / 125 (initial heal) 15 / 20 / 25 / 40 (health per second)
Duration:20% / 25% / 35% / 45% (bleedout slow)
Range:N/A
Misc: 100% (armor buff cap) 2x (ally armor buff) 90% (bleedout slow cap)

Info

- Oberon expends 25 energy to channel a blessed field, granting Iron Renewal to himself and allies within Affinity Range, granting the following effects:
  - Oberon and allies are immediately healed for 50 / 75 / 100 / 125 Health, then regenerate 15 / 20 / 25 / 40 health per second. When fully healed, Oberon and allied units are cleansed of all Status Effects.
    - Health restore for NPCs is reduced to 5 / 6.7 / 8.3 / 13.3 health per second.
    - This does not grant Status Immunity, Oberon can still be Staggered.
  - Oberon has his current Armor increased by 20% / 30% / 40% / 50%, while allies are granted 2x the armor Oberon gained.
    - Armor increase is applied after all other armor buffs.
    - Armor buff changes dynamically based on Oberon's current armor, rather than snapshotting his armor value on cast.
    - Armor buff is capped at 100% at 200% Ability Strength.
  - Downed allies (including Oberon) have their Bleedout timer slowed by 20% / 25% / 35% / 45%.
    - Allies will have their bleedout timer extended or reduced even if they are already incapacitated when Renewal starts/stops affecting them.
    - Bleedout slow is capped at 90% at 200% Ability Duration.
  - Renewal consumes 3.5 energy per second while active. Renewal will remain active until Oberon's energy is depleted or the ability is deactivated by pressing the ability key again.
  - Oberon cannot replenish energy using Energy Vampire, Rally Point, Rift Plane's innate energy regeneration, Squad Energy Restores, Energy Siphon, Energy Nexus, Dreamer's Bond, and/or Wellspring while Renewal is active.
    - Energy Orbs, Death Orb's energy restores, Rage, Hunter Adrenaline, Spellbound Harvest, Syndicate Radial Effects, Arcane Energize, and Emergence Dissipate's Energy Motes can still replenish Oberon's energy while Renewal is active.
  - While active, Renewal will remain on allies even if they move out of range.
  - If allies lose Renewal (e.g. from Death or Nullifier Crewman bubbles), they can regain it upon re-entering Oberon's Affinity Range. However, if Oberon himself enters a nullifier field or falls Out of Bounds, Renewal will be dispelled from the entire squad.
- Allies affected by Renewal include all Warframes, Companions, Eidolon Lures, summoned allied units such as Specters, allied Invasion units, Hostages, Kavor Defectors, Sortie and Arbitrations Defense Operatives, and Defense Objects.
  - Does not affect Mirror Defense objects.
- Does not stack with Renewals from other Oberon players, only the buff with the highest armor will apply.

Kit Interactions

- Renewal's Health restore per second is multiplied by 2x when standing on Hallowed Ground.
- Renewal can multiply and share bonus Armor from Reckoning and Hallowed Reckoning.

Augment

- Main article: Phoenix Renewal

Phoenix Renewal is a Warframe Augment Mod for Oberon's Renewal that prevents affected players from entering Bleedout upon receiving fatal damage, becoming healed for a percentage of their health and are granted 5 seconds of Invulnerability with a 60 second cooldown.

Rank | Health Restored | Invulnerability | Cooldown | Cost
0 | 20% | 5s | 60s | 6
1 | 25% | 5s | 60s | 7
2 | 35% | 5s | 60s | 8
3 | 50% | 5s | 60s | 9

Tips & Tricks

- Bonus Armor from Renewal provides Damage Reduction to Oberon and his allies.
  - Armor can be diminished or bypassed with Status Effects - namely Ignite, Corrosion, and Bleed. However, Oberon protects himself and allies using Hallowed Ground or Renewal.
  - Armor stacks multiplicatively with DR abilities and mods, but unlike them - Armor has no hard limit. Here are some DR examples following the formula for Tenno:
    1. 1350 current Armor: (1350 * 2) / (1350 * 2 + 300) =90% DR. Equivalent to Splinter Storm, original Self Portrait, Desolate Hands, etc.
    2. 5850 current Armor: (5850 * 2) / (5850 * 2 + 300) =97.5% DR. Equivalent to any 90% DR ability + subsumed Self Portrait.
      - Four times stronger than example n. 1, and currently the highest amount of team-wide DR achievable by any single frame besides Oberon.
    3. 14850 current Armor: (14850 * 2) / (14850 * 2 + 300) =99% DR. Equivalent to 2 Citrines. Note that Preserving Shell can only affect Warframes, which is not the case for Renewal.
      - Ten times stronger than example n. 1, probably achievable solo with a very specialized build.
    4. 5850 current Armor (n. 2) + subsumed Self Portrait (75% DR): 1 - (1 - 97.5%) * (1 - 75%) =99.375% DR. Hard to make a sensible comparison.
      - Sixteen times stronger than example n. 1, achievable solo with a mid-game build.
      - Oberon Prime at rank 30 has 465 Health, with this much DR he will have 465 / (1 - 99.375%) =74,400 Effective Health.
- Use Fosfor Blau, Fosfor Rahd, or Mending Unity before casting, to increase the range of this ability.
- Renewal's added Armor affects Primary Bulwark (725 to max), and Arcane Battery (1500 to max).
- Use Mecha Pulse, or Parasitic Armor to generate enormous amounts of Armor that will be multiplied and shared by Renewal. Flat Armor bonuses (e.g. Health Conversion, Azure Archon Shard) are also recommended.
- Using the slow Bleedout, Oberon and allied players can recover without spending a revive, by shooting Health Orbs with Mending Shot.

Maximization

Phoenix Renewal?
Current Armor:

Renewal

This section is transcluded from Reckoning. To change it, please edit the transcluded page.

 | 4 100 | Reckoning Lifts enemies into the air and then hurls them down with conviction, removing their Armor. Enemies hit by this ability will grant Oberon additional Armor and have a chance to spawn a Health Orb when they die. Introduced in Update 11.5 (2013-12-19) | Strength:10% / 20% / 30% / 60% (armor reduction) 6000 / 6500 / 7000 / 7500 ( Radiation damage) 450 / 550 / 650 / 750 (damage per Radiation status effect) 4 / 6 / 8 / 10 (bonus armor per enemy) 2 / 3 / 4 / 5 (bonus armor per Radiation status effect)
Duration:15 / 20 / 25 / 30 s (bonus armor duration)
Range:8 / 10 / 12 / 15 m (cast radius)
Misc: 25% / 35% / 45% / 50% (health orb chance) 1000 (bonus armor cap)

Info

- Oberon expends 100 energy to lift all enemies within 8 / 10 / 12 / 15 meters and in direct Line of Sight up into the air and violently slam them to the ground, permanently reducing their Armor by 10% / 20% / 30% / 60% before dealing 6000 / 6500 / 7000 / 7,500 Radiation damage, plus an additional 450 / 550 / 650 / 750 damage per Radiation Status Effect.
  - Applies Radiation and Knockdown procs.
  - An enemy hit by Reckoning and then killed from any source has a 25% / 35% / 45% / 50% chance of spawning a Health Orb.
  - Oberon gains 4 / 6 / 8 / 10 Armor per enemy hit plus 2 / 3 / 4 / 5 Armor per Radiation proc, up to a maximum of 1000 bonus Armor, for 15 / 20 / 25 / 30 seconds.
    - If Reckoning affects enemies on recast, the bonus armor values are replaced by the new values, otherwise the bonus values will not change and the duration will not be refreshed.
  - Enemy armor is fully removed at 167% Ability Strength.

Kit Interactions

- Increased Health Orb generation provides stacks for Oberon's Righteous Negation.
- Smite instantly applies maximum Radiation procs to its target, maximizing the damage the target will take from Reckoning.
- Smite Infusion adds Radiation damage to your weapon, allowing your weapon attacks to apply status procs that will boost Reckoning's damage.
- Hallowed Ground and Hallowed Reckoning rapidly apply Radiation procs to boost Reckoning's damage.
- Bonus Armor can be multiplied and shared with Renewal.

Augment

- Main article: Hallowed Reckoning

Hallowed Reckoning is a Warframe Augment Mod for Oberon's Reckoning that makes enemies hit drop patches on the ground, dealing Radiation damage over time to enemies and providing armor to allies standing on them with a brief grace period upon stepping off. It also passively increases Reckoning's range.

Rank | Ability Range | Radiation Damage per second | Armor Bonus | Radius | Duration | Armor Bonus Grace Period | Cost
0 | +40% | 150 | 150 | 1.5m | 7s | 3s | 6
1 | +40% | 200 | 180 | 2m | 8s | 3s | 7
2 | +40% | 250 | 210 | 2.5m | 9s | 3s | 8
3 | +40% | 300 | 250 | 3m | 10s | 3s | 9

- Main article: Defiled Reckoning

Defiled Reckoning is a Conclave-exclusive Warframe Augment Mod for Oberon's Reckoning that makes Health Orbs created by kills from Reckoning temporarily invisible to, and unusable by, enemies.

Rank | Duration | Cost
0 | 3s | 6
1 | 5s | 7
2 | 8s | 8
3 | 10s | 9

Tips & Tricks

- With one player using Corrosive Projection, 100% armor strip can be achieved at 137% Ability Strength.
- Use Reckoning when surrounded by a large group of enemies to maximize its offensive effects and health orb generation.
  - Health Orb generation synergizes greatly with Equilibrium, Health Conversion, and Arcane Blessing.
- Equip Hallowed Reckoning and Arcane Universal Fallout to leave zones generating Universal Orbs (works on Arbitration Shield Drones).

Maximization

Hallowed Reckoning?

Reckoning
Added Radiation damage: | / Confusion stack
Added Armor bonus: | / Confusion stack

This section is transcluded from Metronome. To change it, please edit the transcluded page.

 | 3 75 | Metronome Grants buffs to those who consistently perform actions in time to Octavia's music. Timed jumps offer the Vivace speed buff. Crouching on the beat grants cloaking with the Nocturne buff. Firing rhythmically bestows Opera multishot buff. Timed melee swings give the Forte damage buff. Introduced in Update 20.0 (2017-03-24) | Strength:10 / 15 / 20 / 35 % (armor bonus) 10 / 15 / 20 / 30 % (speed bonus) 12 / 20 / 25 / 30 % (multishot bonus) 20 / 25 / 25 / 30 % (melee damage bonus)
Duration:8 / 12 / 16 / 20 s (ability duration) 5 / 8 / 12 / 15 s (buff duration)
Range:6 / 8 / 10 / 12 m

Info

- Octavia expends 75 energy to produce a melodic musical aura with a radius of 6 / 8 / 10 / 12 meters for 8 / 12 / 16 / 20 seconds. Octavia and her allies gain an 10% / 15% / 20% / 35% Armor bonus while inside the melodic aura.
  - Metronome's music is in tune with the Melody section of the Mandachord, drawing from the preset musical notes to determine the melodic aura's note intervals.
  - While the player and allies can hear the melody, Metronome's aura is considered silent to enemies.
- While inside the melodic aura, Octavia and her allies can perform specific actions in sync to the melodic music to gain various Sync Buffs that can be active simultaneously:

How to Synchronize with Metronome:

- Each line of Melody notes is visually represented as a concentric ring of light, which begins at the edge of the melodic aura and shrinks toward Octavia’s feet, where the ring disappears as the sound of the notes are played.
- In order to gain buffs, players must time their actions to sync with the moment a concentric ring is centered on Octavia, as the sound of the notes are played. A flash of light will appear below the player upon a successful sync.
  - Synchronize percentages are listed between 0% and 100%, and will raise or lower depending on the player's timing. Once the percentage reaches 100%, the player gains the corresponding buff.
  - Synchronize percentage is displayed as an icon with the current stored percentage beside the health and shield indicators on the HUD. Once synchronized, the corresponding buff icon will also be displayed with the remaining buff duration beneath and bonus percentage at the top-right of the icon.
  - Each player must perform actions individually to gain buffs. Sync buffs are gained per-player and are not shared between allies in range.
  - If a player does not perform an action when the ring disappears, their existing synchronize percentage does not decrease. however, if they do perform an action at the wrong time, their synchronize percentage resets; meaning that players can skip certain beats and focus on precision if they cannot keep up with the Mandachord's rapid pace. This is particularly important for weapons with low or high fire rate / attack speed and with the Vivace (movement speed) buff.
- The amount of synchronize percentage gained for a correctly timed action is based on the number of melody beats (beats with at least one melody note) within 8 beats of the action, and how close those melody beats are. Correctly timed actions on tightly packed melody beats will yield significantly less synchronize percentage compared to melody beats that are spread far apart.
  - With no melody beats on the 8 beats before or after a correctly timed action, the maximum synchronize percentage will be gained.
  - Multiple melody beats within 8 beats of each other will reduce the synchronize percentage gained on each of those beats, with the reduction being greater the closer the beats are to each other.
  - Having multiple melody notes on the same beat has no effect on the synchronize percentage gained.
- Mistiming an action will reduce the current synchronize percentage by 80% of the amount that would be gained from a correctly timed action. For example, if a correctly timed action would give 50% synchronize percentage, a mistimed action would instead reduce it by 40%.
  - With extremely spaced apart melody beats, the reduction can actually vary from about 75% to 85%. Mistimed actions that are close to a melody beat will give a smaller penalty than mistimed actions far away from one.
- The amount of notes on one line of the Melody section on the Mandachord determines the brightness of the concentric rings.

- By synchronizing with jumps (default Space ), Octavia and her allies can gain the Vivace buff which increases Movement Speed by 10% / 15% / 20% / 30% for 5 / 8 / 12 / 15 seconds.
  - A correctly timed action will yield 18% - 76% synchronize percentage towards activating the buff, based on the number and spacing of melody beats within 8 beats of the action.
- Double jump (default press Space twice), wall climb (face wall and press Space ), and wall jump (face wall + W + Space ) can also be used to synchronize.

- By synchronizing with crouching (default Ctrl ) or sliding (default W + Ctrl ), Octavia and her allies can gain the Nocturne buff which grants them and their Companion Invisible for 5 / 8 / 12 / 15 seconds.
  - A correctly timed action will yield 18% - 76% synchronize percentage towards activating the buff, based on the number and spacing of melody beats within 8 beats of the action.

- By synchronizing with ranged weapon fire (default LMB ), Octavia and her allies can gain the Opera buff, granting 12% / 20% / 25% / 30% ranged weapon Multishot for 5 / 8 / 12 / 15 seconds.
  - A correctly timed action will yield 8% - 34% synchronize percentage towards activating the buff, based on the number and spacing of melody beats within 8 beats of the action.
- While all other categories of firearms can inherently synchronize shots with each shot fired, Beam Weapons (except for the Tenet Flux Rifle because of its Auto Trigger) uniquely cannot. Upon activating Metronome and emptying the magazine of a beam weapon by holding down the trigger, you will gain minimum charge, requiring you to tap-fire in time with your Mandachord.
- Multishot bonus stacks additively with multishot mods such as Split Chamber.
- Alternate-fire or secondary attacks on select weapons e.g. Redeemer Prime can gain multishot from Opera.

- By synchronizing with melee weapons (default E ), Octavia and her allies can gain the Forte buff, granting 20% / 25% / 25% / 30% bonus melee weapon damage for 5 / 8 / 12 / 15 seconds.
  - A correctly timed action will yield 12% - 51% synchronize percentage towards activating the buff, based on the number and spacing of melody beats within 8 beats of the action.
- Damage bonus stacks additively with base damage mods like Pressure Point.

- Metronome can be recast while active to refresh its duration. On recast, existing synchronize percentages will not carry over and will be reset to 0%.
- Casting Metronome is not a One-Handed Action and interrupts other actions, but allows movement.
- Casting animation is affected by Casting Speed.
- When Octavia is standing on higher elevations or objects, the concentric rings of light from the melodic aura will partially fade depending on the surrounding terrain to allow better visibility.
- Concentric ring color and Nocturne cloak effect are affected by Octavia’s chosen Warframe energy color.
- Metronome affects the visuals and audio of any nearby Mallet and Resonator belonging to Octavia herself.

Tips & Tricks

- Having the mandachord's melody set to a consistent rhythm makes it much easier to sync up your buffs.
- Similar to Octavia's other abilities, without a melody this skill will do nothing.
- The longer the pause is between notes, the higher is the percentage gained per successful action.
- The intensity of light rings is determined by the number of notes in a particular column.

Maximization

Metronome

This section is transcluded from Warcry. To change it, please edit the transcluded page.

 | 2 75 | Warcry Valkyr lets out a rallying cry that bolsters Armor and Attack Speed for allies while in Affinity Range. Introduced in Update 11.0 (2013-11-20) | Strength:15 / 20 / 25 / 50 % (attack speed buff) 25 / 35 / 45 / 50 % (armor buff)
Duration:10 / 14 / 17 / 20 s
Range:N/A
Subsumable to Helminth

Info

- Valkyr expends 75 energy to let out a rallying cry, generating an aura within Affinity Range that strengthens Valkyr and her allies with 15% / 20% / 25% / 50% Attack Speed and 25% / 35% / 45% / 50% Armor for 10 / 14 / 17 / 20 seconds.
  - If allies lose Warcry such as from death or nullifiers, they can regain it upon re-entering Valkyr's Affinity Range. However, if Valkyr herself enters a nullifier field or falls out-of-bounds, Warcry will be dispelled from the entire squad.
  - Attack Speed bonus is additive to mods (e.g., Fury).
    - A maxed Fury and Intensify with a rank-3 Warcry will increase Valkyr's attack speed by: Attack Speed Mods + Warcry Modifier × (1 + Strength Mods) = 0.3 + 0.5 × (1 + 0.3) = 95%
  - The armor buff is based off of the affected Warframe's base armor value, and therefore stacks additively with other armor bonuses.
    - For example, a Valkyr with a max rank Steel Fiber, 130% Ability Strength, and while using Warcry increases her armor to: Base Armor × (1 + Armor Mods + Warcry Modifier × (1 + Strength Mods)) = 855 × (1 + 1 + 0.5 × (1 + 0.3)) = 2,265.75
  - Warcry affects other Warframes, Companions, Hostages, Defense objectives, Shadows, and Specters.

Kit Interactions

- Warcry's armor bonus is multiplied by 3x when used while Hysteria is active.
- Warcry's melee attack speed bonus allows Valkyr to charge her Rage passive faster, making it easier to reach the death prevention threshold while she is still invulnerable after a fatal hit.

Helminth

- Subsuming Valkyr to the Helminth will offer Warcry and its augments to be used by other Warframes.
  - However, Subsumed Warcry's attack speed bonus is reduced to 9% / 12% / 15% / 30%.

Augment

- Main article: Eternal War

Eternal War is a Warframe Augment Mod for Valkyr that extends Warcry's duration for each melee kill.

Rank | Duration bonus | Cost
0 | 1.25s | 6
1 | 1.5s | 7
2 | 1.75s | 8
3 | 2s | 9

Maximization

Eternal War?
Infused?
Hysteria active?

Warcry

This section is transcluded from Defy. To change it, please edit the transcluded page.

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

- Main article: Sonic Siphon

Sonic Siphon is a Warframe Augment Mod for Banshee's Sonic Boom that gives Armor when enemies are hit by it.

Rank | Duration | Cost
0 | 12s | 6
1 | 15s | 7
2 | 18s | 8
3 | 20s | 9

- Main article: Gourmand

Gourmand is a Warframe Augment Mod for Grendel's Feast to consume health instead of energy and increases armor for enemies in his gut.

Rank | Health Cost | Armor Bonus | Cost
0 | 300 | 75 | 6
1 | 260 | 100 | 7
2 | 240 | 125 | 8
3 | 200 | 150 | 9

- Main article: Hallowed Reckoning

Hallowed Reckoning is a Warframe Augment Mod for Oberon's Reckoning that makes enemies hit drop patches on the ground, dealing Radiation damage over time to enemies and providing armor to allies standing on them with a brief grace period upon stepping off. It also passively increases Reckoning's range.

Rank | Ability Range | Radiation Damage per second | Armor Bonus | Radius | Duration | Armor Bonus Grace Period | Cost
0 | +40% | 150 | 150 | 1.5m | 7s | 3s | 6
1 | +40% | 200 | 180 | 2m | 8s | 3s | 7
2 | +40% | 250 | 210 | 2.5m | 9s | 3s | 8
3 | +40% | 300 | 250 | 3m | 10s | 3s | 9

- Main article: Ironclad Charge

Ironclad Charge is a Warframe Augment Mod that temporarily increases Rhino's armor for each enemy hit by Rhino Charge.

Rank | Armor Bonus per hit | Duration | Cost
0 | 12% | 4s | 6
1 | 25% | 6s | 7
2 | 37% | 8s | 8
3 | 50% | 10s | 9

### Arcanes

- Arcane Circumvent
- Arcane Guardian
- Arcane Reaper
- Arcane Tanker
- Arcane Ultimatum
- Melee Fortification
- Magus Husk (Operator only)

Armor bonus from Arcanes stack additively after mods:

Total Armor=Base Armor(1+Mod Multiplier)+Arcane Bonus

### Focus

This section is transcluded from Focus/Unairu § Stone Skin. To change it, please edit the transcluded page.

 | Stone SkinPassive Warframe And OperatorIncreases Armor for Warframe and Operator by 50 / 100 / 150 / 200. | 60,000 / 105,000 / 215,000 / 400,000
Additional armor is a flat bonus, added after mods and abilities.

This section is transcluded from Focus/Unairu § Tempered Benison. To change it, please edit the transcluded page.

 | Tempered Benison Warframe And OperatorShockwaves create 2 / 3 / 4 / 5 Armor Motes that grant +450 temporary Armor. Max 5. | 95,000 + 2 /160,000 + 3 /325,000 + 5 /600,000 + 6
Motes behave identically to Health Conversion, and are only consumed when taking damage to health. Shares its stack limit with Health Conversion, allowing all 5 motes to be carried between both buffs.

Cogron Tauron Strike

This section is transcluded from Focus/Vazarin § Enduring Tides. To change it, please edit the transcluded page.

 | Enduring TidesPassive, Way-Bound OperatorIncreases Operator Health and Armor by 50 / 100 / 150 / 200%. | 60,000 / 105,000 / 215,000 / 400,000 / 750,000 + Brilliant Eidolon Shard
Enduring Tides is additive to bonuses provided by Magus Vigor and Magus Husk.

### Archon Shards

Azure Archon Shard +150 Armor each. Tauforged Azure Archon Shard +225 Armor each.

## Warframe Armor and Effective Health

Unlike health and shield, a Warframe's base armor doesn't change as it advances from Rank 0 to Rank 30, with the exceptions of Nidus, Lavos, and Kullervo.

Armor | Damage Reduction | EHP Multiplier | Warframe(s)
105 | 26% | 1.4x | Ash, Banshee, Gyre, Gyre Prime, Ivara, Limbo, Loki, Mag, Mesa, Mirage, Nekros, Nova, Nyx, Titania, Trinity, Uriel, Volt, Yareli, Yareli Prime, Zephyr
125 | 29% | 1.4x | Dagath, Oraxia
135 | 31% | 1.5x | Banshee Prime, Ember, Equinox, Ivara Prime, Jade, Limbo Prime, Loki Prime, Mag Prime, Mesa Prime, Nekros Prime, Nokko, Nova Prime, Nyx Prime, Protea, Revenant, Revenant Prime, Titania Prime, Trinity Prime, Volt Prime, Zephyr Prime
145 | 33% | 1.5x | Dante
146 | 33% | 1.5x | Xaku
150 | 33% | 1.5x | Cyte-09
160 | 35% | 1.5x | Ember Prime, Equinox Prime, Gara, Octavia, Octavia Prime, Sevagoth, Sirius & Orion, Vauban
165 | 35% | 1.6x | Narin
167 | 36% | 1.6x | Xaku Prime
185 | 38% | 1.6x | Ash Prime, Baruuk, Gauss, Gauss Prime, Harrow, Harrow Prime, Mirage Prime, Protea Prime, Sevagoth Prime, Wisp
200 | 40% | 1.7x | Gara Prime, Nezha, Voruna
210 | 41% | 1.7x | Vauban Prime, Wisp Prime
240 | 44% | 1.8x | Baruuk Prime, Excalibur, Hydroid, Inaros, Inaros Prime, Rhino, Saryn
265 | 47% | 1.9x | Citrine, Nezha Prime, Styanax, Styanax Prime, Voruna Prime, Wukong
290 | 49% | 2x | Caliban, Caliban Prime, Hydroid Prime, Khora, Rhino Prime, Wukong Prime
315 | 51% | 2.1x | Excalibur Prime, Excalibur Umbra, Frost, Frost Prime, Garuda, Hildryn, Hildryn Prime, Saryn Prime
325 | 52% | 2.1x | Citrine Prime, Follie, Temple
345 | 53% | 2.2x | Khora Prime
350 | 54% | 2.2x | Nidus (Unranked)
370 | 55% | 2.2x | Chroma, Grendel
385 | 56% | 2.3x | Oberon
400 | 57% | 2.3x | Grendel Prime
420 | 58% | 2.4x | Garuda Prime
425 | 59% | 2.4x | Nidus Prime (Unranked)
444 | 60% | 2.5x | Koumei
450 | 60% | 2.5x | Chroma Prime, Nidus (Max Rank), Oberon Prime
475 | 61% | 2.6x | Atlas
500 | 63% | 2.7x | Atlas Prime
525 | 64% | 2.7x | Nidus Prime (Max Rank)
550 | 65% | 2.8x | Kullervo (Unranked)
575 | 66% | 2.9x | Lavos (Unranked), Lavos Prime (Unranked)
650 | 68% | 3.2x | Kullervo (Max Rank)
675 | 69% | 3.2x | Lavos (Max Rank), Lavos Prime (Max Rank)
855 | 74% | 3.8x | Valkyr
875 | 74% | 3.9x | Qorvex
1000 | 77% | 4.3x | Valkyr Prime

### Armor Calculator

This calculator feature is sunsetted on the wiki thus some of these calculations may be depreciated. Stats are stored on MediaWiki:Calculator.js. It may not see further updates, but will be present on articles for the time being since some people still find use for them. See User blog:Cephalon Scientia/Sunsetting of Maximization Calculators for more details.

Error: JS unable to load. If you can read this consider activating javascript or changing to a device that supports javascript.

## Abilities Benefiting from Armor

Some abilities have values which are increased by the armor of the Warframe casting them. These are outlined below:

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

- Base health and armor multiplier are affected by Ability Strength.
- Iron Skin's health uses the following expression when accounting for Ability Strength: Modified Health = (Base Health + (Armor Multiplier × Base Armor × (1 + Armor Bonus))) × (1 + Ability Strength) + Absorbed Damage.
- Note that the base armor value is different between Rhino and Rhino Prime; while Rhino has 190 Base Armor, Rhino Prime has 275 Base Armor.
- As an example for Rhino:
  - With a maxed Steel Fiber and Intensify, a Rank 3 Iron Skin cast by Rhino will have an initial health of (1200 + (2.5 × 190 × 2.1)) × 1.3 = 2,856.75 before absorbing damage.

 | 3 50 | Snow Globe Frost deep freezes any vapor and moisture in the area, creating a protective sphere with brief invulnerability to boost its strength. Introduced in Update 6.0 (2013-01-29) | Strength:5x (armor multiplier) 1500 / 2500 / 3000 / 3500 (base health) 50 / 100 / 125 / 150 (break damage)
Duration:10 s (freeze duration)
Range:5m (radius)
Misc: 1 / 2 / 3 / 4 s (invulnerability duration) 10 ( Cold status procs on cast) 0.33 ( Cold status proc per second) 3 ( Cold status procs on break) 4 (globe limit) 1,000,000 (health cap)

Info

- Frost expends 50 Energy to create a protective globe of ice with a radius of 5 meters, a base health of 1500 / 2500 / 3000 / 3500, and additional health equal to 500% of Frost's base armor bonuses. Upon activation, the globe is invulnerable for 1 / 2 / 3 / 4 seconds. Incoming damage that is absorbed during this time is converted into health and added to the globe's health.
  - Snow Globe's health uses the following expression when accounting for Ability Strength: Modified Health = { Base Health + Armor Multiplier × [ Frost's Base Armor × (1 + Base Armor Bonus) + Additional Armor) ] } × (1 + Ability Strength) + Absorbed Damage
    - For example, with a maxed Steel Fiber and Intensify, rank-3 Snow Globe will have an initial health of { 3500 + 5 × [ 315 × (1 + 1) ] } × (1 + 0.3) = 8,645 before converting absorbed damage.
  - While active, a health counter becomes visible on the ability icon that tracks the health percentage of the most recently placed Snow Globe from 100% to 0%.
  - Frost and his allies do not contribute to Snow Globe's health gain by shooting the globe during the invulnerability period.
  - Most enemy gunfire is blocked from entering the globe. Ally gunfire is able to enter and exit the globe normally.
- Upon activation, enemies within range are inflicted with 10 Cold Status Effects to freeze enemies for 10 seconds and are violently pushed outwards. If the enemies hit obstacles, they can be dealt as much as 50% of their maximum health as True damage.
- Enemies that enter a formed Snow Globe receive a Cold status effect every 3 seconds.
- Snow Globe visually cracks as it receives damage. Upon breaking, it inflicts 50 / 100 / 125 / 150 Cold damage and 3 Cold status effects to enemies inside the globe.
- Snow Globe can be recast multiple times, but there are restrictions on the number of globes that can be created in the environment.
  - A maximum of 4 separate Snow Globes can be cast at any given time. Casting Snow Globe after reaching the maximum will remove the oldest globe.
  - Casting Snow Globe while inside an existing globe will remove the older globe and combine the total remaining health values of both globes for the newer one. The invulnerability period is reactivated for each cast.
    - Snow Globes created inside existing globes do not count toward the maximum number of instances, and Snow Globe's health can stack with repeated casts until reaching a maximum combined health of 1,000,000.
- Nullifier Bubbles do not immediately destroy Snow Globe. Instead, it loses 20% of its health per second, and the damage conversion into health during its invulnerability does not function.

Kit Interactions

- Frost passively gains 50 armor from enemies affected by Cold status effect within his Affinity Range, fortifying Snow Globe.
- Casting Freeze onto the exterior of a globe will destroy it, triggering an icy explosion that deals Freeze's base Cold area damage in an area of effect.
  - The damage does not diminish with distance and bypasses obstacles in the environment.
  - Affected enemies are Ragdolled by the explosion.
  - Freeze is capable of destroying a globe even during its invulnerability period.

Augment

- Main article: Chilling Globe

Chilling Globe is a Warframe Augment Mod for Frost that gives Snow Globe a chance to inflict 10 Cold status effects and freeze enemies solid that enter its range.

Rank | Freeze chance | Freeze Duration | Cost
0 | 30% | 10s | 6
1 | 35% | 10s | 7
2 | 40% | 10s | 8
3 | 50% | 10s | 9

- Main article: Cold Front

Cold Front is a Warframe Augment/Exilus mod for Frost's Snow Globe that changes it to become attached to Frost with a smaller radius while increasing Parkour Velocity. A percentage of Snow Globe's health is also restored upon killing Frozen enemies.

Rank | Globe Health per Kill | Cost
0 | 1% | 6
1 | 2% | 7
2 | 3% | 8
3 | 4% | 9

Tips & Tricks

- Maximized Ability Strength along with Steel Fiber and Armored Agility will add up to a total health of 26,386.75 (using Arcane Squall Helmet and Arcane Guardian is recommended, because they increase Snow Globe's health even further).
- Place over a cryopod in defense missions to shield it from all incoming fire.
- Since allied fire can now both enter and exit Snow Globe, using mods to affect the size of the globe (Ability Range) can now be done for strategy or preference, without worrying about interfering with your allies loadouts.
- When a teammate is downed, place a Snow Globe over them to protect you while reviving.
- When facing a boss with ranged attacks, do not place a Snow Globe on it. Instead, place it where your team is to protect them from incoming damage.
- The particle effect inside the globe can distract players' vision. Having a black energy color will remove this particle effect entirely, allowing better vision inside the globe.
- Recasting the ability after 4 seconds while remaining inside the Snow Globe will allow to sustain an impenetrable Snow Globe, that will grow stronger and stronger. This is due to the fact that it absorbs the enemy fire into its health and adds this health to the next Globe, as long as it is cast inside the first one.
  - Particularly useful in T4 Defense, since the enemies will quickly reach a level where it does not matter how much base health your Snow Globe has.
- Snow Globe's ability to temporarily freeze and push away enemies can be an effective way to rapidly clear a large safe area to revive teammates or remove enemies attacking a defense objective.
- Using Freeze to detonate a Snow Globe can also be done while inside another globe. This will not affect the globe you are in. If multiple globes overlap, it is possible to shatter a globe which protrudes into another globe by aiming at the part inside your globe.
  - It is possible to detonate the Snow Globe that you are in in some Corpus or Void missions by bouncing Freeze off the Bubble of a Nullifier Crewman.(Results May be unpleasant)

Maximization

Current Armor:
Cold Front?

Snow Globe

Bugs

- While using Helios, the Deconstructor projectile can be caught outside the globe and will not return to Helios unless Helios exits the globe.
- The globe can sometimes push enemies through walls and could soft-lock the game if the target is required. This has a higher chance of happening if the enemy is touching a wall.

- Base health and armor multiplier are affected by Ability Strength.
- Snow Globe's health uses the following expression when accounting for Ability Strength: Modified Health = (Base Health + 5 × Frost's Base Armor × Base Armor Bonus) × (1 + Ability Strength) + Absorbed Damage.
  - For example, with a maxed Steel Fiber and Intensify, rank-3 Snow Globe will have an initial health of (5000 + 5 × 300 × 2.1) × (1 + 0.3) = 10,595 before converting absorbed damage.

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

- Base health, armor multiplier, absorption multiplier and damage per second, are affected by Ability Strength.
- Warding Halo's health uses the following expression when accounting for Ability Strength: Modified Health = (Base Health + Armor Multiplier × Nezha's Base Armor × (1 + Base Armor Bonus)) × (1 + Ability Strength) + Absorbed Damage.
  - As an example, with a maxed Steel Fiber and Intensify, a rank-3 Warding Halo will have an initial health of (900 + 2.5 × 175 × 2.1) × 1.3 = 2,364.375 before absorbing damage.

 | 2 50 | Tectonics Summon a Bulwark rock-wall, activate again to send the rocks crashing toward the enemy. Bulwarks attacked by enemies release an area-of-effect Slash powered by the Health it has lost. Introduced in Update 17.5 (2015-10-01) | Strength:600 / 900 / 1200 / 1500 (base health) 1 x (health multiplier to Slash damage) 250 / 300 / 350 / 500 (explosion Puncture damage) 150 / 300 / 450 / 600 (roll Impact damage)
Duration:N/A
Range:3 / 3 / 4 / 5 m (explosion radius)
Misc: 5 x (armor multiplier) 1 / 2 / 3 / 4 s (invulnerability duration) ? m (shrapnel damage radius) 1 (max bulwarks active) 15 m (roll distance) 200 % (petrified rolling speed) 30 m (petrified roll distance) 200 % (petrified damage bonus)

Info

- Reshaping the surrounding terrain, Atlas expends 50 energy to erect a Bulwark made of stone with a base health of 600 / 900 / 1200 / 1500 and additional health equal to 500% of Atlas' armor. Upon activation, the bulwark is Invulnerable for 1 / 2 / 3 / 4 seconds; incoming damage that is absorbed during the invulnerability period is converted and added to the bulwark's health. After the invulnerability phase, whenever the Bulwark receives damage, the amount of health lost multiplied by 1 times is converted into Slash damage and inflicted on all enemies within ? meters from the Bulwark. Atlas can maintain only 1 Bulwark at a time.
    - The bulwark's health uses the following expression when accounting for Ability Strength: Modified Health = (Base Health + 5 × Atlas' Armor) × (Ability Strength) + Absorbed Damage.
    - For example, with a maxed Steel Fiber and Intensify, rank-3 Tectonics will produce a bulwark with an initial health of (1500 + 5 × ( 475 × (1 + 1))) × (1 + 0.3) = 8,125 before converting absorbed damage.
  - While active, a health counter becomes visible on the ability icon that tracks the bulwark's health percentage from 100% to 0%. Placing the HUD's targeting reticle over the bulwark will also display its health bar.
  - Atlas and his allies do not contribute to a bulwark's health gain by shooting it during the invulnerability period.
- Reactivating the ability will cause the bulwark to compact into a Boulder that rolls towards the current direction of aim, dealing 150 / 300 / 450 / 600 Impact damage per second to enemies that are dragged along its path. After rolling 15 meters or hitting an environmental object, the boulder will explode and inflict 250 / 300 / 350 / 500 Puncture damage to enemies within a radius of 3 / 3 / 4 / 5 meters.
  - Enemies affected by the rolling damage are ragdolled.
  - The explosion damage does not bypass obstacles in the environment and diminishes with distance.
- While the bulwark is capable of blocking most hostile gunfire, it does not provide cover from area of effect damage, including the explosive attacks of Grineer Bombards and Napalms.
- Bulwarks and Boulders have collision detection for enemies only. Atlas and allies can move through Tectonics' objects unobstructed.
- Enemies will attack the Bulwark if it obstructs their path. Though some enemies may simply run up against it.
- Upon transforming the Bulwark into a Boulder, Tectonics can be recast immediately to create a new Bulwark.
- The Bulwark will spawn on the same elevation as Atlas, but the bulwark does have gravity and will fall down if created in the air or without a surface directly underneath it.
- Casting and reactivation duration of 1 second are affected by Natural Talent and Speed Drift.

Kit Interactions

- Casting Petrify on the Bulwark hardens it into a Petrified Bulwark. Boulders created from Petrified Bulwarks gain 200% rolling velocity and have their rolling distance increased to 30 meters. They also inflict 200% bonus damage on rolling and explosion damage.
  - Bulwarks and Boulders become silver-colored and metallic when petrified.
  - As the 3 bulwarks created by Tectonic Fracture cannot become boulders, Petrify has no effect on them.
  - Casting Petrify on a moving boulder will not grant it bonuses.

Augment

- Main article: Tectonic Fracture

Tectonic Fracture is a Warframe Augment Mod for Atlas that modifies Tectonics to allow additional simultaneous walls, but sacrifices the ability to turn them into offensive boulders.

Rank | Walls | Health | Cost
0 | 2 | 70% | 6
1 | 2 | 80% | 7
2 | 3 | 90% | 8
3 | 3 | 100% | 9

Tips & Tricks

- Can completely block off narrow enough areas or chokepoints from enemies without limiting the movement of allies.
- The Boulder can be used to push down long corridors, but care should be taken when aiming as the Boulder will detonate when it hits a side wall or standing obstacle.
- The Bulwark's cover can assist in reviving allies who have fallen to a frontal threat.
  - Note that Bulwark's protection is less effective against enemy AoE attacks.
- Enemies will not change their motion to sidestep a rolling Boulder. This makes the boulder very effective against lines of charging foes.
- Although it does not boast above average threat level, The Bulwark can be used to draw fire away from the player as long as it is closer to the enemy than the player is.
  - This is most effective against fast and threatening melee attackers like Thrax Centurions or many infested, which can often force the player into the air to avoid them. Placing a Bulwark can completely halt this attack provided these enemies get close enough to start attacking it instead.
  - Thrax Centurions specifically can be completely neutralized by placing a wall as, for unknown reasons, they will focus on the wall but not attack it. This potentially means they can be indefinitely taken out of the fight as long as the wall is not destroyed or recast.

Maximization

Atlas' Armor:
Absorbed damage:

Tectonics

- The bulwark's health uses the following expression when accounting for Ability Strength: Modified Health = (Base Health + 5 × (Atlas' Base Armor × (1 + Armor Mods)) × (1 + Strength Mods) + Additive Armor) + Absorbed Damage.
  - For example, with a maxed Steel Fiber and Intensify, rank-3 Tectonics will produce a bulwark with an initial health of (3750 + 5 × 450 × 2.1) × (1 + 0.3) = 11,017.5 before converting absorbed damage.

 | 4 100 | Rumblers Summon two elemental stone brawlers to the melee. Summoning petrifies enemies in close proximity to Atlas. When finished, Rumblers collapse into a pile of healing Rubble. Introduced in Update 17.5 (2015-10-01) | Strength:50 / 150 / 250 / 500 (armor) 500 / 750 / 1000 / 1250 ( Blast damage) 500 / 750 / 1000 / 1200 (health) 800 / 1000 / 1400 / 2000 (melee Impact damage) 200 / 250 / 350 / 500 (rock Impact damage)
Duration:15 / 20 / 30 / 45 s (Rumbler duration)
Range:3 / 4 / 5 / 6 m (stone radius) 3 / 4 / 5 / 6 m ( Blast radius) 1 (speed multiplier)
Misc: 2 (number of Rumblers) 10 s (stone duration) 0.5 to 1.5 m/s (min-max speeds) 1 (Rubble dropped on death per Rumbler) ≤ 50 (Rubble health/armor given)

Info

- Atlas expends 100 energy to summon his 2 earthly elemental golems as he instantly petrifies all enemies into stone within a 3 / 4 / 5 / 6 meter radius for 10 seconds. Once summoned, the Rumblers will roam the battlefield seeking nearby enemies to attack. They last for 15 / 20 / 30 / 45 seconds unless they are killed or manually detonated.
  - Petrifying occurs instantly when Atlas begins his casting animation.
  - Not affected by melee mods or Attack Speed buffs (e.g. Warcry).
- Each Rumbler possesses 500 / 750 / 1000 / 1200 Health, 50 / 150 / 250 / 500 Armor, and a speed multiplier of 1.
  - Physical size of each Rumbler along with their health, armor, and all sources of damage are affected by Ability Strength. Health and armor are also affected by Warframe health, shield, and armor mods.
  - Rumbler health uses the following expression when accounting for Ability Strength: Modified Health = Health × (1 + Ability Strength Mods + Health Mods + Shield Mods) + Warframe Rank Health Bonus × (1 + Health Mods) + Flat Health Bonuses + Warframe Rank Shield Bonus × (1 + Shield Mods).
    - For example, with Vitality, Primed Redirection, Intensify, and Atlas all at max rank, rank-3 Rumblers will have a modified health of 1200 × (1 + 0.3 + 1 + 1.8) + 100 × (1 + 1) + 100 × (1 + 1.8) = 5,400.
    - Atlas' rank influences Rumbler health as the "Health Gain" and "Shield Gain" in the expression are referring to bonuses applied to Atlas' respective base stats. As Atlas at max rank will have +100 health and +100 shields, these bonuses will also apply to the Rumblers' health.
  - Rumbler armor uses the following expression when accounting for Ability Strength: Modified Armor = Armor × (1 + Ability Strength Mods + Armor Mods) + Additional Armor.
    - For example, with a maxed Steel Fiber and Intensify, rank-3 Rumblers will have a modified armor value of 500 × (1 + 0.3 + 1) = 1,150.
  - Speed multiplier can not fall below 0.5 or exceed 1.5 under any circumstances.
  - Rumblers are counted as summons and are affected by Summoner's Wrath, Arcane Camisado, and Theorem Infection.
- Rumblers inflict 800 / 1000 / 1400 / 2000 Impact damage and stagger the target backwards with each melee attack; they can occasionally throw stones that home in on enemies to inflict 200 / 250 / 350 / 500 Impact damage and ragdoll enemies hit.
  - Melee damage shows as tier 1 critical damage with yellow text but this critical damage is unmoddable.
    - Melee damage will not be scaled against enemies while their AI is paused resulting in 25% of the normal melee damage.
- If the ability is reactivated or if Atlas becomes incapacitated, active Rumblers will self-destruct and inflict 500 / 750 / 1000 / 1250 Blast damage to enemies within 3 / 4 / 5 / 6 meters.
  - Damage does not bypass obstacles in the environment and diminishes with distance.
- Rumblers are immune to Status Effects, such as knockdowns or Slash procs, but they can be staggered.
- While melee kills by the Rumblers are considered melee kills by Atlas, they do not contribute to the Melee Combo Counter.
- Rumblers have collision detection for enemies only. Atlas and allies can move through Rumblers unobstructed.
- The number of active Rumblers is displayed in the HUD beside Atlas' shield and health indicators, and waypoints are displayed onscreen for each active Rumbler.
- If a Rumbler enters a Nullifier bubble, it will have its health drained.

Kit Interactions

- Self-destructing Rumblers will drop 1 piece of Rubble for Atlas to pick up, restoring 50 health or provides 50 bonus armor.
  - Rumbler Rubble provides reduced amounts of health or armor if Rumblers sustained damage to their health before expiring.
  - Casting Petrify on injured Rumblers will heal them to 100% health.

Augment

- Main article: Rumbled

Rumbled is a Warframe Augment Mod for Atlas's Rumblers in PvE and Conclave that transforms Atlas into a Rumbler and grants Overguard that scales off Atlas' modded health.

Rank | % max health absorbed | Cost
0 | 200% | 6
1 | 225% | 7
2 | 250% | 8
3 | 300% | 9

- Main article: Titanic Rumbler

Titanic Rumbler is a Warframe Augment Mod for Atlas that modifies Rumblers to make one larger Rumbler with more health, damage, and melee range, and will occasionally increase its Threat Level, instead of the normal two Rumblers. The recast ability to remove Rumblers is replaced by the taunt and a slam attack that knocks down all enemies within 15 meters.

Rank | Health | Damage | Slam Radius | Slam Damage | Cost
0 | 200% | 200% | 15m | 200 | 6
1 | 225% | 250% | 15m | 300 | 7
2 | 265% | 300% | 15m | 400 | 8
3 | 300% | 400% | 15m | 500 | 9

Maximization

Percent health bonus:
Flat health bonus:
Percent shield bonus:
Percent armor bonus:
Flat armor bonus:

Rumblers
Rock radius | m
Self destruct radius | m

- Rumbler armor uses the following expression when accounting for Ability Strength: Modified Armor = Armor × (1 + Armor Mods + Ability Strength).
  - For example, with a maxed Steel Fiber and Intensify, rank-3 Rumblers will have a modified armor value of 500 × (1 + 1.1 + 0.3) = 1,200.

 | 4 75 +3-5/s | Mass Vitrify Create an expanding ring of molten glass that slowly crystallizes enemies who enter. When the expansion is complete, the ring hardens to block weapons fire. The ring draws extra strength from the health and shields of crystallized enemies. Use Shattered Lash to smash the ring and send razor-sharp glass flying. Introduced in Update 22.0 (2017-10-12) | Strength:20% / 30% / 40% / 50% (Damage Vulnerability) 500 / 750 / 1000 / 1600 (ring segment base health) 500 / 600 / 700 / 800 (segment explosion damage) 5x (armor multiplier)
Duration:2 / 2.25 / 2.75 / 3 s (expansion time) 10 / 12 / 14 / 16 s (effect duration)
Range:2 m (ring initial radius) 3 m/s (ring expansion rate) 8 / 8.75 / 10.25 / 11 m (ring max radius) 8 / 10 / 12 / 15 m (explosion range)
Misc: 3 m (ring initial height) 15 m (ring max height) 3 s (crystallization time) 12 (ring segments)

Info

- Gara expends 75 Energy and coats herself in a shell of hardened glass, becoming immobile and Invulnerable to damage as she unleashes a radial ring of molten glass that expands outward and downward. The molten glass ring's initial horizontal radius from Gara is 2 meters, which expands horizontally at a rate of 3 meters per second over 2 / 2.25 / 2.75 / 3 seconds, up to a maximum horizontal radius of 8 / 8.75 / 10.25 / 11 meters. Ring expansion initially drains 3 energy per second, which ramps up to 5 energy per second over the course of expansion. The molten glass ring's initial height is 3 meters high, which expands downward up to a maximum height of 15 meters.
  - The maximum wall radius follows the formula 2R + 9RD, where R is power range and D is power duration (both expressed in decimal notation).
  - Molten glass bypasses all entities, obstacles, and terrain as it expands.
  - When the molten glass ring is created, its base is aligned with Gara's feet to ensure that the initial ring height is about Warframe height.
  - Ring height expands downward much faster than ring horizontal radius, reaching full height before expansion time completes.
  - Initial casting animation and release animation are affected by casting speed, from mods such as Natural Talent and Speed Drift.
  - Can be recast while active to expand molten glass and create a new barrier. Only 1 barrier may remain active per player.
  - Molten glass, hardened glass, and crystal tint color and particle effects energy color are affected by Gara's chosen Warframe energy color.
  - If a Nullifier Crewman bubble touches the glass, it will end the ability prematurely if casting, and instantly shatter it without dealing any damage to surrounding enemies if already hardened. However, enemies hardened with glass will only harden prematurely if the nullifier touches them.
- Mass Vitrify's glass undergoes two distinct phases with diverse effects on Gara, allies, and enemies:

Crystallization

- Enemies that contact the molten glass are crystallized over 3 seconds, slowing in movement and attack speed until completely solidified in place for 10 / 12 / 14 / 16 seconds. Crystallized enemies receive 20% / 30% / 40% / 50% Damage Vulnerability. Each enemy crystallized contributes extra health to the barrier formation phase, based on a portion of their maximum Shields and Health.
  - Crystallize converted health is affected by both Ability Strength and Armor mods such as Steel Fiber equipped on Gara.
- If Gara or allies are affected by a Radiation proc, allies may also be vitrified. This includes Sortie Defense Operatives, Syndicates Operatives, and Kavor Defectors in addition to fellow Tenno.
- On death, crystallized enemies shatter into glass with visual and sound effects.

Barrier Formation

- Upon pressing the ability key again (default 4 ), when maximum horizontal radius is reached, or when Gara runs out of Energy, Gara sheds her glass shell as the molten glass ring solidifies into a hardened glass barrier. The glass barrier lasts until all segments are destroyed or when Mass Vitrify is recast.
- The glass barrier consists of a circle made out of 12 individual segments, each possessing 500 / 750 / 1000 / 1600 base health, plus additional health equal to Gara's total armor value multiplied by 500%. For each enemy affected by the crystallization phase, each glass barrier segment gains extra health equal equal to 10% of the enemy's maximum shields and health, or 320 plus 500% of Gara's total armor (whichever value is greater).
  - Health for each Barrier segment uses the following expression: Modified Health = (Base Health + 5 × (Base Armor × (1 + Armor Mods) + Additional Armor)) × (1 + Strength Mods) + Absorbed Health
    - With a maxed Steel Fiber and Intensify a wall segment would have (1600 + 5 × (160 × (1 + 100%))) × (1 + 30%) = 4,160 Health before accounting for converted health from crystallized enemies (values resulting from intermediate calculations are rounded down to the nearest whole number).
  - Absorbed Health:
    - Minimum Health added from each enemy affected by the crystallization phase is: Health Added = (320 + 5 × (Base Armor × (1 + Armor Mods) + Additional Armor)) × (1 + Strength Mods)
    - Maximum Health added is: Health Added = (Max Enemy Health + Max Enemy Shields) ÷ 10
    - Whichever formula results in a greater value is used for health added.
  - During the crystallization phase, the number of total crystallize converted health is displayed beside the shield and health indicators on the HUD, as a buff icon with the number of converted health below the icon.
  - The number of intact glass barrier segments is shown on the ability icon while at least 1 segment exists.
- When a segment's health is depleted, it explodes outward and damages all enemies in a range of 8 / ? / ? / 15 meters for 250 / 300 / 350 / 400 damage. The explosion also reaches inwards to the center of Mass Vitrify.
  - Explosion has a damage composition of 18.75% Impact, 37.5% Puncture, and 37.5% Slash.
- Player and AI interaction with the glass barrier have notable differences:
  - Ally players, allied AI, ally weapon fire, and Warframe abilities can pass through unhindered. However, some friendly projectile-based weapons are deflected when striking either side of the wall, such as Miter and Arca Plasmor.
  - Some allies such as hacked Eidolon Lures and Sortie Defense Operatives cannot pass through.
  - Most enemies are blocked by the glass barrier from moving and attacking through it, including Kuva Clouds. However, most bosses and the Eidolon Teralyst can pass through unhindered.
  - Area of effect attacks (e.g., Shockwave MOAs and Bombards) and weapons with innate punch through (e.g. Tusk Grineer units) can hit through the glass barrier.

Kit Interactions

- If Gara strikes her own Mass Vitrify glass barrier with Shattered Lash's glass longsword, the barrier is shattered and destroyed in an explosion of glass fragments that inflicts Shattered Lash's damage and 500 / 600 / 700 / 800 damage to all enemies within 8 / 10 / 12 / 15 meters from the barrier's exterior surface, as well as all enemies inside the barrier.
  - Explosion has a damage composition of 18.75% Impact, 37.5% Puncture, and 37.5% Slash.
  - Explosion damage is affected by base damage mods (e.g. Pressure Point, Spoiled Strike), elemental damage mods (e.g. North Wind, Melee Exposure), combo multiplier on Shattered Lash, as well as abilities like Roar, Nourish and Lethal Levitation.
  - Explosion damage is not affected by Faction mods, Condition Overload, Vigorous Swap, critical chance or status chance mods as it cannot crit or proc status effects.
  - Explosion is radial and not dependent on the direction Gara strikes Mass Vitrify with Shattered Lash. Gara must strike a currently intact part of the barrier, but the explosion will occur even around broken segments.
- Casting Mass Vitrify will also refresh the duration of Splinter Storm on Gara, as well as any affected allies that contact the molten glass during its expansion.
- If Mass Vitrify's barrier is destroyed by Shattered Lash and Splinter Storm is within the explosion radius of the barrier, 50% of the glass fragments' damage is permanently added to Splinter Storm's damage per second until its duration expires.
  - Absorbed damage can stack from repeated Mass Vitrify explosions inside Splinter Storm's radius.
  - Splinter Storms on Gara herself and allies can absorb damage from Mass Vitrify's explosion, while storms on affected enemies do not.
- Gara's Passive allows casting abilities to have a 15% chance to Blind enemies within 12 meters for 10 seconds, exposing them to Melee Finisher attacks. Blind chance increases by 20% until the blind triggers.

Tips & Tricks

- While Mass Vitrify is a potent defensive tool, it can be converted into an offensive tool by investing in Ability Range and Efficiency, to increase the effective range of the resulting shrapnel explosion and reduce casting cost for repeated use.
  - The damage from the shrapnel scales with Shattered Lash's damage, but has no critical or status chance. This makes base damage increases like Pressure Point and Arcane Fury, and elemental bonuses like Molten Impact and Melee Exposure, particularly effective.
  - Boosting Gara's Ability Strength will increase both Shattered Lash's damage and the shrapnel's base damage.
- As Mass Vitrify scales with enemy health values, the more enemies caught inside the ring, the stronger the glass walls will be. This can be strong enough to stop very high level Demolisher and Acolytes if enough enemies are vitrified inside the ring.
  - The health value of Mass Vitrify is displayed with an on-screen icon, and can be boosted using Arcanes such as Arcane Ultimatum or Arcane Guardian, the Operator Focus skill Stone Skin, Helminth abilities such as Parasitic Armor or Chroma's Cold Elemental Ward, or mods such as Mecha Pulse.
  - Magus Anomaly can be used to pull in a group of enemies to be crystallized, making the resulting wall stronger.
- Enemies that pass through the ring as it expands take 50% more damage from all sources.
- Mass Vitrify can refresh an ally's Splinter Storm timer if they pass through the molten wall while Mass Vitrify is being channeled.

Maximization

Shattered Lash total damage:
Current Armor:

Mass Vitrify

Bugs

- Interrupting the expansion quickly after casting might sometimes result in a "fake" barrier which does not block damage and can not be detonated with Shattered Lash. This can also occasionally happen without voluntarily stopping the expansion.
- Operators that come into contact with the ring while it's expanding are slowed down.

- Barrier segment base health and segment explosion damage are affected by Ability Strength, while crystallize converted health is affected by both Ability Strength and Armor mods such as Steel Fiber equipped on Gara.
  - Barrier segment health uses the following expression: Modified Health = (Base Health + (5 × Base Armor × (1 + Armor Mods))) × (1 + Strength Mods)
  - With a maxed Steel Fiber and Intensify a wall segment would have [2225 + (5 × 125 × (1 + 1.1))] × (1 + 0.3) = 4,598.75 Health before accounting for converted health from crystallized enemies (values resulting from intermediate calculations are rounded down to the nearest whole number).

## Enemy Armor Scaling

- Main article: Enemy Level Scaling

Enemy base armor values are displayed under the codex and infobox, but scale to the enemy's level. Generally, only Grineer and boss enemies have armor, while the only Corpus and Infested units to possess armor are Bursa units, Oxium Osprey, and the Juggernaut. When the enemy health bars are yellow, armor is in effect and damage will be reduced.

Enemy armor produced by level scaling is hard capped at 2,700, granting 90% Damage Reduction under the standard enemy armor formula.

Enemies whose level-scaled armor would be less than 200 have their initial armor value set to the minimum cap of 200 instead. This minimum cap is only for the initial value of their armor, i.e. their armor can still be decreased below 200 through all normal means of armor removal.

For armor, the ranges of level differences at which scaling transitions is between 70 & 80. The formula by which enemy armor scales is as follows:

- f_1(x)=1+0.005(x−Base Level)^(1.75) Lower endpoint curve
- f_2(x)=1+0.4(x−Base Level)^(0.75) Upper endpoint curve

- Armor Multiplier=f32(f_1(Current Level)+f32(f32(f_2(Current Level)−f_1(Current Level))×s))

- Where the Armor Multiplier is the value that multiplies an enemy's base armor to its current armor.

## Removing Enemy Armor (Armor Stripping)

Most armor strip effects removes a percentage of the maximum value. For Heat and Corrosive, it is based on the current value, and thus has diminishing returns. Warframe abilities are based on the total; for example, an ability that strips 50% armor will remove it in just two casts.

### Percentage From Total Armor

#### Mods

- Corrosive Projection is an Aura mod that decreases armor by 18%, up to 72% when paired with a full squad.
- Sharpened Claws is a Kavat mod that allows the Kavat to perform a highly damaging strike while removing 120% armor.
- Vicious Bond is a Companion mod that allows the Companion to remove 15% armor with melee attacks

#### Abilities

- Main article: Seeking Shuriken

Shuriken

Ability Strength

 | 1 25 | Sonic Boom Banshee emits a sonic shockwave that pushes targets in range with enough force to incapacitate attackers and reduce their Armor. Introduced in Update 7.0 (2013-03-18) | Strength:175 / 200 / 225 / 250 ( Impact damage) 70% (Armor Reduction) 5 (Push Force)
Duration:N/A
Range:10 / 12 / 13 / 15 m
Misc: 180° (cone angle) Stagger on hit

Info

- Banshee expends 25 energy to emit a sonic shockwave that propagates forward in a 180° cone in front of her, hitting enemies up to 10 / 12 / 13 / 15 meters away. Enemies caught by the wave receive 175 / 200 / 225 / 250 Impact damage with a guaranteed Impact proc, have 70% of their Armor permanently removed, and are pushed away from Banshee with a Push Force of 5, leaving them momentarily staggered afterwards.
  - Sonic Boom is a one-handed action, allowing Banshee to move, shoot, reload, and perform most other actions while casting.
  - Requires Line of Sight to the target.
- Can be used to break Storage Containers and other breakable decorations in the environment.

Kit Interactions

- Enemies within 20 meters of Banshee when she casts Sonic Boom passively receive 5 Puncture Status Effects.

Augment

- Main article: Sonic Siphon

Sonic Siphon is a Warframe Augment Mod for Banshee's Sonic Boom that gives Armor when enemies are hit by it.

Rank | Duration | Cost
0 | 12s | 6
1 | 15s | 7
2 | 18s | 8
3 | 20s | 9

Tips & Tricks

- Can be used effectively as a source of instant crowd control to get large amounts of enemies out of your face incredibly quickly.
- When combined with Energy Siphon and Maximized Ability Range, this ability can be used continuously to keep large crowds of enemies off their feet until death. This is one of the most energy efficient crowd-control effects in the game.
- Since Sonic Boom can knock most enemies back, it can be used to instantly kill enemies by sending them down a bottomless pit.

Maximization

Sonic Siphon?

Sonic Boom

Localization

Language | Official Translation
(PT) Brazilian Portuguese | A Banshee desferirá uma onda de choque sônica, que empurrará os inimigos atingidos com força suficiente para incapacitá-los e reduzir suas Armaduras.

Banshee

Ability Strength

 | 4 100 | Fusion Strike Converge three streams of raw energy upon a single point, causing a massive explosion. The streams strip armor and shields, and each enemy struck detonates on stream convergence. Summoned Conculysts can wield their own mini Fusion Strikes. Introduced in Update 31.0 (2021-12-15) | Strength:12,000 / 13,000 / 14,000 / 15,000 /s (laser Tau damage per second) 2,500 / 3,000 / 4,000 / 5,000 (enemy detonation Tau damage) 600 / 650 / 700 / 750 (convergence explosion Tau damage) 20 / 25 / 35 / 50 % (armor and shield strip)
Duration:6 / 9 / 12 / 15 s (fallout duration)
Range:15 / 20 / 25 / 30 m (stream range) 5 / 6 / 8 / 10 m (explosion and fallout radius) 2 m (enemy explosion radius)
Misc: 3 (number of streams) ∞ beam Punch Through against enemy bodies Stagger on enemy explosions and final explosion 1 m (enemy explosions damage falloff) 100 % (strip cap) 3% (Lethal Progeny Conculyst laser prism chance on Fusion Strike)

Info

- Caliban expends 100 Energy to expel 3 concentrated streams of pure energy from his chest core and hands, carving a swathe of energized destruction over a range of 15 / 20 / 25 / 30 meters as he converges them into one toward the location on the aiming reticle. Each stream inflicts 12,000 / 13,000 / 14,000 / 15,000 Tau damage per second with 20% status chance and infinite Punch Through against enemy bodies. Caliban is Invulnerable and immobile, but able to aim the reticle with reduced camera panning speed and increased field-of-view to sweep the beam at multiple targets.
- Upon full convergence, enemies that have been directly hit by beams detonate for 2,500 / 3,000 / 4,000 / 5,000 Tau damage in a 2 meter radius and Stagger nearby enemies away; explosion damage has a 1 meter damage falloff. As the streams collapse, a final explosion occurs over a 5 / 6 / 8 / 10 meter radius, inflicting 600 / 650 / 700 / 750 Tau damage and Staggers enemies away from the center, while leaving behind a field of fallout that envelops the targeted area spanning the same radius as the final explosion and lingers for 6 / 9 / 12 / 15 seconds. All enemies directly hit by the beams and wander into the fallout field lose 20% / 25% / 35% / 50% of their Armor and Shields permanently.
  - Enemy armor and shields are fully removed at 200% Ability Strength. With one Corrosive Projection, armor will be fully stripped at 164% Ability Strength.
    - Defense strip only occurs once per ability cast.
    - Shield strip removes a percentage of the current maximum value, as such it has diminishing returns on subsequent casts against the same enemies. Armor strip, however, is a percentage of an enemy's total, requiring only two casts at base strength to fully strip.
      - Enemy shields can still regenerate with natural shield regeneration (such as Armis Ulta, Kuva Lich, or Sisters of Parvos) or while affected by regeneration buffs (such as Shield Ospreys), even while inside the fallout field.
  - Explosion's line of sight restriction is centered on the middle of the fallout field, regardless if Caliban himself sees the enemy or not. Explosion damage diminishes with distance from the center.
  - Caliban can freely reorient his aiming reticle during the convergence to sweep the streams along damaging more enemies, then create the fallout field at the end of the casting animation.
  - Fallout field is created at the first contact point with a solid surface within the stream range, or at the maximum stream range. Fields can be created without a surface and hovering in midair.
  - Fallout field visual effect fades out after a set time, but will remain in effect albeit invisible if ability duration is higher.
- Can be recast while active to create new fallout fields.
- Casting Fusion Strike is a full-body animation that stops Caliban's grounded movement and other actions, except reticle and camera movement.
- Nullifiers cannot nullify the fields by passing over them or Caliban, and they cannot nullify the effects inflicted by the field.

Kit Interactions

- Sentient Wrath's Damage Vulnerability increases Fusion Strike's damage.
- Lethal Progeny's Conculysts fire their own Fusion Strikes as they become briefly Invulnerable and coordinate with Caliban's Fusion Strike aimed at the reticle, with 0.5x damage effectiveness and defense strip, but does not create fallout fields. Caliban's Conculysts have a 3% chance to be empowered from casting Fusion Strike, granting them the Battalyst laser prism special attack for their remaining lifespan.

Tips & Tricks

- With one player using Corrosive Projection, 100% armor strip can be achieved at 168% Ability Strength.

Maximization

Fusion Strike

Bugs

- Beams can apply Tau procs to Drones, which counts toward Condition Overload (Mechanic).

Ability Strength

 | 4 100 | Rakhali's Cavalry Phantom Kaithes charge forth, inflicting Viral Damage upon all in their path. Their attack strips the defenses of Doomed enemies. Introduced in Update 34.0 (2023-10-18) | Strength:15,000 / 20,000 / 25,000 / 30,000 Viral damage per interval per Kaithe 20 / 25 / 30 / 35 % Doom defense reduction per interval per Kaithe
Duration:2 / 2 / 3 / 3 s charge duration
Range:N/A
Misc: 5 number of Kaithes 5 m summon radius 1.5 s invulnerable time 15 m/s charge velocity Stagger on contact 0.15 s damage interval

Info

- Dagath expends 100 Energy to summon 5 spectral remnants of Rakhali's soul in a cavalry charge formation 5 meters away. During the casting time of 1.5 seconds, Dagath becomes Invulnerable then commands the cavalry of phantom Kaithes to continuously charge forward at 15m/s for 2 / 2 / 3 / 3 seconds. Each spectral Kaithe inflicts 15,000 / 20,000 / 25,000 / 30,000 Viral damage and Stagger per 0.15 seconds to all enemies in its path; damage is dealt in full on each interval and continues for as long as enemies remain in physical contact with the phantom Kaithes.
  - All effects apply to enemies in contact with Kaithes during the summoning animation.
    - Enemies touched by Kaithes emit a burst of ghostly light on every hit.
  - Dagath's invulnerability while casting Rakhali's Cavalry scales directly with its casting time. Reducing casting time through Natural Talent or an Amber Archon Shard will reduce this invulnerability by the same amount.
  - Phantom Kaithes charge in a V formation, with the leading Kaithe in the center. Each Kaithe has a sizable hitbox to strike multiple enemies, aided by the stagger effect.
    - When cast while Dagath is on the ground, phantom Kaithes' formation is aligned with the leading Kaithe summoned on the nearest available horizontal surface, regardless of Dagath's own elevation.
    - When cast from the air, the Kaithes align toward the exact direction of Dagath's aiming reticle and can fly through the air. If they touch the ground, they charge forward wherever their head is facing and run along the surface, adhering to any changes in the terrain.
    - Phantom Kaithes will phase through vertical terrain and obstacles as they travel, by visually passing through a ghostly portal aligned with the wall.
  - Phantom Kaithes damage and break destructible Objects such as crates and resource caches.
- Can be recast while active to summon all Kaithes toward a new direction. Previous cavalry charge is removed on recast.

Kit Interactions

- Stampede Doomed foes with Rakhali's Cavalry to trigger Phantom Wrath, and induce 20% / 25% / 30% / 35% permanent Shields and Armor reduction. Defense reduction on Doomed foes occurs on every Viral damage instance from individual Kaithes.
  - Defenses are fully removed at 286% Ability Strength from a single hit. However, because the Cavalry deals multiple instances of damage, far less Strength is necessary, with 143% Ability Strength fully removing defenses after two hits.

Maximization

Rakhali's Cavalry
Viral damage: | /0.15s
Defense Reduction to Doomed enemies: | %/0.15s

Doom

Ability Strength

 | 3 75 | Fire Blast Slam the ground to create a wave of incinerating plasma that knocks back enemies and strips their armor. Introduced in Vanilla (2012-10-25) | Strength:66 / 100 / 141 / 200 ( Heat damage) 50-100% (armor reduction)
Duration:N/A
Range:25 m (wave radius)
Misc: 100% ( Heat status chance) -2%/s (heat generation rate reduction for Immolation) -50% (total heat removal for Immolation)
Subsumable to Helminth

Info

- Ember expends 75 Energy to slam the ground, creating a wave of fire that expands outwards to a radius of 25 meters. Enemies that are on-screen or are in Line of Sight from Ember and within range are dealt 66 / 100 / 141 / 200 Heat damage with a 100% status chance, have their Armor permanently reduced by 50% - 100%, and suffer Knockdown and are violently pushed back.
  - Armor reduction per cast is capped at 50% - 100%, achievable with 100% Ability Strength. As such only values below 100% will have effect.
  - Hit detection consists of the following:
    - An enemy that is visible on-screen will be hit.
    - An enemy that has direct line of sight from Ember will be hit, even if off-screen.
- Has a cast delay of about 0.7 seconds.

Kit Interactions

- Each cast of Fire Blast decreases Immolation's rate of heat generation by 2% per second, while also removing 50% heat.
- Fire Blast's enemy armor reduction scales linearly with Immolation's heat level, with 0 percent heat resulting in the minimum value being removed and 100 percent heat resulting in the maximum.
- Fire Blast's energy cost decreases with Immolation's heat down to 25 energy cost at maximum heat.

Helminth

- Subsuming Ember to the Helminth will offer Fire Blast and its augments to be used by other Warframes.
  - Armor reduction per cast is capped at 75%, achievable with 100% Ability Strength.
  - Healing Flame will not generate Overguard on other Warframes.

Augment

- Main article: Healing Flame

Healing Flame is a Warframe Augment Mod for Ember that heals the player for each enemy hit by Fire Blast. This healing will be converted to Overguard if received while at maximum health.

Rank | Healed Amount | Overguard Cap | Cost
0 | 10-20 | 10,000 | 6
1 | 15-30 | 10,000 | 7
2 | 20-40 | 10,000 | 8
3 | 25-50 | 10,000 | 9

- Main article: Purifying Flames

Purifying Flames is a PvE and Conclave Warframe Augment Mod for Ember's Fire Blast that causes Ember and her allies who enter the fire to have debuffs removed and grant them temporary status immunity.

Rank | Status Immunity Duration | Cost
0 | 1s | 6
1 | 2s | 7
2 | 3s | 8
3 | 4s | 9

Tips & Tricks

- Fire Blast decreases heat gauge and heat generation, helping to negate the negative effects of overheat.
  - Alternatively, deactivating Immolation resets the heat gauge.
- The armor strip is permanent and is not affected by Ability Duration decreases from Fleeting Expertise and Transient Fortitude.
  - Decreasing Ability Duration does impact Ember's other abilities.

Maximization

Immolation level:
Infused?
Healing Flame?
Purifying Flames?

Fire Blast

This ability creates a wave of fire that expands outwards and permanently reduces the armor of enemies hit by 50% - 100%. The armor reduction depends linearly on the Immolation gauge, with a fully filled gauge resulting in the maximum armor reduction.

Heat

 | 4 75 | Plein Air Tie nearby enemies to floating balloons that douse them with Inkblot. Pop the balloons to send them crashing to the ground, splashing damage on nearby enemies. Introduced in Update 42.0 (2026-03-25) | Strength:100 - 10,000 / 150 - 15,000 / 200 - 20,000 / 250 - 25,000 ( Corrosive damage) 35% / 40% / 45% / 50% (Defense Reduction)
Duration:10s / 15s / 20s / 25s
Range:12m / 14m / 16m / 18m (Radius) 3m / 4m (Splash radius)

Info

- Follie expends 75 energy to tangle enemies that are on-screen or in Line of Sight from her within 12 / 14 / 16 / 18 meters to ink balloons and lifts them high into the air, while coating them in Inkblot, reducing their Armor and Shields by 35% / 40% / 45% / 50%, and causing them to float helplessly in mid-air for 10 / 15 / 20 / 25 seconds. Balloons can be popped by player attacks or jumping on top of them, causing the carried enemy to plummet to the ground. Upon colliding with the ground, the dropped enemy and all other enemies 3 / 3 / 4 / 4 meters are splashed with Inkblot and receive a minimum of 100 / 150 / 200 / 250 Corrosive damage to a maximum of 10,000 / 15,000 / 20,000 / 25,000 Corrosive damage based on fall distance and the enemy's health; radial fall damage diminishes with distance from the center. When Plein Air almost expires, the remaining ink balloons slowly lower to the ground until releasing their enemies, inflicting reduced fall damage on impact. Casting Plein Air triggers a brief ability cooldown of 1 second.
  - Enemy armor and shields are fully removed at 200% Ability Strength. With one Corrosive Projection, armor will be fully stripped at 164% Ability Strength.
  - Balloons will lift their targets up until a certain height or until the balloon touches a ceiling.
  - When Plein Air balloons descend, as a falling enemy hits the ground, their splash damage can hit other ballooned enemies, causing a chain reaction.
  - If a player jumps on a balloon, the balloon will pop and the player will bounce upwards and have their double jump/bullet jump refreshed.
  - Enemies that are immune to crowd control, such as bosses or enemies with Overguard, will not ascend but still receive the reduction to their defenses on cast. Additionally, they are tied to an indestructible balloon, which pops shortly thereafter. However, the balloon's only effect is dealing 100 / 150 / 200 / 250 Corrosive damage when it pops. This damage is only dealt to the target and has no Area of Effect.

Kit Interactions

- Shadowgraph objects interact with Plein Air:
  - Thermian RPG and Amphor explosions pop Plein Air balloons.
  - Arc Traps scale their Electricity damage based on enemy Health and Armor, calculated only on the first tick of damage and used for all subsequent ticks. Cast Plein Air on armored enemies zapped at least once by Arc Traps to increase damage dealt by up to 10x (depending on the amount of armor stripped) on the remaining ticks.

Maximization

Plein Air

Bugs

- Does not apply Inkblot on Overguarded enemies.

Ability Strength

 | 4 100 | Avalanche Summons a treacherous landslide of ice that instantly freezes and shatters all enemies in its radius. Introduced in Update 6.0 (2013-01-29) | Strength:800 / 1000 / 1200 / 1500 ( Cold initial damage) 100 / 200 / 300 / 400 ( Cold shatter damage) 60% (armor reduction)
Duration:5 / 6 / 7 / 8 s (freeze duration)
Range:8 / 10 / 12 / 15 m (ability radius) 3 / 3.5 / 4 / 4.5 m (shatter radius)
Misc: 6 ( Cold status procs on cast) 10 ( Cold status procs on pulse)

Info

- Frost expends 100 Energy to crash an avalanche down around him, striking all surrounding enemies within 8 / 10 / 12 / 15 meters and applying 6 Cold Status Effects. Shortly after, an icy pulse rapidly expands over the area, applying 10 Cold Status Effects to freeze enemies in place for 5 / 6 / 7 / 8 seconds and permanently reducing their total armor by 60%, then inflicts 800 / 1000 / 1200 / 1500 Cold damage. If an enemy dies while frozen, they violently shatter upon death, dealing 100 / 200 / 300 / 400 Cold damage to enemies in a 3 / 3.5 / 4 / 4.5 meter radius.
  - Armor is fully removed at 167% Ability Strength. If using a single Corrosive Projection, full armor strip can be achieved at 137% Ability Strength.
  - Shatter damage has 100% falloff over its radius but bypasses obstacles in the environment to strike enemies.
    - The armor reduction is applied after ~1 second of the casting animation has passed, but before the damage is dealt.
- While the avalanche does not affect Storage Containers, the explosion from frozen enemies does.
- Avalanche's casting animation is capped at a 50% bonus Casting Speed.

Augment

- Main article: Icy Avalanche

Icy Avalanche is a Warframe Augment Mod for Frost's Avalanche that grants allies within the Affinity Range Overguard for each enemy hit. A percentage of Frost's armor is also added to the Overguard once per enemy.

Rank | Overguard per enemy | Armor to Overguard Conversion | Cost
0 | 40 | 5% | 6
1 | 45 | 10% | 7
2 | 50 | 15% | 8
3 | 60 | 20% | 9

Tips & Tricks

- With one player using Corrosive Projection, 100% armor strip can be achieved at 137% Ability Strength.
- Avalanche can be used to immobilize large groups of enemies, as even if it does not kill enemies outright it lowers their armor, allowing players to finish off any survivors.
- Avalanche staggers enemies back a small distance when cast, this may result in them being out of range for the freeze and subsequent damage when at the edge of the area of effect, so it is important to make sure you group enemies effectively before casting.
- This ability can damage enemies through walls. Using Avalanche while pressed against a wall can clear a room without even entering.
- Avalanche can hit enemies who are above or below Frost's position.
- Arbitration Shield Drones won't dispel the freeze effect from frozen enemies.
- Avalanche can still serve as crowd control even with low Ability Duration, as the Cold status effects are not affected by mods and will stay on the target even when unfreezing (if the freeze duration is shorter than 6 seconds, that is).
- Avalanche's 50% casting speed cap can be achieved with either a max rank Natural Talent, two Amber Archon Shards, or Madurai's Power Transfer.

Maximization

Current Armor:
Icy Avalanche?

Avalanche
Overguard from new targets: | /new enemy
Overguard from repeat targets: | /repeat enemy

Bugs

- Can kill and ragdoll the Stalker.

Ability Strength

 | 3 50 | Thermal Sunder Siphon kinetic energy from the area, charging the battery and inflicting Cold Status on nearby enemies. Hold reverses the process, draining the battery and inflicting Heat Status on nearby enemies. Introduced in Update 25.7 (2019-08-29) | Strength: 75 - 375 / 100 - 500 / 125 - 625 / 150 - 750 ( Cold damage) Duration: 6 / 9 / 12 / 15 s (area duration) 2.5 - 5 / 3 - 6 / 3.5 - 7 / 4 - 8 s (status duration) Range: 6 / 8 / 10 / 12 m (initial radius) 3 / 4 / 5 / 6 m (final radius) Misc:10% (battery charge) 1 ( Cold status proc on cast) 9 ( Cold status procs on Cold afflicted enemy) 10 ( Cold status procs from Redline) ≤100% (enemy armor reduction from Redline on Heat combination) 4 (limit of areas per element) Strength: 150 - 750 / 200 - 1000 / 250 - 1250 / 300 - 1500 Heat damage) Duration: 6 / 9 / 12 / 15 s (area duration) 2.5 - 5 / 3 - 6 / 3.5 - 7 / 4 - 8 s (status duration) Range: 6 / 8 / 10 / 12 m (initial radius) 3 / 4 / 5 / 6 m (final radius) Misc:10% (battery drain) 1 ( Heat status proc on cast) 100% ( Heat ignite damage bonus) 100% ( Heat ignite chance from Redline) ≤100% (enemy armor reduction from Redline on Cold combination) 4 (limit of areas per element)
Strength: 75 - 375 / 100 - 500 / 125 - 625 / 150 - 750 ( Cold damage)
Duration: 6 / 9 / 12 / 15 s (area duration) 2.5 - 5 / 3 - 6 / 3.5 - 7 / 4 - 8 s (status duration)
Range: 6 / 8 / 10 / 12 m (initial radius) 3 / 4 / 5 / 6 m (final radius)
Misc:10% (battery charge) 1 ( Cold status proc on cast) 9 ( Cold status procs on Cold afflicted enemy) 10 ( Cold status procs from Redline) ≤100% (enemy armor reduction from Redline on Heat combination) 4 (limit of areas per element)
Strength: 150 - 750 / 200 - 1000 / 250 - 1250 / 300 - 1500 Heat damage)
Duration: 6 / 9 / 12 / 15 s (area duration) 2.5 - 5 / 3 - 6 / 3.5 - 7 / 4 - 8 s (status duration)
Range: 6 / 8 / 10 / 12 m (initial radius) 3 / 4 / 5 / 6 m (final radius)
Misc:10% (battery drain) 1 ( Heat status proc on cast) 100% ( Heat ignite damage bonus) 100% ( Heat ignite chance from Redline) ≤100% (enemy armor reduction from Redline on Cold combination) 4 (limit of areas per element)
Subsumable to Helminth

Info

- Gauss expends 50 energy to manipulate the kinetic energy around him to create an area of extreme temperatures with an initial radius of 6 / 8 / 10 / 12 meters, which gradually shrinks to a final radius of 3 / 4 / 5 / 6 meters and lasts for 6 / 9 / 12 / 15 seconds.
  - Tap the ability key (default 3 ) to absorb kinetic energy, charging battery power by 10% to inflict a Cold proc on all enemies within range, lasting for 2.5 - 5 / 3 - 6 / 3.5 - 7 / 4 - 8 seconds based on battery. Enemies caught in the area creation receive 75 - 375 / 100 - 500 / 125 - 625 / 150 - 750 Cold damage based on battery with guaranteed Status Effect; enemies lingering inside the area also receive damage per second, which diminishes in amount with the size of the area. When cast on enemies already affected by Cold proc, they receive 9 additional Cold status procs to be instantly frozen solid for the full status duration.
  - Hold down the ability key to expend kinetic energy, draining battery power by 10% to inflict a Heat proc on all enemies in range, lasting for a minimum duration of 2.5 - 5 / 3 - 6 / 3.5 - 7 / 4 - 8 seconds based on battery. Enemies caught in the area creation receive 150 - 750 / 200 - 1000 / 250 - 1250 / 300 - 1500 Heat damage based on battery with guaranteed Status Effect; enemies lingering inside the area also receive damage per second, which diminishes in amount with the size of the area. When cast on enemies already affected by Heat proc, Thermal Sunder deals its normal damage plus the damage per second of the current Heat proc.
    - The resulting heat proc will scale with the total damage of the Thermal Sunder cast, allowing repeated casts to exponentially scale the damage.
  - Damage per second has a moderate chance to stagger light enemy units within the area.
  - Enemies already afflicted with a status effect of the same type will have it reapplied; its status duration uses the battery power level at the time of the new Thermal Sunder cast.
- Casting Thermal Sunder of the opposite damage type on enemies already afflicted with Cold or Heat procs, combines the damage type into Blast. Affected enemies first have the initial status effect removed, receive the new status effect, they also receive a Blast proc and deals damage based on the mode being used plus the damage of the canceled status.
  - Blast damage is given by: Heat Proc Damage⋅Remaining Proc Duration+Damage of Canceling Cast
    - Remaining Proc Duration is based on the duration of the proc on the enemy being canceled, i.e. casting a Heat Thermal Sunder on an enemy affected by a Cold will use the remaining duration of the Cold proc.
  - For example: Casting a Heat Thermal Sunder at 80% battery followed by a Cold Thermal Sunder at 70% battery with 6 seconds left on the Heat proc will deal: [300 + 0.8 * (1500 - 300)] * 6 + [150 + 0.7 * (750 - 150)] = 8,130 damage.
    - At 100% battery with Redline, this formula can be simplified if the ability is recasted immediately: (12000 * Ability Duration + 750) * Ability Strength
  - The order in which the elemental procs are combined changes the direction in which enemies within the ability area are knocked back by the Blast proc. Casting Cold first then Heat will knock enemies outwards, while casting Heat first then Cold will pull enemies in towards the player.
  - When casting both elements, the elemental proc cast second will override and replace the first element already present, e.g. if enemies were affected by the Cold area first, casting Heat proc on them will remove the Cold proc and replace it with Heat.
- Can be recast while active to create new Cold or Heat sunder areas. Gauss may create up to 4 distinct areas of either element, resulting in only 8 total distinct areas active at once. Casting Thermal Sunder in a new area after reaching the maximum of Heat or Cold areas will remove the oldest area of corresponding element.

Kit Interactions

- Mach Rush through a Thermal Sunder area to add its Cold or Heat damage to Mach Rush's knockdown and shockwave explosion.
- Thermal Sunder gains bonuses to its status effects when Redline is active and above the redline battery charge (>80%):
  - Cold mode applies 10 Cold status procs to instantly freeze enemies solid.
  - Heat mode's damage is doubled. This doubling is applied after the bonus damage from active heat procs on a target, allowing consecutive casts to do double the previous cast's damage.
  - Combining Heat and Cold on an enemy permanently strips their Armor, up to a maximum of 100% with a full battery charge, before damage is dealt.
    - Armor reduction scales linearly from 0% armor reduction at 80% battery to 100% armor reduction at 100% battery.
      - Because the reduction scaling starts from 80%, Corrosive Projection decreases the battery requirement to 96.4% to fully strip armor.

Helminth

- Subsuming Gauss to the Helminth will offer Thermal Sunder and its augments to be used by other Warframes.
  - The damage dealt by Subsumed Thermal Sunder is equivalent to 50% of Gauss's battery: 225 / 300 / 375 / 450 Cold damage and 450 / 600 / 750 / 900 Heat damage.
  - However, the damage scaling from Heat status is capped to 10x of the ability's damage.

Augment

- Main article: Thermal Transfer

Thermal Transfer is a Warframe Augment Mod for Gauss's Thermal Sunder, increasing elemental damage for himself and allies within range.

Rank | Elemental Damage | Duration | Cost
0 | +40% | 18s | 6
1 | +50% | 22s | 7
2 | +60% | 26s | 8
3 | +75% | 30s | 9

Maximization

Battery level:
Thermal Transfer?
Infused?

Thermal Sunder

Cold

Heat

Redline

Blast

 | 3 | Pulverize Grendel curls into a ball. He heals over time as he rolls, knocking over anyone in his path. Jumping slams Grendel into the ground and generates a damaging shockwave. Introduced in Update 26.0 (2019-10-31) | Strength:25 ( Toxin damage per second) 50 / 100 / 150 / 200 (self heal per second) 20 / 30 / 40 / 50% (armor strip) 250 - 1,000 / 250 - 1,200 / 500 - 1,500 / 500 - 2,000 ( Impact damage on collision) 50 - 200 / 100 - 300 / 100 - 400 / 150 - 500 ( Impact damage on ground slam)
Duration:N/A
Range:2 - 6 / 3 - 8 / 4 - 10 / 5 - 15 m (ground slam radius)
Misc: 2.5 - 5 m (collision radius) 100% ( Impact status chance on slam)

Info

- Grendel consumes 0 energy to curl up into a roving sphere that changes his movement controls into a directional physics-based roll. As he roves, Grendel gorges upon enemies inside his stomach, inflicting 25 Toxin damage per second while healing him 50 / 100 / 150 / 200 health per second over 5 seconds which slowly diminishes to half its value after another 5 seconds.
  - Grendel has a base speed of 12 m/s during Pulverize. Sprinting increase this 30 m/s. He can only perform a limited selection of parkour Maneuvers, such as jump, double jump, and wall jump during Pulverize.
  - Grendel is unable to utilize weapons and cannot cast any Helminth subsumed abilities during Pulverize.
  - Activating the ability to enter the sphere form will cause Grendel to automatically drop carriables, such as datamasses.
  - Grendel will accelerate faster when rolling downhill and ricochet off of terrain obstacles.
  - Pulverize consumes 3 energy per second on an empty stomach while active and will remain active until Grendel's energy is depleted or the ability is deactivated by pressing the ability key again. Should Grendel run out of energy during Pulverize, he will automatically unfurl and become stunned in a dizziness animation for 2 seconds.
    - While Pulverize is active, Grendel can replenish energy with flat energy gains, such as: Energy Orbs, Orokin Void Death Orb's energy restores, Rage, Hunter Adrenaline, Spellbound Harvest, Arcane Energize, and Emergence Dissipate's Energy Motes.
    - While Pulverize is active, Grendel can not replenish energy using Energy Vampire, Rift Plane's innate energy regeneration, or Squad Energy Restores.
    - While Pulverize is active, but not draining energy, Grendel can replenish energy using Rally Point, Energy Siphon, and Wellspring. If Grendel has no more enemies in his stomach the energy replenishment from these effects will halt until he refills his belly.
- Grendel tramples over his enemies with varying levels of power and reach, depending on the techniques he uses and the fuel within.
  - Grendel's mobility in Pulverize can be increased by adding to Movement Speed, Sprint Speed, and mods that affect jumping, such as Motus Signal and Anti-Grav Array. Pulverize is not affected by changes to parkour velocity or bullet jump speed.
  - Warframe Abilities that buff movement speed like Volt's Speed will also work to increase Grendel's speed while under the influence of Pulverize.
  - Movement and sprint bonuses from weapons, such as those from Ceramic Dagger, Amalgam Serration, and Incarnon bonuses, will affect Grendel during Pulverize.

- In sphere form, Grendel constantly emits a kinetic field with a 2.5 - 5 meter scaling radius, which reacts to his movement to inflict 250 - 1,000 / 250 - 1,200 / 500 - 1,500 / 500 - 2,000 Impact damage and permanently removes 20% / 30% / 40% / 50% armor against enemies coming into range. Enemies colliding with Grendel receive damage and are knocked away from his path.
  - Impact damage on collision benefits from Ability Strength and amount of enemies stored, increasing by +60% per stored enemy, up to 400% effect with 5 stored enemies.
    - With a maxed Intensify, 5 eaten enemies, Grendel will deal 500 × (1 + 5 × 60%) × (1 + 0.3) = 2,600 Impact damage.
  - Armor is fully removed at 200% Ability Strength.
  - Impact damage on collision does not occur if Grendel is stationary.
- Damage and radius changes as enemies enter and exit Grendel's stomach. His sphere model also enlarges and shrinks based on the eaten enemy count.

- Landing on surfaces from midair causes Grendel to slam into the ground, inflicting 50 - 200 / 100 - 300 / 100 - 400 / 150 - 500 Impact damage to enemies within a 2 - 6 / 3 - 8 / 4 - 10 / 5 - 15 meter scaling radius, including those in his gut.
- Enemies within the slam radius have their armor reduced by 20% / 30% / 40% / 50%, however enemies in his gut will not have their armor reduced.
  - Impact damage on ground slam benefits from Ability Strength and amount of enemies stored, increasing by +70 Impact (+46.6%) per stored enemy up to 500 Impact damage (333% effect).
    - With a maxed Intensify, 5 eaten enemies, Grendel will deal (150 + 5 × 70) × (1 + 0.3) = 650 Impact damage.
- Damage and radius change as enemies enter and exit Grendel's stomach.

Kit Interactions

- Pulverize drains 0 energy when Feast stores enemies in his stomach. The sphere also enlarges with engorged enemies, increasing the collision and ground slam's damage and radius.

Augment

- Main article: Catapult

Catapult is a Warframe Augment Mod/Exilus Mod that lets Grendel launch himself in a given direction with Pulverize.

Rank | Energy cost | Cost
0 | 15 | 6
1 | 10 | 7
2 | 7.5 | 8
3 | 5 | 9

Maximization

Enemies in stomach:
Catapult?

Pulverize

Ability Strength

 | 4 | Regurgitate Violently puke out a bile soaked enemy from Grendel's gut, turning the consumed into a toxic projectile. Nearby enemies are slowed and have their armor dissolved by the bile. Introduced in Update 26.0 (2019-10-31) | Strength:1,000 / 1,250 / 1,600 / 2,000 ( Toxin damage on impact) 75% (armor strip)
Duration:N/A
Range:3 / 4 / 5 / 6 m (splash radius)
Misc: ? m/s (projectile speed) 10% (bonus damage from launched enemy's max health) 80% (slow) 6 s (slow duration) 0.61s (cast time)

Info

- Grendel convulses his stomach as his maw snaps open, expending 50 energy to violently expel out an eaten enemy soaked in acidic bile from inside his gut. The enemy is Ragdolled and launched toward the aiming reticle as a living projectile, traveling at a speed of ? meters per second in an arcing trajectory. On direct collision with other enemies, obstacles or surfaces, the launched enemy and all targets within a radius of 3 / 4 / 5 / 6 meters around the impact point have 75% of their armor permanently removed, then suffer 1,000 / 1,250 / 1,600 / 2,000 damage plus 10% of the launched enemy's max health as Toxin damage with 100% Toxin status chance, and are slowed by 80% which slowly diminishes over 6 seconds.
  - Regurgitate will expel the enemy that has been in Grendel's stomach the longest (i.e. a "first in, first out" system).
    - Eaten enemies will appear in Grendel's stomach UI slots in the same order every time: Middle, top, right, bottom, then left. This order can be used to predict which enemy will be expelled next.
  - Explosion does not require line of sight to damage enemies.
  - Armor removal applies before damage is dealt.
    - Armor is fully removed at 134% Ability Strength.
  - Regurgitate's damage on enemy impact and radial Toxin damage benefits from Ability Strength and enemy health using the following expression: Total Toxin Damage = Toxin Damage × (1 + Ability Strength) + 10% × Max Enemy Health
    - With a maxed Intensify and an eaten enemy with 38,670 max health, Regurgitate will deal 2,000 × (1 + 0.3) + 10% × 38,670 = 6,467 Toxin damage.
  - Explosion has no radial damage falloff, dealing full damage even at the edge of its range.

Kit Interactions

- Regurgitate expels out the next available enemy swallowed by Feast, requiring at least 1 enemy inside Grendel's gut to be cast.

Augment

- Main article: Gastro

Gastro is a Warframe Augment Mod for Grendel's Regurgitate that causes spat out enemies to bounce and create Gas clouds.

Rank | Duration | Cost
0 | 3s | 6
1 | 5s | 7
2 | 6s | 8
3 | 8s | 9

Maximization

Gastro?

Regurgitate

Feast

Ability Strength

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

- Main article: Hydroid/Abilities

Corrosive

Tempest Barrage

Tidal Surge

Tentacle Swarm

Corrosive

Plunder

Corrosive

Corrosive

 | 3 50 | Ophanim Eyes Jade summons an accusatory gaze that slows nearby enemies and dissolves their Shields and Armor. When the gaze falls upon allies, they can be revived from a distance. Introduced in Update 36.0 (2024-06-18) | Strength:20 / 30 / 40 / 50 Heat damage 4 / 6 / 8 / 10 % armor and shield strip per second
Duration:15 / 20 / 25 / 30 s
Range:20 m
Misc: 70° cone angle 6 / 9 / 12 / 15 % slow per second 90% slow cap 0.5s damage ticks Heat status after defense strip Ally bleedout revival at range
Subsumable to Helminth

Info

- Jade expends 50 energy to assemble her beloved Ophanim orbitar choir, accusing all who stand within her Line of Sight in a 20 meter conical gaze with an angle of 70° for 15 / 20 / 25 / 30 seconds. Gazing upon enemies inflicts 20 / 30 / 40 / 50 Heat damage every 0.5 seconds, 6% / 9% / 12%/ 15% Slow per second stacking up to a cap of 90%, and permanently lose 4% / 6% / 8% / 10% of their Armor and Shields per second. Once defenses have been removed, the enemy receives a Heat Status Effect. Gazing upon fallen allies in Bleedout state will halt their bleedout timer and gradually gain revive progress until full revival.
  - Ophanim Eyes hits every 0.5 seconds, with the slow and defense strip applying for half of their value every hit.
  - Holding the ability button (default 3 ) while active will cancel the ability. Tap-cast while active to refresh duration to full.
  - Each Ophanim Eye projects a light streak toward the reticle to indicate Jade's conical gaze direction.
  - The slow effect does not affect enemies with Overguard, but the defense strip and Heat damage and status do.
  - While not in Ophanim Eye's area of effect, slowed enemies gradually regain speed.
  - Though the Heat status is applied only once upon fully removing defenses, enemies with Shields will regain shields after full depletion, allowing Ophanim Eyes to apply another Heat status.
    - Since the slow effect extends enemy shield recharge delay, fully slowed enemies will only regain shields once every 30 seconds.
  - When in Operator mode, Ophanim Eyes remain active and stares at the last direction before Transference from the Warframe's location.

Kit Interactions

- Symphony of Mercy's Power of The Seven Ability Strength bonus enhances Ophanim Eyes' Heat damage and defense strip per second.
- Ophanim Eyes can revive allies during Glory on High, which disables any Use key (default X ) interactions.

Helminth

- Subsuming Jade to the Helminth will offer Ophanim Eyes and its augments to be used by other Warframes.
  - However, Subsumed Ophanim Eyes will not have the ability to revive allies from Bleedout.

Maximization

Enemy has Judgment?

Ophanim Eyes

Bugs

- The slow effect applies to Mind Controlled targets.
- If an enemy was affected by the slowing effect when it entered a Nullifier Crewman's or Demolisher's Nullifier field, the enemy becomes permanently immune to the slow effect, even if Ophanim Eyes expires and is recast.
  - The defense strip and Heat damage and Status Effect still apply.
- If an enemy is within a non-allied Nullifier field (e.g., a Grineer unit within a Corpus Nullifier Crewman's field), the defense strip and slow effect still apply, but the Heat damage and status do not.

- Main article: Fracturing Crush

Crush

Ability Strength

 | 3 75 | Polarize Emit an energy pulse that depletes enemy shields and armor as it restores ally shields. Debris left over from the pulse becomes Polarize Shards. Nearby Polarize Shards orbit Mag and cut enemies, inflicting Slash Status Effect. Introduced in Vanilla (2012-10-25) | Strength:250 / 300 / 350 / 400 ( True damage and shield restoration) 1x / 1.5x / 2x / 2.5x (explosion damage multiplier as Magnetic damage) 50 (Shard Puncture and Slash damage)
Duration:5 s (pulse travel time)
Range:8 m (initial pulse radius)
Misc: 5.9 m/s (pulse travel speed) 3 m (Shard pickup radius) 1 m (Shard damage radius)

Info

- Mag expends 75 energy to emit a spherical pulse of magnetic energy from herself with an initial radius of 8 meters. The pulse expands outwards for 5 seconds, at a constant rate of 5.9 meters per second, reaching a total radius of 37.5 meters. If the pulse comes into contact with an enemy that has shields, the pulse will drain up to 250 / 300 / 350 / 400 of them. If the enemy has armor, it will be permanently drained by up to 250 / 300 / 350 / 400 points with the enemy additionally suffering True damage equal to the amount removed. Any allies that come into contact with the pulse will have their shields restored by up to 250 / 300 / 350 / 400.
  - Restores Mag's own shields, in addition to fellow Tenno, Companions, Shadows of the Dead, hostages, Specters, Sortie Tenno Operatives, static mission objectives (such as Cryopods and Excavators), hacked MOAs (spawned from MOA Cabinet Spawners), and Mind Control targets.
  - Shield restore does not flow into Overshields.
  - Initial radius and traveled distance are summed to: Total Radius = (1 + Ability Range) × 8 + (1 + Ability Duration) × 5 × 5.9.
    - With maxed Stretch and Continuity, rank-3 Polarize will have a total radius of (1 + 0.45) × 8 + (1 + 0.3) × 29.5 = 49.95 meters.
  - Pulse can bypass obstacles to damage enemies.
    - Enemies that are spawned within the radius of the pulse will be damaged the same as if they were touched by the pulse itself.
    - Enemies can only be damaged by the pulse once, even if they leave the pulse radius and are touched by it again.
  - Cast animation of 1 second, affected by Casting Speed.
  - Shields must be completely drained from a target before a new Polarize cast can deplete armor as well.
- All drained enemies will produce a violent outburst of magnetic energy inflicting 100% / 150% / 200% / 250% of the drained shields or armor as Magnetic damage to all other enemies within a 2.5 / 3 / 3.5 / 4 meter radius of them.
  - Explosion radius is increased by 0.5̅5 meters for each meter the pulse grows outwards after the initial radius.
    - Maximum explosion radius is (4 + 16.4) meters when hitting an enemy at the pulse's maximum travel range.
    - Explosion will not target enemies behind obstacles in the environment.
  - Explosion damage diminishes with distance.
  - Explosion can hit objects, such as Containers and Resource Nodes.
  - Enemies who have been drained are not damaged by their own explosion, but they can be damaged by nearby enemies who were also drained.
- All drained enemies drop one Polarize Shard that lingers for 30 seconds, with a 50% chance to drop two. These Shards are automatically picked up by Mag once she is within 3 meters of them, and will rapidly orbit her to attack enemies within 1 meter. Polarize Shards inflict damage equal to 50 plus 25% total shields or armor drained, evenly split between Puncture and Slash damage, and with 100% status chance.
  - Shard damage counts as weapon damage, and as such, can be affected by universal weapon buffs like Grendel's Nourish and Arcane Arachne.
  - Shard damage has 0% critical chance, 1.0x critical multiplier, and 100% status chance.
- Polarize's visual effects, including shards, are affected by Mag's chosen energy color.
- Casting Polarize is a One-Handed Action that can be done while performing many actions without interrupting them, including reloading, charging, shooting, and moving (either sprinting or sliding).
  - Can be used in mid-air, but not while on a zipline.

Kit Interactions

- Pull can bring Polarize Shards to Mag.
- Magnetize will absorb Polarize Shards, trapping the Shards within and allowing them to do immense damage.
  - Shards will return to their previous state when Magnetize ends.

Augment

- Main article: Counter Pulse

Counter Pulse is a Warframe Augment Mod for Mag's Polarize that jams enemy weapons and disables Robotic enemies for a set duration.

Rank | Weapon Jam and Robotic Disable Duration | Cost
0 | 2s | 6
1 | 2.5s | 7
2 | 3s | 8
3 | 4s | 9

Tips & Tricks

- Can be used to restore shields to stationary defense objectives such as Cryopods and Excavators.
- Explosions can damage or break objects such as Containers, Resource Nodes, Laser Plates, and Rotation Plates in the Orokin Tower, given a drained enemy was close enough to them.
- Shards can inflict high amounts of Slash procs, if used in conjunction with Magnetize they can cause immense Bleed damage.
  - Pairing this combo with Nourish will grant Shards Viral damage and status, allowing you increase their Bleed damage even further.
- The damage portion of Polarize is useless in missions where enemies completely lack shields and armor.
- At 139% strength, Polarize will fully replenishes Mag's shields.
- Due to the high base shield replenishment, using Catalyzing Shields will drop down your shields to 111 on max rank, making negative strength still fully replenish at percentages as low as 30% strength.

Maximization

Counter Pulse?

Polarize

 | 2 75 | Terrify Cast fear into the hearts of nearby enemies, causing them to run away in terror. Introduced in Update 10.0 (2013-09-13) | Strength:7 / 12 / 15 / 20 (affected enemies) 30 / 40 / 50 / 60 % (armor reduction)
Duration:10 / 15 / 20 / 25 s
Range:5 / 10 / 12 / 15 m
Subsumable to Helminth

Info

- Nekros expends 75 energy to release a psychic blast that causes up to 7 / 12 / 15 / 20 enemies within 5 / 10 / 12 / 15 meters to enter a state of panic for 10 / 15 / 20 / 25 seconds. While panicked, enemies will not attack and will haphazardly flee, exposing themselves and temporarily reducing their Armor by 30% / 40% / 50% / 60%.
  - Armor is fully removed at 167% Ability Strength. If using a single Corrosive Projection, full armor strip can be achieved at 137% Ability Strength.
  - Enemies unaffected by Terrify are prioritized upon subsequent casts.
  - Bosses are unaffected by this ability.
- Can be recast while active and can refresh the duration on already affected units in the cast range.
- Subsuming Nekros to the Helminth will offer Terrify and its augments to be used by other Warframes.

Augment

- Main article: Creeping Terrify

Creeping Terrify is a Warframe Augment Mod for Nekros' Terrify that slows down affected enemies.

Rank | Movement Speed Reduction | Cost
0 | 30% | 6
1 | 40% | 7
2 | 50% | 8
3 | 60% | 9

Tips & Tricks

- Can be used to scare enemies off when the Cryopod is hoarded by enemies or used when you need to revive teammates stranded in a horde.
- Fully works on Drones in the sense that the AI will attempt to turn away for its duration and also does not trigger alarms even when within their line of sight.
- With a low Power Strength build, it is still possible to affect a large room of enemies, it requires only the appropriate amount of casts.

Maximization

Creeping Terrify?

Terrify

Ability Strength

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

This ability releases 6 telekinetic bolts that temporarily removes armor by 80% from up to 6 enemies in a single cast. At 125% Ability Strength, Psychic Bolts can remove all armor.

 | 1 25 | Smite Focuses deadly energy within a target, dealing massive damage and removing all of its defenses, including Overguard. Enemies near the target also take a portion of the damage. Introduced in Update 11.5 (2013-12-19) | Strength:150 / 200 / 300 / 500 ( Radiation damage) 20% / 25% / 30% / 35% (percentage damage) 10% (AoE percentage damage)
Duration:N/A
Range:20 / 30 / 40 / 50 m (cast range) 4 / 5 / 5 / 6m (AoE range)
Misc: 75% (percentage damage cap) 30% (AoE percentage damage cap) 10 ( Radiation stacks) 100% (initial target Armor and Overguard removal)
Subsumable to Helminth

Info

- Oberon expends 25 energy to smite a single enemy with hallowed light up to 20 / 30 / 40 / 50 meters away, removing 100% of the target's Overguard and Armor, inflicting 20% / 25% / 30% / 35% of their current Health, Shields, and 150 / 200 / 300 / 500 as Radiation damage, while also applying 10 Radiation status effects and blinding them. Enemies within 4 / 5 / 5 / 6 meters of the main target are dealt 10% of the main target's current health, shields and 150 / 200 / 300 / 500 as Radiation damage, and receive Stagger.
  - Percentage damage on main target is capped at 75%, achievable with 215% Ability Strength.
  - AoE percentage damage is capped at 30%, achievable with 300% Ability Strength.
  - Blinded enemies are opened to Melee Finishers.
  - When cast onto a group of enemies, Smite prioritizes targeting Eximus.
- Smite is a one-handed ability and as such will not interrupt full actions such as reloading, shooting, or charging weapons.

Kit Interactions

- Smite instantly applies maximum Radiation procs to its target, maximizing the damage the target will take from Reckoning.

Helminth

- Subsuming Oberon to the Helminth will offer Smite and its augments to be used by other Warframes.
  - However, Subsumed Smite's percentage damage cap is reduced to 50% and the AoE percentage damage cap is reduced to 20%, achievable with 143% and 200% Ability Strength respectively.

Augment

- Main article: Smite Infusion

Smite Infusion is a Warframe Augment Mod for Oberon that allows Smite to be held on cast, creating a wave of energy traveling outward from the user that temporarily grants the caster and nearby allies additional Radiation damage to all attacks.

Rank | Radiation Damage | Duration | Range | Cost
0 | 50% | 28s | 15m | 6
1 | 65% | 32s | 15m | 7
2 | 80% | 36s | 15m | 8
3 | 100% | 40s | 15m | 9

Tips & Tricks

- There are numerous ways to increase the damage of Smite past the 75% enemy current health cap, either by applying damage vulnerability to enemies or by increasing your ability damage using buffs such as Roar.
  - Notably, emerald, violet and topaz Archon shards set to increase ability damage on enemies applied by their respective status effect can be used to increase Smite's damage to 100%, instantly killing most common and Eximus enemies with no damage vulnerability debuffs. Topaz Archon Shards are recommended as Oberon's abilities deal primarily Radiation status effects.
    - The minimum amount of bonus ability damage required to reach 100% smite damage is +33%, achieved by 1 Tauforged shard + 2 regular shards, or alternatively 4 regular shards.
  - Using the Roar method and no Archon shards, 185% Ability Strength is required to deal 100% current enemy health.
    - If Smite is subsumed onto Rhino instead, 200% Ability Strength is required to deal 100% current enemy health.
  - Against enemies resistant to Radiation such as Orokin or Anarchs, significantly more Ability Strength with Roar is required. With 0, 1, 2, 3, 4, or 5 Tauforged shards, at least 556%, 440%, 351%, 280%, 223%, and 203% Ability Strength is required, respectively.
    - Using Precision Intensify with Roar as the 4th ability, only 466% Ability Strength is required.
    - Higher ability strength can be easier to achieve in the Undercroft.
- The 10 stacks of Radiation status that this ability inflicts on enemies can enable the effects of status-related Arcane Enhancements, such as Primary Debilitate, Secondary Irradiate and Universal Fallout.

Maximization

Smite Infusion?
Infused?

Smite
AoE damage: | % of target's Health

Bugs

- The Severed Warden takes no damage from this ability.

This ability permanently removes all armor from a single target.

 | 4 100 | Reckoning Lifts enemies into the air and then hurls them down with conviction, removing their Armor. Enemies hit by this ability will grant Oberon additional Armor and have a chance to spawn a Health Orb when they die. Introduced in Update 11.5 (2013-12-19) | Strength:10% / 20% / 30% / 60% (armor reduction) 6000 / 6500 / 7000 / 7500 ( Radiation damage) 450 / 550 / 650 / 750 (damage per Radiation status effect) 4 / 6 / 8 / 10 (bonus armor per enemy) 2 / 3 / 4 / 5 (bonus armor per Radiation status effect)
Duration:15 / 20 / 25 / 30 s (bonus armor duration)
Range:8 / 10 / 12 / 15 m (cast radius)
Misc: 25% / 35% / 45% / 50% (health orb chance) 1000 (bonus armor cap)

Info

- Oberon expends 100 energy to lift all enemies within 8 / 10 / 12 / 15 meters and in direct Line of Sight up into the air and violently slam them to the ground, permanently reducing their Armor by 10% / 20% / 30% / 60% before dealing 6000 / 6500 / 7000 / 7,500 Radiation damage, plus an additional 450 / 550 / 650 / 750 damage per Radiation Status Effect.
  - Applies Radiation and Knockdown procs.
  - An enemy hit by Reckoning and then killed from any source has a 25% / 35% / 45% / 50% chance of spawning a Health Orb.
  - Oberon gains 4 / 6 / 8 / 10 Armor per enemy hit plus 2 / 3 / 4 / 5 Armor per Radiation proc, up to a maximum of 1000 bonus Armor, for 15 / 20 / 25 / 30 seconds.
    - If Reckoning affects enemies on recast, the bonus armor values are replaced by the new values, otherwise the bonus values will not change and the duration will not be refreshed.
  - Enemy armor is fully removed at 167% Ability Strength.

Kit Interactions

- Increased Health Orb generation provides stacks for Oberon's Righteous Negation.
- Smite instantly applies maximum Radiation procs to its target, maximizing the damage the target will take from Reckoning.
- Smite Infusion adds Radiation damage to your weapon, allowing your weapon attacks to apply status procs that will boost Reckoning's damage.
- Hallowed Ground and Hallowed Reckoning rapidly apply Radiation procs to boost Reckoning's damage.
- Bonus Armor can be multiplied and shared with Renewal.

Augment

- Main article: Hallowed Reckoning

Hallowed Reckoning is a Warframe Augment Mod for Oberon's Reckoning that makes enemies hit drop patches on the ground, dealing Radiation damage over time to enemies and providing armor to allies standing on them with a brief grace period upon stepping off. It also passively increases Reckoning's range.

Rank | Ability Range | Radiation Damage per second | Armor Bonus | Radius | Duration | Armor Bonus Grace Period | Cost
0 | +40% | 150 | 150 | 1.5m | 7s | 3s | 6
1 | +40% | 200 | 180 | 2m | 8s | 3s | 7
2 | +40% | 250 | 210 | 2.5m | 9s | 3s | 8
3 | +40% | 300 | 250 | 3m | 10s | 3s | 9

- Main article: Defiled Reckoning

Defiled Reckoning is a Conclave-exclusive Warframe Augment Mod for Oberon's Reckoning that makes Health Orbs created by kills from Reckoning temporarily invisible to, and unusable by, enemies.

Rank | Duration | Cost
0 | 3s | 6
1 | 5s | 7
2 | 8s | 8
3 | 10s | 9

Tips & Tricks

- With one player using Corrosive Projection, 100% armor strip can be achieved at 137% Ability Strength.
- Use Reckoning when surrounded by a large group of enemies to maximize its offensive effects and health orb generation.
  - Health Orb generation synergizes greatly with Equilibrium, Health Conversion, and Arcane Blessing.
- Equip Hallowed Reckoning and Arcane Universal Fallout to leave zones generating Universal Orbs (works on Arbitration Shield Drones).

Maximization

Hallowed Reckoning?

Reckoning
Added Radiation damage: | / Confusion stack
Added Armor bonus: | / Confusion stack

Ability Strength

- Main article: Temporal Erosion

Grenade Fan

Blaze Artillery

Temporal Anchor

 | 2 25 | Tharros Strike Summon Tharros, the shield of Styanax. Swing Tharros to repel enemies and reduce their shields and armor. Styanax regenerates health for every enemy struck. Introduced in Update 32.0 (2022-09-07) | Strength:250 / 500 / 750 / 1,000 ( Impact damage on swing) 50 / 65 / 80 / 100 HP (health restore per enemy hit) 50 % (defense reduction)
Duration:N/A
Range:9 m
Misc: 9 (number of shields) 135° (horizontal spread angle) 160° (vertical spread angle) 2.5 m (pushback radius) 5 m (pushback distance) 2 s (stun on hit) Melee finisher prompt
Subsumable to Helminth

Info

- Styanax expends 25 energy to sweep his shield Tharros before him to release a horizontal fan of 9 shield projections, which travels a distance of 9 meters toward the reticle, bashing away enemies within a 135 degrees horizontal spread and 160 degrees vertical spread. Enemies within 2.5 meters of Styanax and hit by the shield projections are pushed back for 5 meters, while receiving 250 / 500 / 750 / 1,000 Impact damage, 50% Armor and Shields permanent defense reduction, and becoming Stunned for 2 seconds to prompt melee Finisher (default X ). For each enemy struck, Styanax restores 50 / 65 / 80 / 100 Health points.
  - Defenses are fully removed at 200% Ability Strength.
    - Shield strip removes a percentage of the current maximum value, as such it has diminishing returns on subsequent casts against the same enemies. Armor strip, however, is a percentage of an enemy's total, requiring only two casts at base strength to fully strip.
      - Enemy shields can still regenerate with natural shield regeneration (such as Armis Ulta, Kuva Lich, or Sisters of Parvos) or while affected by regeneration buffs (such as Shield Ospreys).
  - Shield projections possess infinite Punch Through, hitting enemies along their flight path until they fade away at maximum distance.
  - The shield projectiles are only visual effects; the real hit range is a horizontal and vertical degree cone shape.
- Casting Tharros Strike is a full-body animation that interrupts Styanax's grounded movement and other actions.
- Subsuming Styanax to the Helminth will offer Tharros Strike and its augments to be used by other Warframes.

Augment

- Main article: Tharros Lethality

Tharros Lethality is a Warframe Augment Mod for Styanax's Tharros Strike that increases Critical Damage to enemies hit for a duration. The bonus is doubled for Spearguns.

Rank | Critical Damage Bonus | Duration | Cost
0 | +25% | 10s | 6
1 | +50% | 10s | 7
2 | +75% | 10s | 8
3 | +100% | 10s | 9

Tips & Tricks

- With one player using Corrosive Projection, 100% armor strip can be achieved at 164% Ability Strength.
- Tharros Strike opens enemies to finishers briefly. Taking advantage of this requires using the ability at point blank or enemies pinned against a wall.
- Axios Javelin's vortex assists Tharros Strike in en-masse enemy defense reduction and rapid health recovery for Styanax.
- Rally Point taunts enemies to aggressively approach Styanax, potentially grouping inside Tharros Strike's area of effect. Energy regen recovers Tharros Strike's low cost quickly. Tharros Strike's defense reduction permanently cripples enemies for Styanax and rallied allies to kill them for shield recovery.
- Final Stand's Slash and Blast damage effectiveness are enhanced by Tharros Strike's defense reduction.

Maximization

Tharros Lethality?
Using Speargun?

Tharros Strike

Ability Strength

- Main article: Abating Link

Link

Ability Strength

 | 4 100 | Bastille Erect a containment field to capture enemies and suspend them in stasis, stripping their armor and granting it to Vauban and any allies within Bastille's field. HOLD to collapse all Bastilles into a single damaging vortex. Introduced in Update 7.11 (2013-05-17) | Strength:15 ( Blast damage on device hit) 2.5 / 5 / 7.5 / 10 % (armor removal per second) 20 armor per second (bastille armor buff rate) 50 ( Magnetic damage per second in vortex) 40% (vortex status chance)
Duration:8 / 10 / 12 / 15 s (bastille duration) 10 / 12 / 13 / 15 s (vortex duration) 10 s (armor buff duration) 3 s (auto collapse vortex duration)
Range:5 / 7 / 8 / 10 m (capture radius)
Misc: ?% ( Blast status chance) 2x (armor buff rate from armored enemies) ∞ (armor buff duration in field) 1,500 (armor bonus cap) 4 bastille cap 4 vortex cap

Info

- Vauban expends 100 energy to throw a modular device in an arcing trajectory toward the aiming reticle. Upon striking an enemy, the device inflicts 15 Blast damage with a ~10% status chance. Upon contact with a surface, the device erects a Bastille energy containment field that suspends enemies into the air within a 5 / 7 / 8 / 10 meter radius. Armored enemies inside the Bastille's area permanently lose 2.5% / 5% / 7.5% / 10% of their total Armor points per second, while unarmored enemies are simply held captive. Enemies do not have to be suspended by the Bastille to lose armor. Simultaneously, Vauban and allies standing inside the containment field gain 4 armor every 0.2 seconds for each enemy within the containment field, with armored enemies granting 2x more armor. The armor bonus stacks up to 1,500 armor points. Bastille's armor bonus lasts indefinitely while inside the field and remains active for 10 seconds once outside.
  - Bastille armor bonus duration is reset to full when moving into any Bastille containment fields.
  - Suspended enemies are lifted into the air and completely immobilized, allowing headshots to hit their mark without resistance.
- After 8 / 10 / 12 / 15 seconds have elapsed, the containment field automatically collapses into a Vortex singularity for 3 seconds. The Vortex constantly Ragdolls and draws in all enemies within the same radius toward the device, inflicting 12.5 Magnetic damage every 0.25 seconds with 40% status chance per hit.
  - Hold down the ability key (default 4 ) without any containment fields active to throw a new device set to Vortex mode. Hold down the ability key to collapse all active Bastille containment fields into Vortexes. Both methods of manually creating Vortexes resets the new and existing devices to last for 10 / 12 / 13 / 15 seconds.
  - If Bastille fields are in range of each other, manually collapsing them into vortexes causes them to converge on the location of the first active Bastille, based on the order of creation. Enemies and pickups captured by the vortexes will be dragged along toward the new destination.
  - Vortex also draws in Pickups within its radius for convenient collection.
- A maximum of 4 Bastilles and 4 Vortexes can be simultaneously active.
  - Casting a 5th Bastille or Vortex will replace the oldest one of the same type.
- Can be used while performing many actions without interrupting them, including reloading.
- Can be cast multiple times while active.
- If cast while in midair, the casting animation changes with Vauban hovering briefly in the air as he throws the device.
- Bastille is a one-handed action. As such, it can be used while performing various maneuvers and actions without interruption.

Kit Interactions

- Enemies suspended by Bastille or pulled by Vortex passively receive 25% increased damage from Vauban's weapons and abilities.
- Minelayer's Flechette-Tether Orb and Vector-Overdriver Pad can bring enemies into range of Bastille. Enemies tied to Flechette-Tether orbs are released into Bastille's containment field for suspension, freeing the tether to seek new targets.
  - Tethers are not freed if enemies tied to Flechette-Tether Orb are pulled into Bastille's vortex mode, however.
- Photon Strike's targeting beacon is attracted to Bastille's vortex mode, causing the beacon to home in on the device with the laser striking all enemies within range.

Augment

- Main article: Enduring Bastille

Enduring Bastille is a Warframe Augment Mod for Vauban's Bastille that increases Bastille's duration when killing enemies inside it, and increases Vortex's duration for every additional Vortex thrown into it.

Rank | Added Bastille Duration | Added Vortex Duration | Cost
0 | 2s | 50% | 6
1 | 2s | 55% | 7
2 | 2s | 60% | 8
3 | 2s | 70% | 9

Tips & Tricks

- Bastille spawns from a ball that Vauban throws in an arc, so it can be deployed where aimed.
- Unlike many area-affecting abilities, neither Bastille nor Vortex require line of sight to affect enemies. This is disadvantageous for Vortex, as it frequently causes enemies to become stuck in corners or behind doorframes instead of reaching the device, forcing players to go looking for them. To avoid this, Vortex should be placed in open areas.

Maximization

Vauban's Passive?
Enduring Bastille?

Bastille
Armor bonus rate: | /0.2s/enemy
Armor bonus rate from armored enemies: | /0.2s/armored enemy
Vortex Magnetic damage: | /0.25s

Bugs

- If Vauban is playing as client, Photon Strike's beacon will not be attracted to Bastille's vortex even when thrown into its suction range.
- Vortex will slow down allied specters such as the Corrupted Lancer specter.

Enemies suspended by Bastille will be permanently stripped of their armor at a rate of 10% per second.

 | 3 75 | The Lost Cycle through a trio of lost Warframe powers. Accuse manifests a Void fissure to corrupt enemies into allies. Gaze grasps targets in Void tendrils that capture damage and inflict it when the target is released. Deny annihilates with a beam of Void energy, wiping Sentient resistances. Introduced in Update 29.0 (2020-08-25) | Strength: 5 / 6 / 7 / 8 (max targets) Duration: 4 / 8 / 12 / 16 s Range: 5 / 7 / 9 / 11 m Misc:∞ (cast range) Strength: 20 / 30 / 40 / 50 % (defense reduction) Duration: 5 / 8 / 11 / 14 s Range: 10 / 15 / 20 / 25 m (cast range) 6 / 8 / 10 / 12 m (aura radius) Misc:?° (cone angle) 2 (max targets) 100 % (reduction cap) Strength: 1,000 / 2,000 / 3,000 / 4,000 ( Void damage) Duration: 5 / 8 / 11 / 14 s Range: 25 / 30 / 35 / 40 m Misc:? m (beam radius) 100 % (Sentient resistance reset on hit)
Strength: 5 / 6 / 7 / 8 (max targets)
Duration: 4 / 8 / 12 / 16 s
Range: 5 / 7 / 9 / 11 m
Misc:∞ (cast range)
Strength: 20 / 30 / 40 / 50 % (defense reduction)
Duration: 5 / 8 / 11 / 14 s
Range: 10 / 15 / 20 / 25 m (cast range) 6 / 8 / 10 / 12 m (aura radius)
Misc:?° (cone angle) 2 (max targets) 100 % (reduction cap)
Strength: 1,000 / 2,000 / 3,000 / 4,000 ( Void damage)
Duration: 5 / 8 / 11 / 14 s
Range: 25 / 30 / 35 / 40 m
Misc:? m (beam radius) 100 % (Sentient resistance reset on hit)

Info

- Heeding the voices within to harness their powers, Xaku selectively casts one of three abilities originating from the three fallen Warframes. Tapping the ability key freely cycles the selection wheel between the Accuse, Gaze, and Deny sub-abilities. Holding down the ability key (default 3 ) expends 75 energy to cast the selected power.
  - Casting speed is affected by Casting Speed.
  - Tap/hold cast can be inverted in the Settings menu.
  - The Lost's cycle selection wheel appears above Xaku's ability icons. Each ability's duration timer is displayed below their associated sub-ability icons in the wheel.
- Channel the Void to access their lost components' unique powers:

Accuse

- Distorting reality with Accuse, Xaku manifests a Void fissure at the targeted location on the aiming reticle over infinite range. Up to 5 / 6 / 7 / 8 enemies within 5 / 7 / 9 / 11 meters from the fissure become corrupted by Void energy for 4 / 8 / 12 / 16 seconds, stunning them in place then causing them to fight for Xaku and turn on their former allies.
  - Xaku does not require Line of Sight to enemies to corrupt them with Accuse.
  - While Accused enemies are briefly allied with Tenno, they can still be damaged by most sources and affected by some Warframe abilities.
    - Exceptions include Mesa's Peacemaker and Grasp of Lohk's floating weapons.
  - Accused enemies appear on the minimap as allied blue dots.
  - The number of active Accused units is displayed as an icon beside Xaku's shield and health indicators.
- Accused enemies do count toward mission progression (e.g. Defense). They must be slain or their ability duration ended to progress.
- Can be recast while active if under the max targets cap. Recasting on new enemies adds them to the existing number of Accused units up to the cap. Each new Accused unit has its own separate full ability duration.
  - Cannot be recast while at max targets count.
- Casting Accuse is a full-body animation that restricts movement and other actions.
- Xaku's shoulder and arm pieces visually detach and return to position, as Xaku reaches out with their right hand sending the right side pieces into the Void fissure forming at the targeted location. As the Void fissure forms, Void lightning strikes nearby enemies as the ability's area radius becomes briefly visible then fades with the breach's closing, while Xaku's pieces return to their positions on their body.
- Enemies affected by Accuse glow with an upward stream of Void energy that resembles the Vengeful Trickster Ephemera, as well as emitting a Void energy cloud around the shoulders.

Gaze

- Screeching in anguish with voices long lost, Xaku's Gaze freezes an enemy target within 10 / 15 / 20 / 25 meters and a ?° angle cone centered on the aiming reticle. Gazed target becomes entangled in Void tendrils, during which it is disabled, immobile, and Invulnerable to damage for 5 / 8 / 11 / 14 seconds; while captive, the victim stores all damage prevented by its invulnerability and receives it in full when the ability expires. Gazed target also emits a defense reduction aura with a 6 / 8 / 10 / 12 meter radius, which weakens other enemies' maximum Shields and Armor by 20% / 30% / 40% / 50% while within range. Up to 2 Gazed targets may exist at once.
  - Enemy armor and shields are fully removed at 200% Ability Strength. With one Corrosive Projection, armor will be fully stripped at 164% Ability Strength.
    - Shield strip removes a percentage of the current maximum value. Armor strip, however, is a percentage of an enemy's total.
      - Enemy shields can still regenerate with natural shield regeneration (such as Armis Ulta, Kuva Liches, or Sisters of Parvos) or while affected by regeneration buffs (such as Shield Ospreys).
  - While invulnerable, the Gazed target is still susceptible to Status Effects, with exception of the inability to proc Void status.
  - Gaze defense reduction auras will stack with other defense reduction effects, but multiple Gaze auras do not stack with each other, whether from the same caster or from another Xaku in the squad.
  - Enemies regain their reduced shields and armor once they move outside of Gaze's aura.
  - If the enemy target dies before Gaze's entanglement fully takes effect, the casting energy cost is refunded to Xaku.
  - If an enemy that has both shields and armor wanders into Gaze's aura, such as an Oxium Osprey, then shields will be prioritized over armor.
- Holding down the ability key (default 3 ) while aiming directly at a Gazed target releases the victim early, causing it to receive all accumulated damage prevented by its brief invulnerability.
- Gazed enemies do not count towards mission progression.
- Can be recast while active to entangle a new enemy, freeing the oldest affected enemy if cast at max number of targets.
- Casting Gaze is a full-body animation that restricts movement and other actions.
- Xaku's head, face, chest, shoulder and arm pieces visually detach, as Xaku screams into the air above while blob-like substances fly out from their torso. The enemy target is frozen in place as it becomes entangled in a mass of rapidly growing Void tendrils.
  - While affected, the enemy target emits a radial aura visual effect and emits a Void energy cloud around the shoulders.

Deny

- Discharging a torrent of Void energy, Xaku unleashes a ray of piercing light toward the aiming reticle with infinite body Punch Through that travels up to 25 / 30 / 35 / 40 meters away. Enemies struck directly or within a ? meters radius from the beam receive 1,000 / 2,000 / 3,000 / 4,000 Void damage, reset damage resistances if used against Sentient faction, and become suspended in aerial stasis for 5 / 8 / 11 / 14 seconds.
  - Deny's Void damage benefits from Ability Strength, number of Grasp of Lohk's Void replicas, and The Vast Untime's Void damage vulnerability using the following expression: Total Void Damage = Void Damage × (1 + Ability Strength) × (Number of Void Replicas + 1) × Void Damage Vulnerability
    - At ability rank 3 with a maxed Intensify equipped, stolen 6 Void replicas, against an enemy affected by The Vast Untime, Xaku will deal 4,000 × (1 + 0.3) × (6 + 1) × 1.5 = 54,600 Void damage.
    - Deny's damage can be further amplified by Enemy Body Parts multipliers.
  - Enemies with selective crowd control effect immunity such as the Battalyst and Conculyst are unaffected by Deny's aerial stasis.
- Can be recast while active to strike new targets, or damage and refresh all effects on already affected enemies.
- Casting Deny is an upper-body animation that allows reticle repositioning and movement, while restricting other actions.
- Xaku's shoulder and arm pieces visually shiver then detach to hover above Xaku, as a beam of Void energy travels forward from Xaku's left hand, after which the pieces return to their positions.
- Enemies affected by Deny are suspended in the air by an upward stream of Void energy that resembles the Lifted status effect.

- Each active sub-ability is a separate instance from Xaku. As such, the ability nullifying effects of special enemies (e.g. Nullifier Crewman) will not dispel The Lost's sub-abilities if only Xaku is affected.

Kit Interactions

- Xata's Whisper does not grant additional Void damage to The Lost's sub-abilities.
- Grasp of Lohk can disarm and steal the weapons of enemies affected by all sub-abilities of The Lost.
  - Void replicas will not attack enemies corrupted by Accuse, unless affected by Radiation status effect or other faction modifier abilities (e.g. Chaos)
  - Void replicas will not attack an enemy trapped by Gaze.
  - Void replicas amplify Deny's damage, based on the number of stolen weapons hovering around Xaku.
- The Lost's sub-abilities interact with each other in various ways:
  - Accuse can corrupt enemies into allies while they are lifted by Deny. However, it cannot corrupt a Gazed enemy target. Accused units will attack a Gazed enemy target, storing damage to inflict to the victim once released from the Void tendrils.
  - Gaze may be cast on an enemy affected by either Accuse or Deny. Gaze reduces the defenses of Accused units in range. Gazing an Accused unit creates an invulnerable decoy that draws enemy aggro until Accuse expires.
  - Deny does not affect Accused units, but will contribute damage to Gazed enemy targets.
- The Vast Untime renders enemies 50% more vulnerable to Deny's beam and pauses all sub-abilities' ability duration timers while active.

Augment

- Main article: The Relentless Lost

The Relentless Lost is a Warframe Augment Mod for Xaku's The Lost that increases Ability Strength and Ability Efficiency for the ability, stacking up to three times but resets on casting the same sub-ability twice.

Rank | Ability Strength | Ability Efficiency | Cost
0 | +5% | +6% | 6
1 | +15% | +9% | 7
2 | +25% | +12% | 8
3 | +35% | +15% | 9

Tips & Tricks

- With one player using Corrosive Projection, 100% armor strip can be achieved at 164% Ability Strength, otherwise approx. 200% Ability Strength is required.
- Cast Accuse on a nearby surface or the ground below you to quickly corrupt surrounding enemies to help fight alongside you, or cast on a group of enemies off in the distance to create a distraction when faced with ranged threats.
- Accused enemies are allied units to the Tenno, therefore their special auras (such as those of Shield Osprey, Ancient Healer, Eximus, etc) or abilities will be used to briefly benefit you and your team.
- Cast Accuse on or near a mission objective to enlist the enemy to defend them for you.
- Cast Gaze on up to two enemies to completely disable them for the duration, while emitting an aura that reduces the defenses of other enemies in range.
  - All damage prevented by the Gazed target's invulnerability will be dealt in full when the ability ends.
  - Gazed targets do not halt mission progression such as Defense waves, allowing your defense reduction auras to persist in an area until you release the targets.
  - Gazed targets are still susceptible to status effects. Inflict Radiation procs to create an invulnerable distraction for nearby enemies.
  - Cast on enemies in different locations to encompass a larger area with the defense reduction auras.
- Gaze is cast within a cone centered on the aiming reticle. The closest enemy near the sides of the reticle will be automatically targeted by the ability.
- During an Interception mission, when an enemy is using a control console to regain control of the point, cast Gaze upon them. Doing so will keep the control console occupied without giving the enemy control of the tower.
  - Continuously cast The Vast Untime to keep this enemy in stasis nearly indefinitely. If/when the tower is recaptured, to prevent conflict on the point, look at the suspended enemy and cast Gaze on them again to release them.
- Cast Deny against enemies packed in a tight line to maximize its effect.
- Deny's damage is greatly amplified by the number of stolen weapons from Grasp of Lohk. Steal and maintain a large amount of weapons to deal devastating damage with Deny's Void beam.
- Enemies lifted by Deny are made easy targets for headshots from your weapons.
- Activate The Vast Untime to freeze all sub-abilities' duration timers. Accused enemies will remain on your side, Gazed targets stay trapped and emit their auras, and Denied enemies stay lifted airborne for an extended period of time. Strike enemies hit by the Void blast with Deny's Void beam to deal increased damage. This ability also slows enemies, making them easier to keep inside of Gaze's aura radius.

Maximization

Stacks of The Relentless Lost:
Number of Grasp of Lohk weapons:

The Lost

Gaze binds one enemy to produce an aura that temporarily reduces enemy armor by 50% while they are within its aura. At 200% Ability Strength, Gaze can remove all armor. Enemies will regain their armor if they leave the debuff field or the ability ends.

#### Focus

This section is transcluded from Focus/Unairu § Caustic Strike. To change it, please edit the transcluded page.

 | Caustic Strike OperatorSecond Ability launches an energy bomb that explodes with a 5 / 6 / 7 / 8m radius, stripping 40 / 60 / 80 / 100% of enemy armor. Tap 2 again to detonate in-flight. | 60,000 / 105,000 / 215,000 / 400,000
Costs 50 energy to cast.

### Percentage From Current Armor

#### Heat Status Procs

- Main article: Heat Damage

Heat status effects remove 50% of a target's current armor amount temporarily, for the duration of the status effect.

#### Corrosive Status Procs

- Main article: Corrosive Damage

Corrosive status effects remove 26% of a target's armor amount for 8 seconds. This stacks up to 10 times, with each subsequent proc removing 6% armor for a total of 80%.

### Flat Value From Base Armor

Sources that armor strip based on the base armor value of an enemy will remove a flat value from the base armor. This will affect the total armor an enemy will have.

- Shattering Impact is a melee mod that removes 6 base armor when dealing Impact damage.
- Amalgam Argonak Metal Auger is an Amalgam Weapon Augment mod exclusive for the Argonak that removes 6 base armor when attacking with single daggers.

## Media

## Patch History

Update 36.0 (2024-06-18)

Armor Adjustments

Important Note: We have not changed player Armor. This only applies to enemy Armor!

Enemy Armor scaling in its previous current iteration meant that Armor Stripping was almost an all-or-nothing game, especially at higher levels. This resulted in players focusing on Armor Stripping as a way to tackle Grineer at higher difficulty content. Our goal is to reduce some of the extreme damage reduction offered by Armor at high levels, and make partial Armor Stripping more feasible.

To do so, we are making the following changes:

- Armor has a maximum cap of 2700 Armor (90% Damage Reduction).
- Armor has a minimum cap of 200 Armor.
- Steel Path no longer increases Armor values.
- Grineer enemies have increased Health scaling.
- Altered the formula for Armor Reduction to increase the effectiveness of Partial Armor Stripping.
  - For reference, currently around 50% of Damage Resistance came from just 300 Armor, which is why complete Armor Strip felt so needed at higher levels.

Additionally, our goal was to make partial Armor Stripping a more valuable tool. By capping enemy Armor and adjusting how Armor is calculated, a partial Armor Strip will allow players to engage with high-level Grineer more easily - meaning max Corrosion stacks against an Armored enemy (reducing the Armor by 80%) will feel more impactful due to the new distribution of Damage Resistance from Armor values).

Full Armor Strip is still valuable, but we wanted to even the playing field so players didn’t feel forced to build around it.

Update 34.0 (2023-10-18)

HYDROID REWORK

Changing Impact and Magnetic Damage to Corrosive Damage and Status

Previously, Tempest Barrage and Tidal Surge both dealt Impact damage, while Tentacle Swarm dealt Magnetic Damage. These have been changed to Corrosive Damage, which can apply Corrosive Status. Corroding Barrage has been a widely used Augment Mod by Hydroid players, which caused Corrosive Status for Tempest Barrage, and due to its popularity, we looked to incorporate its effect into Hydroid at a base level.

We felt changing Damage to Corrosive Damage in Hydroid’s abilities makes them more thematic to the sea while also incorporating Corroding Barrage’s current effect in a meaningful way. With this change in mind, Corroding Barrage will now apply Viral Status instead of Corrosive - more details on that below.

Passive Changes

Hydroid’s previous Passive had a chance to spawn a tentacle when performing a melee slam attack. We have removed that passive entirely and replaced it with an entirely new effect.

The nature of Hydroid’s previous Passive pushed players to a very specific playstyle (regular usage of melee slam attacks), while not guaranteeing anything useful from each individual slam. We wanted to make the passive feel more reliable and impactful.

New Passive: Enemies damaged by Hydroid are more vulnerable to Corrosion Status, with initial status reducing armor by 50%.

Hydroid’s new Passive affects an enemy once Hydroid damages them, lasting until their death. It makes the first instance of Corrosive Status on an enemy remove 50% of their Armor rather than 26%. Not only does this make the first Corrosive Status stronger, but it also means Corrosion Status can reach 100% Armor Reduction with full stacks!

To clarify, this means Hydroid does not need to apply all, or even any, of the Corrosive Status Effects on an enemy. As long as Hydroid has damaged the enemy, the Corrosive Status Effects can be applied from any source and will receive the benefit.

Ability Changes

Tempest Barrage:

- The Corroding Barrage Augment Mod has been renamed Viral Tempest and now has a chance to apply a Viral Status Effect, rather than Corrosive Status Effect. It also no longer grants Ability Strength.
  - Changing the Impact Damage of Tempest Barrage to Corrosive Damage meant the Corrosive Status Effect from the Augment was already included. We changed this to Viral to maintain its relevance with the other changes. In light of the punch Corrosive and Viral packs in comparison to Corrosive and Impact, the Ability Strength buff was removed for balance purposes.

Tidal Surge:

- Tidal Surge now applies Corrosive Status Effects to enemies based on how long they are carried by its waves.

Plunder:

- A new ability added to Hydroid’s third ability slot.
- All enemies in range will have Corrosive Status Effects remove their armor permanently, increasing Hydroid’s armor and granting bonus Corrosive damage to weapons.
  - This ability is stronger based on the number of Corrosive Status Effects applied to the enemies affected by Plunder.
  - This means with a full stack of Corrosive Status Effects, their Armor will be removed permanently.

Update 32.2 (2022-11-30)

GRENDEL REWORK

Feast

- Replaced the Armor Reduction with 2% of their total Shields and Health overtime (does not scale).

Pulverize

- Added a 50% Armor Reduction (at max rank) to enemies struck by Pulverize (scales with Ability Strength Mods).

Regurgitate

- Added 75% Armor Reduction on Regurgitated enemies (scalable with Ability Strength Mods).

HUD Improvements: The following changes have been made to better communicate an enemy’s state to players via HUD improvements.

- Added a new Armor icon indicator next to enemy Health bars in the HUD.
  - This new icon not only better indicates that an enemy has Armor protection (in addition to their Health bar being yellow), but more specifically how much Armor they have. The icon changes based on three different thresholds to better communicate Armor values to players:
    - 1-499 Armor: No more than ~60% Damage Reduction from Armor
    - 500-2700 Armor: No more than ~90% Damage Reduction from Armor
    - 2700+: More than 90% Damage Reduction from Armor
  - Additionally, as enemy’s Armor is stripped, the icon’s meter changes at 3 stages:
    - Full = 100% Armor
    - Halfway = 50% Armor
    - Empty = 0% Armor

Update 32.0 (2022-09-07)

ARMOR CHANGES

Armor is a fundamental part of Warframe’s balance, but the act of stripping armor has always been somewhat hard to gauge. Currently, when an armor stripping Ability is cast it uses the target’s current armor as the base for its calculation. This means that you may have to cast that Ability several times on the same enemy in order to strip their armor completely.

Players have adapted to this system by maximizing Ability Strength to the point where the armor stripping effect is as close to 100% as possible - thus reducing the number of casts required to strip armor to one.

In the effort of encouraging build diversity and streamlining the way that armor stripping abilities work, we are making the following changes:

ALL Armor Stripping Warframe abilities now apply to the TOTAL armor value.

How it worked before: You cast an ability that strips 50% Armor. The first cast will reduce the foe’s Armor to 50%, the second cast will reduce the armor to 25%, taking half of the existing 50%. This was the case for every ability except Oberon’s Reckoning, and special exceptions like Shattering Impact.

How it works now: Casting an ability that strips 50% Armor will reduce their Armor to 50% on the first cast, and 0% on the second cast.

This applies to every single Armor removal ability in the game. We have also buffed a few of these abilities in the process to bring them up to a usable level in light of these changes:

- Increased Frost's Avalanche armor reduction from 40% to 60% and changed the armor reduction to be permanent.
  - Frost’s Avalanche can also now reduce armor from targets even if they are immune to crowd control abilities.
- Increase Nekros' Terrify armor reduction from 20% to 60%.
- Increase Oberon's Reckoning armor reduction from 30% to 50%.
- Changed Banshee's Sonic Fracture (Augment) armor reduction to be permanent.
- Increase Mag's Fracturing Crush (Augment) armor reduction from 50% to 75%, remove the 80% cap per cast and change the armor reduction to be permanent.
- Increase Trinity's Abating Link (Augment) armor reduction from 45% to 60%.

## See Also

- Attributes
- Enemy Level Scaling
- Health
