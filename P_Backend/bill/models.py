from django.db import models

class Tarifa(models.Model):
    zona= models.CharField(max_length=200,default='')
