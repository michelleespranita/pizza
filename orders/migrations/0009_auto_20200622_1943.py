# Generated by Django 2.0.3 on 2020-06-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200622_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='kind',
            field=models.CharField(choices=[('Regular Pizza', 'Regular Pizza'), ('Sicilian Pizza', 'Sicilian Pizza'), ('Topping', 'Topping'), ('Sub', 'Sub'), ('Addon', 'Addon'), ('Pasta', 'Pasta'), ('Salad', 'Salad'), ('Dinner Platter', 'Dinner Platter')], max_length=30),
        ),
    ]
