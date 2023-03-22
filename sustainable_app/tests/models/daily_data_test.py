from django.test import TestCase

from datetime import datetime, date

from ...models import DailyData, DailyGoalStatus, Goal, User


class DailyDataModelTests(TestCase):
    def setUp(self):
        # Create a user with daily goals
        self.user = User.objects.create()

        date = datetime(2010, 3, 11, 12, 0, 0)
        self.user_data = DailyData.objects.create(user=self.user, date=date)

        # Create goals
        self.goal1 = Goal.objects.create(
            name="Goal 1",
            xp_reward=50,
            point_reward=10,
        )
        self.goal2 = Goal.objects.create(
            name="Goal 2",
            xp_reward=30,
            point_reward=5,
        )

        # Create completions
        self.daily_goal1 = DailyGoalStatus.objects.create(
            user_data=self.user_data,
            goal=self.goal1,
            completed=True
        )

        self.daily_goal2 = DailyGoalStatus.objects.create(
            user_data=self.user_data,
            goal=self.goal2,
            completed=False
        )

    def test_xp_reward_with_no_completions(self):
        """
        Test xp_reward function with no completions
        """
        # Mark not completed
        self.daily_goal1.completed = False
        self.daily_goal1.save()

        # Call the xp_reward method to calculate the reward
        xp_reward = self.user_data.xp_reward()

        # Verify that the calculated reward is correct
        self.assertEqual(xp_reward, 0)

    def test_xp_reward_with_one_completion(self):
        """
        Test xp_reward function with one completion
        """
        # Mark one goal as completed
        self.daily_goal1.completed = True
        self.daily_goal1.save()

        # Call the xp_reward method to calculate the reward
        xp_reward = self.user_data.xp_reward()

        # Verify that the calculated reward is correct
        self.assertEqual(xp_reward, 50)

    def test_xp_reward_with_two_completions(self):
        """
        Test xp_reward function with two completions
        """
        # Mark both goals as completed
        self.daily_goal1.completed = True
        self.daily_goal1.save()

        self.daily_goal2.completed = True
        self.daily_goal2.save()

        # Call the xp_reward method to calculate the reward
        xp_reward = self.user_data.xp_reward()

        # Verify that the calculated reward is correct
        self.assertEqual(xp_reward, 80)

    def test_point_reward_with_no_completions(self):
        """
        Test point_reward function with no completions
        """
        # Mark not completed
        self.daily_goal1.completed = False
        self.daily_goal1.save()

        # Call the point_reward method to calculate the reward
        point_reward = self.user_data.point_reward()

        # Verify that the calculated reward is correct
        self.assertEqual(point_reward, 0)

    def test_point_reward_with_one_completion(self):
        """
        Test point_reward function with one completion
        """
        # Mark one goal as completed
        self.daily_goal1.completed = True
        self.daily_goal1.save()

        # Call the point_reward method to calculate the reward
        point_reward = self.user_data.point_reward()

        # Verify that the calculated reward is correct
        self.assertEqual(point_reward, 10)

    def test_point_reward_with_two_completions(self):
        """
        Test point_reward function with two completions
        """
        # Mark both goals as completed
        self.daily_goal1.completed = True
        self.daily_goal1.save()

        self.daily_goal2.completed = True
        self.daily_goal2.save()

        # Call the point_reward method to calculate the reward
        point_reward = self.user_data.point_reward()

        # Verify that the calculated reward is correct
        self.assertEqual(point_reward, 15)

    def test_str(self):
        """
        Check string operator of DailyData
        """
        self.assertEqual(str(self.user_data), "2010-03-11")

    def test_complete_goal_with_no_daily_data(self):
        """
        Check complete_goal creates daily data
        """
        try:
            DailyData.objects.get(user=self.user, date=date.today())
            self.fail("Expected daily data to not exist")
        except DailyData.DoesNotExist:
            pass

        DailyData.complete_goal(self.user, self.goal1)

        self.assertIsNotNone(DailyData.objects.get(
            user=self.user, date=date.today()))

    def test_complete_goal_with_daily_data(self):
        """
        Check complete_goal uses existing daily data
        and completes daily goal
        """
        daily_data = DailyData.objects.create(
            user=self.user, date=date.today())

        self.assertIs(daily_data.daily_goals.all().count(), 0)

        DailyData.complete_goal(self.user, self.goal1)

        self.assertIs(daily_data.daily_goals.all().count(), 1)


class DailyGoalStatusModelTests(TestCase):
    def setUp(self):
        # Create a user & user data
        self.user = User.objects.create()

        date = datetime(2023, 3, 11, 12, 0, 0)
        self.user_data = DailyData.objects.create(user=self.user, date=date)

        # Create goal
        self.goal = Goal.objects.create(
            name="Goal",
            xp_reward=50,
            point_reward=10,
        )

        # Create daily goal status
        self.daily_goal = DailyGoalStatus.objects.create(
            user_data=self.user_data,
            goal=self.goal,
            completed=True
        )

    def test_xp_reward(self):
        """
        Tests xp_reward returns the goal's xp_reward value
        """
        self.assertEqual(self.daily_goal.xp_reward(), self.goal.xp_reward)

    def test_point_reward(self):
        """
        Tests point_reward returns the goal's point_reward value
        """
        self.assertEqual(self.daily_goal.point_reward(),
                         self.goal.point_reward)
