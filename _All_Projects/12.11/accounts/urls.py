from django.urls import path

from .views import login
from .views import Logout, Register

urlpatterns = [
    path('login/', login),
    # Add Logout & Register
    path('logout/', Logout.as_view()),
    path('register/', Register.as_view())
]
