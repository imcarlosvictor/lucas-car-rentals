from django.contrib import admin

from .models import Order, OrderItem, Invoice
from rentalapp.models import MyUser

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'firstname',
        'lastname',
        'email',
        'country',
        'address',
        'postal_code',
        'city',
        'paid',
        'created',
        'updated',
    ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'transaction_id',
        'transaction_date',
        'customer',
        'amount',
        'paid',
    ]
    list_filter = ['paid']
    prepopulated_fields = {'slug':('transaction_id',)}
