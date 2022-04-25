from multiprocessing import context
from tkinter import Menu
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

#from SalesApp.models import Customer, OrderDetails, OrderMaster, RoomBooking
from SalesApp.models import Customer, OrderDetails, OrderMaster, RoomBooking
from SettingsApp.models import RoomCategory, RoomDetails, MenuItems, Unit

# Create your views here.
class ListCustomerView(ListView):
    model = Customer
    template_name = "Sales/list-customer.html"
    paginate_by = 10

class CreateCustomerView(SuccessMessageMixin, CreateView):
    model = Customer
    success_message = 'Customer Created Sucessfully !!!'
    fields = '__all__'
    template_name = "Sales/add-customer.html"

class UpdateCustomerView(SuccessMessageMixin, UpdateView):
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
    booking_details = RoomBooking.objects.get(pk=pk)
    order_masters = OrderMaster.objects.filter(room=pk, paid=False)
    menu_items = MenuItems.objects.filter(is_active=True)
    unit = Unit.objects.filter(is_active=True)
    if request.method == 'GET':
        if order_masters:
            for order_master in order_masters:
                order_details = OrderDetails.objects.filter(order_master=order_master)
            context = {
                'menuitems' : menu_items,
                'units' : unit,
                'order_masters':order_masters,
                'bookingdetails':booking_details,
                'order_details': order_details
            }
            return render(request, 'Sales/update-order-item.html', context)
        else:
            context = {
                'menuitems' : menu_items,
                'units' : unit,
                'bookingdetails': booking_details,
            }
            return render(request, 'Sales/order-item.html', context)

    if request.method == "POST":
        ## Order Master ##
        if order_masters:
            order_item_id = request.POST.getlist('order-item[]')
            qty = request.POST.getlist('qty[]')
            total = request.POST.getlist('total[]')

            for order_master in order_masters:
                i=0
                for item in order_item_id:
                    order_item = MenuItems.objects.get(id=item)
                    order_details = OrderDetails.objects.filter(order_master=order_master.id, item=order_item)
                    for order_detail in order_details:
                        order_detail.qty = qty[i]
                        order_detail.amt = total[i]
                        order_detail.save()
                    i=i+1
            if request.POST.getlist('new-order-item[]'):
                new_order_item_id = request.POST.getlist('new-order-item[]')
                new_qty = request.POST.getlist('new-qty[]')
                new_unit_id = request.POST.getlist('new-unit[]')
                new_total = request.POST.getlist('new-total[]')

                i=0
                for item in new_order_item_id:
                    order_item = MenuItems.objects.get(id=item)
                    unit = Unit.objects.get(id=new_unit_id[i])
                    order_details = OrderDetails(order_master=order_master, item=order_item, qty=new_qty[i], unit=unit, amt=new_total[i])
                    order_details.save()
                    i=i+1

            room = booking_details
            grand_total = request.POST.get('grand-total')
            for order_master in order_masters:
                order_master.total_bill = grand_total
                order_master.save()
            messages.success(request, 'Successfully Added !!!')
            return HttpResponseRedirect(reverse('list-generate-bill'))

        else:
            room = booking_details
            grand_total = request.POST.get('grand-total')
            order_master = OrderMaster(room=room, total_bill=grand_total)
            order_master.save()

            ## Order Details ##
            order_item_id = request.POST.getlist('order-item[]')
            qty = request.POST.getlist('qty[]')
            unit_id = request.POST.getlist('unit[]')
            total = request.POST.getlist('total[]')
            
            i=0
            for item in order_item_id:
                order_item = MenuItems.objects.get(id=item)
                unit = Unit.objects.get(id=unit_id[i])
                order_details = OrderDetails(order_master=order_master, item=order_item, qty=qty[i], unit=unit, amt=total[i])
                order_details.save()
                i=i+1
            messages.success(request, 'Successfully Added !!!')
            return HttpResponseRedirect(reverse('list-generate-bill'))

def GenerateBill(request, pk):
    room_booking = RoomBooking.objects.get(pk=pk)
    order_master = OrderMaster.objects.get(room=room_booking)
    total = room_booking.days * room_booking.rate
    if request.method == 'GET':
        if room_booking.paid == False:
            room_booking.paid = True
            room_booking.save()
            order_masters = OrderMaster.objects.filter(room=room_booking, paid=False)
            for order_master in order_masters:
                order_master.paid = True
                order_master.save()
        context = {
            'room_booking': room_booking,
            'order_master': order_master,
            'order_details': OrderDetails.objects.filter(order_master=order_master),
            'total_room_bill': total,
            'grand_total': total + order_master.total_bill
        }
        return render(request, 'Sales/generate-bill.html', context)

def SalesReport(request):
    room_booking = RoomBooking.objects.filter(paid=True)
    order_master = OrderMaster.objects.filter(paid=True)
    context = {
        'room_booking': room_booking,
        'order_master': order_master,
    }
    return render(request, 'Sales/list-sales-report.html', context)