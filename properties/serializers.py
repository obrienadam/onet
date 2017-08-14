from rest_framework import serializers

class PropertySerializer(serializers.Serializer):
    substance = serializers.CharField(max_length=128)
    symbol = serializers.CharField(max_length=128)
