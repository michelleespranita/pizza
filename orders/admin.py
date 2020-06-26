from django.contrib import admin

from .models import Menu, Order, ShoppingCartItem

# Register your models here.
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(ShoppingCartItem)