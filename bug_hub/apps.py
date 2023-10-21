"""
Django Application Configuration
"""
from django.apps import AppConfig

class BugHubConfig(AppConfig):
    """
    This class configures BugHub
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bug_hub'
