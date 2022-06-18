from django.conf import settings
from microservice_request.services import ConnectionService

class CartService(ConnectionService):
    api_key = settings.CART_API_KEY
    service = settings.CART_API_URL
