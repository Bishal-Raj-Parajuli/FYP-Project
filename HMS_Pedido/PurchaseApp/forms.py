from django import forms
from .models import PurchaseMaster, PurchaseDetails

class PurchaseMasterForm(forms.ModelForm):
    #invoice_no = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control', "placeholder":"Invoice No"}))
    class Meta:
        model = PurchaseMaster
        fields = ['invoice_no', 'vendor'] 