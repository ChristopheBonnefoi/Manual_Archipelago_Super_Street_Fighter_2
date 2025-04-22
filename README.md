# Archipelago Manual for Super Street Fighter II


## Welcome!
Welcome to the official repository for the Archipelago integration manual for Super Street Fighter II. This community‑driven project enhances the gaming experience by linking objectives and items across multiple games in the Archipelago network. Currently, the randomizer supports the SNES version of Super Street Fighter II. Other versions will be reviewed for compatibility (some modes, like Time Challenge, may not exist everywhere). Hook support for more advanced YAML customization is planned.

## Project Status
We’ve moved from **Alpha** to **Beta**! The core functionality is complete and stable, with ongoing optimizations and new features under development. Every Beta release is tested internally before publishing, but bugs can still slip through—please report any issues you encounter.

## Current Features
- **Super Battle Mode – ALL CLEARS**  
  Win Super Battle Mode with every character.  
- **Street Fighter Token**  
  Collect tokens scattered throughout the game.  
- **Time Challenge Mode – ALL CLEARS**  
  Defeat every opponent in Time Challenge Mode.  
- **ALL CLEARS + TOKENS**  
  Complete all objectives and gather all tokens.

## Planned Features (subject to change) 
- Enforce “win at least one round” requirement for each special‑move check.

## Patch Notes

### Version 0.7.1 – YAML Update
Changes since 0.7.0:
- Migrated to the unstable Archipelago‑Manual framework (v0.7.0)  
- Removed “Difficulty” from the item pool configuration (v0.7.1)  
- Removed “Special Moves” from the item pool configuration (v0.7.1)  

### Version 0.6.0
- Added special moves to the item pool.

### Version 0.5.1
- Fixed migration‑related issues.

### Version 0.5.0
- Migrated to the new Archipelago‑Manual framework (v0.5.0).

### Version 0.4.1 – PopTracker Updates
- PopTracker: added missing items and locations.

### Version 0.4.0 – PopTracker Beta
- Introduced PopTracker (beta) with item & location support.  
- Began work on auto‑tracker integration.

### Version 0.3.3
- Renamed all character‑battle checks for clearer spoiler logs and cleaner item pools.  
- Increased token count to 25.

### Version 0.3.2
- Reordered check names to start with the player’s name.  
- Added three bonus checks without requiring perfect score.

### Version 0.3.1
#### Removals
- Removed three outdated checks after character recategorization.

#### Additions
- Created a new “Special” category.  
- Added three replacement checks.

### Version 0.3.0
#### Fixes
- Corrected “CPU Time Challenge” category title (removed stray capital “I”).

#### Additions
- Added flexible YAML categories for seed creation.  
- Introduced a “token” category in `game.json` (value 0) to allow token removal.  
- Established checks for every character battle, bonus stage, and lore‑inspired challenge.

#### Known Issues
- No multiworld tests yet; edge cases may remain.

### Version 0.2.0
#### Additions
- New checks: “Beat Ryu with Ken” and “Beat Ken with Ryu.”  
- Renamed “Beat the Game” → “Super Battle Mode.”  
- Renamed “Get perfect” → “Get Perfect Round.”  
- Added checks for three bonus stages in Super Battle Mode.  
- Introduced “Game Mode” and “CPU Time Challenge” categories.  
- Renamed several “Character” category items.  
- Renamed “Fun” → “Challenge” and “Defeated” → “Defeated in Super Battle Mode.”  
- Added “Defeated in Time Challenge” checks.  
- Updated goals to “Super Battle Mode – ALL CLEARS,” “Time Challenge Mode – ALL CLEARS,” and “ALL CLEARS + TOKENS.”  
- Randomized starting items for Game Mode and CPU Time Challenge.  
- Increased token count to 20.

#### Known Bugs
- Challenge‑check generator ignores executable flag; currently always requires Super Battle. Ideally it should allow an OR condition with Time Challenge.

### Version 0.1.0
- Removed “Character Battles” goal.  
- Added SFtoken goal and item.  
- Changed filler item to “bandage.”  
- Introduced various new checks.

### Version 0.0.1
- Initial alpha release; core functionality implemented.

## Future Roadmap
- **Difficulty Settings**: Enforce per‑seed difficulty restrictions.  
- **Additional Game Modes**: Support new modes and associated checks.  
- **More Goals**: Diversify playstyles with new victory conditions.  
- **Other Game Versions**: Explore support for SSF2 Turbo (arcade) and beyond.

## Contributing
We welcome all feedback and contributions!  
- **Report bugs** or suggest features via GitHub issues.  
- **Submit PRs** with code fixes or optimizations.  
- **Improve documentation** or add new guides.

## Acknowledgements
Thank you to everyone who’s contributed so far—especially our Discord moderators **Seafo**, **Garbo**, and **RoobyRoo** for all their debugging help!

## Contact
Questions or streams? Reach out on the Archipelago Discord or open an issue here on GitHub. I’ll respond as soon as possible. We look forward to your contributions!  
