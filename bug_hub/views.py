"""
This module defines all the views for the Bug Hub application.
"""
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseServerError
from bug_hub.models import Bug
from config.constants import PAGINATE_BY
from .forms import BugCreationForm

class BugListView(ListView):
    """
    A view for displaying a paginated list of bug reports.

    Attributes:
        model (Bug): The model representing bug reports.
        template_name (str): The path to the HTML template for rendering the bug list.
        context_object_name (str): The name to use for the list of bug reports in the template context.
        paginate_by (int): The number of bug reports to display per page.
        ordering (list of str): The default ordering of bug reports in the list.
    """
    model = Bug
    template_name = "bug_hub/bug_list.html"
    context_object_name = "bugs"
    paginate_by = PAGINATE_BY
    ordering = ["-report_date"]

class BugDetailView(DetailView):
    """
    A view for displaying the details of a single bug report.

    Attributes:
        model (Bug): The model representing bug reports.
        template_name (str): The path to the HTML template for rendering the bug details.
        context_object_name (str): The name to use for the bug report in the template context.
    """
    model = Bug
    template_name = "bug_hub/bug_detail.html"
    context_object_name = "bug"

class BugCreateView(CreateView):
    """
    A view for creating a new bug report.

    This view allows users to create and submit new bug reports.

    Attributes:
        model (Bug): The model representing bug reports.
        form_class (BugCreationForm): The form class for creating bug reports.
        template_name (str): The path to the HTML template for rendering the bug creation form.
        success_url (str): The URL to redirect to after successfully creating a bug report.

    Methods:
        form_valid(form): Handles the form submission and sets the user who reported the bug.
    """
    model = Bug
    form_class = BugCreationForm
    template_name = "bug_hub/bug_create.html"
    success_url = reverse_lazy("bug_hub:bug_list")

    def form_valid(self, form):
        """
        Handle form submission and set the user who reported the bug.

        Returns:
            HttpResponse: A response indicating the success of bug creation.
        """
        try:
            form.instance.reported_by = self.request.user
            return super().form_valid(form=form)
        except Exception:
            error_msg = "An error occurred while creating the bug. Please try again later."
            return HttpResponseServerError(content=error_msg)
