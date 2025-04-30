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


