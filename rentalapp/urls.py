from django.urls import path

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('payments', views.payments, name='payments'),
    path('billing', views.billing, name='billing'),
    path('profile', views.profile, name='profile'),
]
