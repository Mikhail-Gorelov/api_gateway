from rest_framework import serializers
from django_countries.serializer_fields import CountryField

from api.v1.auth_microservice import choices


class LoginEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=7)
    remember_me = serializers.BooleanField()


class LoginPhoneSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(regex=r'^\+?1?\d{9,15}$')
    password = serializers.CharField(min_length=7)
    remember_me = serializers.BooleanField()


class SignUpEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=7)
    password1 = serializers.CharField(min_length=7)


class SignUpPhoneSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(regex=r'^\+?1?\d{9,15}$')
    password = serializers.CharField(min_length=7)
    password1 = serializers.CharField(min_length=7)


class VerifySerializer(serializers.Serializer):
    key = serializers.CharField()


class PasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetPhoneSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(regex=r'^\+?1?\d{9,15}$')


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class ChangeUserPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(min_length=7)
    new_password1 = serializers.CharField(min_length=7)
    new_password2 = serializers.CharField(min_length=7)


class ChangeUserProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)

    last_name = serializers.CharField(required=False)
    gender = serializers.IntegerField(required=False)
    birthday = serializers.DateField(required=False,
                                     allow_null=True,
                                     format="%d-%m-%Y",
                                     input_formats=["%d-%m-%Y", "%Y-%m-%d"]
                                     )
    avatar = serializers.ImageField(required=False)


class ChangeAddressSerializer(serializers.Serializer):
    street_address = serializers.CharField(max_length=256, required=False)
    city = serializers.CharField(max_length=256, required=False)
    postal_code = serializers.CharField(max_length=20, required=False)
    country = CountryField()
