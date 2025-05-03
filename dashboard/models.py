from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    INCOME_SOURCES = [
        ('SALARY', 'Salary'),
        ('FREELANCE', 'Freelance'),
        ('BUSINESS INCOME', 'Business Income'),
        ('INVESTMENTS', 'Investments'),
        ('MULTIPLE', 'Multiple'),
        ('OTHER', 'Other'),
    ]
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    initial_income = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    income_source = models.CharField(max_length=20, choices=INCOME_SOURCES)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Transaction(models.Model):
    transaction_types = [
        ('expenses', 'Expense'),
        ('investments', 'Investment'),
        ('income', 'Income Top-up'),
    ]
    expense_types = [
        ('Food','Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Utilities', 'Utilities'),
        ('Health', 'Health'),
        ('Other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    transaction_type = models.CharField(max_length=20, choices=transaction_types)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, max_length=30)
    expense_category = models.CharField(max_length=20, choices=expense_types, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"


