from rest_framework import serializers


class PaginationQuerySerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False)
    page_size = serializers.IntegerField(required=False, max_value=100)
