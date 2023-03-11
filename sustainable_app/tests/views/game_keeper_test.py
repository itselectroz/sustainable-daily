
from django.test import TestCase
from django.shortcuts import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from sustainable_app.models import User, Location


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
            
    def test_post_view_locations_add_and_remove(self):
        """
        check the location is successfully added and removed
        """
        
        self.user.game_keeper = True
        self.user.save()
        self.client.login(username=self.username, password=self.password)
        
        #----- add location -----
        
        # test image file
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        test_image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        
        # post request for adding location
        self.client.post(reverse('locations_add'), {
            'name': 'test-name',
            'category': 'test-category',
            'clue': 'test-clue',
            'image': test_image,
        }, follow=True)
        
        self.assertTrue(Location.objects.get(name='test-name'))
        Location.objects.get(name='test-name').image.delete()
        Location.objects.get(name='test-name').qr.delete()
        
        #----- remove location -----
        
        # post request for removing location
        self.client.post(reverse('locations_remove'), {
            'location_id': Location.objects.get(name='test-name').id,
        }, follow=True)
        
        self.assertTrue(Location.objects.filter(name='test-name').exists() == False)
        

    def test_post_view_remove_game_keeper(self):
        """
        check the game keeper is sucessfully removed
        """
        
        self.user.game_keeper = True
        self.user.save()
        self.client.login(username=self.username, password=self.password)
        
        # create game keeper to delete (setup)
        new_keeper = User(username='test-username', email='test-email', password='test-password')
        new_keeper.game_keeper = True
        new_keeper.save()
        
        # check game keeper exists
        self.assertTrue(User.objects.filter(username='test-username').exists() == True)
        
        # post request for removing game keeper
        self.client.post(reverse('remove_keeper'), {
            'username': 'test-username',
        }, follow=True)
        
        # check game keeper doesn't exist
        self.assertTrue(User.objects.filter(username='test-username').exists() == False)
        
        