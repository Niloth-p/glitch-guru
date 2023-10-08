from datetime import timezone
from django import forms
from .models import Bug
from .choices import BUG_TYPE_CHOICES, STATUS_CHOICES
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BugCreationForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ["title", "description", "bug_type", "status"]

    title = forms.CharField(
        max_length=250,
        required=True,
        label=_("Bug Title"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text=_("Enter a concise title for the bug report."),
    )

    description = forms.CharField(
        label=_("Description"),
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        help_text=_("Enter a detailed description of the bug."),
    )

    bug_type = forms.ChoiceField(
        label=_("Bug Type"),
        choices=BUG_TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.ChoiceField(
        label=_("Status"),
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    def clean_title(self):
        title = self.cleaned_data["title"]
        # pylint: disable=E1101
        if Bug.objects.filter(title=title).exists():
            # pylint: enable=E1101
            raise ValidationError("A bug report with this title already exists.")
        return title
