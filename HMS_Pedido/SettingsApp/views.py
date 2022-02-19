from django.shortcuts import render, redirect
from SettingsApp.models import PurchaseItemsCategory
# Create your views here.

def ListPurchaseCategory(request):
    if request.method == 'POST':
        search = request.POST['list-search']
        objects = PurchaseItemsCategory.objects.filter(category_name__contains=search)
        context = {
            'objects':objects
        }
        return render(request, 'Settings/Category/list-purchase-category.html', context)
    else:
        objects = PurchaseItemsCategory.objects.all()
        context = {
            'objects': objects
        }
        return render(request, 'Settings/Category/list-purchase-category.html', context)
