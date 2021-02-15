# from rest_framework.test import APITestCase
# from rest_framework import status

# class RegisterAPITest(APITestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.create_user = {
#             'email': 'test@teste.com',
#             'name': 'teste',
#             'password': 'teste123',
#             'confirmPassword': 'teste123',
#         }

#     def test_post_user_api(self):
#         response = self.client.post('/register/', self.create_user)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)