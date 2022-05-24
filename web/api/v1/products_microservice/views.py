from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib.parse import urlencode
from requests import Response as RequestResponse
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
