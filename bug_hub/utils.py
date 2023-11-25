"""
Utility Functions

This module contains utility functions that are not tied to specific Django models or views.
These functions provide common functionality that can be reused across different parts of the project.
"""
def get_choice_display(choices, choice_key):
    """
    Get the display value for a choice key.

    Args:
        choices (list of tuple): The list of choices.
        choice_key (str): The key of the choice.

    Returns:
        str: The display value for the choice.
    """
    return dict(choices).get(choice_key, "All")
