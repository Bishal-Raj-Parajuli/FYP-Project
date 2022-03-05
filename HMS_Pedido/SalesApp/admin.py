import imp
from django.contrib import admin
from .models import Customer, OrderDetails, OrderMaster, RoomBooking

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','address','contact','id_no']

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ['room', 'rate','days','customer','paid']

@admin.register(OrderMaster)
class OrderMasterAdmin(admin.ModelAdmin):
    list_display = ['room','total_bill','paid']

@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['order_master','item','qty','amt']