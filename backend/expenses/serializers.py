from rest_framework import serializers
from .models import Expense
from .models import Income

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ["amount"]