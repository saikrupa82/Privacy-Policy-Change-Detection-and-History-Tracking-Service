from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)

class PolicyTracker(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the AUTH_USER_MODEL setting
        on_delete=models.CASCADE,
        related_name='tracked_policies'
    )
    policy_name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    last_checked = models.DateTimeField(auto_now=True)
    last_changed = models.DateTimeField(null=True, blank=True)
    latest_content = models.TextField()
    content_dict = models.JSONField()

    class Meta:
        unique_together = ('user', 'policy_name',)  # Ensures that the combination of user and policy_name is unique

    def __str__(self):
        return f"{self.policy_name} ({self.user.username})"
