from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializers
from .services import CheckoutService


class CheckoutView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CheckoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CheckoutService(request=request, serializer_data=serializer.data)
        service.validate_cart_content()
        return Response(serializer.data)
