from django.db import models

# Create your models here.
class Budget(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.IntegerField()
    satuan = models.IntegerField()
    status = models.CharField(max_length=50,default="----")

    def __str__(self):
        return "{nama} {harga} {satuan}".format(nama=self.nama,harga=self.harga,satuan=self.satuan)
    def total(self):
        return self.satuan*self.harga

class Warga(models.Model):
    username = models.CharField(max_length=200)
    komentar = models.CharField(max_length=800)

    def __str__(self):
        return self.komentar