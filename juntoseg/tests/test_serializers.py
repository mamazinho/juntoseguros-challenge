from django.test import TestCase
from juntoseg.models import User
from juntoseg.serializers import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class ModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@teste.com',
            name='teste',
            password='teste123',
        )
        self.user_change = {
            'email': 'test@teste.com',
            'token': 'test987654321',
            'password': 'teste321',
            'confirmPassword': 'teste321'
        }

    def test_register_serializer(self):
        serializer = RegisterSerializer(instance=self.user)
        self.assertEqual(serializer.data['email'], 'test@teste.com')

    def test_login_serializer(self):
        serializer = LoginSerializer(instance=self.user)
        self.assertEqual(serializer.data['email'], 'test@teste.com')

    def test_reset_password_serializer(self):
        serializer = ResetPasswordSerializer(instance=self.user)
        self.assertEqual(serializer.data['email'], 'test@teste.com')

    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(serializer.data['email'], 'test@teste.com')