from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def customerdashboard(request):
    return render(request, 'rental/base.html')
