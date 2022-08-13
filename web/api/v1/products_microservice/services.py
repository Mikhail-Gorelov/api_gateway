from django.conf import settings
from microservice_request.services import MicroServiceConnect


class ProductsService(MicroServiceConnect):
    api_key = settings.PRODUCTS_API_KEY
    service = settings.PRODUCTS_API_URL
    PROXY_REMOTE_USER = True

    def custom_headers(self) -> dict:
        return {
            'Host': self.request.get_host(),
            'Remote-User': str(self.request.remote_user.id)
        }
