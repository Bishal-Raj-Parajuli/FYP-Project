from django.db import models
from SettingsApp.models import MenuItems, RoomDetails, Unit, TimeStamp


# Create your models here.
class Customer(TimeStamp):
    id = models.BooleanField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20, unique=True)
    id_type = models.CharField(max_length=100)
    id_photo = models.ImageField()
    id_no = models.IntegerField()

    def __str__(self) -> str:
        return self.name

['room', 'rate','days','customer','paid']
class RoomBooking(TimeStamp):  
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(RoomDetails, on_delete=models.PROTECT)
    rate = models.IntegerField()
    days = models.IntegerField()
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.room
