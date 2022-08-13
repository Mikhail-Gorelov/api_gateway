from datetime import timedelta
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache

from .serializers import TokenRefreshSerializer
from .services import AuthorizationService

from . import serializers


class LoginEmailView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.LoginEmailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-in/email/')
        response = service.service_response(method="post", data=serializer.data)
        token = response.data.get('access_token')
        cache_key = cache.make_key('access_token', token)
        cache.set(cache_key, response.data['user'], timeout=timedelta(minutes=30).total_seconds())
        # response_gateway = Response(response.data, status=response.status_code)
        # response_gateway.set_cookie('Auth_Cookie', f'Bearer {token}', max_age=timedelta(minutes=30).total_seconds(),
        #                             samesite='Lax')
        # response_gateway.set_cookie('sessionid_api_gateway', response.data.get('session_id'))
        print(f'{response.cookies=}', cache.get(cache_key))
        return response


class LoginPhoneView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.LoginPhoneSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-in/phone/')
        response = service.service_response(method="post", data=serializer.data)
        token = response.data.get('access_token')
        cache_key = cache.make_key('access_token', token)
        cache.set(cache_key, response.data, timeout=timedelta(minutes=30).total_seconds())
        response_gateway = Response(response.data, status=response.status_code)
        response_gateway.set_cookie('Auth_Cookie', f'Bearer {token}', max_age=timedelta(minutes=30).total_seconds())
        return response_gateway


class SignUpEmailView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SignUpEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-up/email/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data, status=response.status_code)


class SignUpPhoneView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SignUpPhoneSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-up/phone/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data, status=response.status_code)


class VerifyView(CreateAPIView):
    serializer_class = serializers.VerifySerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/verify-user/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data, status=response.status_code)


class PasswordResetEmailView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.PasswordResetEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/password/reset/email/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data, status=response.status_code)


class PasswordResetPhoneView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.PasswordResetPhoneSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/password/reset/phone/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data, status=response.status_code)


class PasswordResetConfirmView(CreateAPIView):
    serializer_class = serializers.PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/password/reset/confirm/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data, status=response.status_code)


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        service = AuthorizationService(request=request, url='api/v1/logout/')
        response = service.service_response(method="post")
        # cache_key = cache.make_key('access_token', response.data['access_token'])
        # if cache_key in cache:
        #     cache.delete(cache_key)
        view_response = Response(response.data, status=response.status_code)
        view_response.delete_cookie('Auth_Cookie')
        view_response.delete_cookie('sessionid_api_gateway')
        return view_response


class GetUserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = AuthorizationService(request=request, url='/api/v1/user-profile/')
        response = service.service_response(method="get")
        print(request.headers)
        return Response(response.data, status=response.status_code)


class TokenRefreshView(CreateAPIView):
    serializer_class = TokenRefreshSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/refresh-jwt/')
        response = service.service_response(method="post", data=serializer.data)
        token = response.data.get('access')
        response_gateway = Response(response.data, status=response.status_code)
        response_gateway.set_cookie('Authorization', f'Bearer {token}', max_age=timedelta(minutes=30).total_seconds())
        return response_gateway


class ChangeUserPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ChangeUserPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='/api/v1/user-profile/set-password/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data, status=response.status_code)


class ChangeUserProfileView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ChangeUserProfileSerializer
    parser_classes = [MultiPartParser]

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='/api/v1/user-profile/change/')
        response = service.service_response(method="put", data=serializer.data)
        return Response(response.data, status=response.status_code)


class ChangeBillingAddressView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ChangeAddressSerializer

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='/api/v1/default-address/billing/change/')
        response = service.service_response(method="put", data=serializer.data)
        return Response(response.data, status=response.status_code)


class ChangeShippingAddressView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ChangeAddressSerializer

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='/api/v1/default-address/shipping/change/')
        response = service.service_response(method="put", data=serializer.data)
        return Response(response.data, status=response.status_code)
