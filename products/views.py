from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

def all_products(request):
    return render(request, 'products/index.html')

def create(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Start receiving data from the frontend
        product_name = request.POST.get("p-name")
        product_quantity = request.POST.get("p-qtty")
        product_size = request.POST.get("p-size")
        product_price = request.POST.get("p-price")
        
        # Use the data received
        product = Product(name = product_name, quantity = product_quantity, size = product_size, price = product_price)
        product.save()
        
        messages.success(request,"Data saved successfully!")
        return redirect("create-products-url")        
        
    return render(request,'products/create.html')

def details(request):
    return render(request,'products/details.html')

def update(request):
    return render(request, 'products/edit.html')

def payment(request):
    return render(request, 'products/payment.html')