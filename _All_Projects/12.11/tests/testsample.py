from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from accounts.models import User


class AccountTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'somebody', 'password': 'some_password'}
        self.user = User.objects.create_user(**self.user_data)

    def test_login(self):
        url = '/accounts/login/'
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        key = response.data.get('token')
        token_query_set = Token.objects.select_related('user').filter(key=key)
        self.assertTrue(token_query_set.exists())
        token = token_query_set.get()
        self.assertEqual(self.user, token.user)

    def test_register(self):
        url = '/accounts/register/'
        user_data = {
            'username': 'new_user',
            'password': 'strong_pwd',
        }
        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.filter(username=user_data['username'])
        self.assertTrue(user.exists())
