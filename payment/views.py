import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from rentalapp.models import Product
from orders.models import Order, OrderItem
from cart.cart import Cart
from orders.models import Invoice


# STRIPE
# This is your test secret API key.
stripe.api_key = 'sk_test_51LhNbNBGZyNiyiqHLHFvN0Eucgo7IWOQcT33pjpIQ4CQd14nOvqHCJVCsT0aOfRVWQnDV5fd7tGSTTksVADAarlj00GdR1hI4l'

DOMAIN = 'https://lucascarrentals.herokuapp.com/'

# Create your views here.
def build_checkout_session(request):
    """Stripe payment API is used to process payment.

    Returns:
        checkout_session: Stripe checkout session.
        order: User information and order items.
    """

    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    total_cost_to_int = int(total_cost) * 100

    checkout_session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'cad',
                'product_data': {
                    'name': 'Cars',
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
    """Changes availability of products and creates an invoice for the user.

    Returns:
        Successful payment page 
    """

    session, order = build_checkout_session(request)
    order.paid = True
    order.save()
    # Store and format data for invoice
    order_id = request.session.get('order_id')
    customer_name = request.user.firstname + ' ' + request.user.lastname
    customer_name_formatted = customer_name.title()
    customer_email = request.user.email
    total_cost = int(order.get_total_cost())
    # Create invoice 
    Invoice.objects.create(
        slug=order_id,
        transaction_id=order_id,
        customer=customer_name_formatted,
        email=customer_email,
        amount=total_cost,
        paid=order.paid
    )

    # Change product availability
    product_ids = request.session.get('product_ids')
    for product_id in product_ids.values():
        rented_product = Product.objects.get(id=product_id)
        rented_product.available = False
        rented_product.save()

    return render(request, 'payment/success.html')

def checkout_cancelled(request):
    """Marks the order as incomplete.

    Returns:
        Cancelled payment page
    """

    session, order = build_checkout_session(request)
    order.paid = False
    order.save()
    return render(request, 'payment/cancelled.html')
