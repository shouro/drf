from django.contrib import admin

# Register your models here.
from .models import Product, ProductAttribute, ProductPrice

admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductPrice)