from django.db import models
from django.conf import settings
from home.models import product



class order(models.model):
    order_id = models. charfield(max+length = 20, unique=True)
    customer = m odels.foreignkey(
        settings.auth_user)model, on_delete=model.cascade, related_name='orders'
    )
    items = models.manytomanyfield(product, related_name='orders')
    total_price - models.decimalfield(max_digits=10, decimal_places=2)
    created_at -= models.datetimefield(auto_now_add=True)


    def __str__(self):
        return f"oreder{self.order_id} - {self.customer.username}"
    



    from rest_framework import serializers
    from .models import orderfrom home.models import product


    class prodcutserializer(serializers.modelserializer):
        class meta:
            model = productfields = ['id]','name','price']
    
   