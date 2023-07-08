from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Client(models.Model):
    name= models.CharField(max_length=200,default='')
    phone= models.CharField(max_length=200,default='')

class Receipt(models.Model):
    id_Client= models.ForeignKey(Client, on_delete=models.CASCADE)
    date_entry = models.DateTimeField(default=timezone.now)
    date_exit = models.DateTimeField(default=timezone.now)
    ubication= models.CharField(max_length=200,default='')
    #t_contract= models.CharField(max_length=200,default='')

class Contract(models.Model):
    id_Admin= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date_entry = models.DateTimeField(default=timezone.now)
    date_exit = models.DateTimeField(default=timezone.now)
    cost= models.CharField(max_length=200,default='')
    type= models.CharField(max_length=200,default='')

class Contract_Client(models.Model):
    id_Contract= models.ForeignKey(Contract, on_delete=models.CASCADE)
    id_Client= models.ForeignKey(Client, on_delete=models.CASCADE)