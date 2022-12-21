from django.db import models


# Create your models here.
class Employee(models.Model):
    COMPANIES = [
        ("Mogoon Farm", "Mogoon Farm"),
        ("Morombi Escarpment", "Morombi Escarpment"),
        ("Kamatargui Guesthouse", "Kamatargui Guesthouse"),
        ("Other Company", "Other Company"),
    ]
    national_id = models.IntegerField(default='0000000000', blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    Other_names = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False)
    pay_amt = models.DecimalField(decimal_places=2, max_digits=8)
    company = models.CharField(max_length=50, default=None, choices=COMPANIES)
    timestamp_last_updated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    employee_email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    employee_phone = models.CharField(max_length=12, default="+000-000-000-000", null=True)

    def __str__(self):
        return self.national_id


class CashBreakdown(models.Model):
    cashBreakdown_date = models.DateTimeField(auto_now_add=False)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    One_thousands = models.IntegerField(choices=list(zip(range(0, 100001), range(0, 100001))))
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
        return str(self.cashBreakdown_date)

    # you override the save method and calculate for opening
    # def save(self, *args, **kwargs):
    #     self.One_thousands = self.amount % 1000;
    #     self.Five_hundreds = self.amount % 1000 / 500;
    #     self.Two_hundreds = self.amount % 1000 % 500 / 200;
    #     self.One_hundreds = self.amount % 1000 % 500 % 200 / 100;
    #     self.Fifties = self.amount % 1000 % 500 % 200 % 100 / 50;
    #     self.Forties = self.amount % 1000 % 500 % 200 % 100 % 50 / 40;
    #     self.Twenties = self.amount % 1000 % 500 % 200 % 100 % 50 % 40 / 20;
    #     self.Tens = self.amount % 1000 % 500 % 200 % 100 % 50 % 40 % 20 / 10;
    #     self.Fives = self.amount % 1000 % 500 % 200 % 100 % 50 % 40 % 20 % 10 / 5;
    #     self.Ones = self.amount % 1000 % 500 % 200 % 100 % 50 % 40 % 20 % 10 % 5 / 1;
    #     super(CashBreakdown, self).save(*args, **kwargs)
