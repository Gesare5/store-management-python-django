from django.db import models

from store.models import Store

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    # todo figure out how to set username as phone number
    # create serializer class
    # figure out how to link django's user class/object
    # perform migrations
    # setup custom urls
    # check out custom user creation
    # figure out how to return selected users store/products etc
    # products/brands are global
    # formatting of phone numbers and dates
