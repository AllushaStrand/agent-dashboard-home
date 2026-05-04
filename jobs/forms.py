from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "company",
            "role_title",
            "job_url",
            "location",
            "status",
            "decision",
            "score",
            "applied_date",
            "notes",
        ]
        widgets = {
            "applied_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 4}),
        }