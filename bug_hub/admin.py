from django.contrib import admin
from .models import Bug


# Register your models here.
@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ("description", "bug_type", "report_date", "status")
