"""
A module for sorting and displaying names from a dictionary based on first names.
The names of the team's members (Group-25) are the data utilized to run this program.

Module contents:
    - get_first_name(item):
      Extracts the first name from a dictionary item.
    - display_sorted_names(names_dict): Displays names sorted by first names.

Sorting rules:
    - Names are sorted alphabetically by first names,
    - then by last names if first names are identical.
"""

from typing import Dict, Tuple


def get_first_name(item: Tuple[str, str]) -> str:
    """
    Extract the first name from a dictionary item.

    Args:
        item (Tuple[str, str]): A tuple containing (last_name, first_name).
    Returns:
        str: The first name.
    Raises:
        TypeError: If 'item' is not a tuple.
        ValueError: If 'item' does not contain exactly two elements.
    """
    if not isinstance(item, tuple):
        raise TypeError("Input item must be a tuple")
    if len(item) != 2:
        raise ValueError(
            "Input tuple must contain exactly two elements (last_name, first_name)"
        )
    return item[1]


def display_sorted_names(names_dict: Dict[str, str]) -> None:
    """
    Display names in alphabetical order of first names.

    Args:
        names_dict (Dict[str, str]): Dictionary with last names as keys and
        first names as values.
    Returns:
        None. Prints names in format:
        1. FirstName LastName
        2. FirstName LastName
    """
    if not isinstance(names_dict, dict):
        raise TypeError("names_dict must be a dictionary")
    for key, value in names_dict.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Both keys and values must be strings")

    if not names_dict:
        print("No names to display.")
        return

    sorted_names = sorted(
        names_dict.items(), key=lambda item: (item[1].lower(), item[0].lower())
    )

    for i, (last_name, first_name) in enumerate(sorted_names, 1):
        print(f"{i}. {first_name} {last_name}")


# Define group names, then main block
group_names = {
    "Abd Elraheem": "Amin",
    "Mohammed": "Razan",
    "Seedahmed": "Abdalrahman",
    "Solomon": "Alexander",
    "Ibrahim": "Azza",
    "El-Waleed": "Tamir",
    "Saeed": "Mohamed",
    "Alaa": "Mohamed",
    "Albashityalshaer": "Kefah",
    "Makki": "Mohamed",
}

if __name__ == "__main__":
    display_sorted_names(group_names)
