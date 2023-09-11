from django.contrib import admin
from portfolio.models import CategoriaProjeto, Projeto

@admin.register(CategoriaProjeto)
class CategoriaProjetoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',
    list_display_links = 'nome',
    list_per_page = 10
    prepopulated_fields = {
        'slug': ('nome',),
    }
    ordering = 'nome',


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nome',
        'categoria', 'conteudo_capa',
        'visivel', 'status',
    ]
    list_display_links = 'nome',
    list_editable = 'visivel', 'conteudo_capa', 'status',
    list_filter = 'categoria', 'visivel',
    list_per_page = 10
    prepopulated_fields = {
        'slug': ('nome',),
    }
    ordering = '-id',