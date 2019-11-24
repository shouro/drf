from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from products.models import Product, ProductAttribute, ProductPrice
from .serializers import ProductSerializer, ProductAttributeSerializer, ProductPriceSerializer

class ProductViewTest(APITestCase):
    def setUp(self):
        pass