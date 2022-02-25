from csv import list_dialects
from django.contrib import admin
from .models import IssueDetails, PurchaseDetails, PurchaseMaster, Stock, Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone']

class PurchaseMasterAdmin(admin.ModelAdmin):
    list_display = ['invoice_no','vendor','total_bill']   

class PurchaseDetailsAdmin(admin.ModelAdmin):
    list_display = ['purchase_main','item','qty','unit','rate','total'] 

class IssueDetailsAdmin(admin.ModelAdmin):
    list_display = ['item','issue_qty']

class StockAdmin(admin.ModelAdmin):
    list_display = ['item_name','purchase','issue','receive_quantity','issue_quantity','stock_quantity']

admin.site.register(PurchaseDetails, PurchaseDetailsAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseMaster, PurchaseMasterAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(IssueDetails, IssueDetailsAdmin)
