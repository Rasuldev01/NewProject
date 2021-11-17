# Generated by Django 3.2.9 on 2021-11-17 14:21

import client.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=client.models.upload_to),
        ),
    ]