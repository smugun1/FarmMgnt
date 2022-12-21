import calculation
from django import forms
from .models import CashBreakdown, Employee


class TaskForm(forms.ModelForm):
    content = forms.CharField(label='SimKMN', widget=forms.TextInput(
        attrs={'placeholder': 'Add task here...'}))

    class Meta:
        model = Employee
        fields = '__all__'


class UpdateCashBreakdownForm(forms.ModelForm):
    class Meta:
        model = CashBreakdown
        fields = '__all__'


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class CashBreakdownCalcForm(forms.ModelForm):
    class Meta:
        model = CashBreakdown
        fields = '__all__'
        # Code for changing DATE FORMAT (from YYYY-MM-DD to DD-MM-YYYY)
        date = forms.DateField(
            widget=forms.DateInput(format='%d%m%Y'),
            input_formats=['%d-%m-%Y']
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        # your calculate
        amount = int(input("Enter amount"))
        instance.One_thousands = amount // 1000
        instance.Five_hundreds = amount % 1000 / 500
        instance.Two_hundreds = amount % 1000 % 500 / 200
        instance.One_hundreds = amount % 1000 % 500 % 200 / 100
        instance.Fifties = amount % 1000 % 500 % 200 % 100 / 50
        instance.Forties = amount % 1000 % 500 % 200 % 100 % 50 / 40
        instance.Twenties = amount % 1000 % 500 % 200 % 100 % 50 % 40 / 20
        instance.Tens = amount % 1000 % 500 % 200 % 100 % 50 % 40 % 20 / 10
        instance.Fives = amount % 1000 % 500 % 200 % 100 % 50 % 40 % 20 % 10 / 5
        instance.Ones = amount % 1000 % 500 % 200 % 100 % 50 % 40 % 20 % 10 % 5 / 1

        if commit:
            instance.save()
        return instance
