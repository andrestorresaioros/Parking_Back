from .models import Vehicle
from rest_framework import serializers
from Client.serializers import Receipt_Serializer

class Vehicle_Serializer(serializers.ModelSerializer):
    Receipt_Vehicle = Receipt_Serializer(many=True)
    class Meta:
        model= Vehicle
        fields= '__all__'