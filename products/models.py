from django.db import models

class menuitem(models.model):
    name = models.charfield(max_length=255)
    description = models.textfield(blank=True)
    price = models.decimalfield(max_digits=6, decimal_places=2)


def __str__(self):
    return self.name