from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializers
from .services import CheckoutService, PaymentService


class CheckoutView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CheckoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CheckoutService(request=request, serializer_data=serializer.data)
        output_data = service.validate_cart_content()
        output_data['email'] = serializer.data['credentials']['email']
        output_data['notes'] = serializer.data['order_notes']
        output_data['phone_number'] = serializer.data['credentials']['phone_number']
        payment_service = PaymentService(request=request, url='/api/v1/create-payment-intent/')
        response = payment_service.service_response(method="post", json=output_data)
        output_data['client_secret'] = response.data.get('clientSecret')
        return Response(output_data)
