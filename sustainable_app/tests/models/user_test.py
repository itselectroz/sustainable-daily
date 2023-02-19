from django.test import TestCase

from ...models import User

class UserModelTests(TestCase):
    def test_level_with_no_xp(self):
       """
       Checks the level method returns 0 when you have no xp
       """
       user = User()
       user.xp = 0
       self.assertEqual(user.level(), 0)

    def test_level_with_some_xp(self):
       """
       Checks the level method returns 10 when you have 20408 xp
       """
       user = User()
       user.xp = 20409
       self.assertEqual(user.level(), 10)

    def test_xp_for_level_with_level_0(self):
       """
       Checks the xp_for_level method returns 0 for level 0
       """
       user = User()
       self.assertEqual(user.xp_for_level(0), 0)
       
    def test_xp_for_level_with_level_20(self):
       """
       Checks the xp_for_level method returns 81632 for level2 0
       """
       user = User()
       self.assertEqual(user.xp_for_level(20), 81632)