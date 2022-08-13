from django.urls import path
from django.http import HttpResponse

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('rentals/', views.rentalPage, name='rentals'),
    path('payments/', views.paymentPage, name='payments'),
    path('billing/', views.billingPage, name='billing'),
    path('profile/', views.profilePage, name='profile'),
]
