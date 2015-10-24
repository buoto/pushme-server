from django.test import TestCase, Client
from accounts import factories
from accounts.models import User

class LoginViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.actor = User.objects.create_user('asd@asd.ru', 'xdd')

    def test_login_logs_in(self):
        response = self.client.post('/login', {'email':'asd@asd.ru', 'password': 'xdd'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.actor.auth_token.key, response.data['token'])

    def test_login_does_not_logs_in_when_incorrect_email(self):
        response = self.client.post('/login', {'email':'wrong@asd.ru', 'password': 'xdd'})
        self.assertEqual(response.status_code, 400)

    def test_login_does_not_logs_in_when_incorrect_password(self):
        response = self.client.post('/login', {'email':'asd@asd.ru', 'password': 'wrong_pass'})
        self.assertEqual(response.status_code, 400)

    def test_should_handle_wrong_req(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)

class RegistrationViewTest(TestCase):

    def test_should_create_user(self):
        response = self.client.post('/register', {'email':'asd@asd.ru', 'password': 'xdd'})
        self.assertEqual(response.status_code, 201)

        db_user = User.objects.get(email='asd@asd.ru')

        self.assertEqual(db_user.email, 'asd@asd.ru')

