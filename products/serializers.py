'''from rest_framework.serializers import ModelSerializer
from products.models import Category, Product
from rest_framework import serializers

class CategorySerializer(ModelSerializer):
    class Meta:
        Model = Category
        Fields = ['id','name']

        def __str__(self):
            return self.name
        
class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    created_by = serializers.StringRelatedField()
    class Meta:
        Model = Product
        Fields = ['id','name','description','price','category','stock_quantity','image_url','created_by','created_date']'''

from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Include the fields you want to expose in the API

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer for the category
    created_by = serializers.StringRelatedField()  # Use String representation for created_by

    class Meta:
        model = Product  # Make sure this line is correctly set
        fields = [
            'id', 'name', 'description', 'price',
            'category', 'stock_quantity', 'image_url',
            'created_by', 'created_date', 'updated_date'
        ]