from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Account.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,SendPasswordResetEmailSerializer,UserPasswordResetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.

# Helper function to generate tokens for a user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),    # Refresh token is used to get a new access token after it expires
        'access': str(refresh.access_token),   # Access token is used to authenticate API requests
    }


class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            # Generate tokens for the newly registered user
            token=get_tokens_for_user(user)
            return Response({"token":token,"msg":"Registration Sucessful"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self,request,format=None):
        serializers=UserLoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            email= serializers.data.get("email")
            password=serializers.data.get("password")
            user=authenticate(email=email,password=password)
            if user is not None:
                 # Generate tokens for the authenticated user
                token=get_tokens_for_user(user)
                return Response({"token":token,"msg":"Login Success"},status=status.HTTP_200_OK)
            else:
                return Response({"errors":{"non-field error":["Email or Password is invalid"]}},status=status.HTTP_404_NOT_FOUND)
            
        else:
            print("NOt vable to ")


class UserLogoutView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request,format=None):
        try:
            print("warking")
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            print('Added checkout')
            print("hellow ti sis how to find t")
            print(" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6666")
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class userProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class UserChangePasswordView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        print(request.user)
        serializer=UserChangePasswordSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"password changed successfully"},status=status.HTTP_200_OK )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class SendPasswordResetEmailView(APIView):
    def post(self,request,format=None):
        serializer=SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"password reset liink send. Please check your email"},status=status.HTTP_200_OK )
        


class UserPasswordResetView(APIView):
    def post(self,request,uid,token,format=None):
        serializers=UserPasswordResetSerializer(data=request.data,context={"uid":uid,"token":token})
        if serializers.is_valid(raise_exception=True):
            return Response({"msg":"password changed successfully"},status=status.HTTP_200_OK )
        