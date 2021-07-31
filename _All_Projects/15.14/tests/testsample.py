from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Profile


class SignalTest(TestCase):

    def test_profile_signal(self):
        user = User.objects.create_user(username='someuser', password='somestrongpassword')
        try:
            Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            self.fail("profile signal not working")
