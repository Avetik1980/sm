from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'message', 'created_at', 'is_read')  # Corrected 'timestamp' to 'created_at'
    list_filter = ('is_read',)
    search_fields = ('user__username', 'message')
