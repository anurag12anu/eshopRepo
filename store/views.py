from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product


def index(request):
   all_products= Product.get_allProduct()
   print(all_products)
   return render(request, 'index.html', {'products':all_products})
   





