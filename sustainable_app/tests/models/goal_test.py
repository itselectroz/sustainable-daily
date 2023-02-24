from django.test import TestCase

from ...models import Goal


class GoalModelTests(TestCase):
    def test_str(self):
        """
        Checks the __str__ function returns name
        """
        goal = Goal(name="test-name")

        self.assertIs(str(goal), goal.name)
