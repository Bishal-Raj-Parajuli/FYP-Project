from unicodedata import name
from django.urls import path
from .views import ListPurchase, AddPurchase

urlpatterns = [
    path('list-purchase', ListPurchase, name='list-purchase'),
    path('add-purchase', AddPurchase.as_view(), name='add-purchase'),
]