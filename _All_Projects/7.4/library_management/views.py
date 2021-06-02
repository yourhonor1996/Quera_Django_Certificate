from .models import Book
from django.shortcuts import render


def booklist(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'booklist.html', context = context)
