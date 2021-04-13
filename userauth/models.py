from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import (AbstractUser)

LENGTH_MEDIUM = 100
LENGTH_LONG = 255


class UnilinkerUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address', max_length=LENGTH_LONG, unique=True
    )
    name = models.CharField(max_length=LENGTH_LONG)
    about_me = models.TextField(
        default='I am a mystery'
    )
    profile_pic = models.ImageField(
        upload_to='user_profile_pic', default='default_image.png', blank=True, null=True
    )
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'

# Create your models here.
