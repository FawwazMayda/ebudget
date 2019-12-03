from django.urls import path
from . import views

urlpatterns = [
    path('',views.halaman_budget,name='index'),
    path('budget_detail/<int:budget_id>',views.detail_budget,name='detail_budget')

]