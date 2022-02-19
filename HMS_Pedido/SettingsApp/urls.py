from unicodedata import name
from django.urls import path
from SettingsApp import views

urlpatterns = [
    #Purchase Category URLS
    path('list-purchase-category', views.ListPurchaseCategory, name='list-purchase-category')
]