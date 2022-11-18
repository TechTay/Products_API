from rest_framework import serializers
from .models import Products

class Productserializer(serializers.modelSerializer):
    class Meta:
        model = Products
        fields = ['title', 'description', 'price', 'inventory_quantity']