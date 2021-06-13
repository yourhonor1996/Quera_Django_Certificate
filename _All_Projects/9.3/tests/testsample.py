from django.test import TestCase, Client
from musician_list_app.views import *
from musician_list_app.models import Musician, Album


class TestMusicianList(TestCase):
    def setUp(self):
        self.client = Client()

    def test_Musician_list_1(self):
        Musician.objects.create(name="ali", instrument="Accordion")
        musicians_name = ['ali']
        all_names = ""
        for musician_name in musicians_name:
            all_names += musician_name
        response = self.client.get('/musician_list_app/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(all_names), str(response.content.decode("utf-8")))
