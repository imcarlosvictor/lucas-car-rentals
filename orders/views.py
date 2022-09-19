import braintree
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem
from .tasks import order_created
from .forms import OrderCreateForm


gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

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
            # redirect for payment
            return redirect(reverse('payment:checkout'))
    else:
        form = OrderCreateForm()

    client_token = gateway.client_token.generate()
    context = {'cart': cart, 'form': form, 'client_token': client_token}
    return render(request, 'order/create.html', context)
