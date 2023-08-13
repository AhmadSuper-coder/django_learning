from django.contrib import admin
from .models import ShippingMethod, OrderStatus,ShopOrder,OrderLine
# Register your models here.


admin.site.register(ShippingMethod)
admin.site.register(OrderStatus)
admin.site.register(ShopOrder)
admin.site.register(OrderLine)