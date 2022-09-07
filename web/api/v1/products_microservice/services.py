from django.conf import settings
from microservice_request.services import MicroServiceConnect


class ProductsService(MicroServiceConnect):
    api_key = settings.PRODUCTS_API_KEY
    service = settings.PRODUCTS_API_URL
    PROXY_REMOTE_USER = True
    SEND_COOKIES = True

    def custom_headers(self) -> dict:
        headers = {'Host': self.request.get_host()}
        if user := self.request.remote_user:
            headers['Remote-User'] = str(user.id)
        return headers


class SetChannelCookieService:
    def __init__(self, request, response, microservice_response):
        self.request = request
        self.response = response
        self.microservice_response = microservice_response

    def get_current_channel(self):
        try:
            return next(item for item in self.microservice_response.data.get('results')
                        if item["country"] == self.request.data.get('country'))
        except StopIteration:
            return {'country': 'DE'}

    def set_channel_cookie(self):
        self.response.set_cookie(
            key=settings.CHANNEL_SETTINGS['COOKIE_NAME'],
            value=self.get_current_channel(),
            max_age=settings.CHANNEL_SETTINGS['CACHE_ACTIVE_CHANNELS_TIMEOUT'],
        )
