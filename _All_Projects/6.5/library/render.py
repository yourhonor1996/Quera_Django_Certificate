def render_to_readable_output(books):
    """
    This function is not a VIEW. It is just a prettier for output.
    You just need to filter Books and give it to this function.

    For Example
        >>> from django.http import HttpResponse
        >>> from .models import Book
        >>> from .render import render_books_to_readable_output

        >>> def view_name(request):
        >>>     books = Book.objects.filter(name='Steve')
        >>>     output = render_books_to_readable_output(books)
        >>>     return HttpResponse(output)
    """
    books = books.order_by('name')
    splitter = '\n' + ('-' * 70) + '\n'
    output = splitter.join(map(str, books))
    return output
