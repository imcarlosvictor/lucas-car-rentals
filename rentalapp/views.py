from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from .forms import CreateUserForm


def loginPage(request):
    context = {}
    return render(request, 'customer/accounts/login.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'customer/accounts/register.html', context)

def rentalPage(request):
    context = {}
    return render(request, 'customer/dashboard/rentals.html')

def paymentPage(request):
    context = {}
    return render(request, 'customer/dashboard/payments.html')

def billingPage(request):
    context = {}
    return render(request, 'customer/dashboard/billing.html')

def profilePage(request):
    context = {}
    return render(request, 'customer/dashboard/profile.html')
