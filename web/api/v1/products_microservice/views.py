from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from main.permissions import AuthorizedAccess
from . import swagger_schemas as s
from .services import ProductsService


class HotProductsView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**s.hot_products_get_schema)
    def get(self, request: Request):
        channel_cookie = {
            'country': 'DE',
            'currency_code': 'EUR',
        }
        service = ProductsService(request=request, url=f"/api/v1/products/")
        response = service.service_response(method="get", params=request.query_params, cookies=channel_cookie)
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
        service = ProductsService(request=request, url=f"/api/v1/product/{kwargs.get('pk')}/")
        response = service.service_response(method="get")
        return Response(response.data)


class HotProductsDetailView(GenericAPIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**s.hot_product_get_schema)
    def get(self, request, *args, **kwargs):
        channel_cookie = {
            'country': 'DE',
            'currency_code': 'EUR',
        }
        service = ProductsService(request=request, url=f"/api/v1/product/{kwargs.get('pk')}/")
        response = service.service_response(method="get", params=request.query_params, cookies=channel_cookie)
        return Response(response.data)


class AssessmentView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AssessmentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = ProductsService(request=request, url=f"/api/v1/assessment/")
        response = service.service_response(method="post", data=serializer.data)
        return Response(response.data)


class CategoriesDetailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        service = ProductsService(request=request, url=f"/api/v1/category/{kwargs.get('pk')}/")
        response = service.service_response(method="get")
        return Response(response.data)
