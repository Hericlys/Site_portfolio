from django.contrib import admin
from portfolio.models import CategoriaProjeto, Projeto
from django_summernote.admin import SummernoteModelAdmin


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
class ProjetoAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo', )
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