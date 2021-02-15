# from rest_framework.test import APITestCase
# from rest_framework import status

# class LoginAPITest(APITestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.user_login = {
#             'email': 'test@teste.com',
#             'password': 'teste123',
#         }
#         cls.create_user = {
#             'email': 'test@teste.com',
#             'name': 'teste',
#             'password': 'teste123',
#             'confirmPassword': 'teste123',
#         }


#     def test_login_api(self):
#         print('reess masss')
#         response = self.client.post('/register/', self.create_user)
#         print('reess', response)
#         response = self.client.post('/login/', self.user_login)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
