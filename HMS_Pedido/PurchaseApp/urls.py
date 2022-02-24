from unicodedata import name
from django.urls import path
from .views import ListPurchase, AddPurchase, ViewPurchase, DeletePurchase

urlpatterns = [
    path('list-purchase', ListPurchase, name='list-purchase'),
    path('add-purchase', AddPurchase.as_view(), name='add-purchase'),
    path('view-purchase/<int:pk>', ViewPurchase, name='view-purchase' ),
    path('delete-puechase/<int:pk>', DeletePurchase, name='delete-purchase')
]