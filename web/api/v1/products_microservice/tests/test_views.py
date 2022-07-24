import pytest
from django.urls import reverse
from rest_framework import status
from api.v1.products_microservice.services import ProductsService

pytestmark = [pytest.mark.django_db]

@pytest.fixture()
def list_response():
    return {
        'count': 1,
        'next': 'string',
        'previous': None,
        'results': [
            {
                'id': 1,
            }
        ]
    }

def test_hot_products_list(client, mocker, list_response):
    url = reverse('api:v1:products_microservice:hot-products')
    product_service_mock = mocker.patch.object(ProductsService, '_method')
    channel_cookie = {
        'country': 'RU',
        'currency_code': 'RUB',
    }
    expected_headers = {
        'Content-Length': '',
        'Content-Type': 'text/plain',
        'User-Agent': 'python-requests/2.28.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Authorization': 'X-HTTP-KEY 3sgyqgmW.SftRAyxMLuuJdulTqrewFGUYLmqnWUJhPRODUCTSZZ',
        'Host': 'localhost:8002'
    }
    product_service_mock(method='get', url='/api/v1/hot-products/', headers=expected_headers, cookies=channel_cookie)
    product_service_mock.assert_called_once_with(method='get', url='/api/v1/hot-products/', headers=expected_headers, cookies=channel_cookie)
    product_service_mock().json.return_value = list_response
    product_service_mock().status_code = 200
    response = client.get(url)

    product_request_to_service = mocker.patch.object(ProductsService, 'request_to_service')
    product_request_to_service(method='get')
    product_request_to_service.assert_called_once_with(method='get')

    product_service_response = mocker.patch.object(ProductsService, 'service_response')
    product_service_response(method='get', url='/api/v1/hot-products/', headers=expected_headers, cookies=channel_cookie)
    product_service_response.assert_called_once_with(method='get', url='/api/v1/hot-products/', headers=expected_headers,
                                                 cookies=channel_cookie)

    assert product_service_mock.call_count == 4
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    assert response.data == list_response

