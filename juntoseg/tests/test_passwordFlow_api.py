from rest_framework.test import APITestCase
from rest_framework import status
from juntoseg.models import User

class PasswordFlowAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_email = {
            'email': 'test@teste.com'
        }
        cls.user = User.objects.create(
            email = cls.user_email['email'],
            name = 'teste',
            is_active = True
        )
        cls.user.set_password('teste123')
        cls.user.save()

        cls.changePassword = {
            'email': cls.user_email['email'],
            'token': '',
            'password': 'teste321',
            'confirmPassword': 'teste321'
        }

    def test_a_reset_password_api(self):
        response = self.client.post('/reset-password/', self.user_email)
        self.changePassword['token'] = response.json().get('token', '')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_b_change_password_api(self):
        response = self.client.patch('/change-password/', self.changePassword)
        self.assertEqual(response.status_code, status.HTTP_200_OK)