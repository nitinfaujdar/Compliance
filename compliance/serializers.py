from .models import *
from rest_framework import serializers

class ComplianceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compliance
        fields = ['id', 'name', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'updated_at']

class ApplicationSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    compliance_name = serializers.CharField(source='compliance.name', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'compliance', 'compliance_name', 'app_name', 'product', 'product_name', 'created_at', 'updated_at']