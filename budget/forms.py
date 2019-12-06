from django import forms

class BudgetForm(forms.Form):
    nama_barang = forms.CharField(max_length=200)
    harga = forms.IntegerField()
    satuan = forms.IntegerField()
    inventaris_siswa = forms.BooleanField(required=False)
    inventaris_guru = forms.BooleanField(required=False)
    inventaris_sekolah = forms.BooleanField(required=False)
    x = forms.BooleanField(required=False)

class WargaForm(forms.Form):
    username = forms.CharField(max_length=200)
    komentar = forms.CharField(max_length=800)
class MintaOTPForm(forms.Form):
    skpd = forms.CharField(max_length=200)
    nohp = forms.CharField(max_length=200)
class VerifOTPForm(forms.Form):
    otp = forms.CharField(max_length=200)