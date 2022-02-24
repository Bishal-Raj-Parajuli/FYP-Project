from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        invoice_no = request.POST['invoice-no']
        vendor_id = request.POST['vendor']
        if invoice_no == '':
            context = {
                'message': 'Invoice No. is Required !!!'
            }
            return render(request, 'Purchase/add-purchase.html', context)
        vendor = Vendor.objects.get(id=vendor_id)
        total_bill = 2000
        purchase_master = PurchaseMaster(invoice_no=invoice_no, vendor=vendor, total_bill=total_bill)
        purchase_master.save()

        ### TODO SAVE PURCHASE ITEMS IN PURCHASE DETAILS ###
        purchase_id = PurchaseMaster.objects.get(invoice_no=invoice_no)
        
        return HttpResponse("Done")
        