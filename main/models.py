from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=50)

    def __str__(self):
        return self.bank_name


class Currency(models.Model):
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.currency


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    iban = models.CharField(max_length=22)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
