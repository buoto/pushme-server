from django.shortcuts import render
from rest_framework import generics, response
from appclients import serializers


class GenerateKeyView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer
    http_method_names = ['post', 'options']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


