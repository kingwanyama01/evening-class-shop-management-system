from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {"products": products})

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

def update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        # Receive updated data from the frontend
        updated_product_name = request.POST.get("p-name")
        updated_product_quantity = request.POST.get("p-qtty")
        updated_product_size = request.POST.get("p-size")
        updated_product_price = request.POST.get("p-price")
        
        # Update the db data with the newly edited values
        product.name = updated_product_name
        product.quantity = updated_product_quantity
        product.size = updated_product_size
        product.price = updated_product_price
        
        # Return the updated data back to the database
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect("all-products-url")
    return render(request, 'products/edit.html', {"product": product})

def payment(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/payment.html', {"product": product})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request,"Product deleted successfully!")
    return redirect("all-products-url")