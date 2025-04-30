from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('setup/', views.setup_profile, name='setup_profile'),
]