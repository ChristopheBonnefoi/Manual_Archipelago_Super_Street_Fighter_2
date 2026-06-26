from Options import Option, OptionGroup, PerGameCommonOptions
from typing import Type, Any


SSF2_GOAL_ALIASES = {
    "super_battle": 0,
    "super battle": 0,
    "super battle all clears": 0,
    "time_challenge": 1,
    "time challenge": 1,
    "time challenge all clears": 1,
    "all_clears_tokens": 2,
    "all clears tokens": 2,
    "all clears + tokens": 2,
    "street_fighter_token": 3,
    "street fighter token": 3,
}


def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    return options


def after_options_defined(options: Type[PerGameCommonOptions]):
    goal = options.type_hints.get("goal")
    if goal is not None:
        goal.aliases.update(SSF2_GOAL_ALIASES)
        goal.options.update(SSF2_GOAL_ALIASES)


def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    return groups


def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
