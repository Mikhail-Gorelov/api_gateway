from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import BaseFilterBackend
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
import coreapi
from rest_framework.views import APIView

from main.permissions import AuthorizedAccess, AuthorizedAuthentication
from main.swagger_schemas import PaginationQuerySerializer
from .services import ProductsService
from . import swagger_schemas as s


class SimpleFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='page',
            location='query',
            required=True,
            type='integer',
        ),
            coreapi.Field(
                name='page_size',
                location='query',
                required=True,
                type='integer'
        ),
        ]


class HotProductsView(APIView):
    # filter_backends = (SimpleFilterBackend,)
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**s.hot_products_get_schema)
    def get(self, request: Request):
        channel_cookie = {
            'country': 'RU',
            'currency_code': 'RUB',
        }
        service = ProductsService(request=request, url=f"/api/v1/hot-products/")
        response = service.service_response(method="get", data=channel_cookie, params=request.query_params)
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

    def get(self, request):
        service = ProductsService(request=request, url='/api/v1/product/')
        response = service.service_response(method="get")
        return Response(response.data)


class ProductDetailView(GenericAPIView):

    def get(self, request, **kwargs):
        service = ProductsService(request=request, url=f"/api/v1/product/{kwargs.get('pk')}")
        response = service.service_response(method="get")
        return Response(response.data)
