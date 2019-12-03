from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Budget,Warga

# Create your views here.
def halaman_budget(request):
    return HttpResponse("Ini Budget KU")

def all_budget(request):
    budget_list = Budget.objects.all()
    print("HEYY SINIII")
    print(budget_list)
    template = loader.get_template("budget_detail.html")
    context = {
        'Budgets' : budget_list
    }
    return HttpResponse(template.render(context,request))

def all_warga(request):
    warga_list = Warga.objects.all()
    context ={ 'Wargas' : warga_list}
    return render(request, 'komentar_all.html', context)