from unicodedata import name
from django.urls import path
from .views import AddPurchaseView, DeletePurchaseView, ListPurchaseView,StockView, ViewPurchaseView, ListIssueView, ListVendorView

urlpatterns = [
    #Vendor Urls
    path('list-vendor', ListVendorView.as_view(), name='list-vendor'),

    #Purchase URLS
    path('list-purchase', ListPurchaseView.as_view(), name='list-purchase'),
    path('add-purchase', AddPurchaseView.as_view(), name='add-purchase'),
    path('view-purchase/<int:pk>', ViewPurchaseView, name='view-purchase' ),
    path('delete-purchase/<int:pk>', DeletePurchaseView, name='delete-purchase'),

    #Issue Urls
    path('list-issue', ListIssueView, name='list-issue'),
    
    path('view-stock', StockView, name='view-stock'),
]