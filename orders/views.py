import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from cart.cart import Cart
from rentalapp.models import Product
from .models import Order, OrderItem, Invoice
from .tasks import order_created
from .forms import OrderCreateForm
from rentalapp.models import MyUser


# Create your views here.
def order_create(request):
    """
    Displays the order summary and prompts the user to fill out a shipping address form. An email is then send
    to the user the user.
    """

    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Format and store mail info
            subject = 'LucasCarRentals Your order was received'
            body = 'Order successfully created'
            sender = settings.EMAIL_HOST_USER
            recipient = form.cleaned_data['email']

            for item in cart:
                OrderItem.objects.create(
                    order=order, 
                    product=item['product'], 
                    price=item['price'], 
                    quantity=item['quantity']
                )
                # Add order items in a tabular format

            try:
                send_mail(
                    subject, 
                    body, 
                    recipient, 
                    [recipient],
                    fail_silently=False,
                )
                # # Email creation
                # email = EmailMessage(
                #     subject,
                #     body, 
                #     settings.EMAIL_HOST_USER,
                #     [recipient],
                # )
                # email.fail_silently = False
                # email.send()
            except OperationalError:
                print('Connection Refused')

            cart.clear()
            # # Launch asynchronous task 
            # order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # Store the IDs of the products in the session to change availability
            # once the payment is successful
            list_length = range(0, len(cart))
            list_ids = [ item['id'] for item in cart ]
            dict_ids = dict(zip(list_length, list_ids))
            request.session['product_ids'] = dict_ids

            return redirect(reverse('payment:checkout'))
    else:
        form = OrderCreateForm()

    context = {'cart': cart, 'form': form}
    return render(request, 'order/create.html', context)

def invoice_page(request):
    """
    Displays all transactions made by the user, whether it was successful or cancelled.
    """

    invoices = Invoice.objects.all()
    context = {'invoices': invoices}
    return render(request, 'order/invoices.html', context)
