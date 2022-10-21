from django.shortcuts import render, redirect
from .forms import TaskForm, UpdateCashBreakdownForm
from . import models
from .models import *
from django.db.models import Sum, F


# Create your views here.
def Home(request):
    context = {
        "name": {"Home Farm Page"},
        'form': TaskForm
    }
    return render(request, 'homebook/home.html', context)


def Employee(request):
    national_id = models.IntegerField()
    first_name = models.CharField()
    Other_names = models.CharField()
    last_name = models.CharField()
    pay_amt = models.DecimalField()
    timestamp_last_updated = models.DateTimeField()
    timestamp_added = models.DateTimeField()

    context = {
        "national_id": national_id,
        "first_name": first_name,
        "Other_names": Other_names,
        "last_name": last_name,
        "pay_amt": pay_amt,
        "timestamp_last_updated": timestamp_last_updated,
        "timestamp_added": timestamp_added,

    }
    return render(request, 'homebook/employee_register.html', context)


def CashBreakdownTable(request):
    note = CashBreakdown.objects.all()
    cashBreakdown_date = models.DateTimeField()
    money_Notes = models.CharField()
    amount = models.IntegerField()
    Thousands = models.IntegerField()
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
        "cashBreakdown": note,
        "cashBreakdown_date": cashBreakdown_date,
        "money_Notes": money_Notes,
        "amount": amount,
        "Thousands": Thousands,
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


def CashBreakdownUpdate(request):
    # input the amount to be broken_down
    amount = CashBreakdown.objects.all()
    # money_Notes = models.CharField()
    # Thousands = (amount % 1000)
    # Five_hundreds = ((amount % 1000) / 500)
    # Two_hundreds = (((amount % 1000) % 500) / 200)
    # One_hundreds = ((((amount % 1000) % 500) % 200) / 100)
    # Fifties = (((((amount % 1000) % 500) % 200) % 100) / 50)
    # Forties = ((((((amount % 1000) % 500) % 200) % 100) % 50) / 40)
    # Twenties = (((((((amount % 1000) % 500) % 200) % 100) % 50) % 40) / 20)
    # Tens = ((((((((amount % 1000) % 500) % 200) % 100) % 50) % 40) % 20) / 10)
    # Fives = (((((((((amount % 1000) % 500) % 200) % 100) % 50) % 40) % 20) % 10) / 5)
    # Ones = ((((((((((amount % 1000) % 500) % 200) % 100) % 50) % 40) % 20) % 10) % 5) / 1)

    context = {
        "amount": amount,
        # "money_Notes": money_Notes,
        # "Thousands": Thousands,
        # "Five_hundreds": Five_hundreds,
        # "Two_hundreds": Two_hundreds,
        # "One_hundreds": One_hundreds,
        # "Fifties": Fifties,
        # "Forties": Forties,
        # "Twenties": Twenties,
        # "Tens": Tens,
        # "Fives": Fives,
        # "Ones": Ones,

    }

    return render(request, 'homebook/cashBreakdown_update.html', context)


def CashBreakdownCreate(request):
    if request.method == "POST":
        cashBreakdown_date = request.POST['cashBreakdown_date']
        money_Notes = request.POST['money_Notes']
        amount = request.POST['amount']
        Thousands = request.POST['Thousands']
        Five_hundreds = request.POST['Five_hundreds']
        Two_hundreds = request.POST['Two_hundreds']
        One_hundreds = request.POST['One_hundreds']
        Fifties = request.POST['Fifties']
        Forties = request.POST['Forties']
        Twenties = request.POST['Twenties']
        Tens = request.POST['Tens']
        Fives = request.POST['Fives']
        Ones = request.POST['Ones']

        insert = CashBreakdown(cashBreakdown_date=cashBreakdown_date, money_Notes=money_Notes, amount=amount,
                               Thousands=Thousands, Five_hundreds=Five_hundreds, Two_hundreds=Two_hundreds,
                               One_hundreds=One_hundreds, Fifties=Fifties, Forties=Forties, Twenties=Twenties,
                               Tens=Tens, Fives=Fives, Ones=Ones)
        insert.save()
    return redirect('/cashBreakdown_table')


def Employee(request):

    national_id = models.IntegerField()
    first_name = models.CharField()
    Other_names = models.CharField()
    last_name = models.CharField()
    pay_amt = models.DecimalField()
    timestamp_last_updated = models.DateTimeField()
    timestamp_added = models.DateTimeField()
    employee_email = models.EmailField()
    employee_phone = models.IntegerField()

    context = {

        "national_id": national_id,
        "first_name": first_name,
        "last_name": Other_names,
        "pay_amt": last_name,
        "timestamp_last_updated": pay_amt,
        "timestamp_added": timestamp_last_updated,
        "employee_email": timestamp_added,
        "employee_phone": employee_email,
    }
    return render(request, 'homebook/employee_register.html', context)


def AddEmployee(request):
    context = {
        "name": {"Employee update"},
        'form': TaskForm
    }
    return render(request, 'homebook/employee.html', context)


def EmployeeCreate(request):
    if request.method == "POST":
        Employee = request.POST['Employee']
        national_id = request.POST['national_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pay_amt = request.POST['pay_amt']
        timestamp_last_updated = request.POST['timestamp_last_updated']
        timestamp_added = request.POST['timestamp_added']
        employee_email = request.POST['employee_email']
        employee_phone = request.POST['employee_phone']

        insert = Employee(Employee=Employee, national_id=national_id, afirst_name=first_name,
                          last_name=last_name, pay_amt=pay_amt, timestamp_last_updated=timestamp_last_updated,
                          timestamp_added=timestamp_added)
        insert.save()
    return redirect('/employee')


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


def C_delete(request, pk):
    note = CashBreakdown.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/cashBreakdown_table')

    context = {
        'item': note,
    }
    return render(request, 'cashBreakdown/delete.html', context)


def Dashboard(request):
    context = {
        "name": {"Dashboard"},
        'form': TaskForm
    }
    return render(request, 'homebook/dashboard.html', context)
