from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Unit(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    unit_name = models.CharField(max_length=50, unique=True)
    unit_code = models.CharField(max_length=25, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.unit_code

    def get_absolute_url(self):
        return reverse('list-unit')
    class Meta:
        verbose_name_plural = 'Unit'


class MenuCategory(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('list-menu-category')
    class Meta:
        verbose_name_plural = 'Menu Category'

class MenuItems(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(MenuCategory, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    recipe = models.TextField(blank=True)
    thumbnail = models.ImageField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-menu-item')
    class Meta:
        verbose_name_plural = 'Menu Items'

class PurchaseItemsCategory(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('list-purchase-category')
    
    class Meta:
        verbose_name_plural = 'Purchase Category'
class PurchaseItems(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(PurchaseItemsCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255)
    thumbnail = models.ImageField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-purchase-item')
    class Meta:
        verbose_name_plural = 'Purchase Item'
class RoomCategory(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('list-room-category')

    class Meta:
        verbose_name_plural = 'Room Category'
class RoomDetails(TimeStamp):
    ROOM_TYPE = (
        ('Twin Bed','Twin Bed'),
        ('Twin Bed','Couple Bed'),
        ('Twin Bed','King Bed'),
    )
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255)
    price = models.FloatField()
    room_type = models.CharField(choices=ROOM_TYPE, max_length=255)
    room_capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse('list-room-details')

    class Meta:
        verbose_name_plural = 'Rooms'