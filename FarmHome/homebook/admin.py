from django.contrib import admin

# Register your models here.
from .models import Employee, CashBreakdown

admin.site.register(Employee)
admin.site.register(CashBreakdown)

