"""
Module: views.py
================

This module contains views for handling the common pages in the overall Glitch Guru Django project.

"""

from django.views.generic import TemplateView
from django.http import Http404

class HomePageView(TemplateView):
    """
    This class defines the view for the homepage of the web application.
    """
    template_name = "home.html"

class Custom404View(TemplateView):
    """
    This class defines the customized view for the custom 404 error page for the '/404/' URL.
    """
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        """
            Prepares context data for the view. Typically overridden to customize
            the data passed to the template for rendering.

            :param kwargs: Additional keyword arguments.
            :type kwargs: dict
            :return: Dictionary with context data.

            In this implementation, an 'exception' key is added to the context, representing an instance of Django's
            `Http404` exception with a "Page not found" message.
            :rtype: dict        
        """
        context = super().get_context_data(**kwargs)
        context['exception'] = Http404("Page not found. The requested page does not exist.")
        return context
