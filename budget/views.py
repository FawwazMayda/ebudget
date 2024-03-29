from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template import loader
from .models import Budget,Warga
from .forms import BudgetForm,WargaForm
#from .anomali import Anomali

# Create your views here
import os
print(os.listdir())
#An = Anomali()
def index(request):
    return render(request,"awal.html")
@csrf_exempt
def halaman_budget(request):
    if request.method=='GET':
        return JsonResponse({"msg":"Ini Budget"})
    print(request.headers)
    return JsonResponse({"MSG":"Ini Warga"})

def all_budget(request):
    budget_list = Budget.objects.all()
    context = { 'Budgets' : budget_list }
    return render(request,'budget_detail.html',context)

def all_warga(request):
    warga_list = Warga.objects.all()
    context ={ 'Wargas' : warga_list}
    return render(request, 'komentar_all.html', context)

def isi_budget(request):
    if request.method=='GET':
        form = BudgetForm().as_p()
        return render(request,'tambah_budget.html',{'form':form})
    else:
        form = BudgetForm(request.POST)
        if form.is_valid():
            nama_barang = form.cleaned_data['nama_barang']
            satuan = form.cleaned_data['satuan']
            harga = form.cleaned_data['harga']
            siswa = int(form.cleaned_data['inventaris_siswa'])
            guru = int(form.cleaned_data['inventaris_guru'])
            sekolah = int(form.cleaned_data['inventaris_sekolah'])
            #status = An.cek_nama(nama_barang) 
            #status = An.cek_harga(satuan,harga,siswa,guru,sekolah,0.4)
            status = "Preiksa Data"
            d = Budget(nama=nama_barang,harga=harga,satuan=satuan,status=status)
            d.save()
            #return HttpResponse("Form Diterima")
            return HttpResponseRedirect("/ebudget")
        else:
            return HttpResponse("Form gagal")



def isi_komentar(request):
    if request.method=='GET':
        form =  WargaForm().as_p()
        return render(request,'tambah_komentar.html',{'form':form})
    else:
        form=WargaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            komentar = form.cleaned_data['komentar']
            d = Warga(username=username,komentar=komentar)
            d.save()
            #return HttpResponse("Form Diterima")
            return HttpResponseRedirect("/ebudget")
        else:
            return HttpResponse("Form gagal")
