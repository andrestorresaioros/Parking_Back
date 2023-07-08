from .views import Parking_view,Space_view,Type_Parking_view
from django.urls import path

urlpatterns=[path('View-Parkings/', Parking_view),
             path('View-Spaces/',Space_view),
             path('View-Type-Vehicles/',Type_Parking_view),
             ]
