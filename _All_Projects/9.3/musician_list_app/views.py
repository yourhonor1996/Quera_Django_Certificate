from django.shortcuts import render, HttpResponse
from .models import Musician, Album
from django.views import View

class Musician_list(View):
    # type your code here
    def get(self, request):
        musicians = Musician.objects.values_list('name', flat= True).order_by('name')
        return HttpResponse(musicians)
