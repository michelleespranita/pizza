from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orders.models import Menu, Order, ShoppingCartItem
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from django.db.models import Sum
from django.core import mail

def index(request):
    context = {}
    context['user'] = request.user

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
    if not request.user.is_authenticated:
        return HttpResponseNotFound("<h1>Page not found</h1>")
        
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
    cart_item = ShoppingCartItem(username=request.user, kind=kind, name=name, size=size, toppings=toppings, addons=addons, price=price)
    cart_item.save()
    return HttpResponseRedirect(reverse('index'))

# ----- Show items in cart -----

def shopping_cart_view(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    context = {}
    context['user'] = request.user
    items = ShoppingCartItem.objects.filter(username=request.user, purchased=False)
    total_price = items.aggregate(Sum('price'))['price__sum']
    context['shopping_cart_items'] = items
    context['total_price'] = total_price
    return render(request, "orders/shopping_cart.html", context)

# ----- Check out -----

def checkout(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    items = ShoppingCartItem.objects.filter(username=request.user, purchased=False)
    total_price = items.aggregate(Sum('price'))['price__sum']
    order = Order(username=request.user, completed=False)
    order.total_price = total_price
    order.save() # Save it so that the order can be associated with items
    for item in items:
        item.purchased = True
        item.order_id = order
        item.save()
    return HttpResponseRedirect(reverse('index'))

# ----- View orders -----

def orders_list(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    context = {}
    context['user'] = request.user

    all_order_items = []
    if request.user.is_staff:
        orders = Order.objects.all().order_by('completed')
        
    else:
        orders = Order.objects.filter(username=request.user).order_by('completed')

    context["orders"] = orders
    for order in orders:
        order_items = ShoppingCartItem.objects.filter(purchased=True, order_id=order)
        all_order_items.append(order_items)
    context['all_order_items'] = all_order_items
    return render(request, "orders/orders_list.html", context)

# ----- Complete order -----

def completeOrder(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    if not request.user.is_authenticated:
        context = {
            "logged_in": False
        }
    else:
        context = {
            "logged_in": True
        }
    order_id = request.POST['completed']
    order_id = int(order_id.replace('#', ''))
    order = Order.objects.filter(id=order_id)[0]
    order.completed = True
    order.save()
    all_order_items = []
    orders = Order.objects.all().order_by('completed')
    context["orders"] = orders
    for order in orders:
        order_items = ShoppingCartItem.objects.filter(purchased=True, order_id=order)
        all_order_items.append(order_items)
    context['all_order_items'] = all_order_items
    return render(request, "orders/orders_list.html", context)

# ----- Registration, Login and Logout -----

def register_view_get(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    else:
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
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "orders/login.html")

def login_view_post(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "orders/login.html", {"message": "Invalid user credentials."})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view_get'))
