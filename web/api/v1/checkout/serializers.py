from rest_framework import serializers

from api.v1.auth_microservice.serializers import ChangeAddressSerializer
from phonenumber_field.serializerfields import PhoneNumberField


class CheckoutUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = PhoneNumberField()


class CheckoutSerializer(serializers.Serializer):
    credentials = CheckoutUserSerializer()
    shipping_address = ChangeAddressSerializer()
    billing_address = ChangeAddressSerializer()
    order_notes = serializers.CharField()
