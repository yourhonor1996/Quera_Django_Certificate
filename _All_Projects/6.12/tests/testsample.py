from django.test import TestCase, Client

from tasks.models import Task


class TestSampleTasks(TestCase):
    fixtures = ('tasks',)

    def setUp(self):
        self.client = Client()

    def test_sample_delete_existing_task(self):
        task_id = 3
        task = Task.objects.get(id=task_id)
        response = self.client.delete('/tasks/{}/delete/'.format(task_id))
        self.assertEqual(response.status_code, 200)

        expected = "Task Done: '{}'".format(task)
        content = response.content.decode('utf-8').strip()
        self.assertEqual(expected, content)

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)
