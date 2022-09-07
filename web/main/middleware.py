import ast
from typing import TYPE_CHECKING, Optional

import pytz
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from main.services import RemoteUser, UserChannelService

if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.http import HttpResponse


class HealthCheckMiddleware(MiddlewareMixin):
    def process_request(self, request: 'HttpRequest') -> Optional[HttpResponse]:
        if request.META['PATH_INFO'] == settings.HEALTH_CHECK_URL:
            return HttpResponse('pong')


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: 'HttpRequest'):
        if tzname := request.COOKIES.get(getattr(settings, 'TIMEZONE_COOKIE_NAME', 'timezone')):
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)


class JWTRemoteUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: 'HttpRequest'):
        request.remote_user = None
        if header := request.headers.get('Authorization'):
            jwt = header.split(' ')[1]
        else:
            jwt = request.COOKIES.get('access_auth')
        if jwt:
            cache_key = cache.make_key('access_token', jwt)
            user_cache = cache.get(cache_key)
            if user_cache:
                request.remote_user = RemoteUser(**user_cache)
        # request.session['user_id'] = 1
        # request.session.modified = True
        # print(request.COOKIES, request.session.session_key)
        return self.get_response(request)


class UserChannelMiddleware(MiddlewareMixin):
    def process_response(self, request: 'HttpRequest', response: 'HttpResponse'):
        channel_cookie = response.cookies.get('reg_country')
        if not channel_cookie:
            handler = UserChannelService(request=request, response=response)
            handler.check_active_channels_cache_key()
        return response
