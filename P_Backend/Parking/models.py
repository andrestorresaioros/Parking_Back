from django.db import models
from django.contrib.auth.models import User

class Parking(models.Model):
    id_Admin= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    zone= models.CharField(max_length=200,default='')
    quantity_space_moto= models.IntegerField(default=0)
    quantity_space_car= models.IntegerField(default=0)
    quantity_space_heavy= models.IntegerField(default=0)
    def __str__(self):
        return self.zone
    
    def get_next_available_spot_number(self, vehicle_type):
            if vehicle_type.strip() == 'Automóvil':
                return self.get_next_available_spot_for_vehicle_type('quantity_space_car')
            elif vehicle_type.strip() == 'Motocicleta':
                return self.get_next_available_spot_for_vehicle_type('quantity_space_moto')
            elif vehicle_type.strip() == 'Vehículos Pesados':
                return self.get_next_available_spot_for_vehicle_type('quantity_space_heavy')
            return None

    def get_next_available_spot_for_vehicle_type(self, field_name):
        current_value = getattr(self, field_name)
        if current_value > 0:
            setattr(self, field_name, current_value - 1)
            self.save()
            return current_value
        return None