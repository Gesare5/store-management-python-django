from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id,name,storeid, price, brand, type
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    # id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

    # TREEFOREIGNKEY
