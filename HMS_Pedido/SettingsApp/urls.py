from unicodedata import name
from django.urls import path
from SettingsApp import views

urlpatterns = [
    #Purchase Category URLS
    path('list-purchase-category', views.ListPurchaseCategory.as_view(), name='list-purchase-category'),
    path('add-purchase-category', views.AddPurchaseCategory.as_view(), name='add-purchase-category'),
    path('update-purchase-category/<int:pk>', views.UpdatePurchaseCategory.as_view(), name='update-purchase-category'),
    path('delete-purchase-category/<int:pk>', views.DeletePurchaseCategory, name='delete-purchase-category'),

    path('list-purchase-item', views.ListPurchaseItem.as_view(), name='list-purchase-item'),
    path('add-purchase-item', views.AddPurchaseItem.as_view(), name='add-purchase-item'),
    path('update-purchase-item/<int:pk>', views.UpdatePurchaseItem.as_view(), name='update-purchase-item'),
    path('delete-purchase-item/<int:pk>', views.DeletePurchaseItem, name='delete-purchase-item'),
]