# Generated by Django 2.0.3 on 2020-06-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200622_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='large_price',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]
