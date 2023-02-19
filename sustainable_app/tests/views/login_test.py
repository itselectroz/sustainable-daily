from django.contrib import auth
from django.test import TestCase
from django.shortcuts import reverse

from sustainable_app.models import User


class LoginViewTests(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)

    def test_call_view_as_anonymous(self):
        """
        checks the login page returns normally when we are not logged in
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sustainable_app/login.html")

    # TODO: change these two tests to home when we change login

    def test_call_view_as_user(self):
        """
        checks the login page redirects to home when we are logged in
        """
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('login'), follow=True)
        self.assertRedirects(response, reverse('profile'))

        # check for post as well
        response = self.client.post(reverse('login'), {}, follow=True)
        self.assertRedirects(response, reverse('profile'))

    def test_post_view_for_login(self):
        """
        check the user is succeessfully logged in upon correct username/password
        """
        self.assertFalse(auth.get_user(self.client).is_authenticated)

        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        }, follow=True)

        self.assertTrue(auth.get_user(self.client).is_authenticated)
        self.assertRedirects(response, reverse('profile'))

    def test_post_view_for_incorrect_login(self):
        """
        check the user is given an error upon logging in with incorrect details
        """
        self.assertFalse(auth.get_user(self.client).is_authenticated)

        response = self.client.post(reverse('login'), {
            'username': 'wrong-username',
            'password': 'wrong-password'
        }, follow=True)

        self.assertFalse(auth.get_user(self.client).is_authenticated)
        self.assertRedirects(response, reverse('login') + '?error=1')
