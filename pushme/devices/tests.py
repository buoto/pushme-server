from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from push_notifications import models as push_models

class GCMRegisterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor = User.objects.create_user('asd@asd.ru', 'xdd')
        self.client.force_authenticate(user=self.actor)

    def test_should_register_device(self):
        reg_id = 'asdfasdfasd'
        response = self.client.post('/gcms/register', {'registration_id': reg_id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(push_models.GCMDevice.objects.filter(registration_id=reg_id).exists())

class GCMDevicesListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor = User.objects.create_user('asd@asd.ru', 'xdd')
        self.client.force_authenticate(user=self.actor)

    def test_should_return_list_of_actiated_devices(self):
        push_models.GCMDevice.objects.create(user=self.actor, registration_id='asd')
        push_models.GCMDevice.objects.create(user=self.actor, registration_id='dsa')
        push_models.GCMDevice.objects.create(registration_id='qwe')

        response = self.client.get('/devices')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertItemsEqual([d['registration_id'] for d in response.data['results']], ['asd', 'dsa'])


