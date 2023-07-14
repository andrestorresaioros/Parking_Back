from .views import user_view,Receipt_view,Contract_view,Contract_Client_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Manage/', csrf_exempt(user_view)),
             path('Receipt/',csrf_exempt(Receipt_view)),
             path('Contract/',csrf_exempt(Contract_view)),
             path('Contract-Client/',csrf_exempt(Contract_Client_view))
             ]
