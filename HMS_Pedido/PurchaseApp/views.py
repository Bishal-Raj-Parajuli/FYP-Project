from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Vendor, PurchaseMaster, PurchaseDetails
from SettingsApp.models import PurchaseItems, Unit
from .forms import PurchaseMasterForm
# Create your views here.


def ListPurchase(request):
    if request.method == 'GET':
        objects = PurchaseMaster.objects.all()
        context = {
            'objects': objects
        }
        return render(request, 'Purchase/List-purchase.html', context)

class AddPurchase(View):
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
        return HttpResponseRedirect(reverse('list-purchase'))

def ViewPurchase(request, pk):
    if request.method == 'GET':
        purchaseObjects = PurchaseDetails.objects.filter(purchase_main=pk)
        purchaseMasterObjects = PurchaseMaster.objects.get(pk=pk)
        context = {
            'purchaseObjects': purchaseObjects,
            'purchaseMasterObjects': purchaseMasterObjects
        }
        return render(request, 'Purchase/view-purchase.html', context)

def DeletePurchase(request, pk):
    if request.method == 'GET':
        PurchaseMasterobject = PurchaseMaster.objects.get(pk=pk)
        PurchaseDetailobject = PurchaseDetails.objects.filter(purchase_main = pk)
        PurchaseMasterobject.delete()
        PurchaseDetailobject.delete()
        context = {
            'message': 'Successfully Deleted !!!'
        }
        return HttpResponseRedirect(reverse('list-purchase'))