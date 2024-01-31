from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

# Create your views here.
from .models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer


class BrandView(viewsets.ViewSet):
    """
    A simple Viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    """
    A simple Viewset for viewing all products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandListView(APIView):
    """
    A simple view for viewing all brands
    """

    def get(self, request, format=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


class ProductListView(APIView):
    """
    A simple view for viewing all products
    """

    # def get(self, request, format=None):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)
    
    def get(self, request, brand=None):
        queryset = Product.objects.all()
        name = request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(brand__name=name)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


# class ProductDetailView(APIView):
#     """
#     Retrieve Product Detail
#     """

#     def get(self, request, pk, format=None):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

    #     return Response(serializer.data, status=status.HTTP_200_OK)
class ProductDetailView(APIView):
    """
    Update Product details
    Retrieve product, 
    Change detail,
    Save changes to db
    """    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)    
        
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

