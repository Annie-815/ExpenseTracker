from django.urls import path
from . import views
from .views import IncomeView

urlpatterns = [    
   path('list/', views.expense_list, name='expense-list'),
   path('list/<int:pk>/', views.expense_detail, name='expense-detail'),
   path("income/", IncomeView.as_view(), name="income"),

]