from django.db import models
from django.contrib.auth.models import User

class Parking(models.Model):
    id_Admin= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    zone= models.CharField(max_length=200,default='')
    quantity_space_moto= models.IntegerField(default=0)
    quantity_space_car= models.IntegerField(default=0)
    quantity_space_heavy= models.IntegerField(default=0)
    def __str__(self):
        return self.zone