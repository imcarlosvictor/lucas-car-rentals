from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def rentals(request):
    return render(request, 'customer/rentals.html')

def payments(request):
    return render(request, 'customer/payments.html')

def billing(request):
    return render(request, 'customer/billing.html')

def profile(request):
    return render(request, 'customer/profile.html')
