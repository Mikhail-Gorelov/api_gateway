from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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


