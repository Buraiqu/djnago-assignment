from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . models import *
from product.models import *
from . serializer import *


# Create your views here.
# create user(Phone_number,Name,Date_of_birth,Gender,Image), Create user cart while creating user(post request)
class UserCreateView(generics.createAPIView):
    serializer_class = UserSerializer
    
    def Post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        cart = UserCartModel.objects.create(owner=user)
        cart_item = request.data.get('product')
        for item in cart_item:
            product=productMainModel.objects.get(id = item.get('productid'))
            cart_item
            