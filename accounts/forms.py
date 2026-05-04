from django import forms
from .models import UserPreference


class OnboardingForm(forms.ModelForm):
    answer_style = forms.ChoiceField(
        choices=UserPreference.ANSWER_STYLE_CHOICES,
        widget=forms.RadioSelect
    )

    detail_level = forms.ChoiceField(
        choices=UserPreference.DETAIL_LEVEL_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = UserPreference
        fields = ["answer_style", "detail_level", "primary_goal"]
        widgets = {
            "primary_goal": forms.TextInput(attrs={
                "placeholder": "Example: Get a Product Manager job fast"
            }),
        }