from django.db import models

# Create your models here.


# id,name,storeid, price, brand, type
class Brand(models.Model):
    # id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    # id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # TREEFOREIGNKEY
