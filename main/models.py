# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import Adsb

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
