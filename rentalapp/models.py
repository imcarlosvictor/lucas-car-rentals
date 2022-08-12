from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, firstname, lastname, mobile, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have an password')
        if not firstname:
            raise ValueError('User must have a first name')
        if not lastname:
            raise ValueError('User must have a last name')
        if not mobile:
            raise ValueError('User must have a mobile number')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            mobile=mobile,
            **extra_fields
        )
        user.set_password(password) # Hashes password
        user.save(using=self._db)
        return user

    def create_user(self, email, password, firstname, lastname, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, firstname, lastname, mobile, **extra_fields)

    def create_superuser(self, email, password, firstname, lastname, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, firstname, lastname, mobile, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    mobile = models.IntegerField()
    password = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'mobile']

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'


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


class Rent(models.Model):
    RENTAL_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    rental_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=200)
    pickup_date = models.DateField()
    return_date = models.DateField()
    user_id = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    rental_amount = models.DecimalField(max_digits=9, decimal_places=2)
    rental_status = models.CharField(max_length=20, choices=RENTAL_STATUS_CHOICES)

    def __str__(self):
        return 'Transaction ID: ' + transaction_id
