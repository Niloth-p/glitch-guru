from django.core.exceptions import ValidationError
from django.utils import timezone
from config.constants import MIN_CHAR_LENGTH_BUG_TITLE
from .choices import BUG_TYPE_CHOICES, STATUS_CHOICES

def validate_description_not_empty(value):
    """
    Ensures the description field is not empty.

    Args:
        value (str): The value of the description field.

    Raises:
        ValidationError: If the description is empty.
    """
    if not value.strip():
        error_message = "Description cannot be empty."
        raise ValidationError(message=error_message)

def validate_bug_type(value):
    """
    Ensures the bug_type field value is one of the predefined choices.

    Args:
        value (str): The value of the bug_type field.

    Raises:
        ValidationError: If the value is not in the predefined choices.
    """
    choices = [choice[0] for choice in BUG_TYPE_CHOICES]
    if value not in choices:
        error_message = "Invalid bug type."
        raise ValidationError(message=error_message)

def validate_report_date_not_future(value):
    """
    Ensures the report_date is in the past (no future reports allowed).

    Args:
        value (datetime): The value of the report_date field.

    Raises:
        ValidationError: If the report_date is in the future.
    """
    if value > timezone.now():
        error_message = "Report date cannot be in the future."
        raise ValidationError(message=error_message)

def validate_status(value):
    """
    Ensures the status field value is one of the predefined choices.

    Args:
        value (str): The value of the status field.

    Raises:
        ValidationError: If the value is not in the predefined choices.
    """
    choices = [choice[0] for choice in STATUS_CHOICES]
    if value not in choices:
        error_message = "Invalid status."
        raise ValidationError(message=error_message)

def validate_min_length(value):
    """
    Ensures the title field value is at least 10 characters long.

    Args:
        value (str): The value of the title field.

    Raises:
        ValidationError: If the title is shorter than 10 characters.
    """
    if len(value) < MIN_CHAR_LENGTH_BUG_TITLE:
        raise ValidationError(message="Title must be at least 10 characters long.")
