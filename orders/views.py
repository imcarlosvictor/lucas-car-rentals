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
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale ({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True,
            }
        })

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, 
                    product=item['product'], 
                    price=item['price'], 
                    quantity=item['quantity']
                )

            cart.clear()
            # launch asynchronous task with delay()
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment

            if result.is_success:
                # mark the order as paid
                order.paid = True
                # store the unique transaction id
                order.braintree_id = result.transaction.id
                order.save()
                return redirect('order:done')
            else:
                return redirect('order:cancelled')

    else:
        form = OrderCreateForm()

    client_token = gateway.client_token.generate()
    context = {'cart': cart, 'form': form, 'client_token': client_token}
    return render(request, 'order/create.html', context)
