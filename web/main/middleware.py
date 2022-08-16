from typing import TYPE_CHECKING, Optional
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
import pytz
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
import random

from main.services import RemoteUser

if TYPE_CHECKING:
    from django.http import HttpRequest


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
        # else:
            # if not request.session.session_key:
                # request.session = SessionStore()
                # request.session['user_id'] = random.randrange(0, 2000000)
                # request.session.create()
                # s = Session.objects.get(pk=request.session.session_key)
                # request.remote_user = RemoteUser(id=s.get_decoded().get('user_id'), full_name='AnonymousUser')
                # response = self.get_response(request)
                # response.set_cookie(
                #     settings.SESSION_COOKIE_NAME,
                #     request.session.session_key,
                #     expires=settings.SESSION_COOKIE_AGE,
                #     max_age=settings.SESSION_COOKIE_AGE
                # )
                # return self.get_response(request)
            # else:
            #     s = Session.objects.get(pk=request.session.session_key)
            #     request.remote_user = RemoteUser(id=s.get_decoded().get('user_id'), full_name='AnonymousUser')
        request.session['user_id'] = 1
        request.session.modified = True
        print(request.COOKIES, request.session.session_key)
        return self.get_response(request)
