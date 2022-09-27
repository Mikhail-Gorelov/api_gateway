from main.swagger_schemas import PaginationQuerySerializer, ProductVariantsSerializer, ProductsSearchSerializer

tags = ['Product']

hot_products_get_schema = {
    'query_serializer': PaginationQuerySerializer,
    'operation_description': 'Return the most popular products',
    'operation_summary': 'Hot products list',
    'tags': tags
}

hot_product_get_schema = {
    'query_serializer': ProductVariantsSerializer,
    'operation_description': 'Return relevant product variants',
    'operation_summary': 'Hot product',
}

category_get_schema = {
    'tags': tags
}

search_product_get_schema = {
    'query_serializer': ProductsSearchSerializer
}
