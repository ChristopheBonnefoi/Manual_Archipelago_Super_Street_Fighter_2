def _build_location_sort_key(location_index: int) -> str:
    return f"{location_index:06d}"


def after_load_game_file(game_table: dict) -> dict:
    return game_table


def after_load_item_file(item_table: list) -> list:
    return item_table


def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table


def after_load_location_file(location_table: list) -> list:
    for location_index, location in enumerate(location_table):
        location["sort-key"] = _build_location_sort_key(location_index)

    return location_table


def after_load_event_file(event_table: list) -> list:
    return event_table


def after_load_region_file(region_table: dict) -> dict:
    return region_table


def after_load_category_file(category_table: dict) -> dict:
    return category_table


def after_load_option_file(option_table: dict) -> dict:
    return option_table


def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table
