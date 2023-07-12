from .models import Parking
from rest_framework import serializers

class Parking_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Parking
        fields= '__all__'