from django.shortcuts import render, redirect
from . import models
from .forms import TaskForm, UpdateCashBreakdownForm
from .models import *


# Create your views here.


def Home(request):
    context = {
        "name": {"Home Farm Page"},
        'form': TaskForm
    }
    return render(request, 'homebook/home.html', context)


def CashBreakdownTable(requset):
    note = CashBreakdown.objects.all()
    cashBreakdown_date = models.DateTimeField()
    money = models.IntegerField()
    one_thousands = models.IntegerField()
    five_hundreds = models.IntegerField()
    two_hundreds = models.IntegerField()
    one_hundreds = models.IntegerField()
    fifties = models.IntegerField()
    forties = models.IntegerField()
    twenties = models.IntegerField()
    tens = models.IntegerField()
    fives = models.IntegerField()
    ones = models.IntegerField()

    context = {
        "cashBreakdown": note,
        "cashBreakdown_date": cashBreakdown_date,
        "money": money,
        "one_thousands": one_thousands,
        "five_hundreds": five_hundreds,
        "two_hundreds": two_hundreds,
        "one_hundreds": one_hundreds,
        "fifties": fifties,
        "forties": forties,
        "twenties": twenties,
        "tens": tens,
        "fives": fives,
        "ones": ones,

    }
    return render(requset, 'homebook/cashBreakdown_table.html', context)


def CashBreakdownUpdate(requset):
    money = models.IntegerField()
    one_thousands = models.IntegerField()
    five_hundreds = models.IntegerField()
    two_hundreds = models.IntegerField()
    one_hundreds = models.IntegerField()
    fifties = models.IntegerField()
    forties = models.IntegerField()
    twenties = models.IntegerField()
    tens = models.IntegerField()
    fives = models.IntegerField()
    ones = models.IntegerField()

    context = {
        "money": money,
        "one_thousands": one_thousands,
        "five_hundreds": five_hundreds,
        "two_hundreds": two_hundreds,
        "one_hundreds": one_hundreds,
        "fifties": fifties,
        "forties": forties,
        "twenties": twenties,
        "tens": tens,
        "fives": fives,
        "ones": ones,

    }

    return render(requset, 'homebook/cashBreakdown_update.html', context)


def CashBreakdownCreate(request):
    if request.method == "POST":
        money = request.POST['money']
        one_thousands = request.POST['one_thousands']
        five_hundreds = request.POST['five_hundreds']
        two_hundreds = request.POST['two_hundreds']
        one_hundreds = request.POST['one_hundreds']
        fifties = request.POST['fifties']
        forties = request.POST['forties']
        twenties = request.POST['twenties']
        tens = request.POST['tens']
        fives = request.POST['fives']
        ones = request.POST['ones']

        insert = CashBreakdown(money=money, one_thousands=one_thousands,
                               five_hundreds=five_hundreds, two_hundreds=two_hundreds, one_hundreds=one_hundreds,
                               fifties=fifties, forties=forties, twenties=twenties, tens=tens, fives=fives, ones=ones,

                               )
        insert.save()
        return redirect('/cashBreakdown_table')


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


def AddEmployee(request):
    context = {
        "name": {"Employee update"},
        'form': TaskForm
    }
    return render(request, 'homebook/employee.html', context)


def MaterialKitMaster(request):
    context = {
        "name": {"Dashboard"},
        'form': TaskForm
    }
    return render(request, 'homebook/material-kit-master/template.html', context)
