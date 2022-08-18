from django.urls import path
from django.http import HttpResponse

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    # Create a page that lists all products under the same category or stick with table database page
    path('products/', views.productPage, name='products'),
    path('products/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('payments/', views.paymentPage, name='payments'),
    path('billing/', views.billingPage, name='billing'),
    path('profile/', views.profilePage, name='profile'),
]
