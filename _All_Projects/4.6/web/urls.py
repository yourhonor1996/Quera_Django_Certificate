from django.urls import path

from .views import *

urlpatterns = [
    path('sad/<str:name>/', make_sad),
    path('happy/<str:name>/<int:times>/', make_happy)
]
