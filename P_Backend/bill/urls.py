from .views import bill_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('View-Bills/', csrf_exempt(bill_view))]
