from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from bug_hub.choices import BUG_TYPE_CHOICES, STATUS_CHOICES
from bug_hub.model_validators import validate_description_not_empty, validate_bug_type, validate_report_date_not_future, validate_status

class ValidatorsTestCase(TestCase):
    def test_validate_description_not_empty(self):
        """
        Test the validation of bug report descriptinos by passing both empty and non-empty descriptions

        Checks if:
            the function raises a ValidationError when provided with an empty description
            the function does not raise a ValidationError when provided with a non-empty description
        """
        # Test with an empty description
        with self.assertRaises(ValidationError) as context:
            validate_description_not_empty("")
        self.assertEqual(context.exception.message, "Description cannot be empty.")

        # Test with a non-empty description
        try:
            validate_description_not_empty("Non-empty description")
        except ValidationError as e:
            self.fail(f"validate_description_not_empty() raised ValidationError unexpectedly: {e}")

    def test_validate_bug_type(self):
        """
        Test the validation of a bug type by passing both valid and invalid bug types        
        
        Checks if:
            a ValidationError is raised when an invalid bug type is provided. 
            the exception message matches the expected value.
        
        Raises:
            AssertionError: If the validation fails unexpectedly.
            ValidationError: If an invalid bug type is provided.
        """
        # Test with an invalid bug type
        with self.assertRaises(ValidationError) as context:
            validate_bug_type("Invalid Type")
        self.assertEqual(context.exception.message, "Invalid bug type.")

        # Test with a valid bug type
        try:
            validate_bug_type(BUG_TYPE_CHOICES[0][0])
        except ValidationError as e:
            self.fail(f"validate_bug_type() raised ValidationError unexpectedly: {e}")

    def test_validate_report_date_not_future(self):
        """
        Test the validation of bug report dates by passing both past and future dates

        Checks if:
            the function raises a ValidationError when provided with a future date
            the function does not raise a ValidationError when provided with a past date

        Raises:
            AssertionError: If the validation fails unexpectedly.
            ValidationError: If an invalid date is provided.
        """
        # Test with a future date
        future_date = timezone.now() + timezone.timedelta(days=1)
        with self.assertRaises(ValidationError) as context:
            validate_report_date_not_future(future_date)
        self.assertEqual(context.exception.message, "Report date cannot be in the future.")

        # Test with a past date
        past_date = timezone.now() - timezone.timedelta(days=1)
        try:
            validate_report_date_not_future(past_date)
        except ValidationError as e:
            self.fail(f"validate_report_date_not_future() raised ValidationError unexpectedly: {e}")

    def test_validate_status(self):
        """
        Test the validation of bug status by passing both valid and invalid statuses

        Checks if:
            the function raises a ValidationError when provided with an invalid status
            the function does not raise a ValidationError when provided with a valid status

        Raises:
            AssertionError: If the validation fails unexpectedly.
            ValidationError: If an invalid bug status is provided.
        """
        # Test with an invalid status
        with self.assertRaises(ValidationError) as context:
            validate_status("Invalid Status")
        self.assertEqual(context.exception.message, "Invalid status.")

        # Test with a valid status
        try:
            validate_status(STATUS_CHOICES[0][0])
        except ValidationError as e:
            self.fail(f"validate_status() raised ValidationError unexpectedly: {e}")
