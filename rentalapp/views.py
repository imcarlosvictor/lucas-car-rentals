from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import *
from .forms import CreateUserForm


# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created.')

            return redirect('rentalapp:login')

    context = {'form': form}
    return render(request, 'customer/accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('rentalapp:rentals')
        else:
            messages.error(request, 'Email or password is incorrect')
            return render(request, 'customer/accounts/login.html')

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
