# Generated by Django 4.2.14 on 2024-07-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0003_alter_order_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order Item', 'verbose_name_plural': 'Order Items'},
        ),
    ]
