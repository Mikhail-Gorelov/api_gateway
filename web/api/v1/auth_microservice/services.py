from django.conf import settings
from microservice_request.services import MicroServiceConnect


class AuthorizationService(MicroServiceConnect):
    api_key = settings.AUTHORIZATION_API_KEY
    service = settings.AUTHORIZATION_API_URL

    def custom_headers(self) -> dict:
        return {
            'Authorization': self.request.headers.get('Authorization'),
        }
