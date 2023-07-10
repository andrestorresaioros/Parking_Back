from .views import Vehicle_view, consult_Vehicle
from django.urls import path

urlpatterns=[path('View-Vehicles/', Vehicle_view),
             path('View-Vehicles/<plates>/', consult_Vehicle)]

