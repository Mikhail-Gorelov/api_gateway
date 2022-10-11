from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializers
from .services import CartService


class CartAddView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        service = CartService(request=request, url="/api/v1/cart/add/")
        response = service.service_response(method="post")
        return Response(response.data)


class ItemAddView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CartService(request=request, url="/api/v1/item/add/")
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class CartShowView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = CartService(request=request, url=f"/api/v1/cart/show/")
        response = service.service_response(method="get")
        return Response(response.data)


class CartTotalView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = CartService(request=request, url=f"/api/v1/cart/total/")
        response = service.service_response(method="get")
        return Response(response.data)


class ItemOrderAddView(GenericAPIView):
    serializer_class = serializers.ItemOrderSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CartService(request=request, url="/api/v1/item-order/add/")
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class ItemOrderShowDraftView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = CartService(request=request, url="/api/v1/item-order/show/draft/")
        response = service.service_response(method="get")
        return Response(response.data)
