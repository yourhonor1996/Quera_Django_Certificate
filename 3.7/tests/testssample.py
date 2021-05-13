from django.test import TestCase, Client
from modelapp.models import Factory, Car


class TestAll(TestCase):

    def test_factory_name(self):
        factory = Factory.objects.create(name="factory")
        self.assertEqual("factory", factory.name)
