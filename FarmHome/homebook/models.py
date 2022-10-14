from django.db import models


# Create your models here.
class Muster(models.Model):
    pass


class CashBreakdown(models.Model):
    cashBreakdown_date = models.DateTimeField(auto_now_add=False)
    money = models.IntegerField(default=None)
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

    def __str__(self):
        return str(self.one_thousands)
