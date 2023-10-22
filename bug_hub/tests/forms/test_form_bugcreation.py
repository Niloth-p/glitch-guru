from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from bug_hub.forms import BugCreationForm
from bug_hub.models import Bug

class BugCreationFormTestCase(TestCase):
    """
    Test case for the BugCreationForm.
    """
    def setUp(self):
        """
        Create the details of a sample bug instance
        """
        self.data = {
            "title": "Test Bug Title",
            "description": "This is a test bug description.",
            "bug_type": "feature",
            "status": "under_review",
        }

    def test_valid_form_data(self):
        """
        Test the form's validation with valid data.
        """
        form = BugCreationForm(data=self.data)
        self.assertTrue(form.is_valid(), f"Form is invalid. Errors: {form.errors}")

    def test_valid_form_redirection(self):
        """
        Test the redirection after a successful form submission.
        """
        response = self.client.post(
            reverse("bug_hub:bug_create"), data=self.data, follow=True
        )
        self.assertRedirects(response, reverse("bug_hub:bug_list"))

    def test_blank_data(self):
        """
        Test the form's behavior with blank data.
        """
        form = BugCreationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], ["This field is required."])

    def test_clean_title_duplicate(self):
        """
        Test the clean_title() method of the BugCreationForm class when a duplicate title is provided.
        """
        Bug.objects.create(title="Duplicate Title")
        form = BugCreationForm()
        form.cleaned_data = {"title": "Duplicate Title"}
        with self.assertRaises(ValidationError):
            form.clean_title()