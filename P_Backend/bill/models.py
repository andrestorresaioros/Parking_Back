from django.utils import timezone
from django.db import models

class Admin(models.Model):
    user= models.CharField(max_length=200,default='')
    password= models.CharField(max_length=200,default='')

class Bill(models.Model):
   # id_Admin= models.ForeignKey(Admin, on_delete=models.CASCADE)
    date_entry = models.DateTimeField(default=timezone.now)
    date_exit = models.DateTimeField(default=timezone.now)
    zone= models.CharField(max_length=200,default='')
    t_contract= models.CharField(max_length=200,default='')