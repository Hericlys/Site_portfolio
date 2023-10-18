from django.db import models
from utils.model_validators import validate_png
from utils.images import resize_image
from accounts.models import User


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    name = models.CharField(max_length=65)
    
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    favicon = models.ImageField(
        upload_to = 'media/favicon/%Y/%m',
        blank = True,
        default='',
        validators=[validate_png, ]
    )

    logo = models.ImageField(
        upload_to='media/logo/%Y/%m',
        blank=True,
        default='',
        validators=[validate_png, ]
    )

    def save(self, *args, **kwargs):
        current_faveicon_name = str(self.favicon.name)
        current_logo_name = str(self.logo.name)

        super().save(*args, **kwargs)
        favicon_changed = False
        logo_changed = False

        if self.favicon:
            favicon_changed = current_faveicon_name != self.favicon.name

        if self.logo:
            logo_changed = current_logo_name != self.logo.name

        if favicon_changed:
            resize_image(self.favicon, 32)

        if logo_changed:
            resize_image(self.logo, 150)

    def __str__(self):
        return self.name
    