from django.shortcuts import render

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
