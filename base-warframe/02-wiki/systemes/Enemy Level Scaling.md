# Enemy Level Scaling (wiki)
Source : https://wiki.warframe.com/w/Enemy_Level_Scaling

Enemy Level Scaling

Normal stat scaling for health, shields, and armor

All enemies encountered in WARFRAME have a certain level, which determines their strength by increasing some of their base statistics. The stats amplified by enemy level gain are Health, Armor, Shields, Damage dealt, and Affinity on death. The purpose of this article is to show how exactly these stats scale with level, how this translates to useful indicators such as effective health, and what implications this has towards player decision making such as Aura mods or damage type selection.

Enemy levels are normally capped at the limit of 9999, but can be exceeded in Void Fissure missions. In addition, stats of regular enemies don't scale with squad size. Known exceptions are Demolishers, Acolytes and Archons.

Also visit Effects Scaling With Enemy Stats for a list of abilities and other effects that scale up as enemy level increases.

## Common Features of Stat Scaling

Most fundamental enemy stats are obtained by multiplying a base value by a level-dependent multiplier. Each endpoint curve has the following general structure:

- f_i(x)=1+C_iq^(E_i)

Here, C_i and E_i are the coefficient and exponent of endpoint curve i . For most stats,

- q=Current Level−Base Level.

Overguard ignores the enemy's individual base level and instead uses q=Current Level−1 . Affinity is a separate case and uses the current level directly.

For a stat that uses a single curve, that curve is the stat multiplier. For a stat that uses two endpoint curves, the multiplier is obtained using the interpolation procedure described below.

The current stat value is then:

- Current Value=f32(f32(Base Value)×f32(Multiplier))

In these formulae, f32(z) means that z is evaluated and stored as an IEEE 754 binary32 value. The coefficients, exponents, power results, and intermediate arithmetic results must be evaluated in binary32 in the displayed order when reproducing in-game values.

## Scaling of Fundamental Stats

As mentioned, all fundamental stats scale by the above formula structure and common features apply. A standardized graph is shown for each stat. When comparing the graphs, the different Y-axis scaling has to be considered. As of Update 27.2 (2020-03-05) health, shield, and armor scaling follow an "S"-like curve, where below a universal level range these stats grow quickly, and above this range, the stats grow slower and begin to plateau.

Health, shields, armor, Overguard, and the modified Corpus, Grineer, and Techrot damage scaling use two endpoint curves. The two curves do not necessarily intersect. Instead, a smoothstep weight transitions the multiplier from the lower endpoint curve f_1 to the upper endpoint curve f_2 .

For health, shields, and armor, the transition bounds are L=70 and U=80 . Overguard uses L=45 and U=50 . Modified Corpus, Grineer, and Techrot damage scaling uses L=1 and U=25 .

Let q be the applicable level input defined above. The transition value is:

- t=clamp(f32((f32(q−L))/(f32(U−L))),0,1)

The smoothstep weight is evaluated as:

- s=f32(f32(t×t)×f32(3−f32(2×t)))

The final multiplier is evaluated in the following exact order:

- Multiplier=f32(f_1(x)+f32(f32(f_2(x)−f_1(x))×s))

Both endpoint curves are evaluated at every level, including when s=0 or s=1 . For exact binary32 results, the expression must not be rearranged as f_1(x)(1−s)+f_2(x)s , and f_1 or f_2 must not be substituted directly at either endpoint.

### Health

For health, the ranges of level differences from base to current level at which scaling transitions is between 70 & 80.

The formula by which Grineer and Scaldra health scales is as follows:

- f_1(x)=1+0.015(x−Base Level)^(2.12) Lower endpoint curve
- f_2(x)=1+10.7332(x−Base Level)^(0.72) Upper endpoint curve

The formula by which Corpus health scales is as follows:

- f_1(x)=1+0.015(x−Base Level)^(2.12) Lower endpoint curve
- f_2(x)=1+13.4165(x−Base Level)^(0.55) Upper endpoint curve

The formula by which Infested health scales is as follows:

- f_1(x)=1+0.0225(x−Base Level)^(2.12) Lower endpoint curve
- f_2(x)=1+16.0998(x−Base Level)^(0.72) Upper endpoint curve

The formula by which Corrupted health scales is as follows:

- f_1(x)=1+0.015(x−Base Level)^(2.1) Lower endpoint curve
- f_2(x)=1+10.7332(x−Base Level)^(0.685) Upper endpoint curve

The formula by which Murmur, Sentient, Anarchs, and Unaffiliated health scales is as follows:

- f_1(x)=1+0.015(x−Base Level)^2 Lower endpoint curve
- f_2(x)=1+10.7332(x−Base Level)^(0.5) Upper endpoint curve

The formula by which Techrot health scales is as follows:

- f_1(x)=1+0.02(x−Base Level)^(2.12) Lower endpoint curve
- f_2(x)=1+15.0998(x−Base Level)^(0.7) Upper endpoint curve

Eximus units use the health scaling of their respective factions, but have an additional, separate base health increase. This base health increase is dependent on level. Note that the health values listed in the Codex are not an Eximus unit's base health before this base health increase. For Eximus units with Shields or Armor, the base health increase is as follows:

- Eximus Health={{ max(Base Health×1.1, 0.25×(Base Health+900)) x≤15 ; max(Base Health×1.1, 0.25×(Base Health+900)×[1+0.025×(x−15)]), 15<x≤25 ; max(Base Health×1.1, 0.25×(Base Health+900)×[1.25+0.125×(x−25)]), 25<x≤35 ; max(Base Health×1.1, 0.25×(Base Health+900)×[2.5+2/(15)×(x−35)]), 35<x≤50 ; max(Base Health×1.1, 0.25×(Base Health+900)×[4.5+0.03×(x−50)]) 50<x≤100 ; max(Base Health×1.1, 0.25×(Base Health+900)×6), x>100 }

- Eximus Health={{ max(Base Health×1.1, 0.375×(Base Health+900)) x≤15 ; max(Base Health×1.1, 0.375×(Base Health+900)×[1+0.025×(x−15)]), 15<x≤25 ; max(Base Health×1.1, 0.375×(Base Health+900)×[1.25+0.125×(x−25)]), 25<x≤35 ; max(Base Health×1.1, 0.375×(Base Health+900)×[2.5+2/(15)×(x−35)]), 35<x≤50 ; max(Base Health×1.1, 0.375×(Base Health+900)×[4.5+0.03×(x−50)]) 50<x≤100 ; max(Base Health×1.1, 0.375×(Base Health+900)×6), x>100 }

- Where the Health Multiplier is the value that multiplies an enemy's base health to its current health.

### Shields

For shields, the ranges of level differences at which scaling transitions is between 70 & 80.

The formula by which Corpus shields scale is as follows:

- f_1(x)=1+0.02(x−Base Level)^(1.76) Lower endpoint curve
- f_2(x)=1+2(x−Base Level)^(0.76) Upper endpoint curve

The formula by which Corrupted shields scale is as follows:

- f_1(x)=1+0.02(x−Base Level)^(1.75) Lower endpoint curve
- f_2(x)=1+2(x−Base Level)^(0.75) Upper endpoint curve

The formula by which Grineer and Sentient shields scale is as follows:

- f_1(x)=1+0.02(x−Base Level)^(1.75) Lower endpoint curve
- f_2(x)=1+1.6(x−Base Level)^(0.75) Upper endpoint curve

The formula by which Techrot shields scale is as follows:

- f_1(x)=1+0.02(x−Base Level)^(1.76) Lower endpoint curve
- f_2(x)=1+3.5(x−Base Level)^(0.76) Upper endpoint curve

Eximus units use the Shield scaling of their respective factions, but have an additional, separate base Shield increase. This base Shield increase is dependent on level. Note that the Shield values listed in the Codex are not an Eximus unit's base Shields before this base Shield increase. The base Shield increase is as follows:

- Eximus Shields={{ Base Shield×1.1 x≤15 ; max(Base Shield×1.1, Base Shield×[1+0.025×(x−15)]), 15<x≤25 ; max(Base Shield×1.1, Base Shield×[1.25+0.125×(x−25)]), 25<x≤35 ; max(Base Shield×1.1, Base Shield×[2.5+2/(15)×(x−35)]), 35<x≤50 ; max(Base Shield×1.1, Base Shield×[4.5+0.03×(x−50)]) 50<x≤100 ; max(Base Shield×1.1, Base Shield×6), x>100 }

- Where the Shield Multiplier is the value that multiplies an enemy's base shields to its current shields.

### Armor

Enemy armor produced by level scaling is hard capped at 2,700, granting 90% Damage Reduction under the standard enemy armor formula.

Enemies whose level-scaled armor would be less than 200 have their initial armor value set to the minimum cap of 200 instead. This minimum cap is only for the initial value of their armor, i.e. their armor can still be decreased below 200 through all normal means of armor removal.

For armor, the ranges of level differences at which scaling transitions is between 70 & 80. The formula by which enemy armor scales is as follows:

- f_1(x)=1+0.005(x−Base Level)^(1.75) Lower endpoint curve
- f_2(x)=1+0.4(x−Base Level)^(0.75) Upper endpoint curve

- Armor Multiplier=f32(f_1(Current Level)+f32(f32(f_2(Current Level)−f_1(Current Level))×s))

- Where the Armor Multiplier is the value that multiplies an enemy's base armor to its current armor.

### Overguard

Overguard is a unique health buffer to Eximus, though normal units can get overguard in unique situations (like after a Overguard Exodamper is destroyed during Void Armageddon). All Eximus units have a base Overguard of 12.

- f_1(x)=1+0.0015(x−1)^4 Lower endpoint curve
- f_2(x)=1+260(x−1)^(0.9) Upper endpoint curve

Stat scaling between 45-50 inclusive is interpolated from the two functions using smoothstep.

- Overguard Multiplier=f32(f_1(Current Level)+f32(f32(f_2(Current Level)−f_1(Current Level))×s)) Where the Overguard Multiplier is the value that multiplies an enemy's base overguard to its current overguard.

### Damage

The formula by which enemy damage scales is as follows:

- Damage Multiplier=1+0.015×(Current Level−Base Level)^(1.55)

Corpus, Grineer, and Techrot enemies have modified damage scaling, and use the following:

- f_1(x)=1+0.015(x−Base Level)^(1.75) Lower endpoint curve
- f_2(x)=1+0.0075(x−Base Level)^(1.55) Upper endpoint curve

Stat scaling between 1-25 inclusive is interpolated from the two functions using smoothstep.

- Damage Multiplier=f32(f_1(Current Level)+f32(f32(f_2(Current Level)−f_1(Current Level))×s)) Where the Damage Multiplier is the value that multiplies an enemy's base damage to its current damage.

Additionally, Corpus, Grineer, and Techrot have a 2x damage multiplier applied to their attacks. Infested have a 3x damage multiplier applied to their attacks.

- The base damage value of the enemy is equivalent to the damage dealt by this enemy to the player's Overguard when it is at level 1.

### Affinity

The formula by which enemy affinity scales is as follows:

- Affinity Multiplier=1+0.1425×Current Level^(0.5)
- Eximus Affinity Multiplier=3+0.1425×Current Level^(0.5)

Note that this is a special case: for the affinity scaling, base level is not subtracted from the current level. The base affinity multiplied by the Affinity Multiplier value is also rounded down to a whole number, e.g. 62.7 affinity will be rounded down to 62.

## Scaling of Derived Stats

From these fundamental stats, more meaningful stats can be derived.

### Effective Hitpoints

Effective Hit-points is a stat that indicates how much gross damage must be dealt to a target until the net damage thereby inflicted depletes its entire health pool. Effective Hit-points is not a fixed stat for any given enemy, it is heavily dependent on the damage type used against the target, as well as the various buffs and debuffs in effect for both the attacker and the enemy in question. For the following considerations, however, these influences are disregarded, as they do not alter the course of the graphs except for clinching or stretching them as a whole, which manifests as a scaling of the Y-axis.

#### For Enemies with Health only

For targets without shields and armor, the standardized effective hit-point scaling is synonymous with standardized health scaling, the health graph and formula apply.

#### For Enemies with Health and Shields

The standardized effective hit-points of shielded enemies are simply the sum of their shields and health, except for the case when the Toxin damage portion of the gross damage depletes the target's health faster than the rest of the gross damage depletes its shield. Exact effective hit-point calculations considering damage types also become significantly more complex if Toxin damage is involved, but this is disregarded here. The level scaling of standardized effective hit-points of shielded enemies is influenced by the ratio of base shields to base health:

- EHP Multiplier=Health Multiplier+Shield Multiplier×(Base Shields)/(Base Health)

In the cases where you are trying to one-shot shielded enemies without Toxin damage, their effective hit-points will actually be higher due to their shield gate mechanic. Only 5% of total damage dealt will only damage the enemy's health when their shield gate is active. However, attacking enemy weakpoints ignores the shield gate.

#### For Enemies with Health and Armor

The standardized effective hit-points of armored enemies are simply the health divided by the compliment of the damage reduction granted from armor. Because armor adds damage reduction to incoming damage on health the level scaling of standardized effective hit-points of armored enemies is influenced by the base armor itself:

- EHP Multiplier=Health Multiplier×(1+(Base Armor×Armor Multiplier)/(300))

#### For Enemies with Health, Shields, and Armor

The standardized effective hit-points of enemies that are both armored and shielded are more complex than the simple EHP cases from the previous sections above. The level scaling of standardized effective hit-points of these enemies is influenced by the ratio of base shields to base health and base armor, making the formula at least 3 variable:

- EHP Multiplier=Health Multiplier×(1+(Base Armor×Armor Multiplier)/(300))+Shield Multiplier×(Base Shields)/(Base Health)

### Shielding Ratio

The shielding ratio of shielded, unarmored enemies is the ratio of their shield to their health. Since health and shield scale at different rates, this ratio changes with level. Pre-Update 27.2 (2020-03-05) this ratio used to converge towards a 1:2 ratio, where the higher the level the enemies, the closer they were to having twice as much health as shields, regardless of base stats. Currently, the ratio follows this original trend up until level 70, where it suddenly dips below 1:2 then diverges off towards infinity. This is because unlike before when health and shield scaling had same exponents (2), the current shield scaling has an exponent 50% larger than health scaling (0.75 vs 0.5) once past level 80, so it will grow at a faster rate despite having a smaller coefficient. This means the shield ratio will also grow larger over levels rather than converging.

The shielding ratio is relevant for evaluating and selecting damage types against shielded enemies, i.e. weighing benefits against shield types against benefits against health types. Eventually shielded enemies at high enough levels will have more shields than health, so assuming a lack of Toxin or True damage, effectiveness against shields may take more precedence in player builds than health effectiveness.

The shielding ratio of shielded, armored enemies is the ratio of their shield to their armored EHP. Like before, since health and shield scale at different rates, this ratio changes with level, though more complexly since armor scaling will also make an impact. This ratio converges towards a 0:1 ratio, where, as long as the enemy has a base armor of at least one, the higher the level the enemies the closer they are to having a negligible amount of shields relative to their EHP due to armor. Though as seen above, if no armor is present then the ratio will diverge towards infinity.

### Affinity Density

The affinity density of an enemy is its affinity per effective hitpoints and a measure of its profitability for affinity farming.

It is important to note the actual affinity farming profitability is significantly offset off the optimal area as implied by the affinity density function due to the two important practical influences of overkill and retargeting time, which both contribute to shifting the actual optimum from these implications towards higher levels.

### Reflective Kill Rate

Reflective kill rate of an enemy is the ratio of its damage output and effective hit-points. This is inversely proportional to the amount of time or attacks an enemy would need to kill another of its kind. It's a measurement for the effectiveness of damage reflecting effects and abilities, such as the Radiation damage proc, the Reflection mod, and abilities such as Link, Shadows of the Dead, Absorb, Chaos or Mind Control.

## Level Scaling During Endless Gameplay

It's taking longer than I calculated.

This page is actively being worked on and may not be completely correct. Please assist in making this page accurate by adding more info. For guidance on performing research, see WARFRAME Wiki:Research.

During endless missions such as Survival and Defense, enemy spawn level will increase the more reward rotations are completed, following an inconstant increment: it seems to be overall exponential until enemy level 5000, reached after four hours in Survival, later it becomes linear. Typically at around 8+ hours of in-mission time, players will reach the max enemy spawn level, equal to 9999.

In Disruption missions, to calculate the approximate spawn level at a particular conduit number:

Level Increase From Previous Round=L(x)=2.59e^(0.139(Round Number))

Spawn Level=Starting Spawn Level+∑_(x=1)^(Round Number)L(x)

## Effects That Indirectly Scale Off Enemy Level

See Effects Scaling With Enemy Stats and Category:High Scalability.

## External Links

- Interactive calculator for most value multipliers

## References

## Patch History

Update 36.1 (2024-08-21)

- Made the following changes to lower-level missions to offer more engaging combat. Our goal is to strike a balance between not being too punishing, but also encouraging players to adopt behaviors that will help them take on harder content -- ie. not just standing still and shooting folks.
  - Increased enemy spawns on Mercury, Venus, Earth, Mars, Phobos, Ceres, and Jupiter (base version only, Steel Path remains the same).
  - Increased accuracy of Grineer and Corpus enemies below level 55.
  - Adjusted Grineer Trooper behavior to work more closely within their effective weapon range.
  - Increased base damage multiplier for Grineer and Corpus, but amended how it scales to compensate. The goal is to make them hit harder at lower levels, but keep things the same for higher difficulty content.

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

Shield Adjustments

Important note: We have not changed player Shields. This only applies to enemy Shields!

The Grineer are tankier by design, but the Corpus try to make the difference through their Shields. However, Corpus Effective Hit Points (EHP) are significantly lower, making them often trivial to deal with by comparison. Our goal is to reduce the discrepancy between Grineer and Corpus time-to-kill (TTK) by making Corpus Shields a bit more challenging and interesting to fight.

Changes to Enemy Shields:

- Shields now scale more quickly starting at level 80. This means stronger Shields than before as players fight higher-leveled Shielded enemies.
- Shield Recharge Delay is now unified across all enemy types.
- Shield Recharge Delay now has a minimum and maximum length depending on how much damage has been dealt to enemy Shields.
  - The more damage dealt, the slower enemy Shields will begin recharging, so if you can’t outpace enemy Shields right away, you can chip their Recharge Delay down within a maximum and a minimum.
    - For example, if enemy Shields break at any point, it automatically acts as if 200% damage (which becomes the maximum delay) has been inflicted on those Shields. However, if an enemy absorbs 99% damage (so 1% of their shields left), their accumulated damage taken now sets their Recharge Delay in the middle of their respective minimum and maximum delays. Should they Recharge and you deal another 99% damage to their Shields, they’ll have absorbed 198% damage, taking them to the maximum Recharge delay of what that scaled enemy can have.
- Shield Recharge Rate scales with enemy level, recharging at a faster rate for higher-leveled enemies.
  - Shield Recharge Rate will also accelerate while Shields are actively Recharging.
    - Shield Recharge Acceleration Rate’s base multiplier greatly increases after level 80, resulting in faster Recharge rates at higher levels.
- Steel Path Shields are now multiplied by 2.5x, in place of the previous 6.25x. Steel Path Shields were doubly-applying the multiplier unintentionally.

Effective Hit Points (EHP) Adjustments

Enemy stat scalings, such as Health and Shields, now grow faster as enemy level increases, in compensation of the loss in Enemy Armor and to make Shields more engaging to deal with.

Changes:

- After Level 75-80, enemies receive increased stats, such as Health, at a slightly increased rate to prevent EHP stagnation.
  - It’s important to note that the increase in Health scaling is not meant to match the EHP values seen by previous levels of Armor.

Update 27.2 (2020-03-05)

Armor and Damage Changes (Enemy):

This section will go over before and after scenarios with our enemy Armor, Health, and Shield changes. Reading this section should give you a conceptual and on-paper understanding of what we’re changing and why, but practical experiences will tell the full story here. You may need to refresh some aspects of your Builds to truly optimize your power against your enemies.

Before: Armor, Shields and Health on an Exponential Curve After: Armor Shields and Health on an S curve

Damage Changes:

Enemy Damage output should still be close to what is currently on the Live version of the game, but we have made a few changes that will affect how players take Damage in-game.

Infested Damage:

We did not want to overlook the Infested in our review. Infested are close-range enemies that telegraph most attacks - and now if one of those attacks hits you, it simply does more damage. Stay agile, stay moving, and the mission is as good as won!

Why: Having Infested simply deal more Damage encourages you to use mobility in ways that is not the norm for their ranged counterparts. Rewarding mobility is a key part of Warframe.

AI Aimbots

Up until now in Warframe, the higher the enemy level, the better their accuracy. High-level enemies would be pinned at the best Accuracy they are capable of - not quite 100%, but getting pretty close! Things like your movement and Mods would reduce accuracy, but the potential for bad ‘Aimbot’ moments was too high. We have spread this progression across a greater range of AI now We are decoupling enemy accuracy from level to reduce the overall ‘Aimbot’ like behaviours you face at higher levels.

Why: This change allows us more accurate balancing of foes at higher levels. This change alone would be noticed by simply sometimes ‘getting hit less’, but in conjunction with the numerous other changes we are making to enemies, it is part of a holistic Refresh to the underlying mechanics behind Warframe’s enemies.

Hotfix 25.0.7 (2019-05-30)

- Eximus enemies are now capped at Level 9999 like regular enemies.

Update 14.0 (2014-07-18)

- Enemies health is no longer capped at 65535.

Update 11.5 (2013-12-19)

- Armour/Shield/Health/Damage curves have been modified. We’ve lowered the “bullet sponge” to high level enemies, but they now deal more damage. The armour curve was radically dropped. The health and shields curves dropped slightly as well. However, damage output went up.

Update 11.0 (2013-11-20) Source: https://forums.warframe.com/topic/132366-information-on-damage-20/

Enemy Levels

Enemy levels now fall in a more compressed scale. Level 1 enemies are still the easiest, but the difficulty of a Level 40 enemy in Damage 2.0 will be comparable to a Level 100 enemy in Damage 1.0. Infinite mission types will still feature ever increasing enemy levels. Enemies will be wielding weapons that can inflict different types of damage and Procs on the Tenno, meaning the difficulty will come from a combination of their loadouts and their level.

Hotfix 7.7.1 (2013-04-04)

- Increased the curve of AI damage/shields for higher level enemies... but then:
  - After more testing, toned down those same curves for high level enemies (split the difference).
