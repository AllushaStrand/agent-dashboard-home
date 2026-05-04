from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import OnboardingForm
from .models import UserPreference


@login_required
def onboarding(request):
    preference, created = UserPreference.objects.get_or_create(user=request.user)

    if preference.answer_style and preference.detail_level and preference.primary_goal:
        return redirect("dashboard_home")

    if request.method == "POST":
        form = OnboardingForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            return redirect("dashboard_home")
    else:
        form = OnboardingForm(instance=preference)

    return render(request, "accounts/onboarding.html", {"form": form})


@login_required
def profile(request):
    preference, created = UserPreference.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = OnboardingForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = OnboardingForm(instance=preference)

    return render(request, "accounts/profile.html", {"form": form})