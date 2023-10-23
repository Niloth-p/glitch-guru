"""
This module defines custom context processors for the Glitch Guru web application.
Context processors are used to add dynamic data to the context of all templates.
"""

from .constants import PRODUCT_NAME

def constants(request):
    """
    This function is a custom context processor that adds commonly used constants
    to the template context. These constants can be accessed in all templates.

    Args:
        request (HttpRequest): The current HTTP request object.

    Returns:
        dict: A dictionary containing the constants to be included in the template context.
    """
    return {
        'PRODUCT_NAME': PRODUCT_NAME
    }
