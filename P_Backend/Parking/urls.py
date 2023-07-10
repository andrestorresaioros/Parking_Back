from .views import Parking_view,Space_view,Type_Parking_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('View-Parkings/', csrf_exempt(Parking_view)),
             path('View-Spaces/',Space_view),
             path('View-Type-Vehicles/',Type_Parking_view),
             ]
