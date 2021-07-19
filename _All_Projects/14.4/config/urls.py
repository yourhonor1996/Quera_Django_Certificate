from django.urls import path, include

urlpatterns = [
    path('upload/', include('upload_center.urls')),
]
