from __future__ import unicode_literals
from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.contrib.auth import get_user_model

"""
Started the tests for the web-application.
Additional tests required. 
"""


class PageOpenTestCase(TestCase):
    def test_home_page_exists(self):
        url = reverse('home')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_about_page_exists(self):
        url = reverse('about')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_profile_page_exists_with_a_sample_user(self):
        pass


User = get_user_model()


class ProfileTestCase(TestCase):
    def test_profiles_created(self):
        u = User.objects.create_user(email="dummy@example.com")
        self.assertIsNotNone(u.profile)
