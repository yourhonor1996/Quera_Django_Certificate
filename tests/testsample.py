from django.test import TestCase, Client


class AboutUsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_works_fine(self):
        response = self.client.get('/about-us/')
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "نیکوکاران و اعضای خیریه‌ها")
