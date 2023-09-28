from django.contrib.auth.models import AbstractUser
from django.db import models
from secrets import token_urlsafe


class User(AbstractUser):
    telefone = models.CharField(max_length=15, null=True, blank=True)
    validated_email = models.BooleanField(default=False)
    authentication_token = models.SlugField(
        default=str(token_urlsafe()).replace(' ', '-'),
    )
