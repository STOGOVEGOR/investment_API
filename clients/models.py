from django.utils import timezone
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)


class InvestmentType(models.Model):
    type = models.CharField(max_length=100, blank=True)


class Investment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    invest_type = models.ForeignKey(InvestmentType, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=30, decimal_places=10, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
