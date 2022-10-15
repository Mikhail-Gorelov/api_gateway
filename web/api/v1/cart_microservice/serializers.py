from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    product_variant_id = serializers.IntegerField()


class ItemDeleteSerializer(serializers.Serializer):
    product_variant_id = serializers.IntegerField(min_value=1)


class ItemOrderSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
    product_variant_id = serializers.IntegerField(min_value=1)
