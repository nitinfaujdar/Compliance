from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *

# Create your views here.

class ProductView(GenericAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': "Product Added Successfully", 'data': serializer.data},
                        status=status.HTTP_200_OK)
    
    def get(self, request):
        queryset = Product.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return Response({'message': 'Products retrieved Successfully', 'data': response.data}, 
                        status=status.HTTP_200_OK)

class ApplicationView(GenericAPIView):
    serializer_class = ApplicationSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': "Application Added Successfully", 'data': serializer.data},
                        status=status.HTTP_200_OK)
    
    def get(self, request):
        queryset = Application.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return Response({'message': 'Applications retrieved Successfully', 'data': response.data}, 
                        status=status.HTTP_200_OK)