from unicodedata import name
from django.urls import path
from .views import AddPurchaseView, DeletePurchaseView, ListPurchaseView,StockView, ViewPurchaseView

urlpatterns = [
    path('list-purchase', ListPurchaseView, name='list-purchase'),
    path('add-purchase', AddPurchaseView.as_view(), name='add-purchase'),
    path('view-purchase/<int:pk>', ViewPurchaseView, name='view-purchase' ),
    path('delete-purchase/<int:pk>', DeletePurchaseView, name='delete-purchase'),
    path('view-stock', StockView, name='view-stock'),
]