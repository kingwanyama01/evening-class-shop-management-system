from django.shortcuts import render

# This function is responsible for launching the home page (index.html)
def home(request):
    return render(request, "index.html")

# This function is responsible for launching the about page (about.html)
def about(request):
    return render(request,"about.html")

# This function is responsible for launching the register page (register.html)
def register(request):
    return render(request, "register.html")

# This is responsible for launching the login page
def login(request):
    return render(request, 'login.html')

# # This is responsible for launching the gallery page
def gallery(request):
    return render(request,'gallery.html')