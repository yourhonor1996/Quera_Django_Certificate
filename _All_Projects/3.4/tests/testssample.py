from django.test import TestCase, Client
from modelapp.models import Book


class TestAll(TestCase):

    def test_book_name(self):
        book = Book.objects.create(name="book", rate=1)
        self.assertEqual("book", book.name)
