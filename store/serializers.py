from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import Store


class ProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Store
        fields = "__all__"
