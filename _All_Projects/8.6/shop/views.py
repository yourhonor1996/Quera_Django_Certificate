from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Person
from .forms import PersonalInformation

@csrf_exempt
def personal_page(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'main.html', context)

    elif request.method == 'POST':
        form = PersonalInformation(request.POST)
        if form.is_valid():
            person = Person()
            data = form.cleaned_data

            person.gender = data['gender']
            person.full_name = data['full_name']
            person.height = data['height']
            person.age = data['age']
            person.save()
            return HttpResponse(person, status= 201)
    return HttpResponse('Error', status= 400)