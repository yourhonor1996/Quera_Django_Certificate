from django.http import HttpResponse

def make_sad(request, name):
    return HttpResponse(f'Nobody likes you, {name}!')

def make_happy(request, name, times):
    msg = '<br>'.join([f'You are great, {name} :)' for i in range(times)])
    return HttpResponse(msg)