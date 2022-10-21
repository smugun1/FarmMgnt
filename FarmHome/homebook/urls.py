from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('add_employee_update', views.AddEmployee, name='add_employee'),
    path('employee/', views.Employee, name='homebook-employee'),
    path('cashBreakdown_table/', views.CashBreakdownTable, name='homebook-cashBreakdown'),
    path('cashBreakdown_update/', views.CashBreakdownUpdate, name='homebook-cashBreakdown_update'),
    path('cashBreakdown_create/', views.CashBreakdownCreate, name='homebook-cashBreakdown_create'),
    path('dashboard/', views.Dashboard, name='homebook-dashboard'),
    path('c_update/<int:pk>/', views.C_update, name='cashBreakdown-update'),
    path('c_delete/<int:pk>/', views.C_delete, name='cashBreakdown-delete'),
]
