from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User

class UserAPIViewTestCase(APITestCase):
    def setUp(self):
        self.signup_url = reverse('user-signup')
        self.login_url = reverse('user-login')
        self.user = User.objects.create_user(
            nickname='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_signup(self):
        response = self.client.post(self.signup_url, {
            'nickname': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123'
        })
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        response = self.client.post(self.login_url, {
            'email': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 200)

    def test_user_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'email': 'test@example.com',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 400)
