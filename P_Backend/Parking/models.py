from django.db import models

#from P_Backend.bill.models import Admin

class Parking(models.Model):
 #   id_Admin= models.ForeignKey(Admin, on_delete=models.CASCADE)
    zone= models.CharField(max_length=200,default='')
    quantity_space_moto= models.IntegerField(default=0)
    quantity_space_car= models.IntegerField(default=0)
    quantity_space_heavy= models.IntegerField(default=0)

class Space(models.Model):
    id_Parking= models.ForeignKey(Parking, on_delete=models.CASCADE)

class Type_Parking(models.Model):
    id_Parking= models.ForeignKey(Parking, on_delete=models.CASCADE)
    name= models.CharField(max_length=200, default='')
    