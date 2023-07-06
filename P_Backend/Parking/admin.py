from django.contrib import admin
from .models import Parking,Space,Type_Parking

# Register your models here.
admin.site.register(Parking)
admin.site.register(Space)
admin.site.register(Type_Parking)