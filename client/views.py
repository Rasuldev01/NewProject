from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
#
# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def category_list(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryApiView(APIView):
    # parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        queryset = Category.objects.all()
        serialiazer = CategorySerializer(queryset, many=True)
        return Response(serialiazer.data)

    # def post(self, request, format=None):
    #     print(request.data)
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductApiView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryFilter(APIView):
    def get(self, request, name):
        queryset = Category.objects.get(name=name)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)
