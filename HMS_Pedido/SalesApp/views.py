from socket import fromfd
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from SettingsApp.models import RoomCategory, RoomDetails

# Create your views here.
class ListDining(ListView):
    model = RoomCategory
    template_name = 'Sales/list-dining.html'

def ListDiningDetails(request, pk):
    queryset = RoomDetails.objects.filter(category=pk)
    context = {
        'objects':queryset
    }
    return render(request, 'Sales/list-dining-details.html', context)