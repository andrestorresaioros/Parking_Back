from .models import Bill
from rest_framework import serializers

class bill_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bill
        fields= '__all__'