from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Vehicle.models import Vehicle

class Client(models.Model):
    name= models.CharField(max_length=200,default='')
    phone= models.CharField(max_length=200,default='')
    identification= models.CharField(max_length=200,default='')
    def __str__(self):
        return self.name

class Receipt(models.Model):
    id_Client= models.ForeignKey(Client, on_delete=models.CASCADE)
    id_Vehicle= models.ForeignKey(Vehicle, on_delete=models.CASCADE,
                                  related_name="Receipt_Vehicle",null=True)
    date_entry = models.TimeField(default=timezone.now)
    date_exit = models.TimeField(default=timezone.now, null=True,blank=True)
    ubication= models.CharField(max_length=200,default='')
    cost= models.CharField(max_length=200,default='',null=True,blank=True)
    def __str__(self):
        return str(self.id_Client) + " - " + str(self.id_Vehicle)

class Contract(models.Model):
    id_Admin= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date_entry = models.DateTimeField(default=timezone.now)
    date_exit = models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=200,default='')
    def __str__(self):
        return self.type

class Contract_Client(models.Model):
    id_Contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    id_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_Contract) + " - " + str(self.id_Client)