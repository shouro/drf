from rest_framework import serializers
from products import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'code',
        )
        model = models.Product

class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'property',
            'value',
        )
        model = models.ProductAttribute

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'price',
            'begin_date',
            'end_date',
        )
        model = models.ProductPrice