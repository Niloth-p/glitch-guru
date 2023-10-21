from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Bug
from .choices import BUG_TYPE_CHOICES, STATUS_CHOICES

class BugCreationForm(forms.ModelForm):
    """
    A form for creating bug reports.

    This form is used for creating bug reports in the Glitch Guru Django project.

    Attributes:
        title (CharField): Name of the bug report.
        description (CharField): A detailed description of the bug.
        bug_type (ChoiceField): The type of bug, such as error, feature request, enhancement, documentation.
        status (ChoiceField): The current status of the bug report (e.g., To Do, In Progress, Done, Under Review, Won't Fix).

    Methods:
        clean_title(): Custom validation for ensuring that a bug report with the same title does not already exist.
    """
    class Meta:
        model = Bug
        fields = ["title", "description", "bug_type", "status"]

    title = forms.CharField(
        max_length=250,
        required=True,
        label=_(message="Bug Title"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text=_(message="Enter a concise title for the bug report."),
    )

    description = forms.CharField(
        label=_(message="Description"),
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        help_text=_(message="Enter a detailed description of the bug."),
    )

    bug_type = forms.ChoiceField(
        label=_(message="Bug Type"),
        choices=BUG_TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.ChoiceField(
        label=_(message="Status"),
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    def clean_title(self):
        """
        Custom validation to check for duplicate bug titles.

        Returns:
            str: The validated title if it's unique.

        Raises:
            ValidationError: If a bug report with the same title already exists.
        """
        title = self.cleaned_data["title"]
        # pylint: disable=E1101
        if Bug.objects.filter(title=title).exists():
            # pylint: enable=E1101
            raise ValidationError(message="A bug report with this title already exists.")
        return title
