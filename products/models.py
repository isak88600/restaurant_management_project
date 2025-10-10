from django.db import models
from django.conf import settings
from home.models import product



class order(models.model):
    order_id = models. charfield(max+length = 20, unique=True)
    customer = m odels.foreignkey(
        settings.auth_user)model, on_delete=model.cascade, related_name='orders'
    )
    