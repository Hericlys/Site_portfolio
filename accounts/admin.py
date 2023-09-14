from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'first_name',
        'last_name', 'email', 'telefone','is_active'
    ]

    list_display_links = 'username',
    list_editable = 'is_active',
    list_per_page = 10
    list_filter = 'username', 'first_name', 'last_name', 'email'

