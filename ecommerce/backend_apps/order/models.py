from django.db import models
from Account.models import User
from backend_apps.address.models import UserAddress
from backend_apps.product.models import ProductItem
from django.utils import timezone

# Create your models here.

class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add the price field
    # Add more fields as per your requirements

    def __str__(self):
        return self.name



class OrderStatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as per your requirements

    def __str__(self):
        return self.name
    


class ShopOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    shipping_address = models.ForeignKey(UserAddress, on_delete=models.PROTECT)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.PROTECT)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    


class OrderLine(models.Model):
    order = models.ForeignKey(ShopOrder, on_delete=models.PROTECT)
    order_item = models.ForeignKey(ProductItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

