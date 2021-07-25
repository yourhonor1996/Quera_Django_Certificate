
from .models import Profile, User 
from django.http import HttpRequest


class ProfileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request:HttpRequest):
        try:
            username = request.user.get_username()
            # username = request.POST.get('username')
        except User.DoesNotExist:
            pass

        try:
            profile = Profile.objects.get(user__username= username)
            request.profile = profile
        except Profile.DoesNotExist:
            pass
        
        
        response = self.get_response(request)
        return response