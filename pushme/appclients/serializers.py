from rest_framework import serializers
from appclients import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        write_only_fields = (
            'name',
        )
        read_only_fields = (
            'apikey',
            'user'
        )
    def create(self, validated_data):
        c = models.Client(**validated_data)
        c.generate_api_key()
        return c
