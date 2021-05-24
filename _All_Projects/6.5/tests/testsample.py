from django.test import TestCase, Client

from library.models import Book
from library.render import render_to_readable_output


class BookFilterTest(TestCase):
    def setUp(self):
        self.client = Client()

        books = [
            Book(name='ketab1', author='author1', price=1),
            Book(name='ketab2', author='author2', price=2),
            Book(name='book3', author='author3', price=3),
            Book(name='book4', author='author4', price=2),
            Book(name='ketab5', author='author2', price=5),
            Book(name='ketab6', author='author2', price=10),
            Book(name='book7', author='author3', price=7),
            Book(name='book8', author='author1', price=12),
        ]
        Book.objects.bulk_create(books)

    def test_all_blank_params(self):
        response = self.client.get('/books/?max_price=&min_price=&author=&name=')
        self.assertEqual(response.status_code, 200)

        books = Book.objects.all()
        expected = render_to_readable_output(books)
        content = response.content.decode('utf-8')
        self.assertEqual(expected, content)

    def test_max_price_only(self):
        max_price = 2
        response = self.client.get('/books/?max_price={}'.format(max_price))
        self.assertEqual(response.status_code, 200)

        books = Book.objects.filter(price__lte=max_price)
        expected = render_to_readable_output(books)
        content = response.content.decode('utf-8')
        self.assertEqual(expected, content)
