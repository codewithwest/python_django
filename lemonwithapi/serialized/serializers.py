from rest_framework import serializers
from decimal import Decimal
from .models import MemuItems

# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class MenuItemSerializer(serializers.Serializer):
    # stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calc_tax')

    class Meta:
        model = MemuItems
        fields = ['id', 'title', 'price', 'inventory',
                  'price_after_tax', 'category']

    def calc_tax(self, product: MemuItems):
        return product.price * Decimal(1.1)
