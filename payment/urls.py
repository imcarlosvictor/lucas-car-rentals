from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    # path('process/', views.payment_process, name='process'), # braintree
    path('done/', views.payment_done, name='done'),
    path('cancelled/', views.payment_cancelled, name='cancelled'),
    path('checkout/', views.create_checkout_session, name='checkout'), # stripe
    path('success/', views.checkout_success, name='success'),
]
