# Archipelago Manual for Super Street Fighter 2

**Version 0.6.0**

## Welcome!
Welcome to the official repository for the Archipelago integration manual for Super Street Fighter 2. This manual is a community‑driven effort to enhance the gaming experience by linking various elements and goals across games in the Archipelago system. Currently, the randomizer is based on the Super Nintendo (SNES) version of the game. Other versions will be reviewed later to ensure compatibility of all checks, since some modes—like Time Challenge—may not be available everywhere. Hooks support will also be added in the future to improve the YAML integration.

## Project Status
This project has completed its **Alpha** phase and is now in **Beta**. It is fully functional, with many optimizations and additional features underway. Your feedback and contributions remain invaluable for improving the manual and resolving any issues. Each Beta release is tested at least once before being pushed to GitHub. However, no system is infallible, so please report any bugs or inconsistencies.

## Current Features
- **Super Battle Mode – ALL CLEARS**: Complete Super Battle Mode with every character.  
- **Street Fighter Token**: Collect tokens scattered throughout the game.  
- **Time Challenge Mode – ALL CLEARS**: Defeat every opponent in Time Challenge Mode.  
- **ALL CLEARS + TOKENS**: Fulfill all objectives and gather all tokens.

## Future Features (not guaranteed)
- Add character‑specific special moves into the item pool.  
- Require winning at least one round for each special move check.

## Patch Notes

### Version 0.6.0
- Added special moves to the item pool.

### Version 0.5.1
- Fixed migration-related issues.

### Version 0.5.0
- Migrated to the new Manual Archipelago framework (Version 0.5.0).

### Version 0.4.1: PopTracker Updates
- Added items and locations to the PopTracker.

### Version 0.4.0: PopTracker Updates
- Introduced the PopTracker (in beta), with item and location support.  
- Auto‑tracker integration with Archipelago is in development.

### Version 0.3.3
- Renamed all character‑battle checks to improve spoiler logs and item pools.  
- Renamed tokens and increased their count to 25.

### Version 0.3.2
- Reordered check names to start with the player’s name; added three bonus checks without requiring a perfect score.

### Version 0.3.1
#### Removals
- Removed three checks that persisted after character re‑categorization.

#### Additions
- Created a new “Special” category.  
- Added three replacement checks.

### Version 0.3.0
#### Modifications
- Fixed the “CPU Time Challenge” category title by removing the stray capital “I.”  

#### Additions
- Added new YAML categories for more flexible seed creation.  
- Introduced a “token” category in `game.json` (value 0) to allow token removal.  
- Established checks for each character’s battles, bonus stages, and lore‑inspired challenges.

#### Known Issues
- No multiworld tests performed yet; potential edge cases may remain.

### Version 0.2.0
#### Additions
- Added “Beat Ryu with Ken” and “Beat Ken with Ryu” checks.  
- Renamed “Beat the Game” to “Super Battle Mode.”  
- Changed “Get perfect” to “Get Perfect Round.”  
- Added checks for the three bonus stages in Super Battle Mode.  
- Introduced “Game Mode” and “CPU Time Challenge” item categories.  
- Renamed items in the “Characters” category.  
- Renamed “Fun” to “Challenge” and “Defeated” to “Defeated in Super Battle Mode.”  
- Added “Defeated in Time Challenge” checks.  
- Updated goals to “Super Battle Mode – ALL CLEARS,” “Time Challenge Mode – ALL CLEARS,” and “ALL CLEARS + TOKENS.”  
- Randomized starting items in `game.json` for Game Mode and CPU Time Challenge.  
- Increased token count to 20.

#### Known Bugs
- Challenge check generator ignores executable status; currently works around this by always requiring Super Battle, but ideally should allow an OR condition with Time Challenge.

### Version 0.1.0
- Removed the “Character Battles” goal.  
- Added the SFtoken goal and item.  
- Changed the filler item to “bandage.”  
- Introduced various new checks.

### Version 0.0.1
- Initial alpha release.  
- Core functionality implemented; optimizations pending.

## Future Projects
- **Difficulty Settings**: Optionally enforce difficulty restrictions when generating seeds.  
- **Other Game Modes**: Add new modes with unlockable checks/items.  
- **Additional Goals**: Explore more goal types to diversify playstyles.  
- **Game Versions**: Consider support for later releases like Super Street Fighter 2 Turbo (arcade).

## How to Contribute
We welcome all contributions!  
- **Feedback**: Playtest the scenarios and report any issues.  
- **Code**: Submit pull requests with bug fixes or feature suggestions.  
- **Docs**: Improve this README or add new documentation.

## Acknowledgements
Thanks to all contributors and community members whose support makes this project possible. Special thanks to our Discord moderators Seafo, Garbo, and RoobyRoo for their invaluable debugging help.

## Contact
If you’re a streamer or have questions, reach out on the Archipelago Discord or open an issue here on GitHub. I’ll respond as soon as I can.

We look forward to seeing how you help shape this project’s future!
