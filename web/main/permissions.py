from rest_framework.authentication import BaseAuthentication
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


class AuthorizedAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
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

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        pass

# class JWTAuthentication(authentication.BaseAuthentication):
#     """
#     An authentication plugin that authenticates requests through a JSON web
#     token provided in a request header.
#     """
#
#     www_authenticate_realm = "api"
#     media_type = "application/json"
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user_model = get_user_model()
#
#     def authenticate(self, request):
#         header = self.get_header(request)
#         if header is None:
#             return None
#
#         raw_token = self.get_raw_token(header)
#         if raw_token is None:
#             return None
#
#         validated_token = self.get_validated_token(raw_token)
#
#         return self.get_user(validated_token), validated_token
#
#     def authenticate_header(self, request):
#         return '{} realm="{}"'.format(
#             AUTH_HEADER_TYPES[0],
#             self.www_authenticate_realm,
#         )
#
#     def get_header(self, request):
#         """
#         Extracts the header containing the JSON web token from the given
#         request.
#         """
#         header = request.META.get(api_settings.AUTH_HEADER_NAME)
#
#         if isinstance(header, str):
#             # Work around django test client oddness
#             header = header.encode(HTTP_HEADER_ENCODING)
#
#         return header
#
#     def get_raw_token(self, header):
#         """
#         Extracts an unvalidated JSON web token from the given "Authorization"
#         header value.
#         """
#         parts = header.split()
#
#         if len(parts) == 0:
#             # Empty AUTHORIZATION header sent
#             return None
#
#         if parts[0] not in AUTH_HEADER_TYPE_BYTES:
#             # Assume the header does not contain a JSON web token
#             return None
#
#         if len(parts) != 2:
#             raise AuthenticationFailed(
#                 _("Authorization header must contain two space-delimited values"),
#                 code="bad_authorization_header",
#             )
#
#         return parts[1]
#
#     def get_validated_token(self, raw_token):
#         """
#         Validates an encoded JSON web token and returns a validated token
#         wrapper object.
#         """
#         messages = []
#         for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
#             try:
#                 return AuthToken(raw_token)
#             except TokenError as e:
#                 messages.append(
#                     {
#                         "token_class": AuthToken.__name__,
#                         "token_type": AuthToken.token_type,
#                         "message": e.args[0],
#                     }
#                 )
#
#         raise InvalidToken(
#             {
#                 "detail": _("Given token not valid for any token type"),
#                 "messages": messages,
#             }
#         )
#
#     def get_user(self, validated_token):
#         """
#         Attempts to find and return a user using the given validated token.
#         """
#         try:
#             user_id = validated_token[api_settings.USER_ID_CLAIM]
#         except KeyError:
#             raise InvalidToken(_("Token contained no recognizable user identification"))
#
#         try:
#             user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})
#         except self.user_model.DoesNotExist:
#             raise AuthenticationFailed(_("User not found"), code="user_not_found")
#
#         if not user.is_active:
#             raise AuthenticationFailed(_("User is inactive"), code="user_inactive")
#
#         return user
