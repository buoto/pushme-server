from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from appclients.models import Client

class GenerateKeyViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor = User.objects.create_user('asd@asd.ru', 'xdd')
        self.client.force_authenticate(user=self.actor)

    def test_gen_key_should_create_client_and_return_201(self):
        name = "My script"
        response = self.client.post('/gen_key', {'name': name})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ClientTest(TestCase):
    def setUp(self):
        self.actor = User.objects.create_user('asd@asd.ru', 'xdd')

    def test_hash_is_not_empty(self):
        c = Client.objects.create(name='test client', user=self.actor)
        self.assertNotEqual(c.generate_api_key(), '')
