from .views import user_view
from django.urls import path

urlpatterns=[path('Manage/', user_view)]