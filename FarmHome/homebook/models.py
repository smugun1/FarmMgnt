from django.db import models


# Create your models here.
class Employee(models.Model):
    national_id = models.IntegerField()
    first_name = models.CharField(max_length=50, blank=False)
    Other_names = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False)
    pay_amt = models.DecimalField(decimal_places=2, max_digits=8)
    timestamp_last_updated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    employee_email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    employee_phone = models.IntegerField(max_length=12, default=None)

    def __str__(self):
        return self.last_name


class CashBreakdown(models.Model):
    DENOMINATION = [
        ("one_thousands", "Thousands"),
        ("five_hundreds", "Five hundreds"),
        ("two_hundreds", "Two hundreds"),
        ("one_hundreds", "One hundreds"),
        ("fifties", "Fifties"),
        ("forties", "Forties"),
        ("twenties", "Twenties"),
        ("tens", "Tens"),
        ("fives", "Fives"),
        ("ones", "Ones"),
    ]

    cashBreakdown_date = models.DateTimeField(auto_now_add=False)
    money_Notes = models.CharField(max_length=20, default=None, choices=DENOMINATION)
    amount = models.DecimalField(primary_key=Employee, decimal_places=2, max_digits=8)
    Thousands = models.IntegerField(choices=list(zip(range(0, 101), range(0, 101))))
    Five_hundreds = models.IntegerField(choices=list(zip(range(0, 101), range(0, 101))))
    Two_hundreds = models.IntegerField(choices=list(zip(range(0, 101), range(0, 101))))
    One_hundreds = models.IntegerField(choices=list(zip(range(0, 101), range(0, 101))))
    Fifties = models.IntegerField(choices=list(zip(range(0, 101), range(0, 101))))
    Forties = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))))
    Twenties = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))))
    Tens = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))))
    Fives = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))))
    Ones = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))))

    def __str__(self):
        return str(self.amount)
