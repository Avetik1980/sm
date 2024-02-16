from django.contrib import admin
from .models import SocialAccount

@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'uid')  # Corrected field names
    list_filter = ('provider',)  # Corrected field name
    search_fields = ('user__username', 'provider', 'uid')
