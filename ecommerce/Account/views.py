from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Account.serializers import UserRegistrationSerializer
# Create your views here.


class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            return Response({"msg":"Registration Sucessful"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
