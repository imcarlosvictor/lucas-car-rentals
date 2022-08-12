from django import forms
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import MyUser

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         # User = get_user_model()
#         model = MyUser
#         fields = ['email', 'password1', 'password2']
    

class UserCreationForm(forms.ModelForm):
    pass
