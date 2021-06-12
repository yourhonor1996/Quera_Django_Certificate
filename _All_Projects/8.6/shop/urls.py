from django.urls import path
from .views import personal_page

urlpatterns = [
    path('', personal_page)
]
