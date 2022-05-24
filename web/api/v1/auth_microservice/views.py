from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

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
        return Response(response.data)


class SignUpView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthorizationService(request=request, url='api/v1/sign-up/')
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
        return Response(response.data)
