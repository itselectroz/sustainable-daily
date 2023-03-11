from django.contrib import auth
from django.test import TestCase
from django.shortcuts import reverse

from sustainable_app.models import User


class GameKeeperViewTests(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        
    def test_call_view_as_anonymous(self):
        """
        checks the game keeper page returns normally when we are not logged in
        """
        
        # game keeper page
        response = self.client.get(reverse('game_keeper'))
        self.assertRedirects(response, reverse('login'))
        
        # game keeper locations page
        response = self.client.get(reverse('game_keeper_locations'))
        self.assertRedirects(response, reverse('login'))
        
        # game keeper surveys page
        response = self.client.get(reverse('game_keeper_surveys'))
        self.assertRedirects(response, reverse('login'))
        
        # game keeper events page
        response = self.client.get(reverse('game_keeper_events'))
        self.assertRedirects(response, reverse('login'))
        
    def test_call_view_as_user(self):
        """
        checks the game keeper page redirects to home when we are logged in as a normal user
        """
        
        self.client.login(username=self.username, password=self.password)
        
        # game keeper page
        response = self.client.get(reverse('game_keeper'), follow=True)
        self.assertRedirects(response, reverse('home'))
        
        # game keeper locations page
        response = self.client.get(reverse('game_keeper_locations'), follow=True)
        self.assertRedirects(response, reverse('home'))
        
        # game keeper surveys page
        response = self.client.get(reverse('game_keeper_surveys'), follow=True)
        self.assertRedirects(response, reverse('home'))
        
        # game keeper events page
        response = self.client.get(reverse('game_keeper_events'), follow=True)
        self.assertRedirects(response, reverse('home'))
        
    def test_call_view_as_game_keeper(self):
        """
        checks the game keeper page redirects to game_keeper when we are logged in as a game keeper
        """
        self.user.game_keeper = True
        self.user.save()
        self.client.login(username=self.username, password=self.password)

        # game keeper page
        response = self.client.get(reverse('game_keeper'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sustainable_app/game_keeper.html")
        
        # game keeper locations page
        response = self.client.get(reverse('game_keeper_locations'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sustainable_app/game_keeper_locations.html")
        
        # game keeper surveys page
        response = self.client.get(reverse('game_keeper_surveys'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sustainable_app/game_keeper_surveys.html")
        
        # game keeper events page
        response = self.client.get(reverse('game_keeper_events'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sustainable_app/game_keeper_events.html")
        
