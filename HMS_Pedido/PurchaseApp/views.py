from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from .models import Vendor, PurchaseMaster, PurchaseDetails, Stock, Vendor, IssueMaster, IssueDetails
from SettingsApp.models import PurchaseItems, Unit
# Create your views here.
class ListVendorView(LoginRequiredMixin ,ListView):
    model = Vendor
    template_name = "Purchase/list-vendor.html"
    paginate_by = 10

class CreateVendorView(LoginRequiredMixin ,SuccessMessageMixin, CreateView):
    model = Vendor
    success_message = 'Vendor Created Sucessfully !!!'
    fields = '__all__'
    template_name = "Purchase/add-vendor.html"

class UpdateVendorView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vendor
    success_message = 'Vendor Updated Successfully !!!'
    fields = '__all__'
    template_name = 'Purchase/update-vendor.html'

def DeleteVendorView(request, pk):
    object = Vendor.objects.get(pk=pk)
    name = object.name
    object.delete()
    messages.success(request, f'Vendor {name} Deleted Successfully')
    return HttpResponseRedirect(reverse('list-vendor'))
class ListPurchaseView(LoginRequiredMixin ,ListView):
    model = PurchaseMaster
    template_name = "Purchase/list-purchase.html"
    paginate_by = 10
class AddPurchaseView(View):
    def get(self, request, *args, **kwargs):
        vendors = Vendor.objects.all()
        purchaseItems = PurchaseItems.objects.filter(is_active=True)
        units = Unit.objects.filter(is_active=True)
        context ={
            'vendors':vendors,
            'purchaseItems': purchaseItems,
            'units': units,
        }
        return render(request, 'Purchase/add-purchase.html', context)

    def post(self, request, *args, **kwargs):
        ## Purchase Master ##
        invoice_no = request.POST.get('invoice-no')
        vendor_id = request.POST.get('vendor', '')
        grand_total = request.POST.get('grand-total')
        vendor = Vendor.objects.get(id=vendor_id)
        purchase_master = PurchaseMaster(invoice_no=invoice_no, vendor=vendor, total_bill=grand_total)
        purchase_master.save()

        ## Purchase Details ##
        purchase_item_id = request.POST.getlist('purchase-item[]')
        qty = request.POST.getlist('qty[]')
        unit_id = request.POST.getlist('unit[]')
        rate = request.POST.getlist('rate[]')
        total = request.POST.getlist('total[]')
        
        i=0
        for item in purchase_item_id:
            purchase_item = PurchaseItems.objects.get(id=item)
            unit = Unit.objects.get(id=unit_id[i])
            purchase_detail = PurchaseDetails(purchase_main=purchase_master, item=purchase_item, qty=qty[i], unit=unit, rate=rate[i], total=total[i])
            purchase_detail.save()
            i=i+1
        messages.success(request, 'Successfully Added !!!')
        return HttpResponseRedirect(reverse('list-purchase'))

def ViewPurchaseView(request, pk):
    if request.method == 'GET':
        purchaseObjects = PurchaseDetails.objects.filter(purchase_main=pk)
        purchaseMasterObjects = PurchaseMaster.objects.get(pk=pk)
        context = {
            'purchaseObjects': purchaseObjects,
            'purchaseMasterObjects': purchaseMasterObjects
        }
        return render(request, 'Purchase/view-purchase.html', context)

def DeletePurchaseView(request, pk):
    if request.method == 'GET':
        PurchaseMasterobject = PurchaseMaster.objects.get(pk=pk)
        PurchaseDetailobject = PurchaseDetails.objects.filter(purchase_main = pk)
        PurchaseMasterobject.delete()
        PurchaseDetailobject.delete()
        messages.success(request, 'Successfully Deleted')
        return HttpResponseRedirect(reverse('list-purchase'))

class ListIssueView(LoginRequiredMixin ,ListView):
    model = IssueMaster
    template_name = "Purchase/list-issue.html"
    paginate_by = 10

class AddIssueView(View):
    def get(self, request, *args, **kwargs):
        purchaseItems = PurchaseItems.objects.filter(is_active=True)
        units = Unit.objects.filter(is_active=True)
        context ={
            'purchaseItems': purchaseItems,
            'units': units,
        }
        return render(request, 'Purchase/add-issue.html', context)

    def post(self, request, *args, **kwargs):
        ## Purchase Master ##
        issue_no = request.POST.get('issue-no')
        issue_to = request.POST.get('issue-to')
        issue_master = IssueMaster(issue_no=issue_no, issue_to=issue_to)
        issue_master.save()

        ## Purchase Details ##
        issue_item_id = request.POST.getlist('issue-item[]')
        qty = request.POST.getlist('qty[]')
        
        i=0
        for item in issue_item_id:
            issue_item = PurchaseItems.objects.get(id=item)
            issue_detail = IssueDetails(
                issue_main=issue_master,
                item=issue_item,
                issue_qty=qty[i])
            issue_detail.save()
            i=i+1
        messages.success(request, 'Successfully Added !!!')
        return HttpResponseRedirect(reverse('list-issue'))

@require_http_methods(["GET"])
def DeleteIssueView(request, pk):
    obj1 = IssueMaster.objects.get(pk=pk)
    obj2 = IssueDetails.objects.filter(issue_main = pk)
    obj1.delete()
    obj2.delete()
    messages.success(request, 'Successfully Deleted')
    return HttpResponseRedirect(reverse('list-issue'))

def StockView(request):
    if request.method == 'GET':
        purchase_items = PurchaseItems.objects.filter(is_active=True)
        context = {
            'purchase_items': purchase_items
        }
        return render(request, 'Purchase/view-stock.html', context)
    if request.method == 'POST':
        purchase_items = PurchaseItems.objects.filter(is_active=True)
        search_item = request.POST.get('purchase-item')
        purchase_item = PurchaseItems.objects.get(pk=search_item)
        objects = Stock.objects.filter(item_name=purchase_item)
        context ={
            'objects':objects,
            'purchase_items': purchase_items
        }
        return render(request, 'Purchase/view-stock.html', context)


