from .models import Client, Receipt, Contract, Contract_Client
from rest_framework import serializers

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= '__all__'

class Receipt_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Receipt
        fields= '__all__'

class Contract_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Contract
        fields= '__all__'

class Contract_Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Contract_Client
        fields= ['id', 'id_Contract', 'id_Client']