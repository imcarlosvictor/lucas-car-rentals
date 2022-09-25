import weasyprint
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from cart.cart import Cart
from .models import Order, OrderItem
from .tasks import order_created
from .forms import OrderCreateForm


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
                    price_id=item['price_id'],
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

    context = {'cart': cart, 'form': form}
    return render(request, 'order/create.html', context)

def invoice_page(request):
    context = {}
    return render(request, 'order/invoices.html', context)

def invoice_detail(request):
    pass

def create_invoice(request):
    pass

def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('order/pdf.html', {'order': order})
    response = HttpResponse(content_type='applicaiton/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])

    return response
