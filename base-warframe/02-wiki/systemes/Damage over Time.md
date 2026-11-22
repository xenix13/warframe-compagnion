# Damage over Time (wiki)
Source : https://wiki.warframe.com/w/Damage_over_Time

It's taking longer than I calculated.

We might need a better definition of DoT for non-Status classification. Is Crush, Magnetize, and Tornado DoT?

Damage over Time (or DoT) describes effects that periodically deal damage to targets over a set period of time. As opposed to applying damaging effects upon hitting the target's hitbox, DoT effects will deal damage per tick until the DoT duration ends. A DoT tick typically lasts 1 second and may be applied upon DoT trigger without delay.

DoT damage can be ignored if the target becomes invulnerable during the DoT effect or if the associated Status Effect is cleansed prematurely.

The total damage a DoT deals from Status Effects is indicated by a green indicator on the target's Health/Shield/ Overguard bar, which darkens if enough DoTs are applied to kill the target.

## Damage over Time Effects

### Status Effects

These Status Effects deal DoT when procced:

Damage Type | Status Effect | Base Duration | Delay? | Refreshable? | Max # Stacks | Notes
Slash | Bleed | 6-seconds | 1-second delay | DoT not refreshable | No limit | Single-target
Heat | Ignite | 6-seconds | 1-second delay | DoT instance can be refreshed | No limit | Single-target, unique stacking mechanic
Toxin | Poison | 6-seconds | 1-second delay | DoT not refreshable | No limit | Single-target
Electricity | Tesla Chain | 6-seconds | No delay, last tick deals no damage | DoT not refreshable | No limit | Area of Effect
Blast | Detonate | 1.5-seconds | 1.5-second delay, last tick does damage | DoT not refreshable | 10 | Not true damage over time. Technically each Blast proc instance is delayed damage.
Gas | Gas Cloud | 6-seconds | No delay, last tick deals no damage | DoT not refreshable | 10 | Area of Effect

Time From Initial Proc | 0s | 1s | 2s | 3s | 4s | 5s | 6s
Damage Tick Occurred? | Slash | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️
Heat | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️
Toxin | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️
Electricity | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ❌
Blast | ❌ | ❌ | ✔️ | ❌ | ❌ | ❌ | ❌
Gas | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ❌

#### In Empyrean

In Empyrean gamemode, damage types have different behavior:

Damage Type | Status Effect | Base Duration | Delay? | Refreshable?
Slash | Not DoT
Heat | Sear | 5-seconds | No delay | DoT instance can be refreshed
Toxin | Not DoT
Electricity | Not DoT
Blast | Not available
Gas | Not available

### Weapons

Some Weapons have unique mechanics that apply a DoT effect independent of Status Effects.

- Purgator 1 ( Gas proc on direct kill)
- Torid (10 ticks over 10 seconds, 1-second delay)
- Stug ( Corrosive DoT, 2 ticks over 1 seconds, no delay)
- Pox (4 ticks over 4 seconds, 1-second delay)
- Coda Pox (4 ticks over 4 seconds, 1-second delay)
- Tysis ( Corrosive DoT, 3 ticks over 2 seconds, no delay)
- Coda Tysis ( Corrosive DoT, 3 ticks over 2 seconds, no delay)
- Cryotra (6 ticks over 5 seconds, no delay)
- Stinger (3 ticks over 2 seconds, no delay)

### Abilities

- Desiccation, deal True damage over time
- Discharge, deal Electricity damage over time (not proc)
- Heat Elemental Ward, deal Heat damage over time (not proc)
- Toxin Elemental Ward, deal % of an enemy's maximum health as Toxin damage over time (not proc)
- Fire Walker, deal Heat damage over time to enemies standing in an AoE (not proc)
- Hallowed Ground, deal Radiation damage over time to enemies standing in an AoE
- Magnetize, deal Magnetic damage over time in an AoE
- Scarab Swarm, deal % of max health as Corrosive damage over time
- Shuriken, inflict forced Slash proc
- Spores, deal scaling Corrosive damage over time based on active Spores
- Seeking Talons, inflict Slash procs
- Sow, deal True damage over time
- Tentacle Swarm, deal Corrosive damage over time on captured enemies
- Virulence, deal Viral damage over time to enemies standing in an AoE

### Ability Augments

- Cataclysmic Gate
- Contagion Cloud
- Hallowed Reckoning

### Other

- Exodia Contagion (on direct hit, Blast DoT, 4 ticks over 4 seconds, 1-second delay)
- Residual Shock ( Electricity DoT)
- Residual Viremia ( Toxin DoT)
- Internal Bleeding
- Hemorrhage
- Endoparasitic Vector

## Increasing DoT Duration

These only affect DoT from Status Effects:

- Augur Seeker
- Continuous Misery
- Frenzied Posture
- Hunter Track
- Lasting Sting
- Lingering Torment
- Perpetual Agony
- Rapid Resilience
- Toxic Sequence

### Duplicating Stacks

While not exactly increasing the base DoT duration, Sickening Pulse will extend active DoT Status Effects by creating a new proc instance with new timers.

## Calculating Damage Over Time

- Main article: Damage/Calculation#Damage Over Time Final Calculations

Total Ticks=⌊Tick Rate×(Duration−Delay Time)⌋+1 | Tick Rate for most effects is 1 tick per second.
Total Damage over Time=Damage per Tick×Total Ticks | Damage per Tick is affected by sources of Status Damage bonus

For example, when an ability deals 600 damage per tick and it ticks twice per second, the ability will deal 1,200 damage per second. In other words, the ability has a DoT of 1,200.

Tick rates vary across DoT sources. In the example above the tick rate was 2s-1, which is a common rate for DoT from Warframe abilities. For Bleed DoT, damage ticks 6 times over a 6 second duration; this results in a tick rate of 1s-1, and the same applies to all DoT from Status Effects.

If the tick rate does not divide into the total duration evenly, the total number of ticks dealt is rounded down. For example, with a tick rate of 2s-1 and a total duration of 3.4s, the first tick will occur at 0 seconds, with each subsequent tick occurring every 0.5 seconds until 3 seconds have passed. The last tick occurs here because the 3.4 second duration ends before the next tick can occur at the 3.5 second mark. As such, the total number of ticks that occurred is 7.

## DoT Damage Scaling

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

## DoT Detonation

DoT effects may end prematurely but apply all of their damage ticks in a single damage instance under these effects:

- Expedite Suffering
- Final Verse (Tragedy)
- Divine Retribution
- Harmony Heavy Attack

## Patch History

Update 43.0 (2026-06-17)

Damage Over Time Preview

Damage Over Time (DOT) Status Effects are now reflected by a new “Damage Over Time Preview” indicator on healthbars, showcasing the exact amount of damage they will deal over their duration.

- This new indicator will display the damage that will be dealt across Health, Shields, and/or Overguard.
- Damage Over Time that applies lethal damage will result in a black outline around the health bar.
- This indicator only applies to DOT from Status Effects, not Abilities that deal damage over time.
  - Ex: Damage from Saryn’s Spores will not be reflected in this new indicator, but damage from the Status Effects dealt by Koumei’s Bunraku will.
- Players can change the color of this indicator via the Customize Hud Colors screen in the Accessibility settings.
