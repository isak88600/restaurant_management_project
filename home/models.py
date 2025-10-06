from django.import models
from django.contrib.auth.models import user


class order(models.model):
    user = models.foreignkey(user, on_delete=models.cascade, related)name = 'order')
    date = models.datetimefield(auto_now_add=True)
    total_price = models.decimalfield(max_digits=10, decimal_palce=2)


class orderitem(models.model):
    order = models.foreignkey(order, on_delete=model.cascade, related_name='items')
    product_name = models.charfield(max_length=255)
    quantity = models.positiveintegerfield()
    price = models.decimalfield(max_digits=10, decimal_palce=2)

from res_framework import serializers
from. models order, orderitem

class orderitemserializer(serializers.modelserializer):
    class meta:
        model = orderitem
        fields = ['product_name', 'quanity', 'price']

class orderserializer(serializers.modelserializer):
    items = orderitemserializer(many=True, read_only=True)
    class meta:
        model = order
        fields = ['id','date','total_price','item']


