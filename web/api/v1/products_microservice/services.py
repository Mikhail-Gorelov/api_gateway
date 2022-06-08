from django.conf import settings
from microservice_request.services import MicroServiceConnect

class ProductsService(MicroServiceConnect):
    api_key = settings.PRODUCTS_API_KEY
    service = settings.PRODUCTS_API_URL

    def custom_headers(self) -> dict:
        return {'Host': self.request.get_host()}
