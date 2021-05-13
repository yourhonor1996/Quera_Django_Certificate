from django.test import TestCase, Client


class TestAll(TestCase):
    def setUp(self):
        self.client = Client()

    def test_1(self):
        response = self.client.get('/sad/yahya/')
        self.assertEqual(response.status_code, 200)

        content = response.content.decode('utf-8').strip()
        self.assertEqual('Nobody likes you, yahya!', content)
