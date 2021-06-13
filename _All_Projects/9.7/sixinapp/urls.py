from django.urls import path

from .views import MusicianListView, AlbumDetailView

urlpatterns = [
    path('musician_list/', MusicianListView.as_view(), name='musician_list'),
    path('album_detail/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
]

