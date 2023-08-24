from django.db import models

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
    # Add more fields as per your requirement

    def __str__(self):
        return self.name