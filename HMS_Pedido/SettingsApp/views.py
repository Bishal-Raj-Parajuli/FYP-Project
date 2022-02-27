from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.db.models import Q
from SettingsApp.models import PurchaseItemsCategory, PurchaseItems, MenuCategory, MenuItems

### Purchase Category Views ###
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
### Purchase Category Views ###

### Purchase Items Views ###
class ListPurchaseItem(LoginRequiredMixin, ListView):
    model = PurchaseItems
    template_name = 'Settings/Items/list-purchase-item.html'
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by = self.request.GET.get("orderby","category")
        if filter_val != "":
            obj = PurchaseItems.objects.filter(Q(name__contains=filter_val)).order_by(order_by)
        elif order_by == "":
            obj = PurchaseItems.objects.all()
        else:
            obj = PurchaseItems.objects.all().order_by(order_by)
        return obj

    
    def get_context_data(self, **kwargs):
        context = super(ListPurchaseItem, self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","")
        context["all_table_fields"]=PurchaseItems._meta.get_fields()
        return context

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
### Purchase Items Views ###

### Menu Category Views ###
class ListMenuCategory(LoginRequiredMixin, ListView):
    model = MenuCategory
    template_name = 'Settings/Category/list-menu-category.html'
    paginate_by = 10

class AddMenuCategory(LoginRequiredMixin ,SuccessMessageMixin, CreateView):
    model = MenuCategory
    success_message = 'New Category Created Sucessfully !!!'
    fields = '__all__'
    template_name = 'Settings/Category/add-menu-category.html'

class UpdateMenuCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MenuCategory
    success_message = 'Category Updated Successfully !!!'
    fields = '__all__'
    template_name = 'Settings/Category/update-menu-category.html'

def DeleteMenuCategory(request, pk):
    object = MenuCategory.objects.get(pk=pk)
    name = object.category_name
    object.delete()
    messages.success(request, f'{name} Deleted Successfully')
    return HttpResponseRedirect(reverse('list-menu-category'))
### Menu Category Views ###

### Menu Items Views ###
class ListMenuItem(LoginRequiredMixin, ListView):
    model = MenuItems
    template_name = 'Settings/Items/list-menu-item.html'
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by = self.request.GET.get("orderby","category")
        if filter_val != "":
            obj = MenuItems.objects.filter(Q(name__contains=filter_val)).order_by(order_by)
        elif order_by == "":
            obj = MenuItems.objects.all()
        else:
            obj = MenuItems.objects.all().order_by(order_by)
        return obj

    
    def get_context_data(self, **kwargs):
        context = super(ListMenuItem, self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","")
        context["all_table_fields"]=MenuItems._meta.get_fields()
        return context

class AddMenuItem(LoginRequiredMixin ,SuccessMessageMixin, CreateView):
    model = MenuItems
    success_message = 'New Item Created Sucessfully !!!'
    fields = '__all__'
    template_name = 'Settings/Items/add-menu-item.html'

class UpdateMenuItem(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MenuItems
    success_message = 'Item Updated Successfully !!!'
    fields = '__all__'
    template_name = 'Settings/Items/update-menu-item.html'

def DeleteMenuItem(request, pk):
    object = MenuItems.objects.get(pk=pk)
    name = object.name
    object.delete()
    messages.success(request, f'Menu Item {name} Deleted Successfully')
    return HttpResponseRedirect(reverse('list-menu-item'))
### Menu Items Views ###

### Room Category Views ###
##TODO
### Room Category Views ###

### Room Details Views ###
##TODO
### Room Details Views ###



    
