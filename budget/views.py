from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print("ABANG OH BOLA")
    return HttpResponse("Ini Budget KU")