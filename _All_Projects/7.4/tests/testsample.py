from django.test import TestCase, Client

from library_management.models import Book


class TestAll(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_1(self):
        Book.objects.create(author='Saeid', title="one")
        Book.objects.create(author='Mohammad', title="two")
        Book.objects.create(author='Ali', title="three")
        response = self.cli.get('/booklist/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('one' in response.content.decode('utf-8'))
        self.assertTrue('two' in response.content.decode('utf-8'))
        self.assertTrue('three' in response.content.decode('utf-8'))