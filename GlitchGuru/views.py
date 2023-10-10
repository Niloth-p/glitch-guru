from django.views.generic import TemplateView
from django.http import Http404


class HomePageView(TemplateView):
    template_name = "home.html"

class Custom404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exception'] = Http404("Page not found. The requested page does not exist.")
        return context
    