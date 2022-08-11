from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    product_variant_id = serializers.IntegerField()


class ItemOrderSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1)
    product_variant_id = serializers.IntegerField(min_value=1)
