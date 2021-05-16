from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Product, Team, OrderItem, Order


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("category", "model_no", "available", "price")


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product", "quantity", "order")


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("name", "address", "distance", "created_at")
