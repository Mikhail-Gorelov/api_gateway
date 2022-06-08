from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib.parse import urlencode
from requests import Response as RequestResponse

from main.permissions import AuthorizedAccess
from .services import ProductsService

from . import serializers


class HotProductsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        channel_cookie = {
            'country': 'RU',
            'currency_code': 'RUB',
        }
        service = ProductsService(request=request, url='/api/v1/hot-products/')
        response = service.service_response(method="get", data=channel_cookie)
        return Response(response.data)


class SecureView(GenericAPIView):
    permission_classes = (AuthorizedAccess,)

    def get(self, request):
        service = ProductsService(request=request, url='/api/v1/secure/')
        response = service.service_response(method="get")
        return Response(response.data)


class CategoriesView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = ProductsService(request=request, url='/api/v1/categories/')
        response = service.service_response(method="get")
        return Response(response.data)


class ProductListView(GenericAPIView):

    def get(self, request):
        service = ProductsService(request=request, url='/api/v1/product/')
        response = service.service_response(method="get")
        return Response(response.data)


class ProductDetailView(GenericAPIView):

    def get(self, request, **kwargs):
        service = ProductsService(request=request, url=f"/api/v1/product/{kwargs.get('pk')}")
        response = service.service_response(method="get")
        return Response(response.data)
