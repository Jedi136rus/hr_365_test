from rest_framework import serializers


class SwaggerGETdashSerializer(serializers.Serializer):
    base = serializers.CharField()
    to = serializers.CharField()
    value = serializers.FloatField()
