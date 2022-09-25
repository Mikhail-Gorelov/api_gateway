from django.conf import settings
from microservice_request.services import MicroServiceConnect

class CartService(MicroServiceConnect):
    api_key = settings.CART_API_KEY
    service = settings.CART_API_URL
    PROXY_REMOTE_USER = True
    SEND_COOKIES = True

    def custom_headers(self) -> dict:
        return {
            # 'Remote-User': str(self.request.remote_user.id)
            'Remote-User': str(self.request.user.id)
        }
