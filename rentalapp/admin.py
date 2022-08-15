from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'firstname', 'lastname', 'mobile', 'email']
    list_editable = ['firstname', 'lastname', 'mobile', 'email']
    # prepopulated_fields = {'slug': ('user_id',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'model', 'brand', 'category', 'color', 'capacity', 'fuel_type', 'price', 'description', 'available', 'created', 'updated']
    list_editable = ['price', 'available']
    list_filter = ['available', 'brand', 'capacity', 'fuel_type', 'price']
    prepopulated_fields = {'slug': ('model',)}

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['rental_id', 'slug', 'pickup_date', 'return_date', 'user_id', 'vehicle_id', 'rental_amount', 'rental_status']
    # prepopulated_field = {'slug': ('rental_id',)}

