from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    test = models.CharField(max_length=200, default="working")

    def __str__(self):
        return f"Profile({self.user})"


class Link(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(blank=False, default=None)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Link({self.title}:{self.url})"
