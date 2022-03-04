from socket import fromfd
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from SettingsApp.models import RoomCategory, RoomDetails

# Create your views here.
class ListDiningView(ListView):
    model = RoomCategory
    template_name = 'Sales/list-dining.html'

def ListDiningDetailsView(request, pk):
    queryset = RoomDetails.objects.filter(category=pk)
    context = {
        'objects':queryset
    }
    return render(request, 'Sales/list-dining-details.html', context)

class RoomBookingView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        return render(request, 'Sales/book-room.html')