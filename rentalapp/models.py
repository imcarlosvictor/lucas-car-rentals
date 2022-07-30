from django.db import models

# Create your models here.
class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
        ('Other', 'Other'),
    )
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date_of_birth = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    address_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
        ('Other', 'Other'),
    ) 
    emp_id = models.AutoField(primary_key=True)
    super_id = models.IntegerField()
    slug = models.SlugField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)


class Address(models.Model):
    pass


class Vehicle(models.Model):
    FUEL_TYPE_CHOICES = (
        ('Gas', 'Gas'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    )
    VEHICLE_CONDITION_CHOICES = (
        ('Bad', 'Bad'),
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Brand New', 'Brand New'),
    )
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=200)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    dimensions = models.CharField(max_length=200)
    capacity = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    vehicle_condition = models.CharField(max_length=20, choices=VEHICLE_CONDITION_CHOICES)
    available = models.BooleanField()


class BodyStyle(models.Model):
    pass


class Rent(models.Model):
    RENTAL_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    rental_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=200)
    pickup_date = models.DateField()
    return_date = models.DateField()
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    rental_amount = models.DecimalField(max_digits=9, decimal_places=2)
    rental_status = models.CharField(max_length=20, choices=RENTAL_STATUS_CHOICES)

    def __str__(self):
        return 'Transaction ID: ' + transaction_id
