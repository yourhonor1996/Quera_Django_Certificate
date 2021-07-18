from django.test import TestCase

from library_management.models import Book
from library_management.utils import find_the_books


class LibraryTests(TestCase):

    fixtures = ['library_management/book.json']

    def test_1(self):
        the_books = find_the_books()
        books = list(Book.objects.all())
        for book in books:
            words = book.title.lower().split(' ')
            if words.count('the') == 1:
                self.assertTrue(book.pk in the_books)
            else:
                self.assertFalse(book.pk in the_books)