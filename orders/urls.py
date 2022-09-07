from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('done/', views.order_done, name='order_done'),
    path('cancelled/', views.order_cancelled, name='order_cancelled')
]
