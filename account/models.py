from rest_framework import generics
from home.models import table
from home.serializers import tableserializer

class tabledetailapiview(generics.retrieveapiview):
    queryset = table.objects.all()
    serializer_class = tableserializer


from django.urls import path
from home.views import tabledetailsapiview

urlpatterns = [
    path('api/tables/<int:pk/', tabledetailsapiview.as_view(), name = 'table-detail'),
    
]