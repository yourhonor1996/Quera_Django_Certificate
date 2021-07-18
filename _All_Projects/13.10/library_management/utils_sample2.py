from library_management.models import Book


def find_the_books():
    books = list(Book.objects.all())
    new_books = []
    for book in books:
        words = book.title.split(' ')
        if words.count('the') == 1:
            new_books.append(book.pk)
    return new_books
