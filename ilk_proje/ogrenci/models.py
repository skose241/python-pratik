from django.db import models

class Ogrenci(models.Model):
    ad=models.CharField(max_length=30)
    puan=models.IntegerField()

    def __str__(self):
        return self.ad