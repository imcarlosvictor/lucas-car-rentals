from django.urls import path

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('rentals', views.rentalPage, name='rentals'),
    path('payments', views.paymentPage, name='payments'),
    path('billing', views.billingPage, name='billing'),
    path('profile', views.profilePage, name='profile'),
]
