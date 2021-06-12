from bs4 import BeautifulSoup
from django.test import TestCase, Client


class TestHotSeatForm(TestCase):
    def setUp(self):
        self.client = Client()
        response = self.client.get('http://localhost:8000/')
        body = response.content.decode('utf-8')
        soup = BeautifulSoup(body, 'html.parser')
        self.form = soup.find('form')
        self.csrf = self.form.input

    def test_form_appeared(self):
        self.assertIsNotNone(self.form)
