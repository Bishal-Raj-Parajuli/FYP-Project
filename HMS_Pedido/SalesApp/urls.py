from django.urls import path
from .views import ListDiningView, ListDiningDetailsView, RoomBookingView, ListGenerateBillView, OrderItemView

urlpatterns = [
    path('list-dining', ListDiningView.as_view(), name='list-dining'),
    path('list-dining/<int:pk>', ListDiningDetailsView, name='list-dining-details'),
    path('book-room/<int:pk>', RoomBookingView.as_view(), name='book-room'),
    path('list-generate-bill', ListGenerateBillView, name='list-generate-bill'),
    path('order-item/<int:pk>', OrderItemView, name='order-item')
]