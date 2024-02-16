from django.db import models
from django.conf import settings

class PaymentMethod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payment_methods')
    method_type = models.CharField(max_length=255)  # For example, 'PayPal', 'Credit Card', etc.
    details = models.JSONField()  # This field can store various details about the payment method securely
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method_type} for {self.user.username}"

