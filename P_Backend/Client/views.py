from django.shortcuts import render
from .models import Client, Receipt, Contract, Contract_Client
from .serializers import Client_Serializer,Receipt_Serializer
from .serializers import Contract_Serializer,Contract_Client_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from datetime import datetime
from Vehicle.models import Vehicle
from Parking.models import Parking
from bill.models import Bill

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
            #request data se tiene id parking type vehicle 
            if 'id_Contract' in request_data and 'id_Vehicle' in request_data:
                contract_id = request_data['id_Contract']
                vehicle_id = request_data['id_Vehicle']
                if contract_id['type'] == 'Minuto':
                    try:
                        contract = Contract.objects.get(id=contract_id)
                        vehicle = Vehicle.objects.get(id=vehicle_id)
                        parking = Parking.objects.get(id=vehicle.id_Parking)

                        entry_time = datetime.strptime(request_data['date_entry'], '%Y-%m-%dT%H:%M:%S')
                        exit_time = datetime.strptime(request_data['date_exit'], '%Y-%m-%dT%H:%M:%S')
                        minutes = (exit_time - entry_time).total_seconds() // 60

                        if vehicle.type == 'Automóvil':
                            cost_per_minute = float(parking.values_Zone) * float(parking.values_Autos)
                        elif vehicle.type == 'Motocicleta':
                            cost_per_minute = float(parking.values_Zone) * float(parking.values_Motos)
                        elif vehicle.type == 'Vehículos Pesados':
                            cost_per_minute = float(parking.values_Zone) * float(parking.values_Heavys)

                        cost = str(cost_per_minute * minutes)
                        serializer.instance.cost = cost
                        serializer.save()
                    except (Contract.DoesNotExist, Vehicle.DoesNotExist, Parking.DoesNotExist):
                        pass

                elif contract_id['type'] in ['Día', 'Semana', 'Mes', 'Año']:
                    try:
                        contract = Contract.objects.get(id=contract_id)
                        bill = Bill.objects.get(id_Parking=vehicle.id_Parking)

                        if contract.type == 'Día':
                            cost = bill.values_Day
                        elif contract.type == 'Semana':
                            cost = bill.values_Week
                        elif contract.type == 'Mes':
                            cost = bill.values_Month
                        elif contract.type == 'Año':
                            cost = bill.values_Year

                        serializer.instance.cost = cost
                        serializer.save()
                    except (Contract.DoesNotExist, Bill.DoesNotExist):
                        pass
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