# Generated by Django 4.1.10 on 2023-07-13 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_orders_orde_created_743fca_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]