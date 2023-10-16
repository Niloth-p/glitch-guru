from django.core.exceptions import ValidationError
from django.utils import timezone
from .choices import BUG_TYPE_CHOICES, STATUS_CHOICES
from config.constants import MIN_CHAR_LENGTH_BUG_TITLE


def validate_description_not_empty(value):
    """Ensure that the description field is not empty."""
    if not value.strip():
        error_message = "Description cannot be empty."
        raise ValidationError(error_message)


def validate_bug_type(value):
    """Ensure that the bug_type field value is one of the predefined choices"""
    choices = [choice[0] for choice in BUG_TYPE_CHOICES]
    if value not in choices:
        error_message = "Invalid bug type."
        raise ValidationError(error_message)


def validate_report_date_not_future(value):
    """Ensure that the report_date field is in the past (no future reports allowed)."""
    if value > timezone.now():
        error_message = "Report date cannot be in the future."
        raise ValidationError(error_message)


def validate_status(value):
    """Ensure that the status field value is one of the predefined choices"""
    choices = [choice[0] for choice in STATUS_CHOICES]
    if value not in choices:
        error_message = "Invalid status."
        raise ValidationError(error_message)


def validate_min_length(value):
    """Ensure that the title field value is at least 10 characters long"""
    if len(value) < MIN_CHAR_LENGTH_BUG_TITLE:
        raise ValidationError("Title must be at least 10 characters long.")
