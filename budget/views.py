from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Budget

# Create your views here.
def halaman_budget(request):
    return HttpResponse("Ini Budget KU")

def detail_budget(request,budget_id):
    budget_list = Budget.objects.all()
    print("HEYY SINIII")
    print(budget_list)
    template = loader.get_template("budget_detail.html")
    context = {
        'Budgets' : budget_list
    }
    return HttpResponse(template.render(context,request))
