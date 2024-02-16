from django.db import models
from django.contrib.auth.models import User

class SocialAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)  # e.g., 'twitter', 'facebook'
    uid = models.CharField(max_length=255)  # Unique identifier provided by the social platform
    extra_data = models.JSONField(default=dict)  # Store additional data provided by the platform

    def __str__(self):
        return f"{self.user.username}'s {self.provider} account"


# Create your models here.
