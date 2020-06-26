# Generated by Django 2.0.3 on 2020-06-23 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_shoppingcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_items',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]
