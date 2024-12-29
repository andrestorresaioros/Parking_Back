from django.db import models
from django.contrib.auth.models import User
from Parking.models import Parking

class Bill(models.Model):
    id_Admin= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id_Parking= models.ForeignKey(Parking, on_delete=models.CASCADE,null=True)
    values_Zone= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    values_Motos= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    values_Autos= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    values_Heavys= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    values_Day= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    values_Week= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    values_Month= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    values_Year= models.DecimalField(max_digits=1000, decimal_places=2, default=0)
    def __str__(self):
        return self.id_Parking.zone