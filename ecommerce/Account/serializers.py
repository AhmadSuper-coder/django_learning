from rest_framework import serializers
from Account.models import User
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# here model serializers means we can inherit the field from Model class 
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model=User
        fields=["email","name","password","password2","mobile_number"]
        extra_kwargs={
            "password":{"write_only":True}
        }


    #Validating password and confirm password while Registrations, we are overiding the is_validate function here
    def validate(self, attrs):
        password=attrs.get("password")
        password2=attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password and confirm password Does't match ")
        return attrs

    #here in validated data it contains User model all field, and create_user is custome method of the User objects manager in same way you do for the super user also
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    # explicitly we are validating the email to make sure that email is in correct format 
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=["email","password"]



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","email","name"]


class UserChangePasswordSerializer(serializers.ModelSerializer):
    # Validated both password 
    password=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)
    password2=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)

    class Meta:
        model=User
        fields=["password","password2"]

    def validate(self, attrs):
        password=attrs.get("password")
        password2=attrs.get("password2")
        user=self.context.get("user")
        if password != password2:
            raise serializers.ValidationError("Password and confirm password Does't match ")
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=["email"]

    def validate(self, attrs):
        email=attrs.get("email")
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            uid=urlsafe_base64_encode(force_bytes(user.id))
            print("Enocede id ",uid)
            token=PasswordResetTokenGenerator().make_token(user)
            print("password reset tokn",token)
            link = "http://localhost:3000/api/user/reset/"+uid+"/"+token
            print("password reset link: ",link)
            return attrs

        else:
            raise serializers.ValidationError("You are no a Registered User")



class UserPasswordResetSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)
    password2=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)

    class Meta:
        model=User
        fields=["password","password2"]

    def validate(self, attrs):
        try:
            password=attrs.get("password")
            password2=attrs.get("password2")
            uid=self.context.get("uid")
            token=self.context.get("token")
            if password != password2:
                raise serializers.ValidationError("Password and confirm password Does't match ")
            id=smart_str(urlsafe_base64_decode(uid))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError("Token is not valide or expired")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError("Token is not valid or expired")
