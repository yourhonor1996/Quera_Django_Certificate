# Needed imports here
from django.http import HttpResponse
from .models import Task

def list_create_tasks(request):
    if request.method == 'GET':
        tasks = '\n'.join(Task.objects.order_by('name').values_list('name', flat= True))
        return HttpResponse(tasks)


def count_tasks(request):
    if request.method == 'GET':
        count = Task.objects.count()
        return HttpResponse(f"You have '{count}' tasks to do")