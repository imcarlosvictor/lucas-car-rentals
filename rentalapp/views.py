from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, 'User successfully created.')

            return redirect('rentalapp:login')

    context = {'form': form}
    return render(request, 'customer/accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'customer/accounts/login.html')

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
