def get_choice_display(choices, key):
    """Return the display name for a given key from a list of choices or 'All' if the key is not found."""
    for code, display in choices:
        if code == key:
            return display
    return 'All'