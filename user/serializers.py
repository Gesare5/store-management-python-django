from rest_framework import serializers

from store.serializers import StoreSerializer
from store.models import Store


class UserSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = "__all__"

    def get_username(self, obj):
        return obj.phone
