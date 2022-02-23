import imp
from django.shortcuts import render
from django.views import View
from .models import Vendor, PurchaseMaster, PurchaseDetails
# Create your views here.


def ListPurchase(request):
    if request.method == 'GET':
        objects = PurchaseMaster.objects.all()
        context = {
            'objects': objects
        }
        return render(request, 'Purchase/List-purchase.html', context)