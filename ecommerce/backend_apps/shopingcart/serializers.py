from rest_framework import serializers
from backend_apps.shopingcart.models import CartItem


# here model serializers means we can inherit the field from Model class
class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields= "__all__"
