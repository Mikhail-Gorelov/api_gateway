from rest_framework import serializers

from api.v1.auth_microservice import choices


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=7)


class SignUpEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=7)
    password1 = serializers.CharField(min_length=7)


class SignUpPhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=7, required=True)
    password = serializers.CharField(min_length=7)
    password1 = serializers.CharField(min_length=7)


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()
