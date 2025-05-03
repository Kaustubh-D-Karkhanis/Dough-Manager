from django import forms
from .models import UserProfile, Transaction

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = ['initial_income', 'monthly_budget', 'income_source']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields = ['amount', 'expense_category','description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'expense_category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }