from django.test import TestCase
from django.shortcuts import reverse

from sustainable_app.models import User, Item


class ProfileViewTests(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)

        default_items = ['cat', 'none', 'u_black', 'b_white']
        for item_name in default_items:
            item = Item.objects.get(name=item_name)
            self.user.equipped_items.add(item.id)

    def test_call_view_as_anonymous(self):
        """
        checks the profile page redirects to login when we are not logged in
        """
        response = self.client.get(reverse('profile'), follow=True)
        self.assertRedirects(response, reverse('login') + "?next=/profile/")

    def test_call_view_as_user(self):
        """
        checks the proifle page renders normally when logged in
        """
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, "sustainable_app/profile.html")

    def test_call_equip(self):
        """
        checks the profile/equip endpoint equips an item
        """
        self.client.login(username=self.username, password=self.password)

        initial_item = Item.objects.get(name='cat')
        new_item = Item.objects.get(name='badger')

        self.assertTrue(self.user.equipped_items.contains(initial_item))

        response = self.client.post(reverse('equip'), {
            "type": "character",
            "name": "badger"
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.user.equipped_items.contains(new_item))
