from django.test import TestCase
from django.urls import reverse
from bug_hub.models import Bug


class BugCreateViewTestCase(TestCase):
    """
    Test case for the BugCreateView class, which handles the creation of bug reports.
    """

    def setUp(self):
        self.url = reverse("bug_hub:bug_create")
        self.data = {
            "title": "Test Bug Title",
            "description": "This is a test bug description.",
            "bug_type": "feature",
            "status": "under_review",
        }

    def test_get_request(self):
        """Test GET request: 200 status, 'bug_create.html' template used."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_hub/bug_create.html")

    def test_post_request_without_form(self):
        """Test POST request: Redirects to 'bug_list', confirms Bug object creation."""
        response = self.client.post(
            reverse("bug_hub:bug_create"),
            data=self.data,
            follow=True,
        )
        self.assertRedirects(
            response,
            reverse("bug_hub:bug_list"),
        )
        self.assertTrue(Bug.objects.filter(title="Test Bug Title").exists())
