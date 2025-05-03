from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('setup/', views.setup_profile, name='setup_profile'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_investment/', views.add_investment, name='add_investment')
]
