from django.urls import path

from library_management.views import books

urlpatterns = [
    path('books/<str:genre>/', books),
]
