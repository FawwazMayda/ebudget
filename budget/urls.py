from django.urls import path
from . import views

urlpatterns = [
    path('',views.halaman_budget,name='index'),
    path('budget_detail/',views.all_budget,name='all_budget'),
    path('warga_detail/',views.all_warga,name='all_warga')

]