from django.urls import path
from . import views

urlpatterns = [
    path('',views.halaman_budget,name='index'),
    path('budget_detail/',views.all_budget,name='all_budget'),
    path('warga_detail/',views.all_warga,name='all_warga'),
    path('tambah_budget/',views.isi_budget,name='isi_budget'),
    path('tambah_komentar/',views.isi_komentar,name='isi_komentar')

]