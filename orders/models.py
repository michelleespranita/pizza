from django.db import models

# Create your models here.

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
    price = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    large_price = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return f"{self.kind}, {self.name}"