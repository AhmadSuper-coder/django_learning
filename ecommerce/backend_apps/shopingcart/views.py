from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from backend_apps.shopingcart.models import CartItem
# Create your views here.


class UserRegistrationView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request,format=None):
        cart_data=CartItem.objects.get()
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)