from django.contrib import admin
from .models import PaymentMethod

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('user', 'method_type', 'details', 'is_active', 'created_at')  # Corrected 'payment_type' to 'method_type'
    list_filter = ('is_active', 'method_type')  # Corrected 'payment_type' to 'method_type'
    search_fields = ('user__username', 'method_type')  # Added 'method_type' for consistency
