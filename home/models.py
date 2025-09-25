from django.db import models

# Create your models here
class MenuCategroy(models.Model):
    name = models.CharFields(max_length=100, unique=True

    def __str__(self):
        return self.name