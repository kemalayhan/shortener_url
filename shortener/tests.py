from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth.models import User

from shortener.models import UrlShortener


class UrlShortenerAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username='testuser',
            email='testuser@user.com',
        )
        user.set_password('testpassword')
        user.save()

    def login_get_token(self):
        url = api_reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        token = response.data.get('access', 0)
        if token is not None:
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
            return token
        return None

    def test_create_short_url(self):
        token = self.login_get_token()
        if token is not None:
            url = api_reverse('create_list_shortener')
            data = {
                'url': 'https://www.google.com/'
            }
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(UrlShortener.objects.count(), 1)

    def test_create_short_url_fail(self):
        url = api_reverse('create_list_shortener')
        data = {
            'url': 'https://www.google.com/'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status. HTTP_401_UNAUTHORIZED)

