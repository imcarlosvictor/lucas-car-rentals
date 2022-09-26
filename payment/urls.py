from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    path('cancelled/', views.checkout_cancelled, name='cancelled'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('success/', views.checkout_success, name='success'),
]
