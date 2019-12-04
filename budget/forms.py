from django import forms

class BudgetForm(forms.Form):
    nama_barang = forms.CharField(max_length=200)
    harga = forms.IntegerField()
    satuan = forms.IntegerField()

class WargaForm(forms.Form):
    username = forms.CharField(max_length=200)
    komentar = forms.CharField(max_length=800)