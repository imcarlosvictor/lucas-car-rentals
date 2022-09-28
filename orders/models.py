from django.db import models
from django.urls import reverse

from rentalapp.models import Product, MyUser

# Create your models here.
class Order(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=False)
    address = models.CharField(max_length=300, blank=True)
    country = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    postal_code = models.CharField(max_length=200, blank=True)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_price_ids(self):
        return [item.get_price_id() for item in self.items.all()]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def get_price_id(self):
        return price_id


class Invoice(models.Model):
    STATUS_CHOICE = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending')
    )
    slug = models.SlugField(max_length=200)
    transaction_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    transaction_date = models.DateField(auto_now_add=True)
    customer = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    amount = models.FloatField()
    paid = models.BooleanField()

    class Meta:
        index_together = (('transaction_id', 'slug'))

    def __str__(self):
        return 'Transaction ID: ' + str(self.transaction_id)

