# Generated by Django 3.2.9 on 2021-11-19 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='food_value',
        ),
    ]