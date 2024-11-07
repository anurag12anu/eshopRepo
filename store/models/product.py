from django.db import models
from django.utils import timezone

class Product(models.Model):
    name=models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='product/')
    