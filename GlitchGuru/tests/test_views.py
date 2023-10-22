from django.test import TestCase
from GlitchGuru.views import Custom404View
from django.http import Http404

class GlitchGuruViewsTestCase(TestCase):
    """
    Test case for the Glitch Guru Views.
    
    Views:
        Custom404View class

    Methods:
        test_get_context_data_404(): Test the get_context_data() method of the Custom404View class.
    """
    def test_get_context_data_404(self):
        """
    	Tests the 'get_context_data' method of the 'Custom404View' class when a 404 error occurs.
        """
        view = Custom404View()
        context = view.get_context_data()
        self.assertTrue('exception' in context)
        self.assertIsInstance(context['exception'], Http404)
    