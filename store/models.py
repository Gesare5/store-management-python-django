from django.db import models
from django.utils import timezone

from product.models import Product
from user.models import User

# Create your models here.


class Store(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=16)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
