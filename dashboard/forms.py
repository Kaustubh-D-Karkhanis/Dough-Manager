from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = ['initial_income', 'monthly_budget', 'income_source']