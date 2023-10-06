from django.views.generic import ListView, DetailView
from bug_hub.models import Bug
from django.urls import reverse


class BugListView(ListView):
    model = Bug
    template_name = "bug_hub/bug_list.html"
    context_object_name = "bugs"
    paginate_by = 20
    ordering = ["-report_date"]


class BugDetailView(DetailView):
    model = Bug
    template_name = "bug_hub/bug_detail.html"
    context_object_name = "bug"
