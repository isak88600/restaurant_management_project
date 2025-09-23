from django.db import models

# Create your models here.

class menucategory(models.model):
    name = models.charfield(max_length=100)

    def __str__(self):
        return self.name

from rest_framework import serializers
from .models import menucategory

class menucategoryserializer(serializers.modelserializer):
    class meta:
        model = menucategroy
        fields['name']

from rest_framework.generics import listapiview
from .models import menucategory
from .serializers import menucategoryserializer

class menuctegorylistview(listapiview):
    queryset = menucategory.objects.all()
    serializers_class = menucategoryserializer

from django.urls import path
from .views import menucategorylistview

urlpatterns = [
    path('menu-categories/',menucategorylistview.as_view(), name='menu-category-list'),
]

INSTALLED_APPS = [
    'rest_framework',
    'home',
]