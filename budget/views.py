from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Budget,Warga
from .forms import BudgetForm

# Create your views here.
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
            d = Budget(nama=nama_barang,harga=harga,satuan=satuan)
            d.save()
            return HttpResponse("Form Diterima")
        else:
            return HttpResponse("Form gagal")