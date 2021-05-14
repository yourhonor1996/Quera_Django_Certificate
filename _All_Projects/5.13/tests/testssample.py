from django.test import TestCase
from modelapp.models import Book


class TestAll(TestCase):

    def test_sample_sort_by_rate1(self):
        Book.objects.create(name="Book 1", rate=1)
        Book.objects.create(name="Book 2", rate=2)
        book_objects = list(Book.objects.sort_by_rate())
        self.assertEqual(book_objects[0].rate, 2)
