from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from ..checkout.services import PaymentService


class CreateCheckoutSessionView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CreateCheckoutSessionSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = PaymentService(request=request, url='/api/v1/create-checkout-session/')
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class StripeWebhookView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = None

    def post(self, request):
        service = PaymentService(request=request, url='/api/v1/webhooks/stripe/')
        response = service.service_response(method="post")
        return Response(response.data)
