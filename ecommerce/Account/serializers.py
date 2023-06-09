from rest_framework import serializers
from Account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model=User
        fields=["email","name","password","password2","mobile_number"]
        extra_kwargs={
            "password":{"write_only":True}
        }


    #Validating password and confirm password while Registrations
    def validate(self, attrs):
        password=attrs.get("password")
        password2=attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password and confirm password Does't match ")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

