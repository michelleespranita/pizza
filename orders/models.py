from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    TYPES = (
        ('Regular Pizza', 'Regular Pizza'),
        ('Sicilian Pizza', 'Sicilian Pizza'),
        ('Topping', 'Topping'),
        ('Sub', 'Sub'),
        ('Addon', 'Addon'),
        ('Pasta', 'Pasta'),
        ('Salad', 'Salad'),
        ('Dinner Platter', 'Dinner Platter')
    )

    kind = models.CharField(max_length=30, choices=TYPES)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"#{self.id}"

class ShoppingCartItem(models.Model):
    TYPES = (
        ('Regular Pizza', 'Regular Pizza'),
        ('Sicilian Pizza', 'Sicilian Pizza'),
        ('Topping', 'Topping'),
        ('Sub', 'Sub'),
        ('Addon', 'Addon'),
        ('Pasta', 'Pasta'),
        ('Salad', 'Salad'),
        ('Dinner Platter', 'Dinner Platter')
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.CharField(max_length=30, choices=TYPES)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=5)
    toppings = models.CharField(max_length=100, null=True, blank=True)
    addons = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    purchased = models.BooleanField(default=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.username}'s ShoppingCartItem #{self.id}"

