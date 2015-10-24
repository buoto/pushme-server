from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse as Response
from django.views.generic import View
from accounts import models
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import generics
from rest_framework.authtoken import views as auth_views, models as auth_models
from accounts import serializers



class LoginView(auth_views.ObtainAuthToken):
    serializer_class = serializers.LoginUserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.CreateUserSerializer
    def perform_create(self, serializer):
        user = serializer.save()
