from django.urls import path
from . import views

urlpatterns = [
    path("applications/", views.application_list, name="application_list"),
    path("applications/new/", views.application_create, name="application_create"),
]