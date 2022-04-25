from django.urls import path
from .views import ListDiningView, ListDiningDetailsView, RoomBookingView, ListGenerateBillView, OrderItemView, ListCustomerView, CreateCustomerView, UpdateCustomerView, DeleteCustomerView, GenerateBill, SalesReport

urlpatterns = [
    # Customer URLS
    path('list-customer', ListCustomerView.as_view(), name='list-customer'),
    path('create-customer', CreateCustomerView.as_view(), name='create-customer'),
    path('update-customer/<int:pk>', UpdateCustomerView.as_view(), name='update-customer'),
    path('delete-customer/<int:pk>', DeleteCustomerView, name='delete-customer'),

    path('list-dining', ListDiningView.as_view(), name='list-dining'),
    path('list-dining/<int:pk>', ListDiningDetailsView, name='list-dining-details'),
    path('book-room/<int:pk>', RoomBookingView.as_view(), name='book-room'),
    path('list-generate-bill', ListGenerateBillView, name='list-generate-bill'),
    path('order-item/<int:pk>', OrderItemView, name='order-item'),
    path('generate-bill/<int:pk>', GenerateBill, name='generate-bill' ),
    path('sales-report', SalesReport, name='sales-report')
    #path('update-order-item/<int:pk>', OrderItemView, name='update-order-item')
]