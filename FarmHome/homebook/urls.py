from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('', Home, name='home'),
    path('employee/', views.Employee, name='homebook-employee'),
    path('employee_update/', views.EmployeeUpdate, name='homebook-employee_update'),
    path('employee_create/', views.EmployeeCreate, name='homebook-employee_create'),
    path('add_employee_update', views.UpdateEmployee, name='add_employee'),
    path('cashBreakdown_table/', views.CashBreakdownTable, name='homebook-cashBreakdown'),
    path('cashBreakdowntotal/', views.CashBreakdownTotal, name='homebook-cashBreakdowntotal'),
    path('cashBreakdown_update/', views.CashBreakdownUpdate, name='homebook-cashBreakdown_update'),
    path('cashBreakdown_create/', views.CashBreakdownCreate, name='homebook-cashBreakdown_create'),
    path('cashBreakdown_calc/', views.CashBreakdownCalc, name='homebook-cashBreakdown_calc'),
    path('cashBreakdown_results/', views.Results, name='homebook-cashBreakdown_results'),
    path('dashboard/', views.Dashboard, name='homebook-dashboard'),
    path('c_update/<int:pk>/', views.C_update, name='cashBreakdown-update'),
    path('c_delete/<int:pk>/', views.C_delete, name='cashBreakdown-delete'),
    path('e_update/<int:pk>/', views.E_update, name='employee-update'),
    path('e_delete/<int:pk>/', views.E_delete, name='employee-delete'),
]
