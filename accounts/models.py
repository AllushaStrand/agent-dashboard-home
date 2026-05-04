from django.contrib.auth.models import User
from django.db import models


class UserPreference(models.Model):
    ANSWER_STYLE_CHOICES = [
        ("strict", "Strict and direct"),
        ("balanced", "Slightly supportive but honest"),
        ("supportive", "Supportive"),
    ]

    DETAIL_LEVEL_CHOICES = [
        ("short", "Short and concise"),
        ("medium", "Medium detail"),
        ("detailed", "Detailed and step-by-step"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answer_style = models.CharField(max_length=20, choices=ANSWER_STYLE_CHOICES)
    detail_level = models.CharField(max_length=20, choices=DETAIL_LEVEL_CHOICES)
    primary_goal = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"