from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login_pegawai/',views.login_pegawai,name='login_pegawai'),
    path('login_pegawai_otp/',views.login_pegawai_otp,name='login_pegawai_otp'),
    path('indexadmin/',views.indexadmin,name='indexadmin'),
    path('kegiatan/',views.kegiatan,name='kegiatan'),
    path('inputanggaran/',views.inputanggaran,name='inputanggaran'),
    path('budget_detail/',views.all_budget,name='all_budget'),
    path('warga_detail/',views.all_warga,name='all_warga'),
    path('tambah_budget/',views.isi_budget,name='isi_budget'),
    path('tambah_komentar/',views.isi_komentar,name='isi_komentar')

]