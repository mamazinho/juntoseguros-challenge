from rest_framework.test import APITestCase
from rest_framework import status
from juntoseg.models import User

class LoginAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_login = {
            'email': 'test@teste.com',
            'password': 'teste123',
        }
        cls.user = User.objects.create(
            email = 'test@teste.com',
            name = 'teste',
            is_active = True
        )
        cls.user.set_password('teste123')
        cls.user.save()


    def test_login_api(self):
        response = self.client.post('/login/', self.user_login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
