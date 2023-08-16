from django.contrib import admin

from myStore.models import Category, Product, Cart


# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)