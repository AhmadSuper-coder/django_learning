from django.db import models
from Account.models import User
# Create your models here.



class PaymentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserPaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    payment_info = models.CharField(max_length=100)  # Store payment details like card number, UPI ID, etc.
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s {self.payment_type.name} Payment"