from django.contrib import admin
from site_setup.models import SiteSetup


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'name',

    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
