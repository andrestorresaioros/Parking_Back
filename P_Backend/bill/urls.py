from .views import bill_view
from django.urls import path

urlpatterns=[path('View-Bills/', bill_view)]
