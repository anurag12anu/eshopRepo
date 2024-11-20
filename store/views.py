from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category


def index(request):
   all_products= Product.get_allProduct()
   all_Category= Category.get_allCategory()
   print(all_products)
   #return render(request, 'order/order.html')
   
   data={}
   data['products']=all_products
   data['categoris']=all_Category
   return render(request, 'index.html',data)
   

def order(request):

   return render(request, 'order/order.html')
 
   



