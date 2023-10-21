"""
Django admin configuration for the Bug_Hub app
"""

from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    """
    Django admin configuration for the Bug model
    Makes it accessible and manageable through the Django admin interface.
    """

    list_display = ("title", "bug_type", "report_date", "status")
    fields = ("bug_type", "title", "description", "status")
