from typing import Optional, Any
from BaseClasses import MultiWorld


MODE_OPTION_BY_ITEM = {
    "Super Battle": "Super_Battle",
    "Time Challenge": "CPU_Time_Challenge",
}

SETTING_OPTION_BY_CATEGORY = {
    "Difficulty": "Difficulty",
    "Special Moves": "Special_Moves",
    "CPU Time Challenge": "CPU_Time_Challenge",
    "Defeated in Time Challenge": "CPU_Time_Challenge",
    "Defeated in Super Battle Mode": "Super_Battle",
}

DEF_ALWAYS_VISIBLE_CATEGORIES = {"Goal"}
TOKEN_CATEGORY_NAME = "Token"
TOKEN_ITEM_NAME = "Shadaloo Emblem"
TOKEN_GOAL_NAMES = {"ALL CLEARS + TOKENS", "Street Fighter Token"}


def _enabled_mode_items(multiworld: MultiWorld, player: int) -> set[str]:
    return {
        item_name
        for item_name, option_name in MODE_OPTION_BY_ITEM.items()
        if _is_option_enabled(multiworld, player, option_name)
    }


def _is_option_enabled(multiworld: MultiWorld, player: int, option_name: str) -> bool:
    option = getattr(multiworld.worlds[player].options, option_name, None)
    return bool(option and option.value > 0)


def _selected_goal_name(multiworld: MultiWorld, player: int) -> str:
    world = multiworld.worlds[player]
    goal = getattr(world.options, "goal", None)
    goal_index = int(getattr(goal, "value", 0))
    victory_names = getattr(world, "victory_names", [])
    if 0 <= goal_index < len(victory_names):
        return victory_names[goal_index]
    return victory_names[0] if victory_names else ""


def _selected_goal_requires_tokens(multiworld: MultiWorld, player: int) -> bool:
    world = multiworld.worlds[player]
    goal_name = _selected_goal_name(multiworld, player)
    goal_location = getattr(world, "location_name_to_location", {}).get(goal_name, {})
    return TOKEN_ITEM_NAME in str(goal_location.get("requires", "")) or goal_name in TOKEN_GOAL_NAMES


def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == TOKEN_CATEGORY_NAME:
        return _selected_goal_requires_tokens(multiworld, player)
    return None


def before_is_item_enabled(multiworld: MultiWorld, player: int, item: dict[str, Any]) -> Optional[bool]:
    item_name = item.get("name", "")
    if item_name in MODE_OPTION_BY_ITEM:
        return _is_option_enabled(multiworld, player, MODE_OPTION_BY_ITEM[item_name])

    categories = set(item.get("category", []))
    if TOKEN_CATEGORY_NAME in categories or item_name == TOKEN_ITEM_NAME:
        return _selected_goal_requires_tokens(multiworld, player)

    for category in categories:
        if category in SETTING_OPTION_BY_CATEGORY:
            return _is_option_enabled(multiworld, player, SETTING_OPTION_BY_CATEGORY[category])

    return None


def before_is_location_enabled(multiworld: MultiWorld, player: int, location: dict[str, Any]) -> Optional[bool]:
    requires = str(location.get("requires", ""))
    if TOKEN_ITEM_NAME in requires and not _selected_goal_requires_tokens(multiworld, player):
        return False

    if location.get("victory"):
        return True

    categories = set(location.get("category", []))
    if categories.intersection(DEF_ALWAYS_VISIBLE_CATEGORIES):
        return True

    for category in categories:
        if category in SETTING_OPTION_BY_CATEGORY and not _is_option_enabled(multiworld, player, SETTING_OPTION_BY_CATEGORY[category]):
            return False

    referenced_modes = {
        mode_item
        for mode_item in MODE_OPTION_BY_ITEM
        if f"|{mode_item}|" in requires
    }

    if referenced_modes and not referenced_modes.intersection(_enabled_mode_items(multiworld, player)):
        return False

    return None


def before_is_event_enabled(multiworld: MultiWorld, player: int, event: dict[str, Any]) -> Optional[bool]:
    return None
