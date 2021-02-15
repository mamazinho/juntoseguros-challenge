from django.test import TestCase
from juntoseg.models import User

class ModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email = 'test@teste.com',
            name = 'teste',
            is_active = True
        )

    def test_user_model(self):
        record = User.objects.all().first()
        self.assertEqual(record, self.user)