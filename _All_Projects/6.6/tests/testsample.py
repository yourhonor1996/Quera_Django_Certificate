import re

from django.test import TestCase, Client

from tasks.models import Task


class TestSampleTasks(TestCase):
    fixtures = ('tasks',)

    def setUp(self):
        self.client = Client()

    def test_sample_list_all_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        expected = '\n'.join(Task.objects.order_by('name').values_list('name', flat=True)).strip()
        content = response.content.decode('utf-8').strip()
        content = re.sub(r"<(?:[ ]+)?[b][r](?:[ ]+)?(?:[/])?(?:[ ]+)?>", "\n", content)
        self.assertEqual(expected, content)
