from typing import NamedTuple

from django.conf import settings
from microservice_request.services import ConnectionService
from rest_framework.request import Request
from rest_framework.response import Response
from api.v1.cart_microservice.services import CartService


class PaymentService(ConnectionService):
    api_key = settings.PAYMENT_API_KEY
    service = settings.PAYMENT_API_URL
    SEND_COOKIES = True


class AddressData(NamedTuple):
    street_address: str
    city: str
    postal_code: str
    country: str


class UserData(NamedTuple):
    email: str
    first_name: str
    last_name: str
    phone_number: str


class CheckoutService:
    def __init__(self, request: Request, serializer_data: dict):
        self.user_data = UserData(**serializer_data['credentials'])
        self.shipping_address = AddressData(**serializer_data['shipping_address'])
        self.billing_address = AddressData(**serializer_data['billing_address'])
        self.request = request

    def validate_cart_content(self):
        service = CartService(request=self.request, url="/api/v1/cart/checkout/")
        response = service.service_response(method="get")
        return response.data
