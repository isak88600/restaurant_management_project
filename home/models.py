from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    name = models.charfield(max_length=100)

    def __str__(self):
        return self.name

from rest_framework import serializers
from .models import MenuCategory

class Menucategoryserializer(serializers.modelserializer):
    class meta:
        model = Menucategoryserializer
        fields = ['name']




