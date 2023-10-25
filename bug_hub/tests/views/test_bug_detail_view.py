"""
This module contains unit tests for validating the view when 
viewing the details of a bug report in the Bug Hub application.
"""
from django.test import TestCase
from django.urls import reverse
from bug_hub.models import Bug


class BugDetailViewTestCase(TestCase):
    """
    Test case for the BugDetailView class.

    :param Bug bug: A Bug object created for testing.
    :param str url: The URL for the bug detail view.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test Bug object and initializing the URL.
        """
        # pylint: disable=E1101
        self.bug = Bug.objects.create(
            title="Test Bug",
            bug_type="enhancement",
            status="wont_fix",
        )
        # pylint: enable=E1101
        self.url = reverse("bug_hub:bug_detail", args=[self.bug.pk])

    def test_bug_detail_view(self):
        """
        Test the bug detail view's response, template usage, and context data.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_hub/bug_detail.html")
        self.assertEqual(response.context["bug"], self.bug)
