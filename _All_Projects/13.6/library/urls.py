from django.urls import path, include

urlpatterns = [
    path('', include('library_management.urls'))
]
