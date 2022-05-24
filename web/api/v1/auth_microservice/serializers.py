from rest_framework import serializers

from api.v1.auth_microservice import choices


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=7)


class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(min_length=2, max_length=100, required=True)
    last_name = serializers.CharField(min_length=2, max_length=100, required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(min_length=7, required=True)
    password = serializers.CharField(min_length=7)
    password1 = serializers.CharField(min_length=7)
    birthday = serializers.DateField(required=False)
    gender = serializers.ChoiceField(required=False, choices=choices.GenderChoice.choices)


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()
