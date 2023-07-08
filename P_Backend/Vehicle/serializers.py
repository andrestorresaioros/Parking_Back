from .models import Vehicle
from rest_framework import serializers

class Vehicle_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Vehicle
        fields= '__all__'