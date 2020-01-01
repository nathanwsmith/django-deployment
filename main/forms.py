from django.forms import ModelForm
from .models import Bank, Account, Currency

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'name', 'currency', 'iban']
