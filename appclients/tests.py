from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from appclients.models import Client

class GenerateKeyViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor = User.objects.create_user('asd@asd.ru', 'pass')
        self.client.force_authenticate(user=self.actor)

    def test_gen_key_should_create_client_and_return_201(self):
        name = "My script"
        response = self.client.post('/gen_key', {'name': name})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        db_client = Client.objects.get(user=self.actor)
        self.assertEqual(db_client.name, name)
        self.assertTrue(len(db_client.apikey) > 5)

class ClientListTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.actor = User.objects.create_user('asd@asd.ru', 'pass')
        self.client.force_authenticate(user=self.actor)

    def test_should_list_clients(self):
        name = "My script"
        another_user = User.objects.create_user('asdf@asd.ru', 'pass')
        c = Client.objects.create(name='test client', user=self.actor)
        c = Client.objects.create(name='My script', user=self.actor)
        c = Client.objects.create(name='Not mine script', user=another_user)
        response = self.client.get('/keys', {'name': name})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertItemsEqual([c['name'] for c in response.data['results']],
                ['test client', 'My script'])

class ClientTest(TestCase):
    def setUp(self):
        self.actor = User.objects.create_user('asd@asd.ru', 'pass')

    def test_hash_is_not_empty(self):
        c = Client.objects.create(name='test client', user=self.actor)
        self.assertTrue(len(c.regenerate_api_key()) > 5)
        c.refresh_from_db()
        self.assertTrue(len(c.apikey) > 5)

class SendViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.actor = User.objects.create_user('asd@asd.ru', 'pass')

    def test_returns_200(self):
        c = Client.objects.create(name='test client', user=self.actor)
        response = self.client.post('/send', {'apikey': c.apikey, 'content': 'asdsadasda'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_returns_401_when_nonexistant_apikey(self):
        response = self.client.post('/send', {'apikey': 'pass', 'content': 'asdsadasda'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_returns_400_on_bad_req(self):
        response = self.client.post('/send', {'token': 'pass', 'content': 'asdsadasda'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_send_with_token_authentication(self):
        self.client.force_authenticate(user=self.actor)
        response = self.client.post('/send', {'content': 'asdsadasda'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
