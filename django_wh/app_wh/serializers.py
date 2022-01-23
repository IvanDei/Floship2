from rest_framework import serializers
from .models import Order, Warehouse


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'label',
            'warehouse',
        )
