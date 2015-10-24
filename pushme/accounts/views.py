from django.shortcuts import render
from accounts import models
from rest_framework import generics, permissions, status, response
from rest_framework.authtoken import views as auth_views, models as auth_models
from accounts import serializers



class LoginView(auth_views.ObtainAuthToken):
    serializer_class = serializers.LoginUserSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CreateUserSerializer


    def perform_create(self, serializer):
        user = serializer.save()
        auth_models.Token.objects.get_or_create(user=user)
