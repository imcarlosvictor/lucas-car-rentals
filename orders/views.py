import datetime
import random
import weasyprint
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from cart.cart import Cart
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
                # Invoice details 
                invoice_id = random.randint(100000, 999999)
                invoice_date = datetime.date.today()
                customer_name = request.user.firstname
                # Create Invoice
                Invoice.objects.create(
                    slug=invoice_id,
                    transaction_id=invoice_id,
                    transaction_date=invoice_date,
                    customer=customer_name,
                    rental=item['product'],
                    amount=item['price'],
                    paid=False
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
    invoices = Invoice.objects.all()

    context = {'invoices': invoices}
    return render(request, 'order/invoices.html', context)

def invoice_detail(request):
    # Customer Info
    user_id = request.session.user_id
    user = get_object_or_404(MyUser, user_id)

    # Product Info
    product_id = request.session.get('order.id')
    product = get_object_or_404(Order, product_id)

    context = {'user': user, 'product': product}
    return render(request, 'order/invoid_detail.html', context)
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
