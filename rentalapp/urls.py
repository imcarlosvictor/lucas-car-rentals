from django.urls import path

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('', views.login, name='login'),
    path('rentals', views.rentals, name="rentals"),
    path('payments', views.payments, name='payments'),
    path('billing', views.billing, name='billing'),
    path('profile', views.profile, name='profile'),
]
