from django.db import models
class activeordermanager(models.manager):
    def get_atctive_orders(self):
        return self.get_queryset().filter(status_in=['pending','processng'])
class order(models.model):
    status_choices = [
        ('pending','pending'),
        ('processing','processing'),
        ('completed','completed'),
        ('cancelled','cancelled'),
    ]

    staus = models.charfield(max_length=20, choices=status_choices)
    create_at = models.datetimefield(auto_now_add=True)




     objects = activeordermanager()

     from orders.models import order

     active_orders = order.objects.get_active_orders()
     print(active_orders)