from unicodedata import name
from django.urls import path
from .views import AddPurchaseView, DeletePurchaseView, ListPurchaseView,StockView, ViewPurchaseView, ListIssueView, ListVendorView, CreateVendorView, UpdateVendorView, DeleteVendorView, AddIssueView, DeleteIssueView

urlpatterns = [
    #Vendor Urls
    path('list-vendor', ListVendorView.as_view(), name='list-vendor'),
    path('create-vendor', CreateVendorView.as_view(), name='create-vendor'),
    path('update-vendor/<int:pk>', UpdateVendorView.as_view(), name='update-vendor'),
    path('delete-vendor/<int:pk>', DeleteVendorView, name='delete-vendor'),

    #Purchase URLS
    path('list-purchase', ListPurchaseView.as_view(), name='list-purchase'),
    path('add-purchase', AddPurchaseView.as_view(), name='add-purchase'),
    path('view-purchase/<int:pk>', ViewPurchaseView, name='view-purchase' ),
    path('delete-purchase/<int:pk>', DeletePurchaseView, name='delete-purchase'),

    #Issue Urls
    path('list-issue', ListIssueView.as_view() , name='list-issue'),
    path('add-issue', AddIssueView.as_view(), name='add-issue'),
    path('delete-issue/<int:pk>', DeleteIssueView, name='delete-issue'),

    path('view-stock', StockView, name='view-stock'),
]