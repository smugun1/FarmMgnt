from django.db.models import Sum, F
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from decimal import Decimal
from . import models
from .forms import TaskForm, UpdateCashBreakdownForm, UpdateEmployeeForm
from .models import *


# Create your views here.
def Home(request):
    context = {
        "name": {"Home Farm Page"},

    }
    return render(request, 'homebook/home.html', context)


def Dashboard(request):
    context = {
        "name": {"Dashboard"},

    }
    return render(request, 'homebook/dashboard.html', context)


def Employee(request):
    note = Employee
    national_id = models.IntegerField()
    first_name = models.CharField()
    Other_names = models.CharField()
    last_name = models.CharField()
    pay_amt = models.DecimalField()
    company = models.CharField()
    timestamp_last_updated = models.DateTimeField()
    timestamp_added = models.DateTimeField()
    employee_email = models.EmailField()
    employee_phone = models.CharField()

    context = {
        "employee": note,
        "national_id": national_id,
        "first_name": first_name,
        "Other_names": Other_names,
        "last_name": last_name,
        "pay_amt": pay_amt,
        "company": company,
        "timestamp_last_updated": timestamp_last_updated,
        "timestamp_added": timestamp_added,
        "employee_email": employee_email,
        "employee_phone": employee_phone,

    }
    return render(request, 'homebook/employee_register.html', context)


def EmployeeUpdate(request):
    national_id = models.IntegerField()
    first_name = models.CharField()
    Other_names = models.CharField()
    last_name = models.CharField()
    pay_amt = models.DecimalField()
    company = models.CharField()
    timestamp_last_updated = models.DateTimeField()
    timestamp_added = models.DateTimeField()
    employee_email = models.EmailField()
    employee_phone = models.CharField()
    context = {

        "national_id": national_id,
        "first_name": first_name,
        "Other_names": Other_names,
        "last_name": last_name,
        "pay_amt": pay_amt,
        "company": company,
        "timestamp_last_updated": timestamp_last_updated,
        "timestamp_added": timestamp_added,
        "employee_email": employee_email,
        "employee_phone": employee_phone,

    }
    return render(request, 'homebook/employeeupdate.html', context)


def EmployeeCreate(request):
    if request.method == "POST":
        national_id = request.POST['national_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pay_amt = request.POST.get('pay_amt')
        company = request.POST.get('company')
        timestamp_last_updated = request.POST['timestamp_last_updated']
        timestamp_added = request.POST['timestamp_added']
        employee_email = request.POST['employee_email']
        employee_phone = request.POST['employee_phone']

        insert = Employee(national_id=national_id, first_name=first_name,
                          last_name=last_name, pay_amt=pay_amt, company=company,
                          timestamp_last_updated=timestamp_last_updated,
                          timestamp_added=timestamp_added, employee_email=employee_email,
                          employee_phone=employee_phone)
        insert.save()
    return redirect('/employee')


@never_cache
def CashBreakdownTable(request):
    # calculate the change from each denomination
    note = CashBreakdown.objects.all()
    cashBreakdown_date = models.DateTimeField()
    amount = CashBreakdown.objects.filter()
    One_thousands = F(amount) % F(1000)
    Five_hundreds = F(amount) % F(1000) / F(500)
    Two_hundreds = F(amount) % F(1000) % F(500) / F(200)
    One_hundreds = F(amount) % F(1000) % F(500) % F(200) / F(100)
    Fifties = F(amount) % F(1000) % F(500) % F(200) % F(100) / F(50)
    Forties = F(amount) % F(1000) % F(500) % F(200) % F(100) % F(50) / F(40)
    Twenties = F(amount) % F(1000) % F(500) % F(200) % F(100) % F(50) % F(40) / F(20)
    Tens = F(amount) % F(1000) % F(500) % F(200) % F(100) % F(50) % F(40) % F(20) / F(10)
    Fives = F(amount) % F(1000) % F(500) % F(200) % F(100) % F(50) % F(40) % F(20) % F(10) / F(5)
    Ones = F(amount) % F(1000) % F(500) % F(200) % F(100) % F(50) % F(40) % F(20) % F(10) % F(5) / F(1)

    context = {
        "cashBreakdown": note,
        "cashBreakdown_date": cashBreakdown_date,
        "amount": amount,
        "One_thousands": One_thousands,
        "Five_hundreds": Five_hundreds,
        "Two_hundreds": Two_hundreds,
        "One_hundreds": One_hundreds,
        "Fifties": Fifties,
        "Forties": Forties,
        "Twenties": Twenties,
        "Tens": Tens,
        "Fives": Fives,
        "Ones": Ones,

    }
    return render(request, 'homebook/cashBreakdown_table.html', context)


@never_cache
def CashBreakdownUpdate(request):
    amount = models.DecimalField()
    One_thousands = models.IntegerField()
    Five_hundreds = models.IntegerField()
    Two_hundreds = models.IntegerField()
    One_hundreds = models.IntegerField()
    Fifties = models.IntegerField()
    Forties = models.IntegerField()
    Twenties = models.IntegerField()
    Tens = models.IntegerField()
    Fives = models.IntegerField()
    Ones = models.IntegerField()

    context = {
        "note": CashBreakdown,
        "amount": amount,
        "One_th": One_thousands,
        "Five_hu": Five_hundreds,
        "Two_hu": Two_hundreds,
        "One_hu": One_hundreds,
        "Fifties_sh": Fifties,
        "Forties_sh": Forties,
        "Twenties_sh": Twenties,
        "Tens_sh": Tens,
        "Fives_sh": Fives,
        "Ones_sh": Ones,

    }

    return render(request, 'homebook/cashBreakdown_update.html', context)


@never_cache
def CashBreakdownCreate(request):
    if request.method == "POST":
        cashBreakdown_date = request.POST['cashBreakdown_date']
        amount = request.POST['amount']
        One_thousands = request.POST['One_thousands']
        Five_hundreds = request.POST['Five_hundreds']
        Two_hundreds = request.POST['Two_hundreds']
        One_hundreds = request.POST['One_hundreds']
        Fifties = request.POST['Fifties']
        Forties = request.POST['Forties']
        Twenties = request.POST['Twenties']
        Tens = request.POST['Tens']
        Fives = request.POST['Fives']
        Ones = request.POST['Ones']

        insert = CashBreakdown(cashBreakdown_date=cashBreakdown_date, amount=amount, One_thousands=One_thousands,
                               Five_hundreds=Five_hundreds, Two_hundreds=Two_hundreds, One_hundreds=One_hundreds,
                               Fifties=Fifties, Forties=Forties, Twenties=Twenties, Tens=Tens, Fives=Fives, Ones=Ones)
        insert.save()
    return redirect('/cashBreakdown_table')


# update the column totals

def CashBreakdownTotal(request):
    total = CashBreakdown.objects.filter('cashBreakdown_date').aggregate(total_amt=Sum('amount'),
                                                                         total_one=Sum('One_thousands'),
                                                                         total_five=Sum('Five_hundreds'),
                                                                         total_two=Sum('Two_hundreds'),
                                                                         total_on=Sum('One_hundreds'),
                                                                         total_fifty=Sum('Fifty'),
                                                                         total_forty=Sum('Forty'),
                                                                         total_twenty=Sum('Twenty'),
                                                                         total_ten=Sum('Ten'),
                                                                         total_ne=Sum('One'))
    amount_sum = total['amount__sum'] or 0
    if total.get('total_amt') is None:
        total['total_amt'] = 0
    else:
        CashBreakdown.objects.filter('cashBreakdown_date').aggregate(total_amt=Sum('amount'),
                                                                     total_one=Sum('One_thousands'),
                                                                     total_five=Sum('Five_hundreds'),
                                                                     total_two=Sum('Two_hundreds'),
                                                                     total_on=Sum('One_hundreds'),
                                                                     total_fifty=Sum('Fifty'),
                                                                     total_forty=Sum('Forty'),
                                                                     total_twenty=Sum('Twenty'),
                                                                     total_ten=Sum('Ten'),
                                                                     total_ne=Sum('One'))
    amount_sum = total['amount__sum'] or 0

    context = {
        "total": total,
        "amount_sum": amount_sum,
    }

    return render(request, 'homebook/cashBreakdown_table.html', context)


@never_cache
def CashBreakdownCalc(request):
    amount = request.POST.get('amount')
    One_thousands = request.POST.get('One_thousands')
    Five_hundreds = request.POST.get('Five_hundreds')
    Two_hundreds = request.POST.get('Two_hundreds')
    One_hundreds = request.POST.get('One_hundreds')
    Fifties = request.POST.get('Fifties')
    Forties = request.POST.get('Forties')
    Twenties = request.POST.get('Twenties')
    Tens = request.POST.get('Tens')
    Fives = request.POST.get('Fives')
    Ones = request.POST.get('Ones')

    if One_thousands == 0 or Five_hundreds == 0 or Two_hundreds == 0 or One_hundreds == 0 or \
            Fifties == 0 or Forties == 0 or Twenties == 0 or Tens == 0 or Fives == 0 or \
            Ones == 0:
        a = int(input(amount))
        b = int(One_thousands)
        c = int(Five_hundreds)
        d = int(Two_hundreds)
        e = int(One_hundreds)
        f = int(Fifties)
        g = int(Forties)
        h = int(Twenties)
        i = int(Tens)
        j = int(Fives)
        k = int(Ones)

        if b == 0 and c == 0 and d == 0 and e == 0 and f == 0 and g == 0 and h == 0 and i == 0 and j == 0 and k == 0:
            res = "Zero divide error"
            return render(request, "homebook/input.html", {"results": res})
        else:
            res = int(input())
            b = a // 1000
            a = a % 1000
            c = a // 500
            a = a % 500
            d = a // 200
            a = a % 200
            e = a // 100
            a = a % 100
            f = a // 50
            a = a % 50
            g = a // 40
            a = a % 40
            h = a // 20
            a = a % 20
            i = a // 10
            a = a % 10
            j = a // 10
            a = a % 10
            k = a // 1
            a = a % 1

            return render(request, "homebook/results.html", {"results": res})
    else:
        res = "Only digits are allowed"
        return render(request, "homebook/input.html", {"results": res})


@never_cache
def Results(request):
    context = {
        "name": {"Results Page"},

    }
    return render(request, 'homebook/results.html', context)


@never_cache
def C_update(request, pk):
    note = CashBreakdown.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateCashBreakdownForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/cashBreakdown_table')

    else:
        form = UpdateCashBreakdownForm(instance=note)

    context = {
        'form': form, 'UpdateCashBreakdownForm': UpdateCashBreakdownForm,

    }
    return render(request, 'cashBreakdown/update.html', context)


@never_cache
def C_delete(request, pk):
    note = CashBreakdown.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/cashBreakdown_table')

    context = {
        'item': note,
    }
    return render(request, 'cashBreakdown/delete.html', context)


@never_cache
def UpdateEmployee(request):
    context = {
        "name": {"Employee update"},
        'form': TaskForm
    }
    return render(request, 'homebook/employee.html', context)


@never_cache
def E_update(request, pk):
    note = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateEmployeeForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/cashBreakdown_table')

    else:
        form = UpdateEmployeeForm(instance=note)

    context = {
        'form': form, 'EmployeeForm': UpdateEmployeeForm,

    }
    return render(request, 'employee-register.html', context)


@never_cache
def E_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employee')

    context = {
        'item': employee,
    }
    return render(request, 'employee/delete.html', context)
