# Archipelago Manual for Super Street Fighter 2

## Welcome!
Welcome to the official repository for the Archipelago integration manual for Super Street Fighter 2. This manual is part of a community-driven effort to enhance the gaming experience by linking various elements and goals across games in the Archipelago system. Currently, the randomizer is based on the Super Nintendo version of the game. I plan to review other versions later to ensure that all checks are compatible, as some modes like Time Challenge may not be present everywhere. I also intend to learn about hooks in the future to further improve the YAML quality.

## Project Status
This project has completed its **Alpha** phase and is now in **Beta**. It is functional, with many optimizations and additional features underway. Your feedback and contributions are still highly valued as they help further improve the manual and fix potential issues. Each Beta release is tested at least once before being uploaded to GitHub. However, since no system is infallible, please do not hesitate to report any errors.

## Current Features
- **Super Battle Mode - ALL CLEARS**: Players must complete the Super Battle Mode for all characters.
- **Street Fighter Token**: Players collect tokens to complete the game.
- **Time Challenge Mode - ALL CLEARS**: Defeat all opponents in Time Challenge Mode.
- **ALL CLEARS + TOKENS**: Achieve all objectives and collect tokens.

## Future Features (not guaranteed)
- Adding character-specific techniques to the item pool.
- Implementing a requirement to win a round for each special technique.

## Patch Notes

### Version 0.3.3:
- Renamed all checks related to character battles to improve the spoiler log and item pool.
- Renamed tokens and increased their number to 25.

### Version 0.3.2:
- Renamed all checks to have the player's name first and added bonus checks 1, 2, and 3 cleared without necessarily getting a perfect score.

### Version 0.3.1:

#### Removals
- Removed 3 checks that were inadvertently left after the re-categorization of each character.

#### Additions
- Added a new "Special" category in the checks.
- Introduced 3 new checks to replace the removed ones.

### Version 0.3.0

#### Modifications
- Corrected the "CPU Time Challenge" category by removing the unnecessary capital "I" in "Time."

#### Additions
- Added new YAML categories for more flexible seed creation options.
- Added a "token" category in `game.json` with a value of 0 to allow for token removal from the pool (still in progress).
- Created checks for each character, covering all combats, bonus stages, and additional fun checks based on the series' general lore, not strictly the game.

#### Known Issues
- No issues have been identified yet, as the seed has not been tested in a multiworld environment.

### Version 0.2.0

#### Additions
- Added requirements for the checks "Beat Ryu with Ken" and "Beat Ken with Ryu."
- Renamed the "Beat the Game" category to "Super Battle Mode."
- Changed "Get perfect" to "Get Perfect Round."
- Added checks related to the three bonus stages in the "Super Battle Mode" category.
- Introduced new item categories: "Game Mode" and "CPU Time Challenge."
- Renamed items in the "Characters" category.
- Renamed the "Fun" category to "Challenge."
- Renamed the "Defeated" category to "Defeated in Super Battle Mode."
- Added checks for the "Defeated in Time Challenge" category.
- Changed the goal "All Characters Complete!" to "Super Battle Mode - ALL CLEARS."
- Introduced new goals: "Time Challenge Mode - ALL CLEARS" and "ALL CLEARS + TOKENS."
- Updated and added goals in the .yaml configuration.
- Randomized starting items in "Game Mode" and "CPU Time Challenge" in `game.json`.
- Updated and added necessary requirements.
- Increased the token count to 20.

#### Known Bugs
- During challenge check generation, the system does not account for the executable status. Currently, this is addressed by requiring "Super Battle," but ideally, it should support an OR condition for "Time Challenge" + the dedicated character.

### Version 0.1.0
- Removed the "Character Battles" goal.
- Added the "SFtoken" goal and item.
- Changed the filler item to "bandage."
- Added various checks.

### Version 0.0.1
- Initial alpha release.
- Functionality in place but pending optimization.

## Future Projects
- **Difficulty Settings**: Allow players to choose whether to activate difficulty restrictions during seed generation.
- **Other Game Modes**: Plan to add other game modes to introduce new checks and possibly make them unlockable items.
- **Other Goals**: Exploring other types of goals to diversify gameplay.
- **Game Version**: Considering using a more recent version of the game, such as Super Street Fighter 2 Turbo for arcade.

## How to Contribute
We welcome contributions from everyone. Here are a few ways you can help:
- **Feedback**: Play through the scenarios and provide feedback on gameplay and manual instructions.
- **Code Contributions**: Submit pull requests with bug fixes or feature suggestions.
- **Documentation**: Help improve this README or add other documentation.

## Acknowledgements
A special thank you to all the contributors and community members who have supported this project. Your dedication and passion make these enhancements possible. Additional thanks to our Discord moderators Seafo, Garbo, and RoobyRoo for their invaluable debugging assistance.

## Contact
If you are a streamer or have any queries, do not hesitate to reach out on our Archipelago Discord or submit an issue here on GitHub. I will make an effort to respond when available.

We are excited to see how you will help shape the future of this project!
