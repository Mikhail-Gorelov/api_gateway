from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main.permissions import AuthorizedAccess
from . import serializers
from . import swagger_schemas as s
from .services import ProductsService, SetChannelCookieService


class HotProductsView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**s.hot_products_get_schema)
    def get(self, request: Request):
        service = ProductsService(request=request, url=f"/api/v1/products/")
        response = service.service_response(method="get", params=request.query_params)
        return response


class SecureView(GenericAPIView):
    permission_classes = (AuthorizedAccess,)

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
        service = ProductsService(request=request, url=f"/api/v1/product/{kwargs.get('pk')}/")
        response = service.service_response(method="get", params=request.query_params)
        return Response(response.data)


class ProductsVariantView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        service = ProductsService(request=request, url=f"/api/v1/product-variant/{kwargs.get('pk')}/")
        response = service.service_response(method="get")
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


class AssessmentShowView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        service = ProductsService(request=request, url="/api/v1/assessment/show/")
        response = service.service_response(method="get", params=request.query_params)
        return Response(response.data)


class CategoriesDetailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        service = ProductsService(request=request, url=f"/api/v1/category/{kwargs.get('pk')}/")
        response = service.service_response(method="get")
        return Response(response.data)


class ChannelListView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        service = ProductsService(request=request, url=f"/api/v1/channel-list/")
        response = service.service_response(method="get")
        return response


class SetChannelCookieView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.SetChannelCookieSerializer

    def post(self, request):
        service = ProductsService(request=request, url=f"{settings.CHANNEL_SETTINGS['GET_CHANNELS_URL']}")
        microservice_response = service.service_response(method="get")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = Response(data=serializer.data)
        handler = SetChannelCookieService(request=request,
                                          response=response,
                                          microservice_response=microservice_response
                                          )
        handler.set_channel_cookie()
        return response


class GetChannelCookieView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        if channel_cookie := request.COOKIES.get('reg_country'):
            return Response({'name': channel_cookie})
        return Response()


class SearchProductView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(**s.search_product_get_schema)
    def get(self, request: Request):
        service = ProductsService(request=request, url=f"/api/v1/search-products/")
        response = service.service_response(method="get", params=request.query_params)
        return response
