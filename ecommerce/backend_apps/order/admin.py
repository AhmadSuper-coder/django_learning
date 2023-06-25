from django.contrib import admin

# Register your models here.
from .models import ShippingMethod, OrderStatus

admin.site.register(ShippingMethod)
admin.site.register(OrderStatus)