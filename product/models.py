from django.db import models

# Create your models here.
class productMainModel(models.Model):
    Title=models.CharField( max_length=100)
    Description=models.CharField(max_length=500)
    Unique_id=models.IntegerField(unique=True)
    
class productImageModel:
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)  
    image=models.IntegerField() 