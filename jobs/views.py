from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import JobApplicationForm
from .models import JobApplication


@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "jobs/application_list.html", {
        "applications": applications
    })


@login_required
def application_create(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect("application_list")
    else:
        form = JobApplicationForm()

    return render(request, "jobs/application_form.html", {
        "form": form
    })