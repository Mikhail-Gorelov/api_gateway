import logging
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
from urllib.parse import urlencode

import requests
from django.conf import settings
from django.core.cache import cache
from microservice_request.services import ConnectionService
from rest_framework.status import HTTP_200_OK

from main.utils import get_remote_ip_from_request, find_dict_in_list

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


def get_active_channels() -> list[dict]:
    channels_settings = settings.CHANNEL_SETTINGS
    cache_key = cache.make_key(channels_settings['CACHE']['KEY'])
    if _cache := cache.get(cache_key):
        return _cache
    service = CeleryProductsService(url=f"{channels_settings['GET_CHANNELS_URL']}")
    response = service.service_response(method="get")
    data: list[dict] = response.data
    cache.set(
        cache_key,
        data,
        timeout=channels_settings['CACHE']['TIMEOUT']
    )
    return data


class UserChannelService:

    def __init__(self, request: 'HttpRequest', response: 'HttpResponse') -> None:
        self.request = request
        self.response = response
        self.channel_settings = settings.CHANNEL_SETTINGS

    def get_ip_credentials(self) -> dict:
        ip_address = self.channel_settings.get('FORCED_IP_ADDRESS', get_remote_ip_from_request(self.request))
        ip_server_url = self.channel_settings.get('GET_IP_SERVER').format(ip_address=ip_address)
        r = requests.get(ip_server_url)
        if not r.status_code == HTTP_200_OK:
            logging.error(f'Ip server returned {r.status_code} {r.json()}')
            return {'id': 1, 'country': 'DE'}
        return r.json()

    def set_active_channels_cache_key(self) -> None:
        ip_credentials: dict = self.get_ip_credentials()
        channel_list: list[dict] = get_active_channels()
        current_channel = find_dict_in_list(channel_list, 'country', ip_credentials['country']) or {'country': 'DE'}
        self.set_channel_cookie(current_channel=current_channel)

    def set_channel_cookie(self, current_channel: dict):
        return self.response.set_cookie(
            key=self.channel_settings['COOKIE']['NAME'],
            value=urlencode(current_channel),
            max_age=self.channel_settings['CACHE']['TIMEOUT'],
            secure=self.channel_settings['COOKIE']['IS_SECURE'],
        )
