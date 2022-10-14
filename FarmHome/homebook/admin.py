from django.contrib import admin

# Register your models here.
from .models import Muster, CashBreakdown

admin.site.register(Muster)
admin.site.register(CashBreakdown)
