from main.swagger_schemas import PaginationQuerySerializer

tags = ['Product']

hot_products_get_schema = {
    'query_serializer': PaginationQuerySerializer,
    'operation_description': 'Return the most popular products',
    'operation_summary': 'Hot products list',
    'tags': tags
}

category_get_schema = {
    'tags': tags
}
