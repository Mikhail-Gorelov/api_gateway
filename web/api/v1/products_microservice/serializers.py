from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from . import choices


class AssessmentSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    vote = serializers.ChoiceField(choices=choices.LikeChoice.choices)


class SetChannelCookieSerializer(serializers.Serializer):
    country = CountryField()
    currency_code = serializers.CharField(max_length=20)
