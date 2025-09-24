from django.db import models
from orders import pending, processing, completed,cancelled

# Create your models here.
from django.db import models
class orderstatus(models.model):
    name = models.charfield(max_lenght=50, unique=True)
    def __str__(self):
        return self.name
