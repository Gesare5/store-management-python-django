from django.db import models

from product.models import Product

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=16)
    description = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
