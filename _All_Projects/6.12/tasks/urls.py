from django.urls import path

from .views import delete_task

urlpatterns = [
    path('tasks/<int:task_id>/delete/', delete_task),
]