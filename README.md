# Archipelago Manual for Super Street Fighter 2

## Welcome!
Welcome to the official repository for the Archipelago integration manual for Super Street Fighter 2. This manual is part of a community-driven effort to enhance the gaming experience by linking various elements and goals across games in the Archipelago system.

## Project Status
This project has completed its **Alpha** phase and is now in **Beta**. It is functional, with many optimizations and additional features underway. Your feedback and contributions are still highly valued as they help further improve the manual and fix potential issues. Each Beta release is tested at least once before being uploaded to GitHub, but as no system is infallible, please do not hesitate to report any errors.

## Current Features
- **Arcade Mode Completion**: Players must complete the arcade modes for all characters.
- **Token Completion**: Players collect tokens to complete the game.

## Patch Notes
### Version 0.2.0

#### Additions
- Added requirements for the checks "Beat Ryu with Ken" and "Beat Ken with Ryu".
- Renamed "Beat the Game" category to "Super Battle Mode".
- Changed "Get perfect" to "Get Perfect Round".
- Added checks related to the 3 bonus stages in the "Super Battle Mode" category.
- Introduced "Game Mode" and "CPU Time Challenge" item categories.
- Renamed items in the "Characters" category.
- Renamed the "Fun" category to "Challenge".
- Renamed the "Defeated" category to "Defeated in Super Battle Mode".
- Added checks for the "Defeated in Time Challenge" category.
- Changed the goal "All Characters Complete!" to "Super Battle Mode - ALL CLEARS".
- Introduced goals "Time Challenge Mode - ALL CLEARS" and "ALL CLEARS + TOKENS".
- Updated and added goals in the .yaml configuration.
- Randomized starting items in "Game Mode" and "CPU Time Challenge" on game.json.
- Updated and added necessary requirements.
- Increased the token count to 20.

#### Known Bugs
- During challenge check generation, the system does not account for the executable status; currently, this is addressed by requiring "Super Battle", but ideally, it would also support an OR condition for "Time Challenge" + the dedicated character.

### Version 0.1.0
- Removed the "Character Battles" goal.
- Added the "SFtoken" goal and item.
- Changed the filler item to "bandage".
- Added various checks.

### Version 0.0.1
- Initial alpha release.
- Functionality in place but pending optimization.

## Future Projects
- **Difficulty Settings**: Allow players to choose whether to activate difficulty restrictions during seed generation.
- **Other Game Modes**: Plan to add other game modes to introduce new checks and possibly make them unlockable items.
- **Other Goals**: Exploring other types of goals to diversify the gameplay.
- **Game Version**: Considering using a more recent version of the game like Super Street Fighter 2 Turbo for arcade.

## How to Contribute
We welcome contributions from everyone. Here are a few ways you can help:
- **Feedback**: Play through the scenarios and provide feedback on gameplay and manual instructions.
- **Code Contributions**: Submit pull requests with bug fixes or feature suggestions.
- **Documentation**: Help improve this README or add other documentation.

## Acknowledgements
A special thank you to all the contributors and community members who have supported this project. Your dedication and passion are what make these enhancements possible.
Additional thanks to our Discord moderators Seafo, Garbo, and RoobyRoo for their invaluable debugging assistance.

## Contact
If you are a streamer or have any queries, do not hesitate to reach out on our Archipelago Discord or submit an issue here on GitHub. I will make an effort to respond when available.

We are excited to see how you will help shape the future of this project!
