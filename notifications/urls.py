# notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send_request/<int:recipient_id>/', views.send_request, name='send_request'),
    path('respond_request/<int:request_id>/<str:response>/', views.respond_request, name='respond_request'),
    path('notifications/', views.notifications, name='notifications'),
]
