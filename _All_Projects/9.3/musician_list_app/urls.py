from django.contrib import admin
from django.urls import include, path

from .views import Musician_list

urlpatterns = [
    path('', Musician_list.as_view(), name='musician_list'),
]