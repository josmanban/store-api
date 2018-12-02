from rest_framework import serializers
from models import *


class CategorySerializer(serializers.ModelSerializer)
    class Meta:
        model = Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

class SaleStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleState

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
