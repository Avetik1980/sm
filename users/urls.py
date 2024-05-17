from django.urls import path
from . import views
from .views import profile, search

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('recipients/', views.recipient_list, name='recipient_list'),
    path('donators/', views.donator_list, name='donator_list'),
]
