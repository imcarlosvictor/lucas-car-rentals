from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, Vehicle, Rent

# Register your models here.
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'firstname', 'lastname', 'mobile', 'email']
    list_editable = ['firstname', 'lastname', 'mobile', 'email']
    # prepopulated_field = {'slug': ('id',)}

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'model', 'brand', 'color', 'dimensions', 'capacity', 'fuel_type', 'vehicle_condition', 'available']
    list_editable = ['vehicle_condition', 'available']
    # prepopulated_field = {'slug': ('id',)}

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['rental_id', 'slug', 'pickup_date', 'return_date', 'user_id', 'vehicle_id', 'rental_amount', 'rental_status']
    # prepopulated_field = {'slug': ('rental_id',)}

