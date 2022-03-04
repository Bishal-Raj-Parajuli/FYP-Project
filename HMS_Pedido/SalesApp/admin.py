import imp
from django.contrib import admin
from .models import Customer, RoomBooking

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','address','contact','id_no']

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ['room', 'rate','days','customer','paid']
