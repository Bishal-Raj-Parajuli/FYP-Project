from django.db import models
from SettingsApp.models import MenuItems, RoomDetails, Unit, TimeStamp


# Create your models here.
class Customer(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20, unique=True)
    id_type = models.CharField(max_length=100)
    id_photo = models.ImageField()
    id_no = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class RoomBooking(TimeStamp):  
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(RoomDetails, on_delete=models.PROTECT, related_name='room_booking')
    rate = models.IntegerField()
    days = models.IntegerField()
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.room)

class OrderMaster(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(RoomBooking, on_delete=models.PROTECT, related_name='order_master')
    total_bill = models.IntegerField()
    paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.room)

class OrderDetails(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    order_master = models.ForeignKey(OrderMaster, on_delete=models.CASCADE, related_name='order_details')
    item = models.ForeignKey(MenuItems, on_delete=models.PROTECT)
    qty = models.IntegerField()
    amt = models.IntegerField()

    def __str__(self) -> str:
        return str(self.item)

