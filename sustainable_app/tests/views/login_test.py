from django.contrib import auth
from django.test import TestCase
from django.shortcuts import reverse

from sustainable_app.models import User


class LoginViewTests(TestCase):
    def setUp(self):
        """
        creates a user for testing
        """
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

    def test_call_view_as_user(self):
        """
        checks the login page redirects to home when we are logged in
        """
        
        # normal user
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('login'), follow=True)
        self.assertRedirects(response, reverse('home'))
        
         # check for post as well
        response = self.client.post(reverse('login'), {}, follow=True)
        self.assertRedirects(response, reverse('home'))
        
        # game keeper
        self.user.game_keeper = True
        self.user.save()
        response = self.client.get(reverse('login'), follow=True)
        self.assertRedirects(response, reverse('game_keeper'))
        
        # check for post as well
        response = self.client.post(reverse('login'), {}, follow=True)
        self.assertRedirects(response, reverse('game_keeper'))

       
        
        

    def test_post_view_for_login(self):
        """
        check the user is succeessfully logged in
        upon correct username/password
        """
        
        # normal user
        self.assertFalse(auth.get_user(self.client).is_authenticated)

        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        }, follow=True)

        self.assertTrue(auth.get_user(self.client).is_authenticated)
        self.assertRedirects(response, reverse('home'))
        
        # logout
        self.client.logout()
        
        # game keeper
        self.assertFalse(auth.get_user(self.client).is_authenticated)
        self.user.game_keeper = True
        self.user.save()
        
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        }, follow=True)
        
        self.assertTrue(auth.get_user(self.client).is_authenticated)
        self.assertRedirects(response, reverse('game_keeper'))

    def test_post_view_for_incorrect_login(self):
        """
        check the user is given an error upon logging in
        with incorrect details
        """
        self.assertFalse(auth.get_user(self.client).is_authenticated)

        response = self.client.post(reverse('login'), {
            'username': 'wrong-username',
            'password': 'wrong-password'
        }, follow=True)

        self.assertFalse(auth.get_user(self.client).is_authenticated)
        self.assertTemplateUsed(response, "sustainable_app/login.html")
