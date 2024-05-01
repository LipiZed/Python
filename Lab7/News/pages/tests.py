from django.test import TestCase

from django.urls import reverse, resolve

from .views import HomePageView

class TestPages(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_information(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Log in')
        self.assertContains(self.response, 'Sign up')
        self.assertTemplateUsed(self.response, 'home.html')

    def test_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
