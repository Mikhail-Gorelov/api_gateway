from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main.permissions import AuthorizedAccess
from . import swagger_schemas as s
from .services import ProductsService


class HotProductsView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**s.hot_products_get_schema)
    def get(self, request: Request):
        channel_cookie = {
            'country': 'RU',
            'currency_code': 'RUB',
        }
        service = ProductsService(request=request, url=f"/api/v1/hot-products/")
        print(f'{service=}')
        response = service.service_response(method="get", params=request.query_params, cookies=channel_cookie)
        print(f'{response=}')
        print(response.data)
        return Response(response.data)


class SecureView(GenericAPIView):
    permission_classes = (AuthorizedAccess,)

    # authentication_classes = (AuthorizedAuthentication,)

    def get(self, request):
        service = ProductsService(request=request, url='/api/v1/secure/')
        response = service.service_response(method="get")
        return Response(response.data)


class CategoriesView(GenericAPIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**s.category_get_schema)
    def get(self, request):
        service = ProductsService(request=request, url='/api/v1/categories/')
        response = service.service_response(method="get")
        return Response(response.data)


class ProductListView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = ProductsService(request=request, url='/api/v1/product/')
        response = service.service_response(method="get")
        return Response(response.data)


class ProductDetailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, **kwargs):
        service = ProductsService(request=request, url=f"/api/v1/product/{kwargs.get('pk')}")
        response = service.service_response(method="get")
        return Response(response.data)
