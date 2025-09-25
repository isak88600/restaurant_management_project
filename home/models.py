from django.db import models
from .models import orderstatus

class order(models.model):

    status = models.foreignkey(orderstatus, on_delete=models.set_null, null=True)


    def __str__(self):
        return f"order #{self.id} - self : {self.status}"