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
from dateutil.parser import parse as dateutil_parse


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
        request_data = JSONParser().parse(request)
        serializer = Receipt_Serializer(data=request_data)
        if serializer.is_valid():
            contract_type = request_data['type_Contract']
            vehicle_id = request_data['id_Vehicle']
            try:
                vehicle = Vehicle.objects.get(id=vehicle_id)
                parking = Parking.objects.get(id=vehicle.id_Parking.id)

                # Asignar cupo al vehículo
                spot_number = parking.get_next_available_spot_number(vehicle.type)
                if spot_number is None:
                    return JsonResponse({'message': 'No hay cupos disponibles para este tipo de vehículo'}, status=status.HTTP_400_BAD_REQUEST)
                entry_time = dateutil_parse(request_data['date_entry'])
                exit_time = dateutil_parse(request_data['date_exit'])
                minutes = (exit_time - entry_time).total_seconds() // 60

                if contract_type == 'Minuto':
                    try:
                        bill = Bill.objects.get(id_Parking=vehicle.id_Parking)
                        if vehicle.type.strip() == 'Automóvil':
                            cost_per_minute = (float(bill.values_Zone) * float(bill.values_Autos) + 1)
                        elif vehicle.type == 'Motocicleta':
                            cost_per_minute = float(bill.values_Zone) * float(bill.values_Motos)
                        elif vehicle.type == 'Vehículos Pesados':
                            cost_per_minute = float(bill.values_Zone) * float(bill.values_Heavys)
                        cost = cost_per_minute * (minutes + 1)
                    except Exception as e:
                        print("Error al calcular el costo:", e)
                        pass
                elif contract_type in ['Día', 'Semana', 'Mes', 'Año']:
                    try:
                        bill = Bill.objects.get(id_Parking=vehicle.id_Parking)
                        if contract_type == 'Día':
                            cost = bill.values_Day
                        elif contract_type == 'Semana':
                            cost = bill.values_Week
                        elif contract_type == 'Mes':
                            cost = bill.values_Month
                        elif contract_type == 'Año':
                            cost = bill.values_Year
                    except Exception as e:
                        print("Error al calcular el costo:", e)
                        pass
                
                # Guardar el serializador primero
                serializer.save()

                # Asignar el número de cupo al vehículo en el campo 'ubication'
                serializer.instance.ubication = f"Cupo {spot_number}"
                serializer.save()

                # Asignar el costo calculado al campo 'cost'
                serializer.instance.cost = cost
                serializer.save()
                
            except Exception as e:
                print("Error al calcular el costo o asignar cupo:", e)
                pass

            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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