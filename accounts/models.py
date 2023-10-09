from django.contrib.auth.models import AbstractUser
from django.db import models
from secrets import token_urlsafe
from utils.images import resize_image

class User(AbstractUser):
    telefone = models.CharField(max_length=15, null=True, blank=True)
    validated_email = models.BooleanField(default=False)
    authentication_token = models.SlugField(
        default=str(token_urlsafe()).replace(' ', '-'),
    )
    image_profile = models.ImageField(
        upload_to='profile/user/%Y/%m',
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):

        current_profile_name = str(self.image_profile.name)
        super().save(*args, **kwargs)
        profile_changed = False

        if self.image_profile:
            profile_changed = current_profile_name != self.image_profile.name

        if profile_changed:
            resize_image(self.image_profile, 900)

        return super().save(*args, **kwargs)
