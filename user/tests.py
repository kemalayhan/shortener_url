from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth.models import User


class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username='testuser',
            email='testuser@user.com',
        )
        user.set_password('testpassword')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='testuser')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        url = api_reverse('register')
        data = {
            'username': 'userfail',
            'password': 'failpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['password2'][0], 'This field is required.'
        )

    def test_api_register(self):
        url = api_reverse('register')
        data = {
            'username': 'usersuccess',
            'password': 'secretpassword',
            'password2': 'secretpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_login(self):
        url = api_reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = len(response.data.get('access', 0))
        self.assertGreater(token, 0)
