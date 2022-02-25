from django.db import models
from SettingsApp.models import PurchaseItems, TimeStamp, Unit

# Create your models here.
class Vendor(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Vendor Details'


class PurchaseMaster(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    invoice_no = models.CharField(max_length=100, unique=True, blank=False, null=False)
    vendor = models.ForeignKey(Vendor, default='', on_delete=models.SET_DEFAULT, null=False, blank=False)
    total_bill = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Purchase Master'

class PurchaseDetails(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    purchase_main = models.ForeignKey(PurchaseMaster, on_delete=models.CASCADE)
    item = models.ForeignKey(PurchaseItems, on_delete=models.PROTECT)
    qty = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    rate = models.FloatField()
    total = models.FloatField(editable=False, default=0)

    def __str__(self) -> str:
        return str(self.purchase_main)

    class Meta:
        verbose_name_plural = 'Purchase Details'

['item_name','stock_quantity','receive_quantity','issue_quantity','issue_to','reorder_level','created_at']
class Stock(TimeStamp):
    item_name = models.OneToOneField(PurchaseItems, on_delete=models.PROTECT)
    stock_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)

    def __str__(self):
	    return str(self.item_name)

