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
