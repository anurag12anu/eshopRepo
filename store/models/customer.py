from django.db import models
from django.utils import timezone
from .category import Category

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mno=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    password=models.EmailField(max_length=500)
    
    