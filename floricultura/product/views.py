from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()[0:4]
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)