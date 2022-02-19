from django.shortcuts import render, redirect
from SettingsApp.models import PurchaseItems
# Create your views here.

def ListPurchaseCategory(request):
    context = {
        'objects': PurchaseItems.objects.all()
    }
    return render(request, 'Settings/Category/list-purchase-category.html', context)
