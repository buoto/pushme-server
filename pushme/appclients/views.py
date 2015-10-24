from django.shortcuts import render
from rest_framework import generics, response
from appclients import serializers, models


class GenerateKeyView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer

    def perform_create(self, serializer):
        client = serializer.save(user=self.request.user)

class ClientListView(generics.ListAPIView):
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()
    paginate_by = 50

    def filter_queryset(self, q):
        return q.filter(user=self.request.user)
