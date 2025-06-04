from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User

class UserAPIViewTestCase(APITestCase):
    def setUp(self):
        self.signup_url = reverse('user-signup')
        self.login_url = reverse('token_obtain_pair')
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
        self.assertEqual(response.status_code, 401)

class JWTAuthTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            nickname="tester",
            password="password123"
        )

    def test_obtain_token(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        # 먼저 로그인해서 refresh 토큰 얻기
        token_url = reverse('token_obtain_pair')
        token_res = self.client.post(token_url, {
            "email": "test@example.com",
            "password": "password123"
        })
        refresh = token_res.data['refresh']

        # refresh 토큰으로 새 access 토큰 받기
        refresh_url = reverse('token_refresh')
        response = self.client.post(refresh_url, {"refresh": refresh})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
