from rest_framework import serializers
from . import choices


class AssessmentSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    vote = serializers.ChoiceField(choices=choices.LikeChoice.choices)
