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

    :param Bug model: The model representing bug reports.
    :param str template_name: The path to the HTML template for rendering the bug list.
    :param str context_object_name: The name to use for the list of bug reports in the template context.
    :param int paginate_by: The number of bug reports to display per page.
    :param list of str ordering: The default ordering of bug reports in the list.

    """
    model = Bug
    template_name = "bug_hub/bug_list.html"
    context_object_name = "bugs"
    paginate_by = PAGINATE_BY
    ordering = ["-report_date"]

    def get_queryset(self):
        """
        Returns a queryset object containing the filtered results
        based on the filter parameters provided in the request.GET.        
        """
        queryset = super().get_queryset()
        status_filter = self.request.GET.get('status', 'all')  
        type_filter = self.request.GET.get('type', 'all')      
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(title__icontains=query)
        elif status_filter != 'all':
            queryset = queryset.filter(status=status_filter)
        elif type_filter != 'all':
            queryset = queryset.filter(bug_type=type_filter)

        self.status_filter = status_filter
        self.type_filter = type_filter

        return queryset

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :param kwargs: The keyword arguments passed to the function.
        :return: The context data with additional filters.
        """
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.status_filter
        context['type_filter'] = self.type_filter
        return context

class BugDetailView(DetailView):
    """
    A view for displaying the details of a single bug report.

    :param Bug model: The model representing bug reports.
    :param str template_name: The path to the HTML template for rendering the bug details.
    :param str context_object_name: The name to use for the bug report in the template context.

    """
    model = Bug
    template_name = "bug_hub/bug_detail.html"
    context_object_name = "bug"

class BugCreateView(CreateView):
    """
    A view for creating a new bug report.

    This view allows users to create and submit new bug reports.

    :param Bug model: The model representing bug reports.
    :param BugCreationForm form_class: The form class for creating bug reports.
    :param str template_name: The path to the HTML template for rendering the bug creation form.
    :param str success_url: The URL to redirect to after successfully creating a bug report.
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
