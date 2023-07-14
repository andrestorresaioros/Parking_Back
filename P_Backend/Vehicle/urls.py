from .views import Vehicle_view, consult_Vehicle
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('View-Vehicles/', csrf_exempt(Vehicle_view)),
             path('View-Vehicles/<plates>/', consult_Vehicle)]

