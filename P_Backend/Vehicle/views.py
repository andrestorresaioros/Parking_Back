from django.shortcuts import render
from .models import Vehicle
from .serializers import Vehicle_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.

def Vehicle_view(request, *args, **kwargs):
    if request.method == 'GET':
        Vehicles = Vehicle.objects.all()
        serializer=Vehicle_Serializer(Vehicles,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Vehicle_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def consult_Vehicle(request,plates):
        Vehicles = Vehicle.objects.filter(plate=plates)
        serializer=Vehicle_Serializer(Vehicles,many=True)
        return JsonResponse(serializer.data,safe=False)