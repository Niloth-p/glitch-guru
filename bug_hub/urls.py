"""
URL configuration for routing web requests to views in Bug_Hub.
"""
from django.urls import path
from . import views

# pylint: disable=C0103
app_name = "bug_hub"
# pylint: enable=C0103

urlpatterns = [
    path(route="", view=views.BugListView.as_view(), name="bug_list"),
    path(route="<int:pk>/", view=views.BugDetailView.as_view(), name="bug_detail"),
    path(route="createBug/", view=views.BugCreateView.as_view(), name="bug_create"),
]
