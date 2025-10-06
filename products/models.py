from django.db import models

class menuitem(models.model):
    name = models.charfield(max_length=255)
    description = models.textfield(blank=True)
    price = models.decimalfield(max_digits=6, decimal_places=2)


def __str__(self):
    return self.name


from rest_framework import serializers
from .models import menuitem

class menuitemserializer(serializers.modelserializer):
    class meta:
        model = menuitem
        fields = ['id','name','description','price','is_availabe']

def validate_price(self, value):
    if value < 0:
        raise serializers.validateerror("price must be a positive number.")
    return value