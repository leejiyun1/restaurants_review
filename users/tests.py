from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            nickname="tester",
            password="securepassword"
        )

    def test_user_manager_create_user(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("securepassword"))
        self.assertFalse(self.user.is_superuser)

    def test_user_manager_create_superuser(self):
        admin = User.objects.create_superuser(
            email="admin@example.com",
            nickname="admin",
            password="adminpassword"
        )
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
