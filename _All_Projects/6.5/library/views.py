from django.http import HttpResponse

from .models import Book
from .render import render_to_readable_output


def book_list(request):
    min_price = request.GET.get('min_price') or 0
    # Other query parameters
    max_price = request.GET.get('max_price') or 100000
    author = request.GET.get('author') or ''
    name = request.GET.get('name') or ''

    # fill `.filter()` with query parameters
    all_books = Book.objects.filter(price__lte = max_price, price__gte= min_price, name__icontains= name, author__icontains= author )

    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)
