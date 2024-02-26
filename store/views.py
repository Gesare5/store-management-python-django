from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StoreSerializer
from .models import Store


# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/ figure out user app and permissions
# Now that we've got some users to work with, we'd better add representations of those users to our API. Creating a new serializer is easy. In serializers.py add:

# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']

# Because 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.

# We'll also add a couple of views to views.py. We'd like to just use read-only views for the user representations, so we'll use the ListAPIView and RetrieveAPIView generic class-based views.

# from django.contrib.auth.models import User


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class StoreListView(APIView):
    """
    A simple view for viewing all stores
    """

    def get(self, request, format=None):
        # try:
        number = request.query_params["name"]
        print(number)
        # if number != None:
        stores = Store.objects.get(name=number)
        # except:
        # stores = Store.objects.all()
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
    Update Store details
    Retrieve Store,
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

    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
