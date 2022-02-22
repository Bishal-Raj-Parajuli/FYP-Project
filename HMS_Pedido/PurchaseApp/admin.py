from django.contrib import admin
from .models import PurchaseDetails, PurchaseMaster, Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone']

class PurchaseMasterAdmin(admin.ModelAdmin):
    list_display = ['invoice_no','vendor','total_bill']   

class PurchaseDetailsAdmin(admin.ModelAdmin):
    list_display = ['purchase_main','item','qty','unit','rate','total']   

admin.site.register(PurchaseDetails, PurchaseDetailsAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseMaster, PurchaseMasterAdmin)