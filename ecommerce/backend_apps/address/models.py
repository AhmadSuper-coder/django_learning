from django.db import models
from Account.models import User
# Create your models here.


class Address(models.Model):
    house_number=models.CharField(max_length=100)
    land_mark = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.state}"
    
class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_default=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.name}'s Address: {self.address}"