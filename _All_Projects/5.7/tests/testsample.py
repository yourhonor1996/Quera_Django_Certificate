from django.test import TestCase

from mobilestore import queries
from mobilestore.models import Brand, Mobile

class TestTasks(TestCase):
    fixtures = ('store',)

    def test_list_all_brands(self):
        solution = Brand.objects.all()
        answer = queries.list_all_brands()
        self.assertQuerysetEqual(solution, answer, ordered=False, transform=lambda x: x)

    def test_most_expensive_mobile(self):
        solution = Mobile.objects.order_by('-price').first()
        answer = queries.most_expensive_mobile()
        self.assertEqual(solution.id, answer.id)
