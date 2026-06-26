# Archipelago Manual for Super Street Fighter II

## Welcome!
Welcome to the official repository for the Archipelago Manual integration for **Super Street Fighter II**.
This community-driven project links SSF2 objectives and progression items into the Archipelago multiworld network.

The manual currently targets the SNES version of **Super Street Fighter II**. Other versions may be reviewed later, because some modes and checks can differ between releases.

## Project Status
The project is moving into **Version 1.0.0** with the current Manual Archipelago framework.
The core gameplay data is still SSF2-focused, while the package structure, client, hooks, token handling, YAML template, and documentation have been refreshed for the release update.

## Current Features
- **Super Battle Mode - ALL CLEARS**
  Win Super Battle Mode with every character.
- **Time Challenge Mode - ALL CLEARS**
  Defeat every opponent in Time Challenge Mode.
- **Street Fighter Token**
  Collect Shadaloo Emblems as the token objective.
- **ALL CLEARS + TOKENS**
  Complete all clear objectives and gather the required Shadaloo Emblems.

---

## Patch Notes

### Version 1.0.0 - Release Update

**Manual framework update**
- Synced the source package with the newer Manual Archipelago stable base (`manual_stable_20260319`).
- Updated the Manual core files for data loading, item creation, rules, regions, options, validation, helper APIs, and client support.
- Added `container.py` for modern `.apmanual` zip container support.
- Saved and reloaded `categories.json` in `.apmanual` files, with a fallback for older files that do not contain categories yet.
- Added an empty `data/events.json` so the project is ready for the current Manual event system.
- Added the stable Manual test package under `manual_ssf2_narusnake/test/`.
- Updated the Manual client foundation with newer tracker support, client settings, item/location sorting, search refresh behavior, DeathLink UI support, and modern `.apmanual` reading.

**SSF2 hooks and generation logic**
- Added SSF2-specific token logic for `Shadaloo Emblem`.
- Token goals now add Shadaloo Emblems to the pool; non-token goals remove them from the pool.
- Added configurable token requirements through `shadaloo_emblems_required`.
- Added configurable token availability through `shadaloo_emblems_available_percentage`.
- Extra Shadaloo Emblems above the required amount are classified as useful instead of progression.
- Added a `Filler` category hook. When filler items are added later, the world can choose from that category; until then it falls back to the game filler item.
- Added and translated the current dedicated `Filler` category items into English.
- Added goal-based option forcing so required modes stay enabled for their selected goals.
- Added support for forcing `Super_Battle` and `CPU_Time_Challenge` when a selected goal needs them. Token handling is inferred from the selected goal.
- Added stable location sort keys through `hooks/Data.py` so the Manual client can keep the intended location order.

**Options, categories, and YAML**
- Added `Super_Battle` and `CPU_Time_Challenge` options.
- Removed the public `Token` YAML toggle and kept token item placement goal-driven through `Shadaloo Emblem` requirements.
- Clarified that disabling `Special_Moves` removes special-move items from the pool but leaves special-move checks available, because moves can be used freely without item restrictions.
- Added `shadaloo_emblems_required` and `shadaloo_emblems_available_percentage` goal settings.
- Added goal aliases for cleaner YAML values.
- Added category wiring for Super Battle checks, Time Challenge checks, CPU Time Challenge items, Special Moves, Difficulty, Token, and future Filler items.
- Standardized character naming across items, locations, categories, and requirements with the canonical item spellings: `E.Honda`, `M.Bison`, `T.Hawk`, and `Chun-Li`.
- Reworked `Manual_SSF2_NaruSnake.yaml` using the Tekken 2 template style.
- Updated the YAML template to require Archipelago `0.6.7`.
- Added `random`, `random-low`, `random-high`, and `random-range-*` entries for numeric options.
- Added `plando_items` to the YAML template.

**Documentation**
- Updated this README for the 1.0.0 release update.
- Added a French README at `manual_ssf2_narusnake/docs/README_FR.md`.
- Added an English YAML guide at `manual_ssf2_narusnake/docs/guide.md`.
- Added a French YAML guide at `manual_ssf2_narusnake/docs/guide_fr.md`.
- The guides explain YAML weights, random values, checks, game modes, goals, Shadaloo Emblem token settings, exact item/location names, and example presets.

**Notes for this release**
- Dedicated filler items are currently present in the `Filler` category. The hook can use that category and still falls back to the game filler item if the category is empty later.
- Rebuild the `.apworld` after changing source files when preparing a distributable release.

---

### Version 0.8.0 - New Logic Update
- Made some categories visible again in the client through `categories.json`.
- Overhauled logic so several challenges can be completed in Time Challenge mode.
- Time Challenge checks now require the matching CPU character where needed.
- Changed the syntax of all `requires` entries.
- Added a **Stage** check category and related checks.
- Added **First Attack** checks for each character.
- Added subcategories for special moves in `items.json`.
- Added checks related to special moves.
- Made special moves progression items.
- Displayed all special moves in the **Special Moves** category in the client.
- Added extra checks in the **Special Moves** category.

---

### Version 0.7.1 - YAML Update
Changes since 0.7.0:
- Migrated to the unstable Archipelago Manual framework.
- Removed **Difficulty** from the item pool configuration.
- Removed **Special Moves** from the item pool configuration.

---

### Version 0.6.0
- Added special moves to the item pool.

---

### Version 0.5.1
- Fixed migration-related issues.

---

### Version 0.5.0
- Migrated to the new Archipelago Manual framework.

---

### Version 0.4.1 - PopTracker Updates
- PopTracker: added missing items and locations.

---

### Version 0.4.0 - PopTracker Beta
- Introduced PopTracker beta with item and location support.
- Began work on auto-tracker integration.

---

### Version 0.3.3
- Renamed all character-battle checks for clearer spoiler logs and cleaner item pools.
- Increased token count to 25.

---

### Version 0.3.2
- Reordered check names to start with the player's name.
- Added three bonus checks without requiring a perfect score.

---

### Version 0.3.1
**Removals**
- Removed three outdated checks after character recategorization.

**Additions**
- Created a new **Special** category.
- Added three replacement checks.

---

### Version 0.3.0
**Fixes**
- Corrected the **CPU Time Challenge** category title.

**Additions**
- Added flexible YAML categories for seed creation.
- Introduced a token category in `game.json` to allow token removal.
- Established checks for every character battle, bonus stage, and lore-inspired challenge.

**Known Issues**
- No multiworld tests yet; edge cases may remain.

---

### Version 0.2.0
**Additions**
- Added checks for **Beat Ryu with Ken** and **Beat Ken with Ryu**.
- Renamed **Beat the Game** to **Super Battle Mode**.
- Renamed **Get perfect** to **Get Perfect Round**.
- Added checks for three bonus stages in Super Battle Mode.
- Introduced **Game Mode** and **CPU Time Challenge** categories.
- Renamed several character category items.
- Renamed **Fun** to **Challenge** and **Defeated** to **Defeated in Super Battle Mode**.
- Added **Defeated in Time Challenge** checks.
- Updated goals to **Super Battle Mode - ALL CLEARS**, **Time Challenge Mode - ALL CLEARS**, and **ALL CLEARS + TOKENS**.
- Randomized starting items for Game Mode and CPU Time Challenge.
- Increased token count to 20.

**Known Bugs**
- Challenge-check generation was still too tied to Super Battle and needed broader Time Challenge support.

---

### Version 0.1.0
- Removed the old **Character Battles** goal.
- Added the Street Fighter token goal and item.
- Changed the filler item to **Bandage**.
- Introduced various new checks.

---

### Version 0.0.1
- Initial alpha release with core functionality implemented.

---

## Future Roadmap
- **Filler item review**: Review, replace, or expand the dedicated `Filler` category item list as needed.
- **Difficulty settings**: Continue refining per-seed difficulty restrictions.
- **Additional game modes**: Support new modes and associated checks where the target game version allows them.
- **More goals**: Diversify playstyles with new victory conditions.
- **Other game versions**: Explore SSF2 Turbo, arcade variants, and beyond.

---

## Contributing
Feedback and contributions are welcome.
- Report bugs or suggest features through GitHub issues.
- Submit PRs with code fixes or optimizations.
- Improve documentation or add new guides.

---

## Acknowledgements
Thank you to everyone who has contributed so far, especially the Discord moderators **Seafo**, **Garbo**, and **RoobyRoo** for debugging help and feedback.

---

## Contact
Questions, streams, or bug reports? Reach out on the Archipelago Discord or open an issue on GitHub.
