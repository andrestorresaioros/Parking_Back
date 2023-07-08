from .models import Client, Receipt, Contract, Contract_Client
from rest_framework import serializers

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= ['id', 'name', 'phone']
        #fields= '__all__'


