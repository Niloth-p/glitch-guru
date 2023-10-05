from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Bug


def validate_description_not_empty(value):
    """Ensure that the description field is not empty."""
    if not value.strip():
        raise ValidationError("Description cannot be empty.")


def validate_bug_type(value):
    """Ensure that the bug_type field value is one of the predefined choices"""
    choices = [choice[0] for choice in Bug.BUG_TYPE_CHOICES]
    if value not in choices:
        raise ValidationError("Invalid bug type.")


def validate_report_date_not_future(value):
    """Ensure that the report_date field is in the past (no future reports allowed)."""
    if value > timezone.now():
        raise ValidationError("Report date cannot be in the future.")


def validate_status(value):
    """Ensure that the status field value is one of the predefined choices"""
    choices = [choice[0] for choice in Bug.STATUS_CHOICES]
    if value not in choices:
        raise ValidationError("Invalid status.")
