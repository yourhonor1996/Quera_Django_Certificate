from django.http import JsonResponse

from library_management.models import Book


def books(request, genre):
    return JsonResponse(data={
        'title': 'List of Books',
        'genre': genre,
        'books': list(Book.objects.filter(genre=genre).values_list('id', flat=True))
    })
