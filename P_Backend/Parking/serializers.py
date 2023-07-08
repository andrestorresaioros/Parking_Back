from .models import Parking, Space, Type_Parking
from rest_framework import serializers

class Parking_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Parking
        fields= '__all__'

class Space_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Space
        fields= '__all__'

class Type_Parking_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Type_Parking
        fields= '__all__'