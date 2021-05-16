# from .views import
from rest_framework import routers
from .views import OrderAPIView, OrderItemAPIView, ProductAPIView, TeamAPIView

router = routers.DefaultRouter()
router.register(r"product", ProductAPIView, basename="product")
router.register(r"team", TeamAPIView, basename="team")
router.register(r"order-item", OrderItemAPIView, basename="order-item")
router.register(r"order", OrderAPIView, basename="order")

urlpatterns = router.urls
