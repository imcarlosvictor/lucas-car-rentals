from django.urls import path

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.customerdashboard, name="cust_dashboard"),
    path('payments', views.customerpayments, name='cust_payments')
]
