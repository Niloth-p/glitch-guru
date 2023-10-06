from django.urls import path
from . import views

app_name = "bug_hub"

urlpatterns = [
    path("", views.BugListView.as_view(), name="bug_list"),
    path("<int:pk>/", views.BugDetailView.as_view(), name="bug_detail"),
]
