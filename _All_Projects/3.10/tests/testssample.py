from django.test import TestCase, Client
from modelapp.models import User


class TestAll(TestCase):

    def test_User_name(self):
        user = User.objects.create(name="user", password="pass", score=2)
        self.assertEqual("user", user.name)
