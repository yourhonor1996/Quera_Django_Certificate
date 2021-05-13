from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def signup_view(request):
    return HttpResponse('Sign up Completed!')