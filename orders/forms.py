from django import forms

from .models import Order
from rentalapp.models import BillingAddress


# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['firstname', 'lastname', 'email', 'address', 'postal_code', 'city']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address',  'country', 'province', 'city', 'postal_code']
