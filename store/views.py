from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StoreSerializer
from .models import Store


# TODO:
# Rename the apps to be plural
# write views for store
class StoreListView(APIView):
    """
    A simple view for viewing all stores
    """

    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create the Store with given data
        """
        data = {
            "name": request.data.get("name"),
            "number": request.data.get("number"),
            "description": request.data.get("description"),
            "product": request.data.get("product"),
        }
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetailView(APIView):
    """
    Update Brand details
    Retrieve Brand,
    Change detail,
    Save changes to db
    """

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)

        #   def get_object(self, pk):
        # try:
        # return Product.objects.get(pk=pk)
        # except Product.DoesNotExist:
        # raise Http404


# class BrandDetailView(APIView):
#     """
#     Update Brand details
#     Retrieve Brand,
#     Change detail,
#     Save changes to db
#     """

#     def get_object(self, pk):
#         try:
#             return Brand.objects.get(pk=pk)
#         except Brand.DoesNotExist:
#             raise Http404

#     def get(self, pk, format=None):
#         brand = self.get_object(pk)
#         serializer = BrandSerializer(brand)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk, format=None):
#         brand = self.get_object(pk)
#         serializer = BrandSerializer(brand, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         brand = self.get_object(pk)
#         brand.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
