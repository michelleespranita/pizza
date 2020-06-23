from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from orders.models import Menu, Order, ShoppingCart
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
    
    username = request.user.get_username()
    context['username'] = username

    # Retrieve menu data
    
    regular_pizzas = Menu.objects.filter(kind='Regular Pizza')
    sicilian_pizzas = Menu.objects.filter(kind='Sicilian Pizza')
    toppings = Menu.objects.filter(kind='Topping')
    subs = Menu.objects.filter(kind='Sub')
    pastas = Menu.objects.filter(kind='Pasta')
    salads = Menu.objects.filter(kind='Salad')
    dinner_platters = Menu.objects.filter(kind='Dinner Platter')
    addons = Menu.objects.filter(kind='Addon')

    # Put menu data in context
    
    context['regular_pizzas'] = regular_pizzas
    context['sicilian_pizzas'] = sicilian_pizzas
    context['toppings'] = toppings
    context['subs'] = subs
    context['pastas'] = pastas
    context['salads'] = salads
    context['dinner_platters'] = dinner_platters
    context['addons'] = addons

    return render(request, "orders/index.html", context)

# ----- Save items to cart ------

def addToCart(request):
    kind = request.POST["kind"]
    name = request.POST["name"]
    size = request.POST["size"]
    toppings = request.POST["toppings"]
    addons = request.POST["addons"]
    if size == 'Small':
        price = Menu.objects.filter(kind=kind, name=name)[0].price
    else:
        price = Menu.objects.filter(kind=kind, name=name)[0].large_price
    if addons != '':
        addons_list = addons.split(',') # Ex: ['Mushrooms', 'Onions']
        for addon in addons_list:
            price += Menu.objects.filter(kind='Addon', name=addon)[0].price
    # print(kind, name, size, toppings, addons) 
    cart_item = ShoppingCart(username=request.user, kind=kind, name=name, size=size, toppings=toppings, addons=addons, price=price)
    cart_item.save()
    return HttpResponseRedirect(reverse('index'))

# ----- Show items in cart ------

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
