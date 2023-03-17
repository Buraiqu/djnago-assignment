
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . models import *
from accounts.models import *
from . serializer import *
import uuid
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your views here.
@receiver(pre_save, sender=productMainModel)
class ProductCreateView(sender, instance, *args, **kwargs):
    if not instance.unique_id:
        instance.unique_id = str(uuid.uuid4()).replace('-','')
    