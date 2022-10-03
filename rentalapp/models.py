from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse

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
    password = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200, blank=True, null=True)

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


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rentalapp:product_list_by_category', args=[self.slug])


class Product(models.Model):
    FUEL_TYPE_CHOICES = (
        ('Gas', 'Gas'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=200)
    model = models.CharField(max_length=200, db_index=True)
    brand = models.CharField(max_length=200, db_index=True)
    color = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/media/images/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    capacity = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('model',)
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.brand + " " + self.model

    def get_absolute_url(self):
        return reverse('rentalapp:rental_detail', kwargs={'id': self.id, 'slug': self.slug})
