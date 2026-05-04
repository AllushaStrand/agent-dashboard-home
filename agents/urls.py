from django.urls import path
from . import views

urlpatterns = [
    path("job-agent/", views.job_agent, name="job_agent"),
]