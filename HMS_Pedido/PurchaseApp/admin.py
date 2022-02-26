from csv import list_dialects
from django.contrib import admin
from .models import IssueDetails, IssueMaster, PurchaseDetails, PurchaseMaster, Stock, Vendor

# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone']

@admin.register(PurchaseMaster)
class PurchaseMasterAdmin(admin.ModelAdmin):
    list_display = ['invoice_no','vendor','total_bill']   

@admin.register(PurchaseDetails)
class PurchaseDetailsAdmin(admin.ModelAdmin):
    list_display = ['purchase_main','item','qty','unit','rate','total'] 

@admin.register(IssueMaster)
class IssueMasterAdmin(admin.ModelAdmin):
    list_display = ['issue_no','issue_to']

@admin.register(IssueDetails)
class IssueDetailsAdmin(admin.ModelAdmin):
    list_display = ['item','issue_qty']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['item_name','purchase','issue','receive_quantity','issue_quantity','stock_quantity']

