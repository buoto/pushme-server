from rest_framework import serializers
from appclients import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'id',
            'name',
            'apikey',
            'created_at',
        )
        read_only_fields = (
            'id',
            'apikey',
            'created_at',
        )

