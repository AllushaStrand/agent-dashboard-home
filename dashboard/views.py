from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    preference = getattr(request.user, "userpreference", None)

    if not preference or not preference.answer_style or not preference.detail_level or not preference.primary_goal:
        return redirect("onboarding")

    return render(request, "dashboard/home.html")