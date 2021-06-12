from django.test import TestCase, Client

from shop.forms import PersonalInformation


class TestPersonalForm(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_is_valid(self):
        form_data = {
            'gender': 'm',
            'full_name': 'Mohammad This Is Title Jafari',
            'age': 38,
            'height': 210
        }
        form = PersonalInformation(data=form_data)
        self.assertTrue(form.is_valid())
