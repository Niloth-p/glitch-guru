"""
This module contains constant values used throughout the application.

These constants are used to provide a centralized location for storing and managing
values that remain unchanged during the application's operation.

The module serves as a convenient reference for developers and ensures consistency
in the usage of important values.

Usage:
    The constants defined in this module can be imported and used in other parts
    of the application for various purposes, such as configuration settings or
    specifying default values.

Example:
    To use the PRODUCT_NAME constant in another module:

    ```python
    from constants import PRODUCT_NAME

    product_name = PRODUCT_NAME
    ```
"""
PAGINATE_BY = 10
MAX_CHAR_LENGTH_BUG_TITLE = 250
MIN_CHAR_LENGTH_BUG_TITLE = 10
PRODUCT_NAME = "Glitch Guru"
