from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
class Income(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="income")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"