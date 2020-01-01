from django.contrib import admin
from .models import Bank, Account, Currency

# Register your models here.
admin.site.register(Bank)
admin.site.register(Currency)
admin.site.register(Account)

