
# Create your models here.

"""
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

class StockDetail(models.Model):
    stockName = models.CharField(max_length=100)
    currentFreeCashFlow = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    CurrentMarketCap = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    GrowthRateYear1_3 = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    GrowthRateYear4_6 = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    GrowthRateYear7_10 = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    DiscountRate = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    FCF = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    ExcessCash = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    TerminalMultiple = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)


    set_name = models.CharField(max_length=100)
    def __str__(self):
       return self.set_name

       """
    