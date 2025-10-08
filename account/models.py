class category(models.model):
    category_name = models. charfield(max_length=100)


class menuitems(models.model):
    name = models.charfield(max_length=100)
    price = models.decimalfield(max_digits=6, decimal_palces=2)
    category -models.foreignkey(category, on_delete=models.cascade)

    from rest_framework import serializers 
    from .models import menuitems

    class menuitemsserializers(serializers.modelserializer):
        class meta:
            model = menuitems
            fields = '__all__'

    from rest_framework. views import apiview
    from rest_framework. response import response
    from rest_framework import status
    from. models import menuitems
    from. serializers import menuitemsserializers

    class menuitemsbycategoryapiview(apiview):
        def get(self,request):
            category_name = request.query_params.get('category')
            if