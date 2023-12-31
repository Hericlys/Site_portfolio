from django.contrib import admin
from blog.models import Tag, Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe
from django.urls import reverse


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'slug',
    list_display_links = 'nome',
    search_fields = 'id', 'nome', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('nome',),
    }


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'content', 
    list_display = 'id', 'title', 'is_published', 'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title',
    list_per_page = 50
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'update_at', 'update_by', 'created_by',
    prepopulated_fields = {
        'slug': ('title',),
    }
    autocomplete_fields = 'tags', 'category',

    def save_model(self, request, obj, form, change):
        if change:
            obj.update_by = request.user
        else:
            obj.created_by = request.user
        obj.save()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = 'id', 'user',
    list_display_links = 'user',
    ordering = 'user', '-id'
    readonly_fields = 'created_at', 'update_at', 'update_by', 'created_by',

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            
        obj.save()

