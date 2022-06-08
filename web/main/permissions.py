from rest_framework.permissions import BasePermission
from rest_framework.status import HTTP_200_OK
from django.core.cache import cache

from api.v1.auth_microservice.services import AuthorizationService


class AuthorizedAccess(BasePermission):
    def has_permission(self, request, view):
        if not request.headers.get('Authorization'):
            return False

        if token := request.headers.get('Authorization').split(' ')[1] \
                         and request.headers.get('Authorization').split(' ')[0] == 'Bearer':
            cache_key = cache.make_key('token', token)
            if cache_key in cache:
                return True
            service = AuthorizationService(request=request, url='/api/v1/verify-jwt/')
            response = service.service_response(method="post", data={"token": token})
            cache.set(cache_key, response.data, timeout=600)
            return bool(response.status_code == HTTP_200_OK)
        return False
