# Patch note : Jade Shadows: Constellations: Hotfix 43.0.4
Date : 2026-06-23
Source : https://forums.warframe.com/topic/1513074-jade-shadows-constellations-hotfix-4304/

Changes:

- Restored the Syndir Ephemera's effect applying to Attachments and Syandanas for those with Particle Quality set to Medium or higher.
- This was removed due to performance concerns in 43.0.2, but we are bringing it back at player request.

- Reduced the SFX of squadmate Sirius & Orion's attacks in Celestial Clash.
- Made various polish changes to the Jade Shadows: Constellations quest.
- Newly acquired Honoria will now be tagged with the "new" icon (like new equipment in the Arsenal) to help players find them.
- Added extra support for Camera Position offsets to Hildryn’s Balefire and Gyre’s Rotorswell.
- Updated the Daurus Prime Armor's tint order to match that of Styanax Prime (swapped the Primary and Tertiary channels).
- Improved handling of corrupt shader caches on PC when running DirectX 12.

Top Fixes:

- Fixed Clients not seeing all mission rewards in the End of Mission screen in Uranus Proxima missions.
- This was a UI-only issue, players were still receiving rewards in their accounts.

- Fixed Sevagoth and Nokko not receiving the full amount of Emerald or Crimson Talents from Uranus Proxima missions if they extracted while in Shadow or Reroot forms respectively.
- Also protected against other cases of Clients not receiving full Talents due to End of Mission timing. We are aware of complaints related to Sirius & Orion specifically, and we hope this will address their issues, but we'll continue to watch for reports!

- Fixed being able to enter Last Gasp immediately after failing to revive yourself with it, which often led to loss of function or crashing.
- Also fixed Sirius & Orion being able to enter Transference after failing Last Gasp, resulting in an invisible unkillable Operator/Drifter that is unable to abort the mission.

- Fixed the Neo V12 Relic having the Akbronco Prime Blueprint listed twice in its common rewards. The duplicate reward has been replaced with the Paris Prime Blueprint.
- Fixed Arcane Bellicose causing Nidus's Parasitic Vitality buff to be permanent for allies.
- Fixed the following Clan Research components dropping from Uranus Proxima missions, resulting in error messages when players attempted to repair them via the Salvage menus:
- Tycho Seeker MK III
- Milati MK III
- Galvarc MK III
- Note: Players who incorrectly received these Ordnances via mission droptables have had them replaced with other Salvage from the droptables via an account update with this hotfix.

- Fixed The Roundtable Protoframes' KIM ranks being changed to "Associate" if you were Best Friends before Jade Shadows: Constellations. Your ranks have been reverted to pre-update values!
- Fixed Client Sevagoth and Inaros being able to be locked out of the boss arena if they get dragged into it in their special death states in Uranus Proxima missions.
- Fixed cases of Sirius & Orion not being eligible for Relic Rewards despite having 10 Reactant.
- Fixed various Line of Sight (LOS) issues with Sirius & Orion's Celestial Clash:
- Fixed LOS checks being done on enemies within 5m of Sirius & Orion — usually LOS abilities do not perform checks on foes within that range to avoid Warframes inadvertently blocking their own attacks.
- Fixed swapping between the Sons sometimes causing attacks to use non-player LOS checks (instead of the improved LOS system), resulting in foes often getting missed.
- This helps address the common issue of enemies in Orion's Event Horizon not being hit by Celestial Clash.

- Fixed the Courier vehicle flying out of mission bounds in Archwing Pursuit missions, causing players to fail the mission.

Incarnon Changes & Fixes

- Improved performance issues caused by Ballistica Prime's ghosts.
- Known Issue: Ballistica Prime’s ghost mechanic is being affected by multishot while in Incarnon Form, resulting in players spawning more than one ghost per enemy, often rivalling the King of the Dead’s army. While fun, these Ghosts are often useless and can block player vision, so we are looking to fix this issue in a future hotfix.

- Increased the Vectis Incarnon "Lone Enforcer" Evolution's stats as follows:
- Increased Base Damage from +50 to +75 (+100 to +150 for Vectis Prime).
- Increased Multishot from 20% to 25%.

- Increased the Vectis Incarnon form's projectile speed from 200 to 300.
- Fixed the Destreza Incarnon Evolution III challenge tracking progress off of any Incarnon (instead of just the Destreza).
- Fixed the Obex Incarnon Evolution I giving 8000% Finisher damage instead of the intended 80%.
- Fixed Obex's Incarnon Evolution II and III challenges earning progress off of kills with any weapon.
- Fixed the Stug's Incarnon form being able to hit enemies through Limbo's Rift.
- Fixed cases of Incarnons not displaying full information when previewed at Cavalero.

Uranus Proxima Changes & Fixes

- Various "waiting for players" objectives in Uranus Proxima missions will now trigger a teleport timer if half of the squad is waiting at the objective.
- Improved performance issues in Uranus Proxima missions caused by various enemy VFX.
- Fixed the "Defeat the Ship's Captain" objective never completing if the Captain was killed while a player was downed in the Scoria's Angel mission.
- Fixed cases of not enough Guards spawning in The Kuva Wytch mission, resulting in a progression stop.
- Fixes towards players getting stuck under the Scoria's Angel after being pushed out by one of Ryoku's traps.
- Fixed a Host Migration during the Orowyrm section of The Kuva Wytch mission causing returning players to be progression stopped.
- Fixed the Comet Shredder Captain's waypoint sometimes not disappearing when they die.
- Fixed flickering decals on the walls of Vena's ship in The Kuva Wytch mission.
- Fixed buzzing SFX when charging up Forward Artillery rapidly in The Kuva Wytch missions.
- Fixed performance issues in The Kuva Wytch mission.
- Fixed a script error when transitioning between ships in The Kuva Wytch mission.
- Fixed a script error in Uranus Proxima missions.
- Fixed a crash during Vena's boss fight in The Kuva Wytch missions.

Sirius & Orion Fixes

- Fixed Sirius & Orion not receiving Research Points in Archimedea if Orion is the Primary Son.
- Fixed swapping between Sirius & Orion in a Mastery Rank test causing the test to immediately fail.
- Fixed the Secondary Son being able to bypass respawn restrictions.
- Fixed Blessings not applying to both Sons when using Sirius & Orion in The Descendia.
- Fixed the Inactive Son consuming ammo if a Heavy Weapon is equipped by the Active Son.
- Fixed cases of Orion losing context actions if a Heavy Weapon is equipped in Uranus Proxima missions.
- Fixed the Hold Sprint setting not being respected when swapping between Sirius & Orion.
- Fixed the Secondary Son not spawning during a fight segment in The New War quest.
- Fixed the Secondary Son being invisible during certain segments of The New War quest.
- Fixed the Secondary Son running around during a cinematic in The War Within quest.
- Fixed Sirius & Orion's Prex card appearing low resolution.
- Fixed various script errors related to Sirius & Orion's Celestial Clash.
- Fixed a script error related to Sirius' Coronal Ejection.

Fixes

- Fixed "Hunhow's Trinket" missing swing trail VFX (if you know you know).
- Fixed being able to acquire the Neo V11 Relic via Relic Packs (despite it being vaulted in 43.0.2).
- Fixed casting Follie's Shadowgraph resulting in D-Pad icons appearing over her ability icons.
- Fixed cases of players getting stuck on the same login day if they selected a Credits reward.
- This was patched live on Friday, but we are calling out in patch notes for those who were in this state.

- Fixed the Dread and Paris Prime missing weapon stats in the Arsenal if installed with an Incarnon Genesis.
- Fixed various issues with Stug's stats in the Upgrade Screen:
- Critical Chance, Radial Status Chance, and Status Chance always displaying as 0%.
- Blob Embed Damage causing Elemental Damage to appear twice for Quick Shot stats.

- Fixed Stalker being able to roll out of a cinematic in the Jade Shadows: Constellations quest.
- Fixed "Primary Son" terminology making it into the name selection screen in the Jade Shadows quest.
- Fixed the Drifter's right arm turning invisible during the Ryoku and Vena Gemini Emotes.
- Fixed low SFX from the music puzzle on Lua.
- Fixed Jade's default emissive tint being unintentionally changed to blue.
- Fixed being unable to spawn the Exo Gokstad Officer in the Simulacrum.
- Fixed the Bladeswarm and Bloodfrenzy Domestik Drones having incorrect pathing behaviours in the Dojo.
- Fixed a crash caused by Arcane Compression.
- Fixed an issue related to the Anarch Capsarii's shield drone ability.
- Fixed various script errors related to Xaku's The Vast Untime.
- Fixed a possible crash in the Jade Shadows: Constellations quest.
- Fixed a script error related to Whispers in Albrecht's Laboratories missions.
- Fixed a script error related to Nidus' Link.
- Fixed a script error caused by enemy Maggots' latching ability.
- Fixed a crash when looking through KIM Conversation History.
- Fixed a random crash.
- Fixed a rare crash that could occur when using DirectX12.
- Fixed a rare crash on the End of Mission screen.

For list of known issues that are on our radar, visit our dedicated thread: https://forums.warframe.com/topic/1509550-known-issues-jade-shadows-constellations/
