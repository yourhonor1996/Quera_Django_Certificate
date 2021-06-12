from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)


def submit_person(request):
    if request.method == 'GET':
        form = PersonalInformation()
        return render(request, 'new_person.html', {'form':form})

    elif request.method == 'POST':
        form = PersonalInformation(request.POST)
        if form.is_valid():
            person = Person()
            data = form.cleaned_data
            
            person.full_name = data['full_name']
            person.height = data['height']
            person.gender = data['gender']
            person.age = data['age']
            person.save()
            return HttpResponse(person, status= 201)
        return HttpResponse('Error', status= 400)
