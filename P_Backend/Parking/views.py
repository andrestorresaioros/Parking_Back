from django.shortcuts import render
from .models import Parking, Space, Type_Parking
from .serializers import Parking_Serializer,Space_Serializer
from .serializers import Type_Parking_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.

def Parking_view(request, *args, **kwargs):
    if request.method == 'GET':
        Parkings = Parking.objects.all()
        serializer=Parking_Serializer(Parkings,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Parking_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Space_view(request, *args, **kwargs):
    if request.method == 'GET':
        Spaces = Space.objects.all()
        serializer=Space_Serializer(Spaces,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Space_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Type_Parking_view(request, *args, **kwargs):
    if request.method == 'GET':
        Type_Parkings = Type_Parking.objects.all()
        serializer=Type_Parking_Serializer(Type_Parkings,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Type_Parking_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
