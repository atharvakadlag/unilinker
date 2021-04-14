from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import (AbstractUser)
from django.core.validators import URLValidator, validate_slug

LENGTH_MEDIUM = 100
LENGTH_LONG = 255


def default_links():
    return {}


def link_json_validator(value):
    title_validator = validate_slug()
    url_validator = URLValidator(schemes=['http', 'https'])
    value = json.loads(value)
    for title, url in a.items():
        title_validator(title)
        url_validator(url)


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
    links = models.JSONField('Links', default=default_links, validators=[
                             link_json_validator])

    USERNAME_FIELD = 'username'
