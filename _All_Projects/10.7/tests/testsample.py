from django.contrib import admin
from django.test import TestCase

from store.models import Product


class CustomAdminTest(TestCase):
    fixtures = ['store']

    def setUp(self):
        self.prod_admin = admin.site._registry.get(Product)

    def test_product_models_is_registered(self):
        self.assertTrue(Product in admin.site._registry)

    def test_fieldsets_identification(self):
        answer_id, _ = self.prod_admin.fieldsets
        expected_id = ('Identification', {
            'fields': ('name', 'price', 'is_active')
        })
        self.assertEqual(expected_id[0], answer_id[0])
        self.assertDictEqual(expected_id[1], answer_id[1])
