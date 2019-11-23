# Create your views here.
from rest_framework import status, viewsets

from products import models
from .serializers import ProductSerializer, ProductAttributeSerializer, ProductPriceSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core import serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    @action(detail=True, methods=['get', 'post', 'put', 'delete'])
    def attributes(self, request, *args, **kwargs):
        product = self.get_object()

        if request.method == "GET":
            attributes = product.attributes.all()
            serializer = ProductAttributeSerializer(attributes, many=True)
            return Response(serializer.data)

        if request.method == "POST":
            serializer = ProductAttributeSerializer(data=request.data)
            if serializer.is_valid():
                pa = models.ProductAttribute.objects.create(property=serializer.data['property'], value=serializer.data['value'])
                product.attributes.add(pa)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        if request.method == "PUT":
            serializer = ProductAttributeSerializer(data=request.data)
            if serializer.is_valid():
                pa = models.ProductAttribute.objects.filter(pk=request.data['id'])
                if len(pa):
                    pa.update(property=serializer.data['property'], value=serializer.data['value'])
                    return Response(serializer.data)
                else:
                    return Response({'error': 'wrong id: {}'.format(request.data['id'])}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == "DELETE":
            qid = request.query_params.get('id', None)
            pa = models.ProductAttribute.objects.filter(pk=qid)
            if len(pa):
                pa.delete()
                return Response({'id': qid, 'status': 'success'})
            else:
                return Response({'error': 'wrong id: {}'.format(qid)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'post', 'put', 'delete'])
    def prices(self, request, *args, **kwargs):
        product = self.get_object()
        if request.method == "GET":
            prices = product.prices.all()
            serializer = ProductPriceSerializer(prices, many=True)
            return Response(serializer.data)

        if request.method == "POST":
            serializer = ProductPriceSerializer(data=request.data)
            if serializer.is_valid():
                pp = models.ProductPrice.objects.create(
                    price=serializer.data['price'],
                    begin_date=serializer.data['begin_date'],
                    end_date=serializer.data['end_date']
                    )
                product.prices.add(pp)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        if request.method == "PUT":
            serializer = ProductPriceSerializer(data=request.data)
            if serializer.is_valid():
                pp = models.ProductPrice.objects.filter(pk=request.data['id'])
                if len(pp):
                    pp.update(
                        price=serializer.data['price'],
                        begin_date=serializer.data['begin_date'],
                        end_date=serializer.data['end_date']
                        )
                    return Response(serializer.data)
                else:
                    return Response({'error': 'wrong id, {}'.format(request.data['id'])}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == "DELETE":
            qid = request.query_params.get('id', None)
            pp = models.ProductPrice.objects.filter(pk=qid)
            if len(pp):
                pp.delete()
                return Response({'id': qid, 'status': 'success'})
            else:
                return Response({'error': 'wrong id: {}'.format(qid)}, status=status.HTTP_400_BAD_REQUEST)
