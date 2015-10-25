from django.shortcuts import render
from rest_framework import generics, response, status, permissions
from appclients import serializers, models


class GenerateKeyView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ClientListView(generics.ListAPIView):
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()
    paginate_by = 50

    def filter_queryset(self, q):
        return q.filter(user=self.request.user)

class SendView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.SendSerializer
    allowed_methods = ['post', 'get', 'options']

    def post(self, *args, **kwargs):
        return self.handle(args, kwargs)

    def get(self, *args, **kwargs):
        return self.handle(args, kwargs)


    def handle(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)

        if not serializer.is_valid():
            user = self.request.user
            if 'content' in serializer.data and user.is_authenticated():
                return self.send_pushes_and_ok(user, serializer.data['content'])
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        q = models.Client.objects.filter(apikey=data['apikey'])
        if not q.exists():
            return response.Response({'error': 'Non-existant apikey!'}, status.HTTP_401_UNAUTHORIZED)

        user = q[0].user

        return self.send_pushes_and_ok(user, data['content'])

    def send_pushes_and_ok(self, user, content):

        recipients = user.devices
        for recipient in recipients:
            recipient.send_message(content)

        return response.Response({'count': recipients.count(),
            'recipients': [r.registration_id for r in recipients]}, status=status.HTTP_200_OK)
