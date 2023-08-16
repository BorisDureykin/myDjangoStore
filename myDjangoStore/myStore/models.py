from django.contrib.auth.models import User
from django.db import models
from django.template.backends import django


# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=1024, db_index=True)
    slug = models.SlugField(max_length=64)
    status = models.BooleanField(default=True)
    offerSale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    description = models.TextField(max_length=1024)
    price = models.FloatField()
    countProduct = models.IntegerField()
    slug = models.SlugField(max_length=64)
    status = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
    offerSale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    slug = models.SlugField(max_length=64)
    products = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user, self.products
