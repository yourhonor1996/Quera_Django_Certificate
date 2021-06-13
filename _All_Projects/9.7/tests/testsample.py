from django.test import TestCase, Client, RequestFactory
from sixinapp.views import MusicianListView, AlbumDetailView
from sixinapp.models import Musician, Album
from django.views.generic import ListView, DeleteView


class TestMusicianList(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        Musician.objects.create(name='farhad', instrument='Cello')
        Musician.objects.create(name='ali', instrument='Cello')
        Musician.objects.create(name='zahra', instrument='Cello')

    def test_ListView_subclass(self):
        self.assertTrue(MusicianListView, ListView)

    def test_DetailView_subclass(self):
        self.assertTrue(AlbumDetailView, DeleteView)