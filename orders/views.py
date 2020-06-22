from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from orders.models import Menu
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError

def index(request):
    if not request.user.is_authenticated:
        context = {
            "logged_in": False
        }
    else:
        context = {
            "logged_in": True
        }
    
    # Retrieve data
    

    # Put data in context
    

    return render(request, "orders/index.html", context)

# ----- Registration, Login and Logout ------

def register_view_get(request):
    return render(request, "orders/register.html")

def register_view_post(request):
    email = request.POST["email"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    username = request.POST["username"]
    password = request.POST["password"]
    if email is not None and username is not None and password is not None:
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, "orders/register.html", {"message": "Username already exists. Please choose another username."})
        if firstname is not None:
            user.first_name = firstname
        if lastname is not None:
            user.last_name = lastname
        user.save()
        return HttpResponseRedirect(reverse('login_view_get'))
    else:
        return render(request, "orders/register.html", {"message": "Please enter all the required information."})


def login_view_get(request):
    return render(request, "orders/login.html")

def login_view_post(request):
    username = request.POST["username"]
    password = request.POST["password"]
    print(username, password)
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "orders/login.html", {"message": "Invalid user credentials."})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view_get'))
