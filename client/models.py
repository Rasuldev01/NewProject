from django.db import models
from django.utils.html import format_html
from main.models import User
from project_app.helpers import price_filter
from rest_framework.response import Response


class Imageclass(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(Imageclass, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    info = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



    