from rest_framework import serializers
from .models import Category, Product, Imageclass


class ImageCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Imageclass
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    image = ImageCategorySerializer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'image']





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'










