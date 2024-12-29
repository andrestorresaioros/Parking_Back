from .views import Parking_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

urlpatterns=[path('View-Parkings/', csrf_exempt(Parking_view))]

#login_required(csrf_exempt(Parking_view)))]
#urlpatterns=[path('View-Parkings/', permission_required('parking.add_parking')(Parking_view))]
