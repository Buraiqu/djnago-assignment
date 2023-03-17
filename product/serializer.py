from rest_framework import serializers
from . models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fiels="__all__"
        
        