from rest_framework import status
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

class CategoryApiView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return Response({'success': True,
                         'message': status.HTTP_200_OK,
                         'data': serializer.data

                         })






class CategoryFilter(APIView):
    def get(self, request, pk):
        queryset = Category.objects.filter(pk=pk)
        serializer = CategorySerializer(queryset, many=True)
        return Response({'success': True,
                         'message': status.HTTP_200_OK,
                         'data': serializer.data
                         })



class ProductModelViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'success': True,
                         'message': status.HTTP_200_OK,
                         'data': serializer.data
                         })

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True,
                             'message': status.HTTP_200_OK,
                             'data': serializer.data
                             })
        return Response({'success': False,
                         'message': status.HTTP_400_BAD_REQUEST,
                         'data': serializer.errors
                         })


class ProductUpdate(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def put(self, request, pk):
        queryset = Product.objects.filter(pk=pk)
        serializer = ProductSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True,
                             'message': status.HTTP_200_OK,
                             'data': serializer.data
                             })
        return Response({'success': False,
                         'message': status.HTTP_400_BAD_REQUEST,
                         'data': serializer.errors
                         })


class ProductFilter(ModelViewSet):
    def list(self, request, pk):
        queryset = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response({'success': True,
                         'message': status.HTTP_200_OK,
                         'data': serializer.data
                         })


