from django.test import TestCase
from .models import Product, ProductPrice, ProductAttribute

class ProductAttributeTestCase(TestCase):
    def test_productattribute(self):
        self.assertEquals(ProductAttribute.objects.count(), 0)
        ProductAttribute.objects.create(property='color', value='red')
        ProductAttribute.objects.create(property='size', value='large')
        self.assertEquals(ProductAttribute.objects.count(), 2)


class ProductPriceTestCase(TestCase):
    def test_productprice(self):
        self.assertEquals(ProductPrice.objects.count(), 0)
        ProductPrice.objects.create(price='120', begin_date='2019-5-1', end_date='2020-5-15')
        ProductPrice.objects.create(price='200', begin_date='2019-5-16', end_date='2020-5-31')
        self.assertEquals(ProductPrice.objects.count(), 2)


class ProductTestCase(TestCase):
    def test_product(self):
        self.assertEquals(Product.objects.count(), 0)
        Product.objects.create(name='mug 3p', slug='mug-3p', code='1234')
        Product.objects.create(name='mug 6p', slug='mug-6p', code='4321')
        self.assertEquals(Product.objects.count(), 2)

