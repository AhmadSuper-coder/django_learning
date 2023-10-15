from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from backend_apps.shopingcart.models import CartItem
from backend_apps.shopingcart.serializers import UserCartSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.


class CartDetails(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request,format=None):
        print(request)
        print("hiting the car api ")

        cart_data=CartItem.objects.filter(cart__user__email=request.user.email)
        serializer=UserCartSerializer(cart_data,many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

