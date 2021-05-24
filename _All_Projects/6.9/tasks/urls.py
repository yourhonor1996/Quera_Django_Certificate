from django.urls import path

from .views import list_create_tasks

urlpatterns = [
    path('tasks/', list_create_tasks),
]
