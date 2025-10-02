from rest_framework.decorators import api_view
from rest_framework import status
from .models import Expense
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer
from rest_framework.response import Response
from .models import Income
from .serializers import IncomeSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def expense_list(request):
    if request.method == 'GET':
        expenses = Expense.objects.filter(user=request.user)  # show only user's expenses
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['user'] = request.user.id  # assign logged in user automatically
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def expense_detail(request, pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Income
from .serializers import IncomeSerializer

class IncomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        income, _ = Income.objects.get_or_create(user=request.user)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    def post(self, request):
        income, _ = Income.objects.get_or_create(user=request.user)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)