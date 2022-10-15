from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . import serializers


class CheckoutView(GenericAPIView):
    serializer_class = serializers.CheckoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
