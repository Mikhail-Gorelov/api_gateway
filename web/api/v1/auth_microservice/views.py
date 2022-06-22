from datetime import datetime, timedelta
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache

from .serializers import TokenRefreshSerializer
from .services import AuthorizationService

from . import serializers


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-in/')
        response = service.service_response(method="post", data=serializer.data)
        token = response.data.get('access_token')
        cache_key = cache.make_key('access_token', token)
        cache.set(cache_key, response.data, timeout=timedelta(minutes=30).total_seconds())
        return Response(response.data)


class SignUpEmailView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SignUpEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-up/email/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class SignUpPhoneView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SignUpPhoneSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-up/phone/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class VerifyEmailView(CreateAPIView):
    serializer_class = serializers.VerifyEmailSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/verify-email/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class PasswordResetView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/password/reset/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class PasswordResetConfirmView(CreateAPIView):
    serializer_class = serializers.PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/password/reset/confirm/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        service = AuthorizationService(request=request, url='api/v1/logout/')
        response = service.service_response(method="post")
        # cache_key = cache.make_key('access_token', response.data['access_token'])
        # if cache_key in cache:
        #     cache.delete(cache_key)
        return Response(response.data)


class GetUserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = AuthorizationService(request=request, url='/api/v1/user-profile/')
        response = service.service_response(method="get")
        return Response(response.data)


class TokenRefreshView(CreateAPIView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/refresh-jwt/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)
