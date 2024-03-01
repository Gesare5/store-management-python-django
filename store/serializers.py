from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = "__all__"

    def get_username(self, obj):
        return obj.number
