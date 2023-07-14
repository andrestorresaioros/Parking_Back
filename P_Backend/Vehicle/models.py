from django.db import models

from Parking.models import Parking

# Create your models here.
class Vehicle(models.Model):
    id_Parking= models.ForeignKey(Parking, on_delete=models.CASCADE,null=True)
    color= models.CharField(max_length=200,default='',null=True,blank=True)
    plate= models.CharField(max_length=200,default='')
    brand= models.CharField(max_length=200,default='',null=True,blank=True)
    model= models.CharField(max_length=200,default='',null=True,blank=True)
    type= models.CharField(max_length=200,default='')
    def __str__(self):
        return self.plate