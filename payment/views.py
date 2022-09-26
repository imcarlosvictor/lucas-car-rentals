import braintree, stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from cart.cart import Cart


# STRIPE
# This is your test secret API key.
stripe.api_key = 'sk_test_51LhNbNBGZyNiyiqHLHFvN0Eucgo7IWOQcT33pjpIQ4CQd14nOvqHCJVCsT0aOfRVWQnDV5fd7tGSTTksVADAarlj00GdR1hI4l'

DOMAIN = 'http://127.0.0.1:8000/'

# Create your views here.
def build_checkout_session(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    total_cost_to_int = int(total_cost) * 100

    checkout_session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'cad',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': total_cost_to_int,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url= DOMAIN + 'payment/success/',
        cancel_url= DOMAIN + 'payment/cancelled/',
    )

    return checkout_session, order

def checkout_view(request):
    session, order = build_checkout_session(request)
    return redirect(session.url)

def checkout_success(request):
    session, order = build_checkout_session(request)
    order.paid = True
    order.save()
    return render(request, 'payment/success.html')

def checkout_cancelled(request):
    session, order = build_checkout_session(request)
    order.paid = False
    order.save()
    return render(request, 'payment/cancelled.html')
