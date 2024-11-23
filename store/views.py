from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
import sys


def index(request):
   all_products=None
   
   all_Category= Category.get_allCategory()
   print(all_products)
   #return render(request, 'order/order.html')
   categoryID=request.GET.get('category')
   if categoryID:
      all_products= Product.get_allProduct_Category_by_id(categoryID)
   
   else:
      all_products= Product.get_allProduct()

   data={}
   data['products']=all_products
   data['categoris']=all_Category
   return render(request, 'index.html',data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        mno = postData.get('mno')  # Mobile number
        email = postData.get('email')
        password = postData.get('password')

        # Validation
        if not all([first_name, last_name, mno, email, password]):
            return HttpResponseBadRequest("All fields are required.")

        # Save to database
        error_message=None
        
        if (not first_name):
            error_message="first_name is required"
        elif len(first_name)<4:
            error_message="first_name should be 4 char"
        
        if not error_message:
            
            try:
                customer = Customer(
                first_name=first_name,
                last_name=last_name,
                mno=mno,
                email=email,
                password=password  # Consider hashing the password
            )
                customer.register()
            except Exception as e:
                return HttpResponseBadRequest(f"Error saving customer: {str(e)}")

        # Return success response
        return render(request, 'signup.html', {'message': f'Signup successful for {email}!'})
    return HttpResponse("Method not allowed", status=405)

def signin(request):
   return render(request,'signin.html')

def logout(request):
   return render(request,'signin.html')
   

def order(request):

   return render(request, 'order/order.html')
 
   



