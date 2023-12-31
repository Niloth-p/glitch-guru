"""
Database models for storing bug information and related data
"""

from django.db import models
from config.constants import MAX_CHAR_LENGTH_BUG_TITLE
from .choices import BUG_TYPE_CHOICES, STATUS_CHOICES
from .model_validators import (
    validate_bug_type,
    validate_description_not_empty,
    validate_report_date_not_future,
    validate_status,
    validate_min_length,
)

class Bug(models.Model):
    """
    Model for storing bug details in a database.

    This model represents various attributes related to bugs, including their description,
    type, reporting date, and status.

    :param CharField title: Name of the bug.
    :param TextField description: A detailed description of the bug.
    :param CharField bug_type: The type of bug, such as error, feature request, enhancement, documentation.
    :param DateTimeField report_date: The date when the bug was reported. User cannot set it. Only auto-generated.
    :param CharField status: The current status of the bug (e.g., To Do, In Progress, Done, Under Review, Won't Fix).
    """

    title = models.CharField(
        max_length=MAX_CHAR_LENGTH_BUG_TITLE,
        unique=True,
        verbose_name="Bug Title",
        help_text="Enter a concise title for the bug report.",
        validators=[validate_min_length],
    )

    description = models.TextField(
        verbose_name="Bug Description",
        help_text="Provide a detailed description of the bug, including steps to reproduce.",
        validators=[validate_description_not_empty],
    )

    bug_type = models.CharField(
        max_length=20,
        choices=BUG_TYPE_CHOICES,
        blank=False,
        null=False,
        verbose_name="Bug Type",
        help_text="Select the type of the bug",
        validators=[validate_bug_type],
    )

    report_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Report Date",
        help_text="Date when the bug was reported",
        validators=[validate_report_date_not_future],
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
        default="todo",
        verbose_name="Bug Status",
        help_text="Indicate the current status of bug resolution",
        validators=[validate_status],
    )

    def __str__(self):
        """Returns a string representation of the bug."""
        return str(object=self.title)

    # pylint: disable=R0903
    class Meta:
        """
        :param str verbose_name: A human-readable singular name for the model.
        :param str verbose_name_plural: A human-readable plural name for the model.
        :param list of str ordering: The default ordering of records in the database.
        """

        verbose_name = "Bug"
        verbose_name_plural = "Bugs"
        ordering = ["-report_date"]
    # pylint: disable=R0903
