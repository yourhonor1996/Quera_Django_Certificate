from django.contrib import admin
from django.test import TestCase

from store.models import Product, Company, Address, Category


class CustomAdminTest(TestCase):
    fixtures = ['store']

    def setUp(self):
        self.prod_admin = admin.site._registry.get(Product)
        self.comp_admin = admin.site._registry.get(Company)
        self.addr_admin = admin.site._registry.get(Address)
        self.catg_admin = admin.site._registry.get(Category)

    def test_models_are_registered(self):
        self.assertTrue(Product in admin.site._registry)
        self.assertTrue(Company in admin.site._registry)
        self.assertTrue(Address in admin.site._registry)
        self.assertTrue(Category in admin.site._registry)
