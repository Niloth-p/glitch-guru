"""
Django admin configuration for the bug_hub app
"""

from django.contrib import admin
from .models import Bug


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    """
    Django admin configuration for the Bug model
    """

    list_display = ("title", "bug_type", "report_date", "status")
    fields = ("bug_type", "title", "description", "status")
