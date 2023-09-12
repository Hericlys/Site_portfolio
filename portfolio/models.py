from django.db import models
from utils.rands import slugify_new
from utils.images import resize_image


class CategoriaProjeto(models.Model):
    class Meta:
        verbose_name = 'Categoria de projeto'
        verbose_name_plural = 'Categorias de projeto'

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


class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )
    categoria = models.ForeignKey(
        CategoriaProjeto,
        on_delete=models.SET_NULL,
        null=True,
    )
    capa = models.ImageField(upload_to='projetos/%Y/%m/')
    descricao = models.CharField(max_length=255)
    conteudo_capa = models.BooleanField(
        default=True,
        help_text='Este campo precisará estar marcado para exibir a capa nos detalhes do projeto'
    )
    conteudo = models.TextField()
    visivel = models.BooleanField(
        default=True,
        help_text='Este campo precisará estar marcado para o projeto ser exibida publicamente'
    )
    STATUS_CHOICES = [
        ("Em produção", "Em produção"),
        ("Finalizado", "Finalizado"),
        ("descontinuado", "descontinuado"),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    repositorio_link = models.URLField(default='https://github.com/Hericlys/')
    projeto_aplicado = models.BooleanField(
        default=False,
        help_text="Este campo deve ser marcado apenas se hover uma aplicação a esse projeto."
    )
    link_aplicacao = models.URLField(
        blank=True, null=True,
        help_text="Preencha esse campo apenas se hover uma aplicação para esse projeto."
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)

        current_capa_name = str(self.capa.name)
        super().save(*args, **kwargs)
        capa_changed = False

        if self.capa:
            capa_changed = current_capa_name != self.capa.name

        if capa_changed:
            resize_image(self.capa, 900)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
