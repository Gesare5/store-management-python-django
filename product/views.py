from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.decorators import permission_classes

# Create your views here.
from .models import Product, Brand
from .permissions import IsOwnerOrReadOnly,IsOwner
from .serializers import ProductSerializer, BrandSerializer


# TODO: REPLICATE
# THE DETAIL GET, PUT, DELETE FOR BRANDS
#  REPLICATE THE CREATE/POST METHOD


class BrandListView(APIView):
    """
    A simple view for viewing all brands
    """
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        # brands = Brand.objects.filter(user=request.user)
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create the Brand with given data
        """
        data = {"name": request.data.get("name")}
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetailView(APIView):
    """
    Update Brand details
    Retrieve Brand,
    Change detail,
    Save changes to db
    """

    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk, request):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand = self.get_object(pk, request)
        serializer = BrandSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        brand = self.get_object(pk, request)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk, request)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListView(APIView):
    """
    A simple view for viewing all products
    """

    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]
    permission_classes= [permissions.IsAdminUser]

    # def filter_queryset(self, queryset):
    #     """
    #     Given a queryset, filter it with whichever filter backend is in use.
    #     You are unlikely to want to override this method, although you may need
    #     to call it either from a list view, or from a custom `get_object`
    #     method if you want to apply the configured filtering backend to the
    #     default queryset.
    #     """
    #     for backend in list(self.filter_backends):
    #         queryset = backend().filter_queryset(self.request, queryset, self)
    #     return queryset

    def get(self, request, brand=None):
        queryset = Product.objects.filter(user=request.user)
        name = request.query_params.get("name")
        # queryset = self.filter_queryset(unfiltered_queryset)
        # description = request.query_params.get("description")
        if name is not None:
            queryset = queryset.filter(name=name)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Product with given data
        """
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "price": request.data.get("price"),
            "brand": request.data.get("brand"),
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    """
    Update Product details
    Retrieve Product,
    Change detail,
    Save changes to db
    """
    # permission_classes= [permissions.IsAuthenticated]


    def get_object(self, pk, request):
        try:
            return Product.objects.get(pk=pk, user=request.user)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk, request)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        product = self.get_object(pk, request)
        if not product:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk, request)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class BrandView(viewsets.ViewSet):
#     """
#     A simple Viewset for viewing all brands
#     """

#     queryset = Brand.objects.all()

#     @extend_schema(responses=BrandSerializer)
#     def list(self, request):
#         serializer = BrandSerializer(self.queryset, many=True)
#         return Response(serializer.data)


# class ProductView(viewsets.ViewSet):
#     """
#     A simple Viewset for viewing all products
#     """

#     queryset = Product.objects.all()

#     @extend_schema(responses=ProductSerializer)
#     def list(self, request):
#         serializer = ProductSerializer(self.queryset, many=True)
#         return Response(serializer.data)


# def get(self, request, format=None):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

# class ProductDetailView(APIView):
#     """
#     Retrieve Product Detail
#     """

#     def get(self, request, pk, format=None):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     return Response(serializer.data, status=status.HTTP_200_OK)
