from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import UserCreationForm


# Create your views here.
def registerPage(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
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
            return redirect('rentalapp:products')
        else:
            messages.error(request, 'Email or password is incorrect')
            return render(request, 'customer/accounts/login.html')

    context = {}
    return render(request, 'customer/accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('rentalapp:login')

def productPage(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product_list = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_list = product.filter(category=category)

    # Pagination
    paginator = Paginator(product_list, 10) # 10 products in each page
    page_number = request.GET.get('page')
    try:
        products = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.get_page(1)
    except EmptyPage:
        # If page is out of range devliver last page of results
        products = paginator.get_page(paginator.num_pages)

    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'customer/dashboard/products.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    context = {'product': product}
    return render(request, 'customer/dashboard/detail.html', context)

def paymentPage(request):
    context = {}
    return render(request, 'customer/dashboard/payments.html')

def billingPage(request):
    context = {}
    return render(request, 'customer/dashboard/billing.html')

def profilePage(request):
    context = {}
    return render(request, 'customer/dashboard/profile.html')
