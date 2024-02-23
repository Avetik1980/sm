from django.urls import path
from . import views
from .views import profile, search

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', profile, name='profile'),
    path('search/', search, name='search'),

]
