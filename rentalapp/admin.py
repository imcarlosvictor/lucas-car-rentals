from django.contrib import admin

from .models import Customer, Vehicle, Employee, Rent

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'firstname', 'lastname', 'date_of_birth', 'gender', 'phone', 'email', 'address', 'created_at', 'updated_at']
    list_editable = ['phone', 'email', 'address']
    prepopulated_field = {'slug': ('id',)}

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'slug', 'super_id', 'firstname', 'lastname', 'date_of_birth', 'gender']
    list_editable = ['super_id']
    prepopulated_field = {'slug': ('emp_id',)}

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'model', 'brand', 'color', 'dimensions', 'capacity', 'fuel_type', 'vehicle_condition', 'available']
    list_editable = ['vehicle_condition', 'available']
    prepopulated_field = {'slug': ('id',)}

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['rental_id', 'slug', 'pickup_date', 'return_date', 'customer_id', 'vehicle_id', 'rental_amount', 'rental_status']
    prepopulated_field = {'slug': ('rental_id',)}

