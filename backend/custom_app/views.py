from django.db import transaction
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Product, Team, OrderItem, Order
from .serializers import (
    OrderItemSerializer,
    OrderSerializer,
    ProductSerializer,
    TeamSerializer,
)

# Create your views here.
class ProductAPIView(ModelViewSet):
    """
    This is a CURD API for product items
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ()
    authentication_classes = ()


class TeamAPIView(ModelViewSet):
    """
    This is a CURD API for Team items
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = ()
    authentication_classes = ()


class OrderItemAPIView(ModelViewSet):
    """
    This is a CURD API for OrderItem items
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = ()
    authentication_classes = ()


class OrderAPIView(ModelViewSet):
    """
    This is a CURD API for Order items
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = ()
    authentication_classes = ()
