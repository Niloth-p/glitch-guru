from django.views.generic import ListView, DetailView, CreateView
from bug_hub.models import Bug
from django.urls import reverse_lazy
from .forms import BugCreationForm
from django.http import HttpResponseServerError


class BugListView(ListView):
    model = Bug
    template_name = "bug_hub/bug_list.html"
    context_object_name = "bugs"
    paginate_by = 10
    ordering = ["-report_date"]


class BugDetailView(DetailView):
    model = Bug
    template_name = "bug_hub/bug_detail.html"
    context_object_name = "bug"


class BugCreateView(CreateView):
    model = Bug
    form_class = BugCreationForm
    template_name = "bug_hub/bug_create.html"
    success_url = reverse_lazy("bug_hub:bug_list")

    def form_valid(self, form):
        try:
            form.instance.reported_by = self.request.user
            return super().form_valid(form)
        except Exception as e:
            error_msg = "An error occurred while creating the bug. Please try again later."
            return HttpResponseServerError(error_msg)
