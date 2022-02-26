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

    def save(self, *args, **kwargs):
        # Stock Ledger
        stock = Stock.objects.filter(item_name=self.item).order_by('-id').first()
        if stock:
            qty = float(self.qty)
            totalBal = stock.stock_quantity+qty
        else:
            totalBal = self.qty
        super(PurchaseDetails, self).save(*args, **kwargs)
        Stock.objects.create(
            item_name = self.item,
            purchase = self,
            issue =  None,
            receive_quantity = self.qty,
            issue_quantity = None,
            stock_quantity = totalBal,
        )

['issue_no','issue_to']
class IssueMaster(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    issue_no = models.CharField(max_length=100, unique=True, blank=False, null=False)
    issue_to = models.CharField(max_length=100 ,null=False, blank=False)

    def __str__(self) -> str:
        return str(self.issue_no)

class IssueDetails(TimeStamp):
    id = models.BigAutoField(primary_key=True)
    issue_main = models.ForeignKey(IssueMaster, on_delete=models.CASCADE)
    item = models.ForeignKey(PurchaseItems, on_delete=models.PROTECT)
    issue_qty = models.FloatField()

    def __str__(self) -> str:
        return str(self.item)

    def save(self, *args, **kwargs):
        # Stock Ledger
        stock = Stock.objects.filter(item_name=self.item).order_by('-id').first()
        if stock:
            qty = float(self.issue_qty)
            totalBal = stock.stock_quantity-qty
        else:
            pass
        super(IssueDetails, self).save(*args, **kwargs)
        Stock.objects.create(
            item_name = self.item,
            purchase = None,
            issue =  self,
            receive_quantity = None,
            issue_quantity = self.issue_qty,
            stock_quantity = totalBal,
        )
class Stock(TimeStamp):
    item_name = models.ForeignKey(PurchaseItems, on_delete=models.PROTECT)
    purchase = models.ForeignKey(PurchaseDetails, on_delete=models.PROTECT, default=0, null=True)
    issue = models.ForeignKey(IssueDetails, on_delete=models.PROTECT, default=0, null=True)
    receive_quantity = models.FloatField(default='0', blank=True, null=True)
    issue_quantity = models.FloatField(default='0', blank=True, null=True)
    stock_quantity = models.FloatField()

    def __str__(self):
	    return str(self.item_name)

