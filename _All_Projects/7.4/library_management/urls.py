from django.conf.urls import url

from library_management import views

urlpatterns = [
    url('booklist/', views.booklist, name='booklist')
]