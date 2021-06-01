from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Task
@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        current = Task.objects.filter(id = task_id)
        if len(current) != 0:
            current_task = current[0]
            current_task.delete()
            return HttpResponse(f"Task Done: '{current_task.name}'")
        else:
            return HttpResponse(f"There isn't any task with id '{task_id}'")            
