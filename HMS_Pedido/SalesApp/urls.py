from django.urls import path
from .views import ListDining, ListDiningDetails

urlpatterns = [
    path('list-dining', ListDining.as_view(), name='list-dining'),
    path('list-dining/<int:pk>', ListDiningDetails, name='list-dining-details'),
]