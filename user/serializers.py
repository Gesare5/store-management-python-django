from rest_framework import serializers

from store.serializers import StoreSerializer
from store.models import Store


class UserSerializer(serializers.ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = Store
        fields = "__all__"
