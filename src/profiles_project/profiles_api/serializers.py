from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for test API view."""

    name = serializers.CharField(max_length=30)
