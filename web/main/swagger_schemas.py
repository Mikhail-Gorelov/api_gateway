from rest_framework import serializers


class PaginationQuerySerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False)
    page_size = serializers.IntegerField(required=False, max_value=100)
    sort_by_rating = serializers.BooleanField(required=False)
    price_from = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)
    price_to = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)


class ProductVariantsSerializer(serializers.Serializer):
    price_from = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)
    price_to = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)
