from .views import Parking_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('View-Parkings/', csrf_exempt(Parking_view))]
