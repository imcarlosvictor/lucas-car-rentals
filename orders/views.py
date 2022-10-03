import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from cart.cart import Cart
from rentalapp.models import Product
from .models import Order, OrderItem, Invoice
from .tasks import order_created
from .forms import OrderCreateForm
from rentalapp.models import MyUser


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, 
                    product=item['product'], 
                    price=item['price'], 
                    quantity=item['quantity']
                )

            # clear cart
            cart.clear()
            # launch asynchronous task 
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # store product id to change availability later on
            list_length = range(0, len(cart))
            list_ids = [ item['id'] for item in cart ]
            dict_ids = dict(zip(list_length, list_ids))
            request.session['product_ids'] = dict_ids
            # redirect for payment
            return redirect(reverse('payment:checkout'))
    else:
        form = OrderCreateForm()

    context = {'cart': cart, 'form': form}
    return render(request, 'order/create.html', context)

def invoice_page(request):
    invoices = Invoice.objects.all()

    context = {'invoices': invoices}
    return render(request, 'order/invoices.html', context)
