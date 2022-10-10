from rest_framework import serializers
from django_countries.serializer_fields import CountryField


class AssessmentSerializer(serializers.Serializer):
    product = serializers.IntegerField()


class SetChannelCookieSerializer(serializers.Serializer):
    country = CountryField()
    currency_code = serializers.CharField(max_length=20)
