"""pushme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin
from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet
import accounts.views
import devices.views
import appclients.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', accounts.views.LoginView.as_view()),
    url(r'^register', accounts.views.RegisterView.as_view()),
    url(r'^gcms/register', devices.views.GCMRegisterView.as_view()),
    url(r'^devices', devices.views.GCMDevicesList.as_view()),
    url(r'^gen_key', appclients.views.GenerateKeyView.as_view()),
    url(r'^keys', appclients.views.ClientListView.as_view()),
]
