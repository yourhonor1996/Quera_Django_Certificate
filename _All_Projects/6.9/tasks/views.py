from django.views.decorators.csrf import csrf_exempt
# Other required imports here
from .models import Task
from django.http import HttpResponse

@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        Task.objects.create(name = task_name)
        return HttpResponse(f"Task Created: '{task_name}'")
