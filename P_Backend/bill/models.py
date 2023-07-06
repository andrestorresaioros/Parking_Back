from django.utils import timezone
from django.db import models

class Bill(models.Model):
    id_Bill= models.AutoField(primary_key=True)
    date_Entry = models.DateTimeField(default=timezone.now)
    date_Exit = models.DateTimeField(default=timezone.now)
    zone= models.CharField(max_length=200,default='')
    t_Contract= models.CharField(max_length=200,default='')

class Admin(models.Model):
    id_Admin= models.AutoField(primary_key=True)
    user= models.CharField(max_length=200,default='')
    password= models.CharField(max_length=200,default='')

