from django.db import models
from django.contrib.auth.models import User
from Parking.models import Parking

class Bill(models.Model):
    id_Admin= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id_Parking= models.ForeignKey(Parking, on_delete=models.CASCADE,null=True)
    values_Zone= models.CharField(max_length=200,default='')
    values_Motos= models.CharField(max_length=200,default='')
    values_Autos= models.CharField(max_length=200,default='')
    values_Heavys= models.CharField(max_length=200,default='')
    values_Day= models.CharField(max_length=200,default='')
    values_Week= models.CharField(max_length=200,default='')
    values_Month= models.CharField(max_length=200,default='')
    values_Year= models.CharField(max_length=200,default='')
    def __str__(self):
        return self.id_Parking.zone