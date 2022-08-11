from django.conf import settings
from microservice_request.services import MicroServiceConnect


class AuthorizationService(MicroServiceConnect):
    api_key = settings.AUTHORIZATION_API_KEY
    service = settings.AUTHORIZATION_API_URL
    SEND_COOKIES = True

    def custom_headers(self) -> dict:
        if self.request.COOKIES.get('Auth_Cookie') and self.request.COOKIES.get('Auth_Cookie').split(' ')[1] != 'None':
            return {
                'Authorization': self.request.COOKIES.get('Auth_Cookie'),
            }
        return {}
