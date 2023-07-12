from django.shortcuts import render
from .models import Client, Receipt, Contract, Contract_Client
from .serializers import Client_Serializer,Receipt_Serializer
from .serializers import Contract_Serializer,Contract_Client_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.

def user_view(request, *args, **kwargs):
    if request.method == 'GET':
        users = Client.objects.all()
        serializer=Client_Serializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Client_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Receipt_view(request, *args, **kwargs):
    if request.method == 'GET':
        Receipts = Receipt.objects.all()
        serializer=Receipt_Serializer(Receipts,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Receipt_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Contract_view(request, *args, **kwargs):
    if request.method == 'GET':
        Contracts = Contract.objects.all()
        serializer=Contract_Serializer(Contracts,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Contract_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def Contract_Client_view(request, *args, **kwargs):
    if request.method == 'GET':
        Contract_Clients = Contract_Client.objects.all()
        serializer=Contract_Client_Serializer(Contract_Clients,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Contract_Client_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#def exit_Vehicle(request, plate):
    #receipt. .....
    #saca hora entrada
    #se saca la hora de salida
    