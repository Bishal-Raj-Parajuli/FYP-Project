from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Customer, RoomBooking
from SettingsApp.models import RoomCategory, RoomDetails

# Create your views here.
class ListCustomerView(LoginRequiredMixin ,ListView):
    model = Customer
    template_name = "Sales/list-customer.html"
    paginate_by = 10

class CreateCustomerView(LoginRequiredMixin ,SuccessMessageMixin, CreateView):
    model = Customer
    success_message = 'Customer Created Sucessfully !!!'
    fields = '__all__'
    template_name = "Sales/add-customer.html"

class UpdateCustomerView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    success_message = 'Customer Updated Successfully !!!'
    fields = '__all__'
    template_name = 'Sales/update-customer.html'

def DeleteCustomerView(request, pk):
    object = Customer.objects.get(pk=pk)
    name = object.name
    object.delete()
    messages.success(request, f'Customer {name} Deleted Successfully')
    return HttpResponseRedirect(reverse('list-customer'))

class ListDiningView(ListView):
    model = RoomCategory
    template_name = 'Sales/list-dining.html'

def ListDiningDetailsView(request, pk):
    queryset = RoomDetails.objects.filter(category=pk)
    booked_rooms = []
    for query in queryset:
        bookings = query.room_booking.filter(paid=False)
        for booking in bookings:
            booked_rooms.append(booking.room)
    context = {
        'objects':queryset,
        'booked_rooms': booked_rooms
    }
    return render(request, 'Sales/list-dining-details.html', context)

class RoomBookingView(View):
    def get(self, request, *args, **kwargs):
        room = RoomDetails.objects.get(pk=kwargs['pk'])
        customer = Customer.objects.all()
        context ={
            'room':room,
            'customers':customer
        }
        return render(request, 'Sales/book-room.html', context)
    
    def post(self, request, *args, **kwargs):
        room_id = kwargs['pk']
        room = RoomDetails.objects.get(pk=room_id)
        customer_id = request.POST.get('customer')
        customer = Customer.objects.get(pk=customer_id)
        days = float(request.POST.get('days'))
        rate = float(request.POST.get('rate'))
        room_booking = RoomBooking(room=room, rate=rate, days=days, customer=customer, paid=False)
        room_booking.save()
        return HttpResponse('Success')

def ListGenerateBillView(request):
    if request.method == 'GET':
        objects = RoomBooking.objects.filter(paid=False)
        context = {
            'objects': objects
        }
        return render(request, 'Sales/list-generate-bill.html', context)

    
def OrderItemView(request, pk):
    if request.method == 'GET':
        return render(request, 'Sales/order-item.html')

