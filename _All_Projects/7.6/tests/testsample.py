from datetime import date
from django.test import TestCase, Client

from library_management.models import Book


class TestAll(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_sample(self):
        Book.objects.create(author='Saeid', title="first")
        Book.objects.create(author='Sajjad', title="second")
        
        response = self.cli.get('/booklist/')
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue('first' in response.content.decode('utf-8'))
        self.assertTrue('second' in response.content.decode('utf-8'))
        
        self.assertTrue('There are 2 books in the library.' in response.content.decode('utf-8'))
        self.assertTrue('/temp/library_management/booklist.css' in response.content.decode('utf-8'))