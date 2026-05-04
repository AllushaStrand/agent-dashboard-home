from django.contrib.auth.models import User
from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("found", "Found"),
        ("applied", "Applied"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
        ("withdrawn", "Withdrawn"),
    ]

    DECISION_CHOICES = [
        ("apply", "Apply"),
        ("maybe", "Maybe"),
        ("skip", "Skip"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    role_title = models.CharField(max_length=255)
    job_url = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="found")
    decision = models.CharField(max_length=30, choices=DECISION_CHOICES, blank=True)
    score = models.IntegerField(null=True, blank=True)
    applied_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.role_title} at {self.company}"