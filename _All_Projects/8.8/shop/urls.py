from django.urls import path
from .views import show_people, submit_person

urlpatterns = [
    path('people/', show_people),
    path('', submit_person),
]
