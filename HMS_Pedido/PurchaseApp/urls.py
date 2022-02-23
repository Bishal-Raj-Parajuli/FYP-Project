from django.urls import path
from .views import ListPurchase

urlpatterns = [
    path('list-purchase', ListPurchase, name='list-purchase')
]