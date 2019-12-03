from django.db import models

# Create your models here.
class Budget(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.IntegerField()
    satuan = models.IntegerField()

class Warga(models.Model):
    username = models.CharField(max_length=200)
    komentar = models.CharField(max_length=800)