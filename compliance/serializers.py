from .models import *
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'updated_at']

class ApplicationSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'app_name', 'product', 'product_name', 'created_at', 'updated_at']