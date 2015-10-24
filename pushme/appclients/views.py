from django.shortcuts import render
from rest_framework import generics, response, status
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

class SendView(generics.GenericAPIView):
    serializer_class = serializers.SendSerializer
    allowed_methods = ['post', 'get', 'options']

    def post(self, *args, **kwargs):
        return self.handle(args, kwargs)

    def get(self, *args, **kwargs):
        return self.handle(args, kwargs)


    def handle(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        q = models.Client.objects.filter(apikey=data['apikey'])
        if not q.exists():
            return response.Response({'error': 'Non-existant apikey!'}, status.HTTP_401_UNAUTHORIZED)

        user = q[0].user
        recipients = user.devices
        for recipient in recipients:
            recipient.send_message(data['content'])

        return response.Response({'count': recipients.count(),
            'recipients': [r.token for r in recipients]}, status=status.HTTP_200_OK)
