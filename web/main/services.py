import ast
import logging
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

import requests
from django.conf import settings
from django.core.cache import cache
from microservice_request.services import ConnectionService
from rest_framework.status import HTTP_200_OK

from main.utils import get_remote_ip_from_request

if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.http import HttpResponse


class CeleryProductsService(ConnectionService):
    api_key = settings.PRODUCTS_API_KEY
    service = settings.PRODUCTS_API_URL


@dataclass
class RemoteUser:
    id: int
    full_name: str
    email: Optional[str] = None
    phone_number: Optional[str] = None


class UserChannelService:

    def __init__(self, request: 'HttpRequest', response: 'HttpResponse') -> None:
        self.request = request
        self.response = response

    def get_ip_credentials(self) -> dict:
        channel_settings = settings.CHANNEL_SETTINGS
        ip_address = channel_settings.get('FORCED_IP_ADDRESS', get_remote_ip_from_request(self.request))
        ip_server_url = channel_settings.get('GET_IP_SERVER').format(ip_address=ip_address)
        r = requests.get(ip_server_url)
        if not r.status_code == HTTP_200_OK:
            logging.error(f'Ip server returned {r.status_code} {r.json()}')
            return {'country': 'DE'}
        return r.json()

    def check_active_channels_cache_key(self) -> None:
        ip_credentials = self.get_ip_credentials()
        if channel_cache := cache.keys(search=f'*{settings.CHANNEL_SETTINGS["CACHE_ACTIVE_CHANNELS_KEY"]}'):
            decoded_cache = self.decode_cache_key(channel_cache)
            current_channel = self.get_current_channel(decoded_cache=decoded_cache, ip_credentials=ip_credentials)
            self.set_channel_cookie(current_channel=current_channel)

    def decode_cache_key(self, channel_cookie: str) -> list[dict]:
        cache_list = list()
        decoded_cache = ast.literal_eval(channel_cookie[0].split(
            f'{settings.CHANNEL_SETTINGS["CACHE_ACTIVE_CHANNELS_KEY"]}'
        )[0].replace(':{', '{').replace('}:', '}'))
        cache_list.append(decoded_cache)
        return cache_list

    def get_current_channel(self, decoded_cache: list[dict], ip_credentials: dict):
        try:
            return next(item for item in decoded_cache if item['country'] == ip_credentials.get('country'))
        except StopIteration:
            return {'country': 'DE'}

    def set_channel_cookie(self, current_channel: dict):
        if self.request.COOKIES.get('reg_country'):
            return
        refresh_cookie_path = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE_PATH', '/')
        cookie_secure = getattr(settings, 'JWT_AUTH_SECURE', False)
        cookie_httponly = getattr(settings, 'JWT_AUTH_HTTPONLY', True)
        cookie_samesite = getattr(settings, 'JWT_AUTH_SAMESITE', 'Lax')
        return self.response.set_cookie(
            key=settings.CHANNEL_SETTINGS['COOKIE_NAME'],
            value=current_channel,
            max_age=settings.CHANNEL_SETTINGS['CACHE_ACTIVE_CHANNELS_TIMEOUT'],
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite,
            path=refresh_cookie_path,
        )
