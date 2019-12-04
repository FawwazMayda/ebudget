from django import forms

class BudgetForm(forms.Form):
    nama_barang = forms.CharField(max_length=200)
    harga = forms.IntegerField()
    satuan = forms.IntegerField()