from django.db import models

class Parking(models.Model):
    zone= models.CharField(max_length=200,default='')
    quantity_space_moto= models.IntegerField(default=0)
    quantity_space_car= models.IntegerField(default=0)
    quantity_space_heavy= models.IntegerField(default=0)

class Space(models.Model):
    id_Parking= models.ForeignKey(Parking, on_delete=models.CASCADE)