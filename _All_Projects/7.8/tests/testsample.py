from datetime import date
from django.test import TestCase, Client

from library_management.models import Book


class TestAll(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_sample(self):
        Book.objects.create(author='Saeid', title="first", available=True)
        Book.objects.create(author='Mohammad', title="second", available=True)
        Book.objects.create(author='Ali', title="third", available=False)
        Book.objects.create(author='Sajjad', title="fourth", available=True)
        Book.objects.create(author='Farhad', title="fifth", available=False)
        
        response = self.cli.get('/booklist/')
        
        self.assertEqual(response.status_code, 200)
        
        self.assertTrue('Saeid wrote first.' in response.content.decode('utf-8'))
        self.assertTrue('Mohammad wrote second.' in response.content.decode('utf-8'))
        self.assertFalse('Ali wrote third.' in response.content.decode('utf-8'))
        self.assertFalse('Sajjad wrote second.' in response.content.decode('utf-8'))
        self.assertFalse('Farhad wrote fifth.' in response.content.decode('utf-8'))