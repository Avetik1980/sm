from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'amount', 'timestamp')  # Removed 'status', 'transaction_date', replaced with 'timestamp'
    search_fields = ('sender__username', 'receiver__username')
