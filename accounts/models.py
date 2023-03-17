from django.db import models
from product.models import *

# Create your models here.
class UserModel(models.Model):
    Phone_number=models.BigIntegerField(unique=True)
    Email=models.EmailField(max_length=254)
    is_customer=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    
class UserProfileModel(models.Model):
    owner=models.OneToOneField(UserModel,on_delete=models.CASCADE) 
    Name=models.CharField(max_length=100)   
    Date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
    Gender_Choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    gender=models.CharField(max_length=1,choices=Gender_Choices)
    image=models.ImageField(upload_to='user/',null=True)    
    
class user_login_topModel(models.Model):
    owner=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    Otp=models.IntegerField()
    active=models.BooleanField(default=False)
    
class UserCartProductModel(models.Model):
    owner=models.ForeignKey(UserModel,on_delete=models.CASCADE)      
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Status_Choices=[
        ('p','pending'),
        ('c','completed')
    ]
    status:models.CharField(max_length=1,choices=Status_Choices)
    
class UserCartModel:
    owner=models.OneToOneField(UserModel,on_delete=models.CASCADE)    
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    price=models.IntegerField()
     