from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from SettingsApp.models import PurchaseItemsCategory, PurchaseItems
# Create your views here.

class ListPurchaseCategory(LoginRequiredMixin, ListView):
    model = PurchaseItemsCategory
    template_name = 'Settings/Category/list-purchase-category.html'
    paginate_by = 10

class AddPurchaseCategory(LoginRequiredMixin ,SuccessMessageMixin, CreateView):
    model = PurchaseItemsCategory
    success_message = 'New Category Created Sucessfully !!!'
    fields = '__all__'
    template_name = 'Settings/Category/add-purchase-category.html'

class UpdatePurchaseCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PurchaseItemsCategory
    success_message = 'Category Updated Successfully !!!'
    fields = '__all__'
    template_name = 'Settings/Category/update-purchase-category.html'

def DeletePurchaseCategory(request, pk):
    object = PurchaseItemsCategory.objects.get(pk=pk)
    name = object.category_name
    object.delete()
    messages.success(request, f'PurchaseItemsCategory {name} Deleted Successfully')
    return HttpResponseRedirect(reverse('list-purchase-category'))

class ListPurchaseItem(LoginRequiredMixin, ListView):
    model = PurchaseItems
    template_name = 'Settings/Items/list-purchase-item.html'
    paginate_by = 10

class AddPurchaseItem(LoginRequiredMixin ,SuccessMessageMixin, CreateView):
    model = PurchaseItems
    success_message = 'New Item Created Sucessfully !!!'
    fields = '__all__'
    template_name = 'Settings/Items/add-purchase-item.html'

class UpdatePurchaseItem(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PurchaseItems
    success_message = 'Item Updated Successfully !!!'
    fields = '__all__'
    template_name = 'Settings/Items/update-purchase-item.html'

def DeletePurchaseItem(request, pk):
    object = PurchaseItems.objects.get(pk=pk)
    name = object.name
    object.delete()
    messages.success(request, f'Purchase Item {name} Deleted Successfully')
    return HttpResponseRedirect(reverse('list-purchase-item'))




    
