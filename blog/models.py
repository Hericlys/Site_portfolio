from django.db import models


class Categoria(models.Model):
    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")

    nome = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

