from django.contrib import admin
from .models import MenuCategory, MenuItems, PurchaseItemsCategory, PurchaseItems, RoomCategory, RoomDetails, Unit
# Register your models here.
admin.site.register(
    [MenuCategory, MenuItems, PurchaseItemsCategory, PurchaseItems, RoomCategory, RoomDetails, Unit]
)