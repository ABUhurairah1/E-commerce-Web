# Generated by Django 5.0.2 on 2024-07-13 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerece', '0009_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
