from django.shortcuts import render

def all_products(request):
    return render(request, 'products/index.html')

def create(request):
    
    return render(request,'products/create.html')

def details(request):
    return render(request,'products/details.html')

def update(request):
    return render(request, 'products/edit.html')

def payment(request):
    return render(request, 'products/payment.html')