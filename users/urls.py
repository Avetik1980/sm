from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', profile, name='profile'),
]
