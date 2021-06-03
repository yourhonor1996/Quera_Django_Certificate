from django.shortcuts import render

from library_management.models import Book


def booklist(request):
    books = Book.objects.all()
    return render(request, 'booklist.html', context = {'books': books})