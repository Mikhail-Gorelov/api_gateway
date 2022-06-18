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
    # product_service_mock = mocker.patch('api.v1.products_microservice.views.ProductsService.service_response')
    product_service_mock = mocker.patch.object(ProductsService, '_method')
    print(f'{product_service_mock()=}')
    product_service_mock().json.return_value = list_response
    product_service_mock().status_code = 200
    response = client.get(url)
    product_service_mock().assert_called_with(method='get', url='/api/v1/hot-products/', headers=self.headers)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    assert response.data == list_response

