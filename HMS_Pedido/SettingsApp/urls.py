from unicodedata import name
from django.urls import path
from SettingsApp import views

urlpatterns = [
    #Purchase Category URLS
    path('list-purchase-category', views.ListPurchaseCategory.as_view(), name='list-purchase-category'),
    path('add-purchase-category', views.AddPurchaseCategory.as_view(), name='add-purchase-category'),
    path('update-purchase-category/<int:pk>', views.UpdatePurchaseCategory.as_view(), name='update-purchase-category'),
    path('delete-purchase-category/<int:pk>', views.DeletePurchaseCategory, name='delete-purchase-category'),

    #Menu Category URLS
    path('list-menu-category', views.ListMenuCategory.as_view(), name='list-menu-category'),
    path('add-menu-category', views.AddMenuCategory.as_view(), name='add-menu-category'),
    path('update-menu-category/<int:pk>', views.UpdateMenuCategory.as_view(), name='update-menu-category'),
    path('delete-menu-category/<int:pk>', views.DeleteMenuCategory, name='delete-menu-category'),

    #Room Category URLS
    path('list-room-category', views.ListRoomCategory.as_view(), name='list-room-category'),
    path('add-room-category', views.AddRoomCategory.as_view(), name='add-room-category'),
    path('update-room-category/<int:pk>', views.UpdateRoomCategory.as_view(), name='update-room-category'),
    path('delete-room-category/<int:pk>', views.DeleteRoomCategory, name='delete-room-category'),

    
    #Purchase Items URLS
    path('list-purchase-item', views.ListPurchaseItem.as_view(), name='list-purchase-item'),
    path('add-purchase-item', views.AddPurchaseItem.as_view(), name='add-purchase-item'),
    path('update-purchase-item/<int:pk>', views.UpdatePurchaseItem.as_view(), name='update-purchase-item'),
    path('delete-purchase-item/<int:pk>', views.DeletePurchaseItem, name='delete-purchase-item'),

    #Menu Items URLS
    path('list-menu-item', views.ListMenuItem.as_view(), name='list-menu-item'),
    path('add-menu-item', views.AddMenuItem.as_view(), name='add-menu-item'),
    path('update-menu-item/<int:pk>', views.UpdateMenuItem.as_view(), name='update-menu-item'),
    path('delete-menu-item/<int:pk>', views.DeleteMenuItem, name='delete-menu-item'),
]