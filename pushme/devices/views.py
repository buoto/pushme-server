from django.shortcuts import render
from rest_framework import generics, response
from push_notifications.models import GCMDevice
from push_notifications.api.rest_framework import GCMDeviceSerializer


class GCMRegisterView(generics.CreateAPIView):
    serializer_class = GCMDeviceSerializer
    device_class = GCMDevice
    http_method_names = ['post', 'options']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GCMDevicesList(generics.ListAPIView):
    serializer_class = GCMDeviceSerializer
    queryset = GCMDevice.objects.all()
    paginate_by = 50

    def filter_queryset(self, q):
        return q.filter(user=self.request.user)

