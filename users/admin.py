from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet_id', 'phone_number', 'hashed_user_id')
    list_filter = ('user__is_active',)
    search_fields = ('user__username', 'user__email', 'wallet_id')

# Register your models here.
