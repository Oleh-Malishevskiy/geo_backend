from django.shortcuts import render
from .serializers import BuildingSerializer, ProductSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Building, Product,Category
from django.http import Http404
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import CrudSerializer
from .serializers import CrudStatSerializer


class MyStatCrud(viewsets.ModelViewSet):
    serializer_class = CrudStatSerializer
    queryset = Product.objects.all()
    
class MyCrud(viewsets.ModelViewSet):
    serializer_class = CrudSerializer
    queryset = Product.objects.all()
    queryset = Category.objects.all()

class LatestProductsList(APIView):
    
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
class allview(ListAPIView):
    serializer_class=BuildingSerializer
    def get_queryset(self):
        return Building.objects.all()

