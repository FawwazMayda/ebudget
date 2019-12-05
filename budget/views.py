from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template import loader
from .models import Budget,Warga
from .forms import BudgetForm,WargaForm,MintaOTPForm,VerifOTPForm
from .otp import makeOTP,verifyOTP,setPhone
#from .anomali import Anomali

# Create your views here
import os
print(os.listdir())
key=21
#An = Anomali()
def index(request):
    return render(request,"landing_page.html")

def login_pegawai(request):
    if request.method=='GET':
        #Minta halaman Login
        form = MintaOTPForm()
        context = {'form':form}
        return render(request,'login_pegawai.html',context)
    else:
        form = MintaOTPForm(request.POST)
        if form.is_valid():
            form2 = VerifOTPForm()
            context2 = {'form':form2}
            skpd = form.cleaned_data['skpd']
            nohp = form.cleaned_data['nohp']
            setPhone(nohp)
            res0 = makeOTP(key)
            print(res0.json())
            return render(request,'login_pegawai_otp.html',context2)

def login_pegawai_otp(request):
    if request.method=='POST':
        form = VerifOTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            res1 = verifyOTP(key,otp).json()
            print(res1)
            if res1['status']==True:
                return HttpResponseRedirect("/ebudget/indexadmin")
            else:
                return HttpResponseRedirect("/ebudget/")


def indexadmin(request):
    return render(request,'indexadmin.html')


def kegiatan(request):
    budget_list = Budget.objects.all()
    context = {'Budgets':budget_list}
    return render(request,'kegiatan.html',context)


def inputanggaran(request):
    if request.method=='GET':
        form = BudgetForm().as_p()
        context = {'form':form}
        return render(request, 'inputanggaran.html',context)
    else:
        form = BudgetForm(request.POST)
        if form.is_valid():
            nama_barang = form.cleaned_data['nama_barang']
            satuan = form.cleaned_data['satuan']
            harga = form.cleaned_data['harga']
            #siswa = int(form.cleaned_data['inventaris_siswa'])
            #guru = int(form.cleaned_data['inventaris_guru'])
            #sekolah = int(form.cleaned_data['inventaris_sekolah'])
            #status = An.cek_nama(nama_barang) 
            #status = An.cek_harga(satuan,harga,siswa,guru,sekolah,0.4)
            status = "Preiksa Data"
            d = Budget(nama=nama_barang,harga=harga,satuan=satuan,status=status)
            d.save()
            #return HttpResponse("Form Diterima")
            return HttpResponseRedirect("/ebudget/indexadmin")

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
