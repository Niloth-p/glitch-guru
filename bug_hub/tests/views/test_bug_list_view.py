"""
This module contains unit tests for validating the view when 
viewing the list of all bug reports in the Bug Hub application.
"""

from django.test import TestCase
from django.urls import reverse
from bug_hub.models import Bug
from config.constants import PAGINATE_BY


class BugListViewTestCase(TestCase):
    """
    Test case for the BugListView class.

    Attributes:
        url (str): The URL for the bug list view.
    """

    def setUp(self):
        """
        Set up the test environment by initializing the URL.
        """
        self.url = reverse("bug_hub:bug_list")

    def test_bug_list_view(self):
        """
        Test the bug list view's GET response and template usage.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_hub/bug_list.html")

    def test_bug_list_pagination(self):
        """
        Test pagination in the bug list view.
        """
        for i in range(25):
            # pylint: disable=E1101
            Bug.objects.create(
                title=f"Bug {i}",
                bug_type="feature",
                status="under_review",
            )
            # pylint: enable=E1101

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["bugs"]), PAGINATE_BY)
