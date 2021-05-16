from django.contrib import admin
from .models import Team, Order, OrderItem, Product


# Register your models here.
admin.site.register(Team)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
