from .views import user_view,Receipt_view,Contract_view,Contract_Client_view
from django.urls import path

urlpatterns=[path('Manage/', user_view),
             path('Receipt/',Receipt_view),
             path('Contract/',Contract_view),
             path('Contract-Client/',Contract_Client_view)
             ]
