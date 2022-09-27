from django.urls import path
from django.http import HttpResponse

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    # Create a page that lists all products under the same category or stick with table database page
    path('rentals/', views.rentalsPage, name='rentals'),
    path('rentals/<int:id>/<slug:slug>/', views.rentalDetail, name='rental_detail'),
    path('profile/', views.profilePage, name='profile'),
    path('', views.registerPage, name='register'),
]
