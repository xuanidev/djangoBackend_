# Generated by Django 4.2.14 on 2024-07-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('mainImg', models.TextField()),
                ('imgsProduct', models.JSONField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availables', models.IntegerField()),
                ('currency', models.CharField(choices=[('EUR', 'Euro'), ('USD', 'US Dollar'), ('GBP', 'British Pound')], default='EUR', max_length=3)),
            ],
        ),
    ]
