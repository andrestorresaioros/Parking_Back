from django.contrib import admin
from .models import Client, Receipt, Contract, Contract_Client

# Register your models here.
admin.site.register(Contract_Client)
admin.site.register(Client)
admin.site.register(Receipt)
admin.site.register(Contract)