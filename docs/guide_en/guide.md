# YAML Guide for Manual_SSF2_NaruSnake

This guide explains how to fill `Manual_SSF2_NaruSnake.yaml` for Super Street Fighter II.
The YAML controls what kind of seed Archipelago generates for your player slot.

## Basic Rule

Keep these top-level fields:

```yaml
name: Player{number}
description: Default Manual_SSF2_NaruSnake Template
game: Manual_SSF2_NaruSnake
requires:
  version: 0.6.7

Manual_SSF2_NaruSnake:
```

All SSF2 options must stay inside the `Manual_SSF2_NaruSnake:` block.
Indentation matters. Use two spaces, not tabs.

## Weighted Options

Most options use weights. Archipelago chooses one entry based on the numbers you put next to each value.

```yaml
Super_Battle:
  'false': 0
  'true': 50
```

This means `true` has weight 50 and `false` has weight 0, so Super Battle will always be enabled.

```yaml
Super_Battle:
  'false': 25
  'true': 75
```

This means Super Battle has a 75 out of 100 chance to be enabled.

For numeric options, the template also supports:

```yaml
random: 0
random-low: 0
random-high: 0
random-range-1-100: 0
```

Use one fixed value when you want control. Use random entries when you want seed variety.

## Goals

The `goal` option decides the victory condition.

```yaml
goal:
  super battle mode -all clears-: 50
  time challenge mode -all clears-: 0
  all clears + tokens: 0
  street fighter token: 0
```

Available goals:

- `super battle mode -all clears-`: clear Super Battle mode with every character. This forces `Super_Battle` on.
- `time challenge mode -all clears-`: defeat every Time Challenge CPU. This forces `CPU_Time_Challenge` on.
- `all clears + tokens`: complete both clear objectives and collect the required Shadaloo Emblems. This forces `Super_Battle` and `CPU_Time_Challenge` on, and enables token handling automatically.
- `street fighter token`: collect the required Shadaloo Emblems. This enables token handling automatically.

Only one goal is selected when the seed is generated.

## Game Modes

`Super_Battle` controls Super Battle progression items and checks.

```yaml
Super_Battle:
  'false': 0
  'true': 50
```

When enabled, the pool can include the `Super Battle` item and Super Battle checks such as character fight clears, bonus clears, and Super Battle defeat checks.

`CPU_Time_Challenge` controls Time Challenge CPU items and checks.

```yaml
CPU_Time_Challenge:
  'false': 0
  'true': 50
```

When enabled, the pool can include CPU items such as `Ryu [CPU for Time Challenge]` and checks from `Defeated in Time Challenge`.

If a selected goal needs a mode, the hook forces that mode on so the seed stays beatable.

## Gameplay Options

`Difficulty` adds difficulty setting items to the item pool.

```yaml
Difficulty:
  'false': 0
  'true': 50
```

`Special_Moves` adds special-move items to the pool.

```yaml
Special_Moves:
  'false': 0
  'true': 50
```

When `Special_Moves` is off, special-move items are removed from the item pool. The move-based checks remain available, because the player can use the character techniques freely without needing item unlocks.

## Token Settings

There is no public `Token` YAML toggle anymore. Token item placement is controlled by the selected `goal`.

If the selected goal needs tokens, `Shadaloo Emblem` items are added to the pool. If the selected goal does not need tokens, `Shadaloo Emblem` is removed from the pool.

`shadaloo_emblems_required` sets how many Shadaloo Emblems are required.

```yaml
shadaloo_emblems_required:
  100: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-1-100: 0
```

`shadaloo_emblems_available_percentage` controls how many Shadaloo Emblems are placed compared to the required amount.

```yaml
shadaloo_emblems_available_percentage:
  100: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-100-400: 0
```

Examples:

- Required `25`, available `100`: 25 Shadaloo Emblems are placed.
- Required `25`, available `200`: 50 Shadaloo Emblems are placed.
- The final amount is capped at 100 Shadaloo Emblems.

## Checks

In Archipelago Manual, checks are locations. When you complete one in game, you mark that location in the client.

This manual includes 470 checks, grouped mostly by character and mode.

Common check groups:

- Character checks: fight clears, bonus clears, first attack, stun, perfect round, special move wins, and character-specific challenges.
- `Defeated in Super Battle Mode`: defeat each character in Super Battle.
- `Defeated in Time Challenge`: defeat each CPU in Time Challenge.
- `Stage`: stage object or stage-specific checks.
- `Special`: multi-character or special challenge checks.
- `Goal`: final victory locations.

Some checks can be completed through either Super Battle or Time Challenge. Their logic usually looks like:

```text
|Character [Player]| and |Super Battle| or (|Time Challenge| and |CPU [CPU for Time Challenge]|)
```

That means the check is valid if you have the playable character and Super Battle, or if Time Challenge is enabled and the matching CPU item is available.

## Exact Names Matter

When you write item or location names in YAML lists, use the exact spelling from the data files.

Canonical character spellings:

- `E.Honda`
- `M.Bison`
- `T.Hawk`
- `Chun-Li`

Useful item name examples:

```yaml
start_inventory:
  "Ryu [Player]": 1
  "Super Battle": 1
```

```yaml
start_inventory_from_pool:
  "Time Challenge": 1
```

Use quotes around names with brackets, apostrophes, or punctuation.

## Useful YAML Fields

`local_items` keeps listed items in your own world.

```yaml
local_items:
  - "Super Battle"
```

`non_local_items` forces listed items into other players' worlds.

```yaml
non_local_items:
  - "Shadaloo Emblem"
```

`start_hints` starts with item hints.

```yaml
start_hints:
  - "Shadaloo Emblem"
```

`start_location_hints` starts with location hints.

```yaml
start_location_hints:
  - "Street Fighter Token"
```

`exclude_locations` prevents important items from being placed on listed locations.

```yaml
exclude_locations:
  - "Ryu - Get Perfect Round"
```

`priority_locations` tries to place important items on listed locations.

```yaml
priority_locations:
  - "Street Fighter Token"
```

`plando_items` is available for planned item placement when your Archipelago setup allows plando.

## Example Presets

Super Battle focused:

```yaml
goal:
  super battle mode -all clears-: 50
  time challenge mode -all clears-: 0
  all clears + tokens: 0
  street fighter token: 0
Super_Battle:
  'false': 0
  'true': 50
CPU_Time_Challenge:
  'false': 50
  'true': 0
```

Time Challenge focused:

```yaml
goal:
  super battle mode -all clears-: 0
  time challenge mode -all clears-: 50
  all clears + tokens: 0
  street fighter token: 0
Super_Battle:
  'false': 50
  'true': 0
CPU_Time_Challenge:
  'false': 0
  'true': 50
```

Token hunt:

```yaml
goal:
  super battle mode -all clears-: 0
  time challenge mode -all clears-: 0
  all clears + tokens: 0
  street fighter token: 50
shadaloo_emblems_required:
  25: 50
shadaloo_emblems_available_percentage:
  200: 50
```

## Validation

Before generating a seed:

- Check indentation.
- Keep `game: Manual_SSF2_NaruSnake`.
- Keep all SSF2 options under `Manual_SSF2_NaruSnake:`.
- Use exact item and location names.
- Validate the YAML with a YAML checker or the Archipelago YAML check page.

