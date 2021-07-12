from django.shortcuts import render
from accounts.models import User

def about_us(request):
    users = User.objects.all()
    context = {'users':users}
    # View for about-us page
    return render(request, 'about_us.html', context= context)
