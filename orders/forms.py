from django import forms

from .models import Order
from rentalapp.models import MyUser


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firstname', 'lastname', 'email', 'address',  'country', 'province', 'city', 'postal_code']
