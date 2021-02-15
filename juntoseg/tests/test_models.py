from django.test import TestCase
from juntoseg.models import User
from datetime import datetime

class ModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email = 'test@teste.com',
            name = 'teste',
            created_at = datetime.now(),
            updated_at = datetime.now(),
            is_admin = False,
            is_active = True
        )

    def test_user_model(self):
        record = User.objects.all().first()
        self.assertEqual(record, self.user)